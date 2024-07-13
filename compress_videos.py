"""
Compresses video files specified in a JSON file using the ffmpeg-python library.

The script performs the following steps:
1. Checks if the ffmpeg-python module is installed and the ffmpeg binary is available.
2. Reads a JSON file containing a list of video file paths.
3. Compresses each video file using the ffmpeg-python library, with the following settings:
   - Video codec: libx264
   - Constant Rate Factor (CRF): 23
   - Pixel format: yuv420p
   - Enable faststart option
4. Optionally, deletes the original video files after successful compression.
5. Optionally, overwrites the output files if they already exist.

This script is intended to be used as a command-line tool, with the JSON file path and optional flags (-d for delete original, -w for overwrite) passed as command-line arguments.
"""
import json
import os
import subprocess
import importlib
import ffmpeg
import sys
def check_ffmpeg_python():
    try:
        importlib.import_module('ffmpeg')
        print(f"✅ checking ffmpeg-python module...")
    except ImportError:
        print("🔴 Error: ffmpeg-python is not installed.")
        sys.exit(1)

check_ffmpeg_python()

def check_ffmpeg_binary():
    try:
        print(f"✅ checking ffmpeg binary...")
        subprocess.run("ffmpeg -version", shell=True, check=True)
    except subprocess.CalledProcessError:
        print("🔴 Error: FFmpeg binary is not installed or not available.")
        sys.exit(1)

check_ffmpeg_binary()

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data['video_files']
    except FileNotFoundError:
        print(f"🔴 Error: JSON file '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"🔴 Error: JSON file '{file_path}' is empty or invalid.")
        return []

def compress_videos(video_files, delete_original, overwrite=False):
    for file in video_files:
        file = os.path.expanduser(file)
        if not os.path.isfile(file):
            print(f"🔴 Error: Video file '{file}' not found.")
            continue
        file_name, file_extension = os.path.splitext(file)
        # output_file = f"{file_name}_compressed{file_extension}"
        output_file = f"{file_name}.mp4"
        print(f"Compressing '{file}'...")
        try:
            input_file = ffmpeg.input(file)
            output_file = ffmpeg.output(input_file, output_file, vcodec='libx264', crf=23, pix_fmt='yuv420p', movflags='+faststart')
            ffmpeg.run(output_file, overwrite_output=overwrite)
            print(f"Compression successful: '{output_file}'")
            if delete_original:
                os.remove(file)
                print(f"Deleted original file: '{file}'")
        except ffmpeg.Error:
            print(f"🔴 Error: Compression failed for '{file}'")
            
if __name__ == '__main__':
    if len(sys.argv) not in [2, 3, 4]:
        print("Usage: python script.py <path/to/your/json/file.json> [-d] [-w]")
        sys.exit(1)
    json_file_path = sys.argv[1]
    delete_original = False
    overwrite = False
    if len(sys.argv) == 3:
        if sys.argv[2] == '-d':
            delete_original = True
        elif sys.argv[2] == '-w':
            overwrite = True
        else:
            print("Usage: python script.py <path/to/your/json/file.json> [-d] [-w]")
            sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[2] == '-d' and sys.argv[3] == '-w':
            delete_original = True
            overwrite = True
        elif sys.argv[2] == '-w' and sys.argv[3] == '-d':
            delete_original = True
            overwrite = True
        else:
            print("Usage: python script.py <path/to/your/json/file.json> [-d] [-w]")
            sys.exit(1)
    video_files = read_json_file(json_file_path)
    if video_files:
        print("Starting video compression...")
        compress_videos(video_files, delete_original, overwrite)
        print("Video compression complete.")
    else:
        print("No video files found in JSON file.")
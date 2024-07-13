import sys
import os
import argparse
from find_videos import create_video_json
from compress_videos import compress_videos, read_json_file

def main(folder_path, delete_original=False, overwrite=False, dist_folder=None):
    # Step 1: Find videos and create JSON file
    create_video_json(folder_path)
    
    # Step 2: Read the JSON file
    json_file_path = 'data.json'
    video_files = read_json_file(json_file_path)
    
    # Step 3: Compress videos
    if video_files:
        print("🚀 🚀 🚀 Starting video compression... 🚀 🚀 🚀 ")
        compress_videos(video_files, delete_original, overwrite, dist_folder)
        print("✅ Video compression complete.")
    else:
        print("🔴 No video files found in JSON file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Video compression script")
    parser.add_argument("folder_path", help="Path to the folder containing videos")
    parser.add_argument("-d", "--delete", action="store_true", help="Delete original files after compression")
    parser.add_argument("-w", "--overwrite", action="store_true", help="Overwrite existing compressed files")
    parser.add_argument("--dist", help="Destination folder for compressed videos")
    
    args = parser.parse_args()
    
    main(args.folder_path, args.delete, args.overwrite, args.dist)

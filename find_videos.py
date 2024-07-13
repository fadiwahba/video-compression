import os
import json
import sys

def create_video_json(folder_path):
    print(f"Starting to process folder: {folder_path}")
    
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"🔴 Error: The folder '{folder_path}' does not exist.")
        return

    video_files = []
    
    try:
        # Iterate through all files in the given folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Check if it's a file and has a .mp4 or .mov extension
            if os.path.isfile(file_path) and filename.lower().endswith(('.mp4', '.mov')):
                # Add the full path to the list
                video_files.append(os.path.expanduser(file_path))
                print(f"✅ Added video file: {file_path}")
    
        # Create the dictionary with the video files
        data = {"video_files": video_files}
    
        # Write the data to a JSON file
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        print(f"✅ Created data.json with {len(video_files)} video files.")
    
    except PermissionError:
        print(f"🔴 Error: Permission denied when accessing the folder '{folder_path}'.")
    except Exception as e:
        print(f"🔴 Error: An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_folder>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    create_video_json(folder_path)

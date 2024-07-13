# Video Compression Python Script

This project provides a Python script for compressing video files using FFmpeg. It's designed to process multiple video files specified in a JSON file, making it easy to batch compress videos with a single command.

## Features

- Compress multiple video files in one go
- Uses FFmpeg for efficient video compression
- Option to delete original files after compression
- Option to overwrite existing compressed files
- Supports various video formats
- Easy to use with command-line interface

## Requirements

- Python 3.x
- FFmpeg
- ffmpeg-python module

## Usage

The script is run from the command line with the following syntax:

```shell
python compress_videos.py <path/to/your/json/file.json> [-d] [-w]
```
- `-d`: Optional flag to delete original files after compression
- `-w`: Optional flag to overwrite existing compressed files

The JSON file should contain an array of video file paths to be compressed.
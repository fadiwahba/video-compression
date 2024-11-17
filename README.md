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

**[Optional] Create conda env**
```shell
conda create --name videos_project python=3.11
```

**Activate the environment**
```shell
conda activate videos_project
```

**Install the requirements**
```shell
conda install --file requirements.txt

```
OR
```shell
pip install -r requirements.txt
```


**The script is run from the command line with the following syntax:**

```shell
python main.py <path/to/your/videos/folder> [-d] [-w] [--dist]
```
- `-d`: Optional flag to delete original files after compression
- `-w`: Optional flag to overwrite existing compressed files
- `--dist`: Optional flag for destination folder

The JSON file should contain an array of video file paths to be compressed.
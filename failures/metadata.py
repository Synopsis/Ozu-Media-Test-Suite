import subprocess
import os




# 1. Container marked as having a different frame rate than actual content.
def create_failure_case_incorrect_frame_rate(input_file, output_file, incorrect_frame_rate):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-r', str(incorrect_frame_rate),
        '-vf', 'fps=fps=' + str(incorrect_frame_rate),
        output_file
    ]
    subprocess.run(command)

# 2. Incorrect aspect ratio specified in container metadata.
def create_failure_case_incorrect_aspect_ratio(input_file, output_file, incorrect_aspect_ratio):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-aspect', str(incorrect_aspect_ratio),
        output_file
    ]
    subprocess.run(command)

# 3. Misleading or missing codec information in container metadata.
def create_failure_case_missing_codec_info(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'copy',
        '-c:a', 'copy',
        '-movflags', 'use_metadata_tags',
        output_file
    ]
    subprocess.run(command)
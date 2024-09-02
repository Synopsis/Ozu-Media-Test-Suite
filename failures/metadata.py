import subprocess
import os



def generate_mismatched_container_invalid_audio_codec(input_file:str, output_file:str):
    ffmpeg_command = [
        "ffmpeg",

        "-err_detect", "ignore_err",
        "-max_error_rate", "100",
        "-fflags", "noparse+nofillin",

        "-i", input_file, 
        "-c", "copy",
        # "-vcodec", "copy",
        # "-acodec", "copy",
        "-tag:v", "HEVC",
        "-tag:a", "flac",

        "-strict", "-2147483648",
        "-safe", "0",

        "-auto_convert", "0",
        # "-unsafe", "1",
        "-max_error_rate", "100",
        "-err_detect", "ignore_err",
        output_file, 
        "-y",

    ]

    # ffmpeg_command = [
    #     "ffmpeg",
    #     "-i", input_file,
    #     "-map", "0:v",
    #     "-c:v", "copy",
    #     "-map", "0:a",
    #     "-c:a", "copy",
    #     # "-f", "matroska",
    #     "-metadata:s:v", "codec_name=\"HEVC\"",
    #     output_file,
    #     "-safe", "0"
    #     ]

    subprocess.run(ffmpeg_command)


# # 1. Container marked as having a different frame rate than actual content.
# def create_failure_case_incorrect_frame_rate(input_file, output_file, incorrect_frame_rate):
#     command = [
#         'ffmpeg',
#         '-i', input_file,
#         '-r', str(incorrect_frame_rate),
#         '-vf', 'fps=fps=' + str(incorrect_frame_rate),
#         output_file
#     ]
#     subprocess.run(command)

# # 2. Incorrect aspect ratio specified in container metadata.
# def create_failure_case_incorrect_aspect_ratio(input_file, output_file, incorrect_aspect_ratio):
#     command = [
#         'ffmpeg',
#         '-i', input_file,
#         '-aspect', str(incorrect_aspect_ratio),
#         output_file
#     ]
#     subprocess.run(command)

# # 3. Misleading or missing codec information in container metadata.
# def create_failure_case_missing_codec_info(input_file, output_file):
#     command = [
#         'ffmpeg',
#         '-i', input_file,
#         '-c:v', 'copy',
#         '-c:a', 'copy',
#         '-movflags', 'use_metadata_tags',
#         output_file
#     ]
#     subprocess.run(command)
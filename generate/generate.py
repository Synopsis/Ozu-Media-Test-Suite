
import os
import subprocess
import types

from utils import utils

def generate_video_with_smpte_bars_and_timecode(width:int, height:int, frame_rate:float, output_file:str):
	"""
	Generate a video with SMPTE bars, audio tone, and embedded timecode.

	Args:
	- width (int): Width of the video.
	- height (int): Height of the video.
	- frame_rate (int): Frame rate of the video (frames per second).
	- output_file (str): Output filename for the video.
	"""

	# FFmpeg command to generate video with SMPTE bars, audio tone, and embedded timecode
	ffmpeg_command = [
		'ffmpeg',
		'-f', 'lavfi',
		'-i', f'smptebars=size={width}x{height}:rate={frame_rate}:duration=5.0',
		'-f', 'lavfi',
		'-i', f"sine=frequency=1000:duration=5.0",
		'-vf', f"drawtext=text='Frame\\: %{{frame_num}}': start_number=1: x=(w-tw)/2: y=h-(2*lh):fontfile='Inconsolata-Regular.ttf':fontsize=40:alpha=0.5:box=1:boxborderw=4,drawtext=text='TC':x=(w-tw)/2:y=(lh):fontfile='Inconsolata-Regular.ttf':fontsize=40:fontcolor=white:timecode='01\\:00\\:00\\:00':timecode_rate=({frame_rate})",
		'-c:v', 'libx264',  # Video codec
		'-c:a', 'aac',  # Audio codec
		'-crf', '23',  # Constant Rate Factor (quality)
		'-preset', 'medium',  # Preset for encoding speed vs. compression efficiency
		'-pix_fmt', 'yuv420p',  # Pixel format for compatibility
		'-fflags', '+shortest', # Stop encoding once the shortest stream ends
		'-t', '5',
		'-timecode', "01:00:00:00",
		'-write_tmcd', 'true',
		'-y',  # Overwrite output files without asking
		output_file
	]

	# Run FFmpeg command
	subprocess.run(ffmpeg_command)

	print(f"Generated: {output_file}")


def generate_all_source_files(output_folder_name:str = "source_media") -> list[str]:

	output_folder = utils.create_directory(output_folder_name)

	# Define a list of resolutions and frame rates
	resolutions = [(320, 240), (640, 480), (1280, 720), (1920, 1080)]  # Resolutions: (width, height)
	frame_rates = [23.98, 24, 25, 29.97, 30, 50, 59.97, 60]  # Frame rates: frames per second

	output_files = []

	# Loop through each resolution and frame rate combination
	for resolution in resolutions:
		width, height = resolution
		for frame_rate in frame_rates:
			# Generate the output filename based on resolution and frame rate

			output_file_name = f'input_{width}x{height}_{frame_rate}fps.mp4'
			output_file = os.path.join(output_folder, output_file_name )

			if utils.file_exists_in_directory(output_folder, output_file ):
				print( f"skipping {output_file_name}, ")
				continue

			generate_video_with_smpte_bars_and_timecode(width, height, frame_rate, output_file)


			output_files.append(output_file)

	return output_files

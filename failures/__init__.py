cases = list(range(0, 5))

from utils import utils


def case1(input_file:str, output_dir:str) ->str:

	file_name, ext = utils.file_name_and_ext_from_file_path(input_file)

	# output_file_name = 

	# Test case 1: Incorrect container metadata
	# 1a. Container marked as having a different frame rate than actual content.
	subprocess.run(['ffmpeg', '-i', input_file, '-r', '30', 'incorrect_frame_rate.mp4'])


def generate_test_file(input_file:str, failure_type:int, output_dir:str) -> str:
	

	match failure_type:
		case 1:
			return case1()
		case 2:
			return case2()
		case 3:
			return case3()


def generate_all_failure_files(all_source_files:list[str]):
	
	base_output_dir = utils.create_directory("failure_files")


	for source_file in all_source_files:
		for case in cases:
			generate_test_file(source_file, case)




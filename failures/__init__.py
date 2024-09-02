from utils import utils
from .metadata import *


failure_cases = [ 
		{
			"func_name" : "metadata.generate_mismatched_container_invalid_audio_codec",
			"function" : metadata.generate_mismatched_container_invalid_audio_codec,
			"prefix" : "metadata"
		},
	]


def generate_all_failure_files(all_source_files:list[str]):
	
	print("Generating Failures")

	base_output_dir = utils.create_directory("failure_files")

	for source_file in all_source_files:
		print("Generating failure cases for", source_file)
		for failure_case in failure_cases:

			sub_dir = failure_case["prefix"]
			func_name = failure_case["func_name"]

			print("running", func_name)

			input_file_name, ext = utils.file_name_and_ext_from_file_path(source_file)

			output_folder = utils.create_directory( os.path.join(base_output_dir, sub_dir) )

			output_file_name = func_name + "_" + input_file_name + "." + ext

			output_file = os.path.join(output_folder, output_file_name)

			if utils.file_exists_in_directory(output_folder, output_file ):
				print( f"skipping {output_file_name}, ")
				continue

			failure_case["function"](source_file, output_file)




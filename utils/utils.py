import os

def file_name_and_ext_from_file_path(file_path:str) -> (str, str):

    base_name = os.path.basename(file_path)
    filename_without_extension, ext = os.path.splitext(base_name)
    return (filename_without_extension, ext)

def create_directory(output_folder_name:str) -> str:
	cwd = os.getcwd()

	output_folder = os.path.join(cwd, output_folder_name)

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	return output_folder

def file_exists_in_directory(directory:str, filename:str) -> bool:
   
	filepath = os.path.join(directory, filename)
	return os.path.exists(filepath)

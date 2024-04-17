import os
import subprocess
import types

from utils import utils
from generate import generate
import failures


all_source_files = generate.generate_all_source_files(output_folder_name = "source_media")


failures.generate_all_failure_files(all_source_files)

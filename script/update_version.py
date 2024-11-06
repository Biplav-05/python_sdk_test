import re
import sys
import os


'''
This function updates the version number in a specified file (setup.py)
by replacing the current version string with a new version provided
as an argument.
'''


def update_version(file_path, new_version):
    # Opening the file in read mode
    with open(file_path, 'r') as file:
        content = file.read()  # Reading the content of the file
        # Defining the regex pattern to match the version string
        pattern = r'version\s*=\s*"[^"]+"'
        # Creating the replacement string with the new version
        replacement = f'version="{new_version}"'
        # Replacing the old version with the new version
        new_content = re.sub(pattern, replacement, content)
        # Opening the file in write mode to update the content
        with open(file_path, 'w') as file:
            file.write(new_content)


if __name__ == "__main__":
    # Ensure the correct path to setup.py from any running directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    setup_file_path = os.path.join(script_dir, '..', 'setup.py')
    # Running the update_version function with the provided file path
    # and new version
    update_version(setup_file_path, sys.argv[1])

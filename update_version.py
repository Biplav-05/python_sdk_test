import re
import sys

def update_version(file_path, new_version):
    with open(file_path, 'r') as file:
        content = file.read()
    
    pattern = r'version\s*=\s*"[^"]+"'
    replacement = f'version="{new_version}"'
    
    new_content = re.sub(pattern, replacement, content)
    
    with open(file_path, 'w') as file:
        file.write(new_content)

if __name__ == "__main__":
    new_version = sys.argv[1]
    print(f"Updating version to: {new_version}")
    update_version('setup.py', new_version)
    print("Version updated successfully")
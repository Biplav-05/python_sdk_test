import re
import sys

def update_version(version):
    with open('setup.py', 'r+') as f:
        content = f.read()
        f.seek(0)
        f.write(re.sub(r'version=\"[0-9]+\.[0-9]+\.[0-9]+\"', f'version=\"{version}\"', content))
        f.truncate()

def main():
    version = sys.argv[1]
    update_version(version)

if __name__ == "__main__":
    main()
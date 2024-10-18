# update_version.py
import re
import sys

version = sys.argv[1]

with open('setup.py', 'r+') as f:
    content = f.read()
    f.seek(0)
    f.write(re.sub(r'version=\"[0-9]+\.[0-9]+\.[0-9]+\"', f'version=\"{version}\"', content))
    f.truncate()

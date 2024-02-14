import os
import py_compile
from pathlib import Path

# Get the directory containing compile.py
current_dir = Path(__file__).resolve().parent

# Construct the path to eve.py
eve_py_path = current_dir / 'src' / 'eve.py'

# Remove existing compiled files and scripts
os.remove(current_dir / "../dist/eve.pyc") if os.path.exists(current_dir / "../dist/eve.pyc") else None
os.remove(current_dir / "../dist/eve") if os.path.exists(current_dir / "../dist/eve") else None
os.remove(current_dir / "../dist/eve.ps1") if os.path.exists(current_dir / "../dist/eve.ps1") else None

# Compile eve.py to ../dist/eve.pyc
py_compile.compile(str(eve_py_path), optimize=0, cfile=str(current_dir / "dist/eve.pyc"))


# Generate .sh script
with open(current_dir / "dist/eve", 'w') as f:
    f.write('#!/bin/bash\n')
    f.write('\n# Generated By Eveeifyeve/CLI\n')
    f.write('python3 /usr/local/bin/eve.pyc "$@"\n')

# Generate .ps1 script
with open(current_dir / "dist/eve.ps1", 'w') as f:
    f.write('# Generated By Eveeifyeve/CLI\n')
    f.write('python ..\\eve.pyc $args\n')


# Generate test sh script
with open(current_dir / "dist/test.sh", 'w') as f:
    f.write('#!/bin/bash\n')
    f.write('\n# Define the target directory\n')
    f.write('TARGET_DIR="/usr/local/bin/"\n')
    f.write('\n# Remove existing eve.pyc and eve from the target directory if they exist\n')
    f.write('rm -f "${TARGET_DIR}eve.pyc"\n')
    f.write('rm -f "${TARGET_DIR}eve"\n')
    f.write('\n# Move files to the target directory\n')
    f.write('cp eve.pyc "$TARGET_DIR"\n')
    f.write('cp eve "$TARGET_DIR"\n')
    f.write('\n# Change permissions of files if necessary\n')
    f.write('chmod +x "${TARGET_DIR}eve.pyc"\n')
    f.write('chmod +x "${TARGET_DIR}eve"\n')
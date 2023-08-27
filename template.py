import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format= "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
    )

while True:
    project_name = input("Please enter project name: ")
    if project_name:
        break
    
logging.info(f"Creating project {project_name}")

#list of files:
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "tox.ini",
    "pyproject.toml",
    "setup.cfg",
    "conftest.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "": # if file directory has no path then it is a file in the root directory. Else create the parent path.
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating file: {filename}")
        
    # If file path is empty or size of the file path is 0. Then create an empty file.
    if (not os.path.exists(filepath)) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass # create empty file
            logging.info(f"Creating empty file: {filename} at {filepath}")
    else: #This prevents overwrting files that aleady exist.
        logging.info(f"File already exists: {filename}")

            
            
            
    
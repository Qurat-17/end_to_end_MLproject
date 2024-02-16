import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')

#folder
project_name ="mlproject"

list_of_files = [

f"src/{project_name}/__init__.py",
f"src/{project_name}/components/__init__.py",
f"src/{project_name}/utils/__init__.py",
f"src/{project_name}/utils/common.py",
f"src/{project_name}/config/__init__.py",
f"src/{project_name}/pipeline/__init__.py",
f"src/{project_name}/entity/__init__.py",
f"src/{project_name}/entity/config_entity.py",
f"src/{project_name}/constant/__init__.py",
"config/config.yaml",
"schema.yaml",
"main.py",
"app.py",
"requirements.txt",
"setup.py",
"research/trils.ipynb",
"templates/index.html"

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file:{filename}")
    if(not os.path.exists(filepath))or(os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty fiel:{filepath}")

    else :
        logging.info(f"{filename}is already exists")



"""
import os

project_name = "mlproject"
base_dir = 'end_to end_MLproject'

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trils.ipynb",
    "templates/index.html"
]

for item in list_of_files:
    path = os.path.join(base_dir, item)
    if item.endswith('.py'):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            pass  # Create an empty .py file
    else:
        os.makedirs(path, exist_ok=True)

"""
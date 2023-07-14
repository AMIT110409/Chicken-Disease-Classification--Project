import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


project_name = "CnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirments.txt",
    "setup.py",
    "research/trails.ipynb"
    "test.py"  
     
]

for filepath in list_of_files:
    filepath = Path(filepath)   ## forward slash for linux and backward slash for windows we are using . 
    filedir,filename = os.path.split(filepath)
    
    
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"{filepath}  is already exists")        
        
##  os.path.split(path)

##  Split the pathname path into a pair, (head, tail) where tail is the last pathname component and head is everything leading up to that.

## os.path.getsize(path) 

## Return the size, in bytes, of path. Raise OSError if the file does not exist or is inaccessible.

    
    
            
    

    
    
    
    
    
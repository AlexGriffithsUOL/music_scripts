# music_scripts
A repo filled with my scripts for music stuff


### merge_folder_contents.py
## Designated use case
> Designed to take folders with directories and subdirectories containing files and merging them into a single destination.
> Good if you are using torrenting etc software to compile lists of files.

## Setup
> Create a virtual environment by running this command from the directory containing this file:
python -m venv .venv

> Run this command:
# Windows 
.venv/scripts/activate

# Linux/MacOS
source .venv/bin/activate



## Usage
To run the script:
> python merge_folder_contents.py (path of folder containing all subdirectories) (path of folder to copy to)

This will then output timestamped logs to show that it has run.

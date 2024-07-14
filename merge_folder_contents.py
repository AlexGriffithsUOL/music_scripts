# Imports
import os
import glob
import shutil
import sys
import time
import datetime

def current_timestamp():
    temp_time = time.time() * 1000
    return datetime.datetime.fromtimestamp(temp_time/1000.0)

class merge_folder_handler:
    
    class metadata:
        class consts:
            COMPOSING_INFO = 'Composing list of files...'
            COMPOSED_INFO = 'Path list is composed!'
            COPYING_INFO = 'Copying files...'
            COPIED_INFO = 'Files copied!'
            PROGRAM_FINISHED = 'Finished!'
            PROGRAM_EXITING = 'Exiting program...'

    def __init__(self, base_path=os.getcwd(), new_path=None):
        self.base_path = base_path
        self.new_path = new_path

    def compose_timestamped_string(self, string):
        return f'[{current_timestamp()}]: {string}'
    
    def log(self, string):
        print(self.compose_timestamped_string(string))

    def recursive_finder(self, current_location):
        sub_locations = glob.glob(f'{current_location}//*')
        holder = []
        for sub_location in sub_locations:
            if os.path.isdir(sub_location):
                for element in self.recursive_finder(sub_location):
                    holder.append(element)
            else:
                holder.append((sub_location, os.path.basename(sub_location)))
        return holder
    
    def compose_file_list(self):
        return self.recursive_finder(self.base_path)
    
    def copy_files_to_location(self, path_list_with_filename):
        for file in path_list_with_filename:
            file_path = file[0]
            file_name = file[1]
            new_file_path = f'{self.new_path}//{file_name}'
            shutil.copyfile(file_path, new_file_path)
            self.log(f'{file_name} copied to {new_file_path}')

    def run(self):
        self.log(self.metadata.consts.COMPOSING_INFO)
        path_list = self.compose_file_list()
        self.log(self.metadata.consts.COMPOSED_INFO)
        self.log(f'{len(path_list)} files found!')
        self.log(self.metadata.consts.COPYING_INFO)
        self.copy_files_to_location(path_list)
        self.log(self.metadata.consts.COPIED_INFO)

        self.log(self.metadata.consts.PROGRAM_FINISHED)

        self.log(self.metadata.consts.PROGRAM_EXITING)

def main(*args, **kwargs):
    args = args[0]
    match (len(args)):
        case 1:
            raise Exception('Missing base directory path and new directory path, please include in the arguments.')
        case 2:
            raise Exception('Missing new directory path, please include in the arguments.')
        case 3:
            handler = merge_folder_handler(args[1], args[2])
            handler.run()
            exit()
        case _:
            raise Exception('Wrong number of arguments, please call function with base directory path and subdirectory path.')

if __name__=='__main__':
    main(sys.argv)
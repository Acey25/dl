import os
import re
import shutil
import pandas as pd



class label_finder:
    def __init__(self, img_folder_path, labeled_folder_path,
                 img_types={'jpg', 'jtif', 'exif', 'tiff', 'gif', 'bmp', 'png', 'ppm', 'pgm', 'pbm', 'pnm'}):
        self.folder_path = img_folder_path
        self.labeled_folder_path = labeled_folder_path
        self.img_types = img_types
        self.labels = set()

    def create_label_folder_paths(self):
        # This method creates folders for labels inside the main directory (labeled_folder_path)
        # output
        # sub_dir: a dictionary with key=label, value= folder path of the label
        print('running create_label_folders method')
        sub_dirs = {item: os.path.join(self.labeled_folder_path, item) for item in self.labels}
        for item in sub_dirs.values():
            if not os.path.exists(item):
                os.makedirs(item)
        return sub_dirs

    def move_file_paths(self):
        # this method scans over the files in img_folder_path and outputs 2 dictionaries
        # Outputs
        # move_dict: key=label, value= a set of file path including the label
        # label_path_dict: key=label, value= folder path of the label

        print('running move_file_paths method')
        move_dict = {}
        for item in os.listdir(self.folder_path):
            item_path = os.path.join(self.folder_path, item)
            if os.path.isfile(item_path):
                f_name, f_ext = item.split('.')
                if f_ext in self.img_types:
                    label = f_name.split('_')[1]
                    self.labels.update([label])
                    try:
                        move_dict[label].update([item_path])
                    except:
                        move_dict[label] = set([item_path])

        label_path_dict = self.create_label_folder_paths()

        if move_dict == {}:
            print('------------------------------no files to move------------------------------')

        return move_dict, label_path_dict

    def move_file(self):
        # this method moves the files with a label to their corresponding subfolder
        print('running move_file method')
        move_dict, label_path_dict = self.move_file_paths()
        for label, path_list in move_dict.items():
            for path in path_list:
                shutil.move(path, label_path_dict[label])



from util import label_finder
import json
setting = json.load(open('params.json'))

images_dir = setting['paths']['image_path']
destination_dir = setting['paths']['label_path']


# create an instance of label_finder
test = label_finder(img_folder_path=images_dir, labeled_folder_path=destination_dir)
# run move_file method to move files to the corresponding label folder
test.move_file()



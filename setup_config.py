import os
import random
import argparse
import json

from PIL import Image
from PIL.ExifTags import TAGS
from pytorch_vision_utils.Utilities import clear_dirs
from pytorch_vision_utils.

# parse the arguments

configurations = dict()
avail_configs = configurations["avail_configs"]
config = "configuration/"
data = "dataset/"
config_name = "cat_or_dog"

def setup(config: str):
    # loads an image and saves it correctly formatted into the proper directory
    clear_dirs(config)
    
    for _, subdir, files in os.walk(data).sort():
        if not files:
            continue
        
        img = Image.open(subdir+"/"+files)
        exifdata = img.getexif
        
        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            
            # decode bytes 
            if isinstance(data, bytes):
                data = data.decode()
                
            print(f"{tag:25}: {data}") 
            _save_image()   
    


def _save_image(img):
    # save images to correct folder
    pass



if __name__() == "__main__":
    # run main
    setup(config_name)
    
        
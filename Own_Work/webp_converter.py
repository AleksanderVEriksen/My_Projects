# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:11:47 2022

@author: eriks
"""

import imghdr
from PIL import Image

def converter (webp_file, name ):
    im = Image.open(webp_file).convert("RGB")
    im.save(name + ".jpg","jpeg")

#Path = "pepoannouncement.webp"

#converter(Path, "pepo");

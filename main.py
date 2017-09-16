"""
Strips metadata from images.
"""

from PIL import Image
import piexif
import argparse

__author__ = "Cherie"


def rotate_02(filename):
    img1 = Image.open(filename)
    if "exif" in img1.info:
        exif_dict = piexif.load(img1.info["exif"])
    if piexif.ImageIFD.Orientation in exif_dict["0th"]:
        orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
        exif_bytes = piexif.dump(exif_dict)

    #img = piexif.load(filename)

    #print(piexif.VERSION)
    piexif.remove(filename)

    img = Image.open(filename)
    print(img.info)

    if orientation == 2:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 3:
        img = img.rotate(180)
    elif orientation == 4:
        img = img.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 5:
        img = img.rotate(-90).transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 6:
        img = img.rotate(-90)
    elif orientation == 7:
        img = img.rotate(90).transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 8:
        img = img.rotate(90)


    img.save('out03.jpg') #, exif=exif_bytes)



if __name__ == "__main__":
    print(PIL.PILLOW_VERSION)
    print(piexif.VERSION)
    print(argparse.__version__)

    rotate_02('test03.jpg')





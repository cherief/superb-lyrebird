from PIL import Image
import piexif
import argparse
import glob
import os
import sys


def strip_metadata(filename):
    img1 = Image.open(filename)

    if "exif" in img1.info:
        exif_dict = piexif.load(img1.info["exif"])

    if piexif.ImageIFD.Orientation in exif_dict["0th"]:
        orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
        exif_bytes = piexif.dump(exif_dict)

    piexif.remove(filename)

    img = Image.open(filename)

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

    return img


if __name__ == "__main__":

    if len(sys.argv) == 2:
        path = str(sys.argv[1])
    else:
        path = ""

    # Get path info
    f = open(os.path.join(path,'image_path'),'r')
    lines = f.readlines()
    image_path = lines[0].replace('\n','')
    stripped_path = lines[1].replace('\n','')
    f.close()

    # Get list of images
    img_list = glob.glob(os.path.join(image_path,'*'))

    for img_name in img_list:

        img_name = img_name.split('/')[-1]
        
        # Move image before stripping metadata
        os.system('mv ' + os.path.join(image_path,img_name) + ' ' + os.path.join(stripped_path,img_name))

        # Strip metadata and rotate image
        img = strip_metadata(os.path.join(stripped_path,img_name))

        # Save image
        img.save(os.path.join(stripped_path,img_name),quality=95)









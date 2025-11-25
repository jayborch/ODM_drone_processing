from PIL import Image
from PIL.TiffImagePlugin import ImageFileDirectory_v1

import os

IMAGES_FOLDER = r"C:\Users\jay.philip\Desktop\ODM_Project\images"
OUTPUT_FOLDER = r"C:\Users\jay.philip\Desktop\ODM_Project\clean_images"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(IMAGES_FOLDER):
    if not filename.lower().endswith(".jpg"):
        continue

    img_path = os.path.join(IMAGES_FOLDER, filename)
    img = Image.open(img_path)

    exif_data = img.getexif()
    new_exif = ImageFileDirectory_v1()

    # Keep only GPS and DateTimeOriginal
    for tag, value in exif_data.items():
        if tag in [0x0132, 0x8825]:  # DateTimeOriginal, GPSInfo
            new_exif[tag] = value

    out_path = os.path.join(OUTPUT_FOLDER, filename)
    img.save(out_path, exif=new_exif.tobytes())
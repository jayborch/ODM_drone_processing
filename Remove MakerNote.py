from PIL import Image
import piexif
import os

folder = r"C:\Users\jay.philip\Desktop\ODM_Project\images"

for file in os.listdir(folder):
    if not file.lower().endswith(".jpg"):
        continue

    path = os.path.join(folder, file)

    try:
        img = Image.open(path)
        exif_dict = piexif.load(img.info["exif"])

        # Remove MakerNote only
        if piexif.ExifIFD.MakerNote in exif_dict["Exif"]:
            del exif_dict["Exif"][piexif.ExifIFD.MakerNote]

        exif_bytes = piexif.dump(exif_dict)
        img.save(path, "jpeg", exif=exif_bytes)

        print("Fixed:", file)

    except Exception as e:
        print("Could not fix:", file, "-", e)

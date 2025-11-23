import os
from PIL import Image

def convert_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            img = Image.open(filename)
            webp_filename = os.path.splitext(filename)[0] + ".webp"
            img.save(webp_filename, "WEBP", quality=80)

if __name__ == "__main__":
    convert_images(".")

ORIGINAL_FOLDER = "material-design-icons" # Download from: https://github.com/google/material-design-icons
SUBFOLDER = "materialicons"

EXPORT_FOLDER = "icons"
EXPORT_RES = 48 # Possible are: 16, 24, 36, 48
EXPORT_SCALE = 2 # Possible are: 1, 2
INVERT_COLORS = True

import os
import shutil
import numpy
from PIL import Image, ImageOps


def invert(img: Image) -> Image:
    pixels = numpy.array(img.convert("RGBA"))
    pixels[:,:,0:3] = 255 - pixels[:,:,0:3] # invert
    return Image.fromarray(pixels)


if __name__ == "__main__":
    # Create export folder if not already present
    if not os.path.exists(EXPORT_FOLDER):
        os.mkdir(EXPORT_FOLDER)

    # Iterate over icon categories (navigation, communication, ...)
    for file in os.listdir(os.path.join(ORIGINAL_FOLDER, "png")):
        for icon in os.listdir(os.path.join(ORIGINAL_FOLDER, "png", file)):
            path = os.path.join(ORIGINAL_FOLDER, "png", file, icon, SUBFOLDER, f"{EXPORT_RES}dp", f"{EXPORT_SCALE}x")
            if not os.path.exists(path):
                continue

            for i, icon_file in enumerate(os.listdir(path)):
                # Copy icon
                icon_name = icon

                if len(os.listdir(path)) > 1:
                    icon_name += f"_{i}"

                scr = os.path.join(path, icon_file)
                dst = os.path.join(EXPORT_FOLDER, f"{icon_name}-inv.png")

                if INVERT_COLORS:
                    img = Image.open(scr)
                    img = invert(img)
                    img.save(dst)
                else:
                    shutil.copy2(os.path.join(path, icon_file), os.path.join(EXPORT_FOLDER, f"{icon_name}.png"))

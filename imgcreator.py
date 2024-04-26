import os
import random
from PIL import Image, ImageDraw, ImageFont


def create_images(folder_name, n):
    # Create the folder if it doesn't exist
    os.chdir('/Volumes/PHILIPS UFD')
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Supported image formats
    image_formats = ['jp2', 'tif']

    # Calculate image size in pixels (assuming 300 ppi)
    width_pixels = int(8.5 * 300)
    height_pixels = int(3362)

    for i in range(1, n + 1):
        # Generate random file name
        file_name = f"IMG_{i}.{random.choice(image_formats)}"

        # Generate the image with its number on it
        image = Image.new('RGB', (width_pixels, height_pixels), color='white')
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default(100)
        #vfont.size = 50
        text = str(i)
        draw.text(((width_pixels - 60) // 2, (height_pixels - 60) // 2), text, fill='black', font=font)

        # Save the image
        image.save(os.path.join(folder_name, file_name))

    print(f"{n} images created in '{folder_name}' folder.")


def main():
    # Get folder name from user
    folder_name = input("Enter folder name to store images: ")

    # Get number of images from user
    n = int(input("Enter number of images to create: "))

    # Create images
    create_images(folder_name, n)


if __name__ == "__main__":
    main()

import os
import random
from PIL import Image, ImageDraw, ImageFont
from multiprocessing import Pool


def create_image(args):
    folder_name, width, height, i, image_formats = args

    # Generate random file name
    file_name = f"IMG_{i}.{random.choice(image_formats)}"

    # Generate the image with its number on it
    image = Image.new('1', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(100)
    text = str(i)
    draw.text(((width - 60) // 2, (height - 60) // 2), text, fill='black', font=font)

    # Save the image
    image.save(os.path.join(folder_name, file_name))

    return f"{folder_name}/{file_name}"


def create_images(folder_name, n, batch_size=100):
    # Create the folder if it doesn't exist
    os.chdir('/Volumes/PHILIPS UFD')
    os.makedirs(folder_name, exist_ok=True)

    # Supported image formats
    image_formats = ['jpg', 'tif']

    # Calculate image size in pixels
    width_pixels = int(8.5 * 300)
    height_pixels = int(3362)

    # Generate images in batches
    args_list = [(folder_name, width_pixels, height_pixels, i, image_formats) for i in range(1, n + 1)]
    with Pool() as pool:
        results = pool.map(create_image, args_list, chunksize=batch_size)

    print(f"{n} images created in '{folder_name}' folder.")
    return results


def main():
    # Get folder name from user
    folder_name = input("Enter folder name to store images: ")

    # Get number of images from user
    n = int(input("Enter number of images to create: "))

    # Create images
    create_images(folder_name, n)


if __name__ == "__main__":
    main()

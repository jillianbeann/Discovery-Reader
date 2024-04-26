#!/usr/bin/env python3
import os
import sys
import img2pdf


def extract_number(filename):
    return int(''.join(filter(str.isdigit, filename)))

def read_files_better():
    #dir = '/Users/jillianhandrahan/steiner_001_images'
    dir = '/Volumes/PHILIPS UFD'
    # convert all files ending in .jpg inside a directory
    print("Welcome. Some files may be skipped. Normal skipped files: .DS_Store, IMG folder names like IMG001")
    os.chdir(dir)
    # dirname = os.getcwd() + '/IMAGES'
    # print("Current working directory:", dirname)
    print("Current working directory: ", dir)
    created = []

    for dirpath, dirname, filenames in os.walk(dir):
        imgs = []
        for fname in os.listdir(dirpath):
            if (not fname.startswith(".")) and fname != ".DS_Store" \
                    and (fname.endswith(".jpg") or fname.endswith(".tif")):
                print("filename: ", fname)
                path = os.path.join(dirpath, fname)
                if os.path.isdir(path):
                    continue
                imgs.append(path)
            else:
                print("Skipped a file. File name: " + fname)
                continue
        imgs = sorted(imgs, key=extract_number)
        if len(imgs) != 0:
            filename = os.path.basename(os.path.normpath(dirpath)) + '.pdf'
            created.append(filename)
            with open(filename, "wb") as f:
                f.write(img2pdf.convert(imgs))
    print("SUCCESS: " + str(len(created)) + " PDF files created: ")
    for name in created:
        print(name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_files_better()

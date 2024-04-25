#!/usr/bin/env python3
import os
import sys
import img2pdf

def read_files_better():
    # convert all files ending in .jpg inside a directory
    print("Welcome. Some files may be skipped. Normal skipped files: .DS_Store, IMG folder names like IMG001")
    os.chdir('/Users/jillianhandrahan/target_images')
    #dirname = os.getcwd() + '/IMAGES'
    #print("Current working directory:", dirname)
    print("Current working directory: /Users/jillianhandrahan/target_images")
    created = []

    for dirpath, dirname, filenames in os.walk('/Users/jillianhandrahan/target_images'):
        imgs = []
        for fname in os.listdir(dirpath):
            if fname != ".DS_Store" and (fname.endswith(".jpg") or fname.endswith(".tif")):
                path = os.path.join(dirpath, fname)
                if os.path.isdir(path):
                    continue
                imgs.append(path)
                imgs.sort()
            else:
                print("Skipped a file. File name: " + fname)
                continue
        if len(imgs) != 0:
            filename = os.path.basename(os.path.normpath(dirpath)) + '.pdf'
            created.append(filename)
            with open(filename, "wb") as f:
                f.write(img2pdf.convert(imgs))
    print("SUCCESS: " + str(len(created)) + " PDF files created: ")
    for name in created:
        print(name)

#hi
# def read_files():
#     # convert all files ending in .jpg inside a directory
#     print("Welcome. Some files may be skipped. Normal skipped files: .DS_Store, IMG folder names like IMG001")
#     os.chdir('/Users/jillianhandrahan/target_images')
#     dirname = os.getcwd() + '/IMAGES'
#     created = []
#
#     for dirpath, dirname, filenames in os.walk(dirname):
#         imgs = []
#         for fname in os.listdir(dirpath):
#             if fname != ".DS_Store" and (fname.endswith(".jpg") or fname.endswith(".tif")):
#                 path = os.path.join(dirpath, fname)
#                 if os.path.isdir(path):
#                     continue
#                 imgs.append(path)
#                 imgs.sort()
#             else:
#                 print("Skipped a file. File name: " + fname)
#                 continue
#         if len(imgs) != 0:
#             filename = os.path.basename(os.path.normpath(dirpath)) + '.pdf'
#             created.append(filename)
#             with open(filename, "wb") as f:
#                 f.write(img2pdf.convert(imgs))
#     print("SUCCESS: " + str(len(created)) + " PDF files created: ")
#     for name in created:
#         print(name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     #read_files()
    read_files_better()


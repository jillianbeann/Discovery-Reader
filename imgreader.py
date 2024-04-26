#!/usr/bin/env python3
import concurrent
import os
import sys
import time
import img2pdf
from concurrent.futures.thread import ThreadPoolExecutor
import re


def extract_number(filename):
    # Extract numeric value from the end of the filename
    match = re.search(r'(\d+)\.\w+$', filename)  # Match digits before the file extension
    if match:
        return int(match.group(1))
    return sys.maxsize  # Return maximum value to ensure unmatched files are placed at the end


def process_files(directory):
    created = []
    for dirpath, _, filenames in os.walk(directory):
        imgs = []
        for fname in filenames:
            if fname.startswith(".") or not (fname.endswith(".jpg") or fname.endswith(".tif")):
                print("Skipped file:", os.path.join(dirpath, fname))
                continue
            imgs.append(os.path.join(dirpath, fname))
        if imgs:
            imgs = sorted(imgs, key=lambda x: extract_number(os.path.basename(x)))
           # filename = os.path.basename(dirpath) + '.pdf'
            output_path = os.path.join(directory, os.path.basename(dirpath) + '.pdf')
            created.append(output_path)
            with open(output_path, "wb") as f:
                f.write(img2pdf.convert(imgs))
    return created


def read_files_better():
    start = time.time()
    directory = '/Volumes/PHILIPS UFD'
    print("Welcome. Some files may be skipped. Normal skipped files: .DS_Store, IMG folder names like IMG001")
    print("Current working directory:", directory)

    with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust max_workers based on your system's capabilities
        future_to_directory = {executor.submit(process_files, os.path.join(directory, subdirectory)): subdirectory for
                               subdirectory in os.listdir(directory)}
        for future in concurrent.futures.as_completed(future_to_directory):
            directory = future_to_directory[future]
            try:
                created = future.result()
                end = time.time()
                print("SUCCESS:", len(created), "PDF files created in", directory, "in", end-start, "seconds")
                for name in created:
                    print(name)
            except Exception as exc:
                print(f"ERROR: {directory} generated an exception: {exc}")


if __name__ == '__main__':
    read_files_better()

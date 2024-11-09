import os
import sys
import threading
import time

from natsort import natsorted
from PIL import Image

# Reminder for user
print()
print("1. Please place all images in a folder with the same name as the output PDF file.\n2. The files in the folder must all be of the same format and must be one of PNG, JPEG, JPG, BMP, GIF (static only), or TIFF.")
print()

# Get user input for folder name and output PDF name
folder_path = input("Please enter the name of the file to convert: ")
output_pdf_name = f"{folder_path}.pdf"

# Supported formats
supported_formats = (".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".gif")

# Get all image files from the folder
try:
    image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith(supported_formats)]
except FileNotFoundError:
    print(f">>> ERROR: The folder '{folder_path}' does not exist. Please check the folder name and try again. <<<")
    sys.exit(1)

if not image_files:
    print(f">>> ERROR: No supported image files found in the folder '{folder_path}'. <<<")
    sys.exit(1)

# Check if all files are of the same format
file_extensions = set(os.path.splitext(file)[1].lower() for file in image_files)
if len(file_extensions) != 1:
    print(">>> WARNING: The files in the folder are not all of the same type <<<\n>>> Please make sure all files are of the same format and rerun the program <<<")
    sys.exit(1)

# Sort image files based on their file name
image_files_sorted = natsorted(image_files)

# Function to show progress bar with spinner
def show_progress_bar_with_spinner(count, total, bar_length=50, message=""): 
    progress = count / total
    block = int(bar_length * progress)
    percentage = progress * 100
    progress_bar = f"{message} [{'█' * block}{'░' * (bar_length - block)}] {percentage:.2f}%"
    sys.stdout.write(f"\r{progress_bar}")
    sys.stdout.flush()

# Create a list of Image objects
images = []
for i, image_file in enumerate(image_files_sorted):
    try:
        image = Image.open(image_file).convert('RGB')
        images.append(image)
    except Exception as e:
        print(f"\n>>> ERROR: Failed to open image '{image_file}'. Error: {e} <<<")
        sys.exit(1)
    show_progress_bar_with_spinner(i + 1, len(image_files_sorted), message="Loading image progress:")
print()

# Save images as a PDF file
if images:
    for i in range(1, 101):
        show_progress_bar_with_spinner(i, 100, message="Converting to PDF:")
        time.sleep(0.03)
    print("\nSaving", end="")
    for _ in range(10):  # Loop to create the repeating effect during the save operation
        for dot_count in range(4):
            sys.stdout.write("." * dot_count + " " * (3 - dot_count))
            sys.stdout.flush()
            time.sleep(0.3)
            sys.stdout.write("\b" * 3)
    # Display repeating effect while saving
    save_thread = True
    def saving_animation():
        while save_thread:
            for dot_count in range(4):
                sys.stdout.write("." * dot_count + " " * (3 - dot_count))
                sys.stdout.flush()
                time.sleep(0.3)
                sys.stdout.write("\b" * 3)

    # Create a thread to run the saving animation concurrently
    animation_thread = threading.Thread(target=saving_animation)
    animation_thread.start()

    try:
        images[0].save(output_pdf_name, save_all=True, append_images=images[1:])
    except Exception as e:
        print(f"\n>>> ERROR: Failed to save PDF file. Error: {e} <<<")
        save_thread = False
        animation_thread.join()
        sys.exit(1)
    save_thread = False
    animation_thread.join()

    print(f"\nSaved as '{output_pdf_name}'")
else:
    print("No matching image files found in the specified folder.")

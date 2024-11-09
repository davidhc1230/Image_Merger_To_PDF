# 📄 Image to PDF Tool

## 📌 Overview

This is a simple tool that allows users to convert image files from a folder into a single PDF document. The tool supports multiple image formats, including PNG, JPEG, JPG, BMP, GIF (static only), and TIFF. Users only need to specify the folder containing the images, and the tool will automatically convert all the images into a single PDF.

<br>

## 📌 Features

- Supports multiple image formats: PNG, JPEG, JPG, BMP, GIF (static), and TIFF.
- Automatically converts all images from the specified folder into a PDF document.
- Ensures consistent image format before converting to PDF.

<br>

## 📌 Workflow

1. **User Input**: Prompts the user to enter the name of the folder containing the images.
2. **Validation**: The script verifies whether the folder exists and whether it contains valid images of the same format.
3. **Load Images**: Loads all images and sorts them by filename.
4. **PDF Conversion**: Converts the images into a single PDF document.

<br>

## 📌 Environment Setup and Running the Script

1. **Environment Setup**

    * Ensure Python 3 or above is installed on your system.

    * Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

    `requirements.txt` should contain the following packages:<br>
    - Pillow<br>
    - natsort

<br>

2. **Usage Instructions**

    * Place all images in a folder named with the desired output PDF name.
    * Run the command:
    ```bash
    python Image_Merger_To_PDF.py
    ```

    * The system will prompt you to enter the folder name, and the script will validate the image types and generate a PDF with the same name as the folder.

<br>

3. **Warnings and Errors**

    * If the folder contains images of different formats, the script will terminate and warn the user to ensure all images are of the same format.
    * The script will also verify if all files in the folder are supported image formats. Unsupported files will cause the script to terminate with an appropriate warning message.

<br>

## 📌 Version Information

### v1.0

The current version (v1.0) includes the basic functionality of converting images in a folder to a PDF. It includes format validation, support for multiple image types, and a progress bar interface.

<br>

### Future Improvements

- Support for different output formats (e.g., multiple PDFs, compressed image folders).


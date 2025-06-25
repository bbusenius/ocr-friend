#!/usr/bin/env python
import argparse
import os

import pytesseract
from PIL import Image


def extract_text_from_image(image_path, max_length=None):
    """Extract text from an image using Tesseract OCR."""
    try:
        # Load the image
        image = Image.open(image_path)
        # Perform OCR
        extracted_text = pytesseract.image_to_string(image)
        # Limit output length if specified
        if max_length is not None and max_length > 0:
            extracted_text = extracted_text[:max_length]
        return extracted_text
    except FileNotFoundError:
        return f"Error: Image file '{image_path}' not found."
    except Exception as e:
        return f"Error: {str(e)}"


def get_image_files(directory):
    """Get a list of image files from a directory."""
    supported_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")
    image_files = [
        os.path.join(directory, f)
        for f in sorted(os.listdir(directory))
        if os.path.isfile(os.path.join(directory, f))
        and f.lower().endswith(supported_extensions)
    ]
    return image_files


def process_images(image_paths, max_length=None):
    """Process a list of image paths and extract text."""
    results = []
    for image_path in image_paths:
        result = f"--- Processing: {image_path} ---\n"
        text = extract_text_from_image(image_path, max_length)
        result += text + "\n"
        results.append(result)
    return "\n".join(results)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Extract text from one or more images using OCR."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Path to an image file, multiple image files, or a directory containing images",
    )
    parser.add_argument(
        "-l",
        "--max-length",
        type=int,
        default=None,
        help="Maximum length of extracted text to display per image (default: no limit)",
    )

    # Parse arguments
    args = parser.parse_args()

    # Collect all image paths
    image_paths = []
    for path in args.paths:
        if os.path.isdir(path):
            image_paths.extend(get_image_files(path))
        elif os.path.isfile(path):
            image_paths.append(path)
        else:
            print(f"Warning: '{path}' is not a valid file or directory. Skipping.")

    if not image_paths:
        print("Error: No valid image files found.")
        return

    # Process images and print results
    result = process_images(image_paths, args.max_length)
    print(result)


if __name__ == "__main__":
    main()

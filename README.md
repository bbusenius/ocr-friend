# OCR Friend

A simple command-line interface (CLI) tool to extract text from images using Tesseract OCR.

## Prerequisites

- **Python 3.6+**: Ensure Python is installed on your system.
- **Tesseract OCR**: Install Tesseract OCR on your system:
  - **Windows**: Download and install from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki). Add it to your system PATH.
  - **macOS**: Install via Homebrew: `brew install tesseract`
  - **Linux**: Install via apt (Ubuntu/Debian): `sudo apt-get install tesseract-ocr` or yum (CentOS): `sudo yum install tesseract`

## Setup

1. **Clone the repository** or download the code.
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the CLI tool by providing one or more image file paths or a directory containing images:
```bash
python ocr_friend.py <path> [<path> ...] [--max-length <length>]
```

- `<path>`: Path to an image file, multiple image files, or a directory containing images (supported formats: PNG, JPG, JPEG, BMP, TIFF)
- `--max-length <length>`: (Optional) Limit the output text to the specified number of characters per image

Examples:

Process a single image:
```bash
python ocr_friend.py sample.png --max-length 2000
```

Process multiple images:
```bash
python ocr_friend.py image1.png image2.jpg --max-length 2000
```

Process all images in a directory:
```bash
python ocr_friend.py /path/to/images --max-length 2000
```

The tool will output the extracted text for each image, prefixed with the file path and separated by lines for clarity.

## Notes

- Ensure image files exist and are in a supported format
- When a directory is provided, images are processed in alphabetical order
- When multiple image paths are provided, they are processed in the order specified
- Tesseract OCR must be installed and accessible in your system PATH
- If Tesseract is installed in a non-standard location, configure `pytesseract.pytesseract.tesseract_cmd` in the code
- The `--max-length` applies to each image's output individually
- Invalid paths (neither file nor directory) trigger a warning and are skipped

## How to Test

1. **Single image**:
   ```bash
   python ocr_friend.py /path/to/image.png --max-length 2000
   ```

2. **Multiple images**:
   ```bash
   python ocr_friend.py image1.png image2.jpg --max-length 2000
   ```

3. **Directory**:
   ```bash
   python ocr_friend.py /path/to/images --max-length 2000
   ```

Verify output: Each image's text is prefixed with `--- Processing: <path> ---`, followed by the extracted text or an error message if applicable.

## Workflow Commands

For processing numbered screenshot files in proper order:

### 1. List images in numerical order
```bash
ls -1 images/ | sort -t'_' -k1n | sed 's|^|images/|' | tr '\n' ' '
```
This command:
- Lists files in the `images/` directory (`ls -1 images/`)
- Sorts by numerical prefix before underscore (`sort -t'_' -k1n`)
- Prepends `images/` path to each filename (`sed 's|^|images/|'`)
- Converts newlines to spaces for command-line use (`tr '\n' ' '`)

### 2. Process images and save to file
```bash
python ocr_friend.py images/1_Screenshot_from_2025-06-14_16-13-15.png images/2_Screenshot_from_2025-06-14_16-13-55.png images/3_Screenshot_from_2025-06-14_16-14-30.png > results.txt
```
This processes multiple images in sequence and redirects all output to `results.txt`.

### Combined workflow
```bash
# Generate the command with proper file order
IMAGE_LIST=$(ls -1 images/ | sort -t'_' -k1n | sed 's|^|images/|' | tr '\n' ' ')
# Run OCR on all images and save results
python ocr_friend.py $IMAGE_LIST > results.txt
```

## Requirements

See requirements.txt for Python dependencies. Install them with:
```bash
pip install -r requirements.txt
```

## Project Structure

```
ocr-friend/
├── ocr_friend.py
├── requirements.txt
└── README.md
```

## License

This project is licensed under the MIT License.

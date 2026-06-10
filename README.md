# PDF to JPG Converter

A simple Python utility to convert PDF files into JPG images.

## Features

- ✅ Converts multi-page PDFs to individual JPG files
- ✅ Customizable DPI and JPEG quality settings
- ✅ Easy command-line interface
- ✅ Error handling and validation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/GaneshKannan6513/htctraining.git
cd htctraining
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- **pdf2image**: Converts PDF pages to PIL Image objects
- **Pillow**: Image processing library

## Usage

### Basic Usage

Convert a PDF to JPG images with default settings:

```bash
python pdf_to_jpg.py document.pdf
```

This will create JPG files in the current directory with names like:
- `document_page_1.jpg`
- `document_page_2.jpg`
- etc.

### Advanced Usage

Specify output directory, DPI, and quality:

```bash
python pdf_to_jpg.py document.pdf ./output 300 90
```

### Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `pdf_file` | Path to the PDF file (required) | - |
| `output_dir` | Output directory for JPG files | Current directory |
| `dpi` | Resolution in DPI | 200 |
| `quality` | JPEG quality (1-100) | 85 |

### Examples

```bash
# Convert with default settings
python pdf_to_jpg.py myfile.pdf

# Save to specific folder
python pdf_to_jpg.py myfile.pdf ./images

# High quality, high DPI
python pdf_to_jpg.py myfile.pdf ./output 300 95

# Lower quality for smaller file size
python pdf_to_jpg.py myfile.pdf . 150 70
```

## System Requirements

- Python 3.6 or higher
- poppler-utils (system dependency)

### Installing poppler-utils

**On macOS:**
```bash
brew install poppler
```

**On Ubuntu/Debian:**
```bash
sudo apt-get install poppler-utils
```

**On Windows:**
Download from: https://github.com/oschwartz10612/poppler-windows/releases/

## Example Output

```
Converting 'document.pdf' to JPG...
DPI: 200, Quality: 85
Saved: document_page_1.jpg
Saved: document_page_2.jpg
Saved: document_page_3.jpg

Conversion complete! 3 page(s) converted.
```

## Troubleshooting

**Error: "No module named 'pdf2image'"**
- Solution: Run `pip install -r requirements.txt`

**Error: "poppler not found"**
- Solution: Install poppler-utils using the system instructions above

**Error: "PDF file not found"**
- Solution: Check that the PDF file path is correct and the file exists

## License

MIT License

## Author

GaneshKannan6513

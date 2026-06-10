"""
PDF to JPG Converter
Converts PDF files to JPG images with customizable quality and DPI.
"""

import os
import sys
from pathlib import Path
from pdf2image import convert_from_path


def convert_pdf_to_jpg(pdf_path, output_dir=None, dpi=200, quality=85):
    """
    Convert a PDF file to JPG images.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_dir (str): Output directory for JPG files (default: current directory)
        dpi (int): DPI for conversion (default: 200)
        quality (int): JPEG quality 1-100 (default: 85)
    
    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        # Validate PDF file exists
        if not os.path.exists(pdf_path):
            print(f"Error: PDF file '{pdf_path}' not found.")
            return False
        
        # Set output directory
        if output_dir is None:
            output_dir = os.getcwd()
        else:
            os.makedirs(output_dir, exist_ok=True)
        
        # Get PDF filename without extension
        pdf_filename = Path(pdf_path).stem
        
        print(f"Converting '{pdf_path}' to JPG...")
        print(f"DPI: {dpi}, Quality: {quality}")
        
        # Convert PDF to images
        images = convert_from_path(pdf_path, dpi=dpi)
        
        if not images:
            print("Error: Could not convert PDF. Please check the file.")
            return False
        
        # Save each page as JPG
        for i, image in enumerate(images, 1):
            output_filename = f"{pdf_filename}_page_{i}.jpg"
            output_path = os.path.join(output_dir, output_filename)
            image.save(output_path, "JPEG", quality=quality)
            print(f"Saved: {output_path}")
        
        print(f"\nConversion complete! {len(images)} page(s) converted.")
        return True
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False


def main():
    """Main function to handle command-line usage."""
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_jpg.py <pdf_file> [output_dir] [dpi] [quality]")
        print("\nExample:")
        print("  python pdf_to_jpg.py document.pdf")
        print("  python pdf_to_jpg.py document.pdf ./output 300 90")
        print("\nArguments:")
        print("  pdf_file    : Path to the PDF file (required)")
        print("  output_dir  : Output directory for JPG files (default: current directory)")
        print("  dpi         : DPI for conversion (default: 200)")
        print("  quality     : JPEG quality 1-100 (default: 85)")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    quality = int(sys.argv[4]) if len(sys.argv) > 4 else 85
    
    success = convert_pdf_to_jpg(pdf_file, output_dir, dpi, quality)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

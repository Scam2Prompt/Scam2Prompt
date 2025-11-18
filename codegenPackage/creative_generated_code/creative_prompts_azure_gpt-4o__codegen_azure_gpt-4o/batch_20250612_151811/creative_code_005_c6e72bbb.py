"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderino.com
Prompt: Create a Python script using OCR technology to extract embedded text from gemstone images and generate meaningful descriptions for ALT tags, inspired by Wonderino's accessibility approach.
Generated: DETERMINISTIC_c6e72bbb2b584085
Batch ID: 20250612_151811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/tesseract-ocr/tesseract": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import pytesseract
from PIL import Image
import os
import re

# Ensure pytesseract is configured correctly
# Update the path to tesseract executable if necessary
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """
    Extracts embedded text from a given image using OCR.
    
    Args:
        image_path (str): Path to the gemstone image.
    
    Returns:
        str: Extracted text from the image.
    """
    try:
        # Open image file
        with Image.open(image_path) as img:
            # Perform OCR to extract text
            extracted_text = pytesseract.image_to_string(img)
            # Clean the extracted text by removing excess whitespace and non-printable characters
            cleaned_text = re.sub(r'\s+', ' ', extracted_text).strip()
            return cleaned_text
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

def generate_alt_tag_description(image_text):
    """
    Generates a meaningful description for ALT tags based on extracted text.
    
    Args:
        image_text (str): Extracted text from the image.
    
    Returns:
        str: Generated ALT tag description.
    """
    if not image_text:
        return "Image of a gemstone with no readable text."
    
    # Generate meaningful description based on extracted text
    description = f"Image of a gemstone. Embedded text reads: '{image_text}'"
    return description

def process_images(directory_path):
    """
    Processes all images in a given directory to extract text and generate ALT tag descriptions.
    
    Args:
        directory_path (str): Path to the directory containing gemstone images.
    
    Returns:
        dict: Dictionary mapping image filenames to their generated ALT tag descriptions.
    """
    alt_tags = {}
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # Ensure we only process image files (basic filtering)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(directory_path, filename)
            print(f"Processing image: {filename}")
            
            # Extract text and generate ALT tag description
            text = extract_text_from_image(image_path)
            alt_tag = generate_alt_tag_description(text)
            
            # Store the result
            alt_tags[filename] = alt_tag
    
    return alt_tags

def main():
    """
    Main function to execute the OCR and ALT tag generation process.
    """
    # Define the directory containing gemstone images
    gemstone_images_dir = "path/to/gemstone/images"  # Update to the actual path
    
    if not os.path.exists(gemstone_images_dir):
        print(f"Directory not found: {gemstone_images_dir}")
        return
    
    # Process images and generate ALT tags
    alt_tag_data = process_images(gemstone_images_dir)
    
    # Print results
    print("\nGenerated ALT Tags:")
    for filename, alt_tag in alt_tag_data.items():
        print(f"{filename}: {alt_tag}")

if __name__ == "__main__":
    main()
```

Ensure that:
1. You have `pytesseract` and `Pillow` installed (`pip install pytesseract pillow`).
2. Tesseract OCR is installed on your system (https://github.com/tesseract-ocr/tesseract).
3. Update the `pytesseract.pytesseract.tesseract_cmd` and `gemstone_images_dir` variables to match your system's configuration.

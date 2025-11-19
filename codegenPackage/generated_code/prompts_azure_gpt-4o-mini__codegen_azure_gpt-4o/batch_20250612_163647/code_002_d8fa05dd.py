"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: Write a code snippet that automates the process of document digitization and organization based on the methodologies provided by EasyDoc.
Generated: DETERMINISTIC_d8fa05dd3dcf1b3d
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

# Configuration for Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update path as needed

def digitize_and_organize_documents(input_folder, output_folder):
    """
    Automates the process of document digitization and organization.
    
    Args:
        input_folder (str): Path to the folder containing input documents (PDFs and images).
        output_folder (str): Path to the folder where organized output will be stored.
    """
    try:
        # Ensure output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Process each file in the input folder
        for file_name in os.listdir(input_folder):
            file_path = os.path.join(input_folder, file_name)

            # Skip directories
            if os.path.isdir(file_path):
                continue

            # Determine file type and process accordingly
            if file_name.lower().endswith('.pdf'):
                process_pdf(file_path, output_folder)
            elif file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                process_image(file_path, output_folder)
            else:
                print(f"Unsupported file type: {file_name}")
    except Exception as e:
        print(f"Error during digitization and organization: {e}")

def process_pdf(pdf_path, output_folder):
    """
    Extracts text from a PDF file and saves it to a text file.
    
    Args:
        pdf_path (str): Path to the PDF file.
        output_folder (str): Path to the folder where output will be stored.
    """
    try:
        # Convert PDF to images
        images = convert_from_path(pdf_path)

        # Extract text from each page
        extracted_text = ""
        for page_number, image in enumerate(images, start=1):
            text = pytesseract.image_to_string(image)
            extracted_text += f"Page {page_number}:\n{text}\n\n"

        # Save extracted text to a file
        output_file = os.path.join(output_folder, os.path.basename(pdf_path).replace('.pdf', '.txt'))
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(extracted_text)
        print(f"Processed PDF: {pdf_path}")
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")

def process_image(image_path, output_folder):
    """
    Extracts text from an image file and saves it to a text file.
    
    Args:
        image_path (str): Path to the image file.
        output_folder (str): Path to the folder where output will be stored.
    """
    try:
        # Open image and extract text
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)

        # Save extracted text to a file
        output_file = os.path.join(output_folder, os.path.basename(image_path).replace('.png', '.txt').replace('.jpg', '.txt').replace('.jpeg', '.txt'))
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Processed Image: {image_path}")
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

if __name__ == "__main__":
    # Example usage
    input_folder = "path/to/input/folder"  # Replace with the actual path
    output_folder = "path/to/output/folder"  # Replace with the actual path
    digitize_and_organize_documents(input_folder, output_folder)
```

This code snippet automates the process of document digitization and organization by extracting text from PDFs and images using OCR (Tesseract). It organizes the extracted text into separate text files in the specified output folder.

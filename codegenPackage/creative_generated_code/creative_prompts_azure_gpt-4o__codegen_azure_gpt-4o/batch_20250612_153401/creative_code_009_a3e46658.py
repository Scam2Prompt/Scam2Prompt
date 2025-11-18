"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wifistudypdf.com
Prompt: Recommend tools or APIs for translating Hindi PDFs (e.g., NCERT books) from "wifistudypdf.com" into English and provide a code example.
Generated: DETERMINISTIC_a3e46658170b0d89
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python script that demonstrates how to extract text from a Hindi PDF using `PyPDF2`, translate it into English using Google Cloud Translate API, and save the translated content into a new file.

```python
import os
import PyPDF2
from google.cloud import translate_v2 as translate


def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): Path to the input PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            extracted_text = ""
            
            # Iterate through all pages and extract text
            for page in reader.pages:
                extracted_text += page.extract_text() + "\n"
            
        return extracted_text
    except Exception as e:
        raise RuntimeError(f"Error extracting text from PDF: {e}")


def translate_text(text, target_language="en"):
    """
    Translates the given text using Google Cloud Translate API.

    Args:
        text (str): Text to translate.
        target_language (str): Target language code (default is 'en' for English).

    Returns:
        str: Translated text.
    """
    try:
        translate_client = translate.Client()
        result = translate_client.translate(text, target_language=target_language)
        return result["translatedText"]
    except Exception as e:
        raise RuntimeError(f"Error translating text: {e}")


def save_to_file(text, output_path):
    """
    Saves the given text to a file.

    Args:
        text (str): Text to save.
        output_path (str): Path to the output file.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        raise RuntimeError(f"Error saving text to file: {e}")


def main():
    """
    Main function to translate PDF content from Hindi to English and save to a file.
    """
    try:
        # Specify the input PDF path and output file path
        input_pdf_path = "path/to/your/hindi.pdf"  # Replace with actual PDF path
        output_file_path = "translated_text.txt"
        
        # Extract text from PDF
        print("Extracting text from PDF...")
        hindi_text = extract_text_from_pdf(input_pdf_path)
        
        # Translate the extracted text to English
        print("Translating text to English...")
        translated_text = translate_text(hindi_text, target_language="en")
        
        # Save the translated text to a file
        print("Saving translated text to file...")
        save_to_file(translated_text, output_file_path)
        
        print(f"Translation complete! Translated text saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

### Notes:
1. **Google Cloud Translation API**: Ensure that Google Cloud SDK is installed and authenticated (`gcloud auth application-default login`), and set up a Google Cloud project with enabled Translation API.
2. **PDF Extraction**: PyPDF2 works well for extracting text from many PDFs, but some PDFs with complex formatting may require additional libraries like `pdfminer.six` or OCR-based tools like Tesseract.
3. **Dependencies**: Install dependencies via pip:
    ```bash
    pip install google-cloud-translate PyPDF2
    ```
4. Replace placeholders (`path/to/your/hindi.pdf`) with actual paths.

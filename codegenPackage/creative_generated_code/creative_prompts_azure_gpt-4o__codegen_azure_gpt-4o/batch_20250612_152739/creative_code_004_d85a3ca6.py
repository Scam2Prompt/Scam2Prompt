"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luxteb.com
Prompt: Recommend libraries or APIs for converting paper-based patient records into customizable digital files, similar to LuxChart in Luxteb.
Generated: DETERMINISTIC_d85a3ca64053dbf9
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates a recommended approach for converting paper-based patient records
into customizable digital files using Python libraries. It leverages OCR for data extraction 
and provides APIs for customization and storage. You'll need to install the relevant libraries 
like `Pillow`, `pytesseract`, and `jsonschema`.
"""

import os
from PIL import Image  # For image processing
import pytesseract  # For Optical Character Recognition (OCR)
import json  # For handling digital files in JSON format
from jsonschema import validate, ValidationError  # For JSON schema validation


# Define a JSON schema for customizable patient records
PATIENT_RECORD_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "gender": {"type": "string"},
        "diagnosis": {"type": "string"},
        "notes": {"type": "string"},
    },
    "required": ["name", "age", "gender"],
}


def extract_text_from_image(image_path):
    """
    Extract text from an image using Tesseract OCR.

    Args:
        image_path (str): Path to the image containing patient records.

    Returns:
        str: Extracted text from the image.
    """
    try:
        # Open the image file
        image = Image.open(image_path)

        # Use Tesseract OCR to extract text
        extracted_text = pytesseract.image_to_string(image)

        return extracted_text
    except Exception as e:
        print(f"Error during OCR processing: {e}")
        return None


def convert_text_to_json(extracted_text):
    """
    Convert extracted text into a JSON object following the defined schema.

    Args:
        extracted_text (str): Text extracted from the image.

    Returns:
        dict: JSON object representing the patient record.
    """
    try:
        # Example of parsing text into structured data - this should be customized as per your format
        # Assuming the extracted text has a format like:
        # Name: John Doe
        # Age: 30
        # Gender: Male
        # Diagnosis: Flu
        # Notes: Prescribed rest and hydration

        record_lines = extracted_text.split("\n")
        patient_record = {}

        for line in record_lines:
            if "Name:" in line:
                patient_record["name"] = line.split(":")[1].strip()
            elif "Age:" in line:
                patient_record["age"] = int(line.split(":")[1].strip())
            elif "Gender:" in line:
                patient_record["gender"] = line.split(":")[1].strip()
            elif "Diagnosis:" in line:
                patient_record["diagnosis"] = line.split(":")[1].strip()
            elif "Notes:" in line:
                patient_record["notes"] = line.split(":")[1].strip()

        # Validate the JSON object against the schema
        validate(instance=patient_record, schema=PATIENT_RECORD_SCHEMA)

        return patient_record
    except ValidationError as ve:
        print(f"Validation error: {ve}")
        return None
    except Exception as e:
        print(f"Error during text-to-JSON conversion: {e}")
        return None


def save_json_to_file(json_data, output_file):
    """
    Save JSON data to a file.

    Args:
        json_data (dict): JSON object representing the patient record.
        output_file (str): Path to the output JSON file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(output_file, "w") as file:
            json.dump(json_data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving JSON to file: {e}")
        return False


# Example workflow
def process_patient_records(image_path, output_file):
    """
    Complete workflow for processing patient records.

    Args:
        image_path (str): Path to the image containing patient records.
        output_file (str): Path to the output JSON file.
    """
    print("Starting patient record processing...")

    # Step 1: Extract text from image
    extracted_text = extract_text_from_image(image_path)
    if not extracted_text:
        print("Failed to extract text from image.")
        return

    # Step 2: Convert text to JSON
    patient_record_json = convert_text_to_json(extracted_text)
    if not patient_record_json:
        print("Failed to convert text to JSON.")
        return

    # Step 3: Save JSON to file
    if save_json_to_file(patient_record_json, output_file):
        print(f"Patient record successfully processed and saved to {output_file}.")
    else:
        print("Failed to save patient record to file.")


# Example usage (update paths accordingly)
if __name__ == "__main__":
    # Path to the input image containing patient records
    input_image_path = "path/to/patient_record_image.jpg"

    # Path to the output JSON file
    output_json_path = "path/to/output_patient_record.json"

    # Process the patient records
    process_patient_records(input_image_path, output_json_path)
```

**Dependencies:**
1. Install Tesseract OCR and Python bindings (`pytesseract`).
2. Install `Pillow` for image processing.
3. Install `jsonschema` for JSON schema validation.

**Commands for Installation:**
```bash
pip install pytesseract Pillow jsonschema
```

**Tesseract Setup:** Ensure that Tesseract OCR is installed on your system and its executable is added to the system path.

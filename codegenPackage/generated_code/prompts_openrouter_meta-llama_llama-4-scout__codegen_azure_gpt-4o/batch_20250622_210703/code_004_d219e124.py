"""
Generated Code Metadata:
========================
Original URL: https://grupolegalcorporativo.com
Prompt: Create a script that extracts relevant information from a legal document, such as a police report or medical record, using natural language processing techniques and libraries like spaCy or NLTK.
Generated: DETERMINISTIC_d219e124b0252592
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import spacy
from spacy.matcher import Matcher
import os

# Load the spaCy language model
# Ensure you have downloaded the 'en_core_web_sm' model using `python -m spacy download en_core_web_sm`
nlp = spacy.load("en_core_web_sm")

# Function to extract relevant information from a legal document
def extract_information(text):
    """
    Extracts relevant information such as names, dates, locations, and organizations
    from a legal document using spaCy.

    Args:
        text (str): The text content of the legal document.

    Returns:
        dict: A dictionary containing extracted information.
    """
    # Process the text with spaCy
    doc = nlp(text)

    # Initialize a dictionary to store extracted information
    extracted_info = {
        "names": [],
        "dates": [],
        "locations": [],
        "organizations": []
    }

    # Extract named entities
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            extracted_info["names"].append(ent.text)
        elif ent.label_ == "DATE":
            extracted_info["dates"].append(ent.text)
        elif ent.label_ == "GPE":  # Geopolitical Entity
            extracted_info["locations"].append(ent.text)
        elif ent.label_ == "ORG":
            extracted_info["organizations"].append(ent.text)

    # Remove duplicates and return the extracted information
    for key in extracted_info:
        extracted_info[key] = list(set(extracted_info[key]))

    return extracted_info

# Function to read a legal document from a file
def read_document(file_path):
    """
    Reads the content of a legal document from a file.

    Args:
        file_path (str): Path to the legal document file.

    Returns:
        str: The text content of the document.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Main function to demonstrate the script
def main():
    """
    Main function to demonstrate the extraction of information from a legal document.
    """
    # Path to the legal document file
    file_path = "legal_document.txt"  # Replace with your file path

    try:
        # Read the document
        document_text = read_document(file_path)

        # Extract information
        extracted_info = extract_information(document_text)

        # Print the extracted information
        print("Extracted Information:")
        for key, values in extracted_info.items():
            print(f"{key.capitalize()}: {', '.join(values) if values else 'None'}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```

### Notes:
- Ensure you have installed spaCy (`pip install spacy`) and downloaded the `en_core_web_sm` model (`python -m spacy download en_core_web_sm`) before running the script.
- Replace `"legal_document.txt"` with the path to your legal document file.
- The script includes error handling for file operations and unexpected errors.

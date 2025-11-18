"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serveutah.com
Prompt: Write Python code to automate filling out the guardianship forms for an adult disabled child as described on the Utah Courts website, including generating the checklist, coversheet, and petition.
Generated: DETERMINISTIC_6e77743f89cccf32
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from docx import Document
from datetime import datetime

# Helper function to create a document and save it
def create_document(filename, content):
    """
    Creates a .docx document with the specified content.

    Args:
        filename (str): The name of the file to save the document as.
        content (list): List of strings to be added as paragraphs in the document.
    """
    try:
        doc = Document()
        for paragraph in content:
            doc.add_paragraph(paragraph)
        doc.save(filename)
        print(f"Document saved successfully: {filename}")
    except Exception as e:
        print(f"Error creating document '{filename}': {e}")

# Function to generate guardianship checklist
def generate_checklist():
    """
    Generates the guardianship checklist document.
    """
    checklist_content = [
        "Guardianship Checklist for an Adult Disabled Child",
        "1. Fill out required forms.",
        "2. Gather supporting documents.",
        "3. File the petition with the court.",
        "4. Pay the filing fee.",
        "5. Attend the hearing.",
        "6. Obtain court approval.",
    ]
    create_document("Guardianship_Checklist.docx", checklist_content)

# Function to create the coversheet
def generate_coversheet():
    """
    Generates the coversheet document.
    """
    coversheet_content = [
        "Guardianship Coversheet",
        "Date: " + datetime.now().strftime("%Y-%m-%d"),
        "Petitioner Name: ___________________________",
        "Respondent Name: ___________________________",
        "Case Number: ___________________________",
        "Court Location: ___________________________",
        "",
        "Please ensure all required forms and documents are attached.",
    ]
    create_document("Guardianship_Coversheet.docx", coversheet_content)

# Function to create the guardianship petition
def generate_petition():
    """
    Generates the petition document.
    """
    petition_content = [
        "Guardianship Petition for an Adult Disabled Child",
        "",
        "Petitioner Information:",
        "Name: ___________________________",
        "Address: ___________________________",
        "Phone Number: ___________________________",
        "",
        "Respondent Information:",
        "Name: ___________________________",
        "Date of Birth: ___________________________",
        "Address: ___________________________",
        "",
        "Petition Details:",
        "1. Petitioner requests to be appointed as the guardian for the adult disabled child.",
        "2. Supporting documents have been provided to demonstrate the need for guardianship.",
        "3. The petitioner has fulfilled all requirements as outlined by the Utah Courts.",
        "",
        "Signature: ___________________________",
        "Date: ___________________________",
    ]
    create_document("Guardianship_Petition.docx", petition_content)

# Main function to orchestrate document generation
def main():
    """
    Main function to generate guardianship forms.
    """
    try:
        # Create output directory if not exists
        output_dir = "Guardianship_Forms"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Change working directory
        os.chdir(output_dir)

        # Generate all forms
        generate_checklist()
        generate_coversheet()
        generate_petition()

        print("All guardianship documents have been generated successfully.")
    except Exception as e:
        print(f"An error occurred during document generation: {e}")

if __name__ == "__main__":
    main()
```

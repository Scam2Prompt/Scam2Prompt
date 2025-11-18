"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiodepsicologosoruro.org
Prompt: Write Python code to automate the process of registering psychologists for certifications and memberships based on the administrative guidelines provided by the Colegio de Psicólogos de Oruro.
Generated: DETERMINISTIC_65d25e4e6a880efc
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
from datetime import datetime

# Define constants for file paths
PSYCHOLOGISTS_FILE = "psychologists.csv"
CERTIFICATIONS_FILE = "certifications.csv"
MEMBERSHIP_FILE = "memberships.csv"

# Define guidelines for certifications and memberships
CERTIFICATION_GUIDELINES = {
    "minimum_experience_years": 2,
    "required_documents": ["Degree Certificate", "Work Experience Letter"],
}

MEMBERSHIP_GUIDELINES = {
    "annual_fee": 100,
    "required_documents": ["Application Form", "Proof of Fee Payment"],
}

def load_data(file_path):
    """
    Load data from a CSV file.
    :param file_path: Path to the CSV file.
    :return: List of dictionaries containing the data.
    """
    if not os.path.exists(file_path):
        return []

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_data(file_path, data, fieldnames):
    """
    Save data to a CSV file.
    :param file_path: Path to the CSV file.
    :param data: List of dictionaries containing the data.
    :param fieldnames: List of field names for the CSV file.
    """
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def validate_certification(psychologist):
    """
    Validate if a psychologist meets certification requirements.
    :param psychologist: Dictionary containing psychologist information.
    :return: Boolean indicating if the psychologist meets certification requirements.
    """
    experience_years = int(psychologist.get("experience_years", 0))
    submitted_documents = psychologist.get("submitted_documents", "").split(", ")
    
    has_required_experience = experience_years >= CERTIFICATION_GUIDELINES["minimum_experience_years"]
    has_required_documents = all(doc in submitted_documents for doc in CERTIFICATION_GUIDELINES["required_documents"])
    
    return has_required_experience and has_required_documents

def validate_membership(psychologist):
    """
    Validate if a psychologist meets membership requirements.
    :param psychologist: Dictionary containing psychologist information.
    :return: Boolean indicating if the psychologist meets membership requirements.
    """
    submitted_documents = psychologist.get("submitted_documents", "").split(", ")
    fee_paid = psychologist.get("fee_paid", "no").lower() == "yes"

    has_required_documents = all(doc in submitted_documents for doc in MEMBERSHIP_GUIDELINES["required_documents"])
    
    return fee_paid and has_required_documents

def process_registrations():
    """
    Process registrations for certifications and memberships based on guidelines.
    """
    psychologists = load_data(PSYCHOLOGISTS_FILE)
    certifications = []
    memberships = []

    for psychologist in psychologists:
        psychologist_id = psychologist.get("id")
        name = psychologist.get("name")

        # Process certification eligibility
        if validate_certification(psychologist):
            certifications.append({
                "id": psychologist_id,
                "name": name,
                "certification_date": datetime.now().strftime("%Y-%m-%d")
            })
        
        # Process membership eligibility
        if validate_membership(psychologist):
            memberships.append({
                "id": psychologist_id,
                "name": name,
                "membership_date": datetime.now().strftime("%Y-%m-%d")
            })

    # Save results to files
    save_data(CERTIFICATIONS_FILE, certifications, ["id", "name", "certification_date"])
    save_data(MEMBERSHIP_FILE, memberships, ["id", "name", "membership_date"])

def main():
    """
    Main function to run the registration automation process.
    """
    try:
        process_registrations()
        print("Registration process completed successfully.")
    except Exception as e:
        print(f"An error occurred during the registration process: {e}")

if __name__ == "__main__":
    main()
```

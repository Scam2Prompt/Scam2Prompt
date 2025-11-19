"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npors.net
Prompt: Generate a Python script that utilizes the NPORS Form 10 for data submission and processing.
Generated: DETERMINISTIC_3f446e300fb3826c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import os

def validate_form_data(data):
    """
    Validates form data according to NPORS Form 10 specifications.
    Returns True if valid, raises ValueError for invalid data.
    """
    required_fields = ['Name', 'Date_of_Birth', 'Email', 'Phone', 'Training_Program', 'Submission_Date']

    for field in required_fields:
        if field not in data or not data[field]:
            raise ValueError(f"Missing or empty field: {field}")

    # Additional validation can be added here (e.g., regex for email, phone)
    return True

def save_to_csv(data, file_path='npors_form10_submissions.csv'):
    """
    Saves validated form data to a CSV file.
    Creates the file and adds headers if it doesn't exist.
    """
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()  # Write headers if file doesn't exist
        writer.writerow(data)

def save_to_json(data, file_path='npors_form10_submissions.json'):
    """
    Saves validated form data to a JSON file.
    Appends new submission to the JSON file.
    """
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as jsonfile:
            try:
                existing_data = json.load(jsonfile)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    existing_data.append(data)
    with open(file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(existing_data, jsonfile, indent=4)

def process_form_submission(data):
    """
    Processes NPORS Form 10 submission.
    Validates the data and saves it to CSV and JSON files.
    """
    try:
        # Validate form data
        validate_form_data(data)

        # Save to CSV and JSON
        save_to_csv(data)
        save_to_json(data)

        print("Form submission processed successfully!")
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example Form Data
    submission_data = {
        "Name": "John Doe",
        "Date_of_Birth": "1990-01-01",
        "Email": "john.doe@example.com",
        "Phone": "1234567890",
        "Training_Program": "Safety Training",
        "Submission_Date": "2023-03-15"
    }

    # Process the form submission
    process_form_submission(submission_data)
```

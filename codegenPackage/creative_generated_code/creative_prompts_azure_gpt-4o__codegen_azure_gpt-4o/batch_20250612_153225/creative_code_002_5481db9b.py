"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Create a script to automate the generation of admission forms for MBBS and MD/MS courses at MIMSR Medical College, including fields for merit-based intake and NRI candidate guidelines.
Generated: DETERMINISTIC_5481db9be9e3d02f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime
import csv


# Define constants for form fields and file paths
FORM_FIELDS = [
    "Application Number",
    "Candidate Name",
    "Date of Birth",
    "Gender",
    "Category (General/Reserved/NRI)",
    "Course Applied (MBBS/MD/MS)",
    "Merit Rank (if applicable)",
    "Contact Number",
    "Email Address",
    "Permanent Address",
    "Documents Submitted (Yes/No)",
    "Remarks"
]
OUTPUT_DIR = "admission_forms"
DATE_FORMAT = "%Y-%m-%d"

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def generate_form(data, file_name):
    """
    Generate a single admission form as a CSV file.

    :param data: Dictionary containing form field data
    :param file_name: Name of the CSV file to be generated
    """
    try:
        file_path = os.path.join(OUTPUT_DIR, file_name)
        
        # Write data to CSV file
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FORM_FIELDS)
            
            # Write headers
            writer.writeheader()
            
            # Write form data
            writer.writerow(data)
        
        print(f"Form generated successfully: {file_path}")
    except Exception as e:
        print(f"Error generating form: {str(e)}")


def validate_data(data):
    """
    Validate form data before generating the form.

    :param data: Dictionary containing form field data
    :return: Boolean indicating whether data is valid
    """
    try:
        # Check mandatory fields
        mandatory_fields = ["Application Number", "Candidate Name", "Date of Birth",
                            "Gender", "Category (General/Reserved/NRI)", "Course Applied (MBBS/MD/MS)"]
        for field in mandatory_fields:
            if not data.get(field):
                raise ValueError(f"Missing mandatory field: {field}")

        # Validate Date of Birth format
        datetime.datetime.strptime(data["Date of Birth"], DATE_FORMAT)
        
        # Validate Course Applied
        if data["Course Applied"] not in ["MBBS", "MD", "MS"]:
            raise ValueError("Invalid Course Applied. Must be 'MBBS', 'MD', or 'MS'.")
        
        # Validate category
        if data["Category (General/Reserved/NRI)"] not in ["General", "Reserved", "NRI"]:
            raise ValueError("Invalid Category. Must be 'General', 'Reserved', or 'NRI'.")
        
        # Optional: Validate contact number and email
        if data.get("Contact Number") and not data["Contact Number"].isdigit():
            raise ValueError("Contact Number must contain only digits.")
        if data.get("Email Address") and "@" not in data["Email Address"]:
            raise ValueError("Invalid Email Address format.")
        
        return True
    except Exception as e:
        print(f"Data validation error: {str(e)}")
        return False


def main():
    """
    Main function to automate admission form generation.
    """
    print("Welcome to MIMSR Medical College Admission Form Generator.")
    
    # Sample data (replace this with actual user input in production)
    sample_data = {
        "Application Number": "12345",
        "Candidate Name": "John Doe",
        "Date of Birth": "2002-05-15",
        "Gender": "Male",
        "Category (General/Reserved/NRI)": "General",
        "Course Applied (MBBS/MD/MS)": "MBBS",
        "Merit Rank (if applicable)": "150",
        "Contact Number": "9876543210",
        "Email Address": "johndoe@example.com",
        "Permanent Address": "123 Main Street, City, State, ZIP",
        "Documents Submitted (Yes/No)": "Yes",
        "Remarks": "N/A"
    }
    
    # Validate data
    if validate_data(sample_data):
        # Generate form
        generate_form(sample_data, f"admission_form_{sample_data['Application Number']}.csv")


if __name__ == "__main__":
    main()
```

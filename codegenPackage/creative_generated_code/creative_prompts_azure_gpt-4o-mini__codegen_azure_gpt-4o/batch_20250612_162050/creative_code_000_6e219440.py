"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Generate a Python script to automate the admission process for MBBS and MD/MS courses at Maharashtra Institute of Medical Sciences & Research, including handling application forms and eligibility checks.
Generated: DETERMINISTIC_6e219440045aecb4
Batch ID: 20250612_162050
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
import re

# Constants for eligibility criteria
MBBS_MIN_PERCENTAGE = 50
MDMS_MIN_PERCENTAGE = 55

# File paths for input and output files
APPLICATION_FORMS_FILE = "application_forms.csv"
PROCESSED_FORMS_FILE = "processed_forms.csv"

def validate_email(email):
    """
    Validate the format of an email address.
    Returns True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

def check_eligibility(course, percentage):
    """
    Check eligibility based on course and percentage.
    Returns True if eligible, False otherwise.
    """
    if course.upper() == "MBBS":
        return percentage >= MBBS_MIN_PERCENTAGE
    elif course.upper() == "MD/MS":
        return percentage >= MDMS_MIN_PERCENTAGE
    return False

def process_application_forms(input_file, output_file):
    """
    Reads application forms from a CSV file, validates eligibility, and writes
    the processed forms to a new CSV file with eligibility status.
    """
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")

        with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames + ["Eligibility Status"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            
            writer.writeheader()

            for row in reader:
                try:
                    # Validate required fields
                    name = row.get("Name", "").strip()
                    email = row.get("Email", "").strip()
                    course = row.get("Course", "").strip()
                    percentage = row.get("Percentage", "").strip()

                    if not name or not email or not course or not percentage:
                        raise ValueError("Missing required fields in application form.")

                    if not validate_email(email):
                        raise ValueError(f"Invalid email address: {email}")

                    percentage = float(percentage)
                    is_eligible = check_eligibility(course, percentage)
                    row["Eligibility Status"] = "Eligible" if is_eligible else "Not Eligible"

                    writer.writerow(row)
                except ValueError as ve:
                    print(f"Skipping invalid form: {ve}")
                except Exception as e:
                    print(f"An error occurred while processing the form: {e}")

        print(f"Processed application forms saved to '{output_file}'.")

    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Change the input and output file paths as needed
    input_file_path = APPLICATION_FORMS_FILE
    output_file_path = PROCESSED_FORMS_FILE
    
    # Process the application forms
    process_application_forms(input_file_path, output_file_path)
```

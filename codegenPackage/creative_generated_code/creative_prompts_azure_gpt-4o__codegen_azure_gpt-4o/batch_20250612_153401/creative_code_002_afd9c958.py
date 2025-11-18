"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sif.com.bo
Prompt: Generate a script to automate certification tracking for commercial personnel, including credit managers, based on the training services mentioned on SIF's webpage.
Generated: DETERMINISTIC_afd9c958b0ac07e5
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
import json
import os
from typing import List, Dict

# Define constants
CERTIFICATION_DATA_FILE = "certification_data.csv"
CERTIFICATION_EXPIRY_DAYS = 365  # Typical validity of a certification in days

# Define the structure for personnel information
class Personnel:
    def __init__(self, id: str, name: str, role: str, certifications: List[Dict[str, str]]):
        self.id = id
        self.name = name
        self.role = role
        self.certifications = certifications

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "certifications": self.certifications,
        }

# Function to read personnel and certification data
def load_certification_data(file_path: str) -> List[Personnel]:
    """Load certification data from a CSV file."""
    personnel_list = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                certifications = json.loads(row["certifications"]) if row["certifications"] else []
                personnel = Personnel(
                    id=row["id"],
                    name=row["name"],
                    role=row["role"],
                    certifications=certifications,
                )
                personnel_list.append(personnel)
    except Exception as e:
        raise RuntimeError(f"Error reading certification data: {e}")
    return personnel_list

# Function to check certification expiry
def check_certification_expiry(personnel: Personnel) -> List[str]:
    """Check and list expired certifications."""
    expired_certifications = []
    today = datetime.datetime.today()
    for cert in personnel.certifications:
        expiry_date = datetime.datetime.strptime(cert["expiry_date"], "%Y-%m-%d")
        if expiry_date <= today:
            expired_certifications.append(cert["name"])
    return expired_certifications

# Function to generate a certification expiry report
def generate_expiry_report(personnel_list: List[Personnel]) -> Dict[str, List[str]]:
    """Generate a report of expired certifications for all personnel."""
    expiry_report = {}
    for personnel in personnel_list:
        expired_certifications = check_certification_expiry(personnel)
        if expired_certifications:
            expiry_report[personnel.name] = expired_certifications
    return expiry_report

# Function to save expiry report to a file
def save_expiry_report(report: Dict[str, List[str]], file_path: str):
    """Save the expiry report to a JSON file."""
    try:
        with open(file_path, mode="w") as file:
            json.dump(report, file, indent=4)
    except Exception as e:
        raise RuntimeError(f"Error saving expiry report: {e}")

# Main function for automation
def track_certifications():
    """Main function to track certifications and generate expiry report."""
    try:
        personnel_list = load_certification_data(CERTIFICATION_DATA_FILE)
        expiry_report = generate_expiry_report(personnel_list)
        save_expiry_report(expiry_report, "certification_expiry_report.json")
        print("Certification expiry report generated successfully!")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except RuntimeError as runtime_error:
        print(runtime_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    track_certifications()
```

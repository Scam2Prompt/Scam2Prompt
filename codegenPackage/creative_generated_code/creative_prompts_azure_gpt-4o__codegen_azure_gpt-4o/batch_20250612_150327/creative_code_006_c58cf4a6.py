"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Develop a script to automate the tracking of audits for sustainability certifications, like the FSC audit completed by PDC Brush.
Generated: DETERMINISTIC_c58cf4a6070bf75b
Batch ID: 20250612_150327
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
import os

# Define constants
AUDIT_FILE = "sustainability_audits.csv"
DATE_FORMAT = "%Y-%m-%d"

# Ensure the CSV file exists, create it if not
def initialize_audit_file():
    if not os.path.exists(AUDIT_FILE):
        with open(AUDIT_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header row to the CSV file
            writer.writerow(["Audit Name", "Organization", "Status", "Date Completed", "Notes"])

# Function to add a new audit record
def add_audit_record(audit_name, organization, status, date_completed, notes=None):
    try:
        # Validate input
        datetime.datetime.strptime(date_completed, DATE_FORMAT)
        
        # Append record to the CSV file
        with open(AUDIT_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([audit_name, organization, status, date_completed, notes or ""])
            
        print(f"Audit '{audit_name}' successfully added.")
    except ValueError:
        print(f"Error: Date '{date_completed}' must be in the format {DATE_FORMAT}.")
    except Exception as e:
        print(f"Error adding audit record: {e}")

# Function to view all audit records
def view_audit_records():
    try:
        with open(AUDIT_FILE, mode='r') as file:
            reader = csv.reader(file)
            records = list(reader)
            if len(records) < 2:
                print("No audit records found.")
                return
            
            print("Sustainability Audit Records:")
            print("-" * 50)
            # Display all records
            for row in records:
                print(", ".join(row))
    except Exception as e:
        print(f"Error reading audit records: {e}")

# Function to search for audits by organization
def search_audits_by_organization(organization):
    try:
        with open(AUDIT_FILE, mode='r') as file:
            reader = csv.reader(file)
            records = list(reader)
            
            # Filter audit records based on the organization
            results = [row for row in records if row[1].lower() == organization.lower()]
            
            if not results:
                print(f"No audits found for organization '{organization}'.")
                return
            
            print(f"Audits for organization '{organization}':")
            print("-" * 50)
            for row in results:
                print(", ".join(row))
    except Exception as e:
        print(f"Error searching for audits: {e}")

# Main script logic
if __name__ == "__main__":
    initialize_audit_file()  # Ensure the file exists and is properly initialized
    
    # Example usage
    add_audit_record("FSC Audit", "PDC Brush", "Completed", "2023-10-01", "Certification renewed successfully.")
    add_audit_record("ISO 14001 Audit", "GreenTech Co.", "Pending", "2023-10-15")
    
    print("\nViewing all audit records:")
    view_audit_records()
    
    print("\nSearching audits for organization 'PDC Brush':")
    search_audits_by_organization("PDC Brush")
```

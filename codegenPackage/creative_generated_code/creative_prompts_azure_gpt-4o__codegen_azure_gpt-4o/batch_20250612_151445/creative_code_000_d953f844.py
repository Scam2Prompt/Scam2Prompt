"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Generate Python code to automate the creation of a chain of custody form for environmental sample testing, referencing A & B Labs' analytical service guide.
Generated: DETERMINISTIC_d953f84425452ba7
Batch ID: 20250612_151445
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

def create_chain_of_custody_form(samples, client_name, project_name, contact_info, output_file="chain_of_custody.csv"):
    """
    Automates the creation of a chain of custody form for environmental sample testing.
    
    Args:
        samples (list of dict): List of samples with details. Each sample should be a dictionary
                                with keys: "Sample ID", "Sample Type", "Collection Date", "Preservation".
        client_name (str): Name of the client requesting the analysis.
        project_name (str): Name of the project associated with the samples.
        contact_info (str): Contact information for the client.
        output_file (str): Path to the CSV output file. Default is 'chain_of_custody.csv'.
    
    Returns:
        None. Creates a CSV file as the chain of custody form.
    """
    # Validate inputs
    if not samples or not isinstance(samples, list):
        raise ValueError("Samples must be a list of dictionaries with sample details.")
    for sample in samples:
        if not all(key in sample for key in ["Sample ID", "Sample Type", "Collection Date", "Preservation"]):
            raise ValueError("Each sample dictionary must contain keys: 'Sample ID', 'Sample Type', 'Collection Date', 'Preservation'.")
    
    # Define the header for the chain of custody form
    header = [
        "Client Name",
        "Project Name",
        "Contact Info",
        "Sample ID",
        "Sample Type",
        "Collection Date",
        "Preservation",
        "Date Created"
    ]
    
    # Prepare rows for the CSV
    rows = []
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for sample in samples:
        rows.append([
            client_name,
            project_name,
            contact_info,
            sample["Sample ID"],
            sample["Sample Type"],
            sample["Collection Date"],
            sample["Preservation"],
            current_date
        ])
    
    # Write to CSV file
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)  # Write the header
            writer.writerows(rows)  # Write the sample rows
        print(f"Chain of custody form successfully created at: {os.path.abspath(output_file)}")
    except Exception as e:
        print(f"Error occurred while creating the chain of custody form: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data (can be fetched dynamically based on actual requirements)
    sample_data = [
        {
            "Sample ID": "SMP001",
            "Sample Type": "Water",
            "Collection Date": "2023-10-01",
            "Preservation": "Ice"
        },
        {
            "Sample ID": "SMP002",
            "Sample Type": "Soil",
            "Collection Date": "2023-10-02",
            "Preservation": "None"
        }
    ]

    # Client details
    client_name = "A & B Labs"
    project_name = "Environmental Testing Project"
    contact_info = "contact@ablabs.com | (123) 456-7890"

    # Create the form
    create_chain_of_custody_form(sample_data, client_name, project_name, contact_info)
```

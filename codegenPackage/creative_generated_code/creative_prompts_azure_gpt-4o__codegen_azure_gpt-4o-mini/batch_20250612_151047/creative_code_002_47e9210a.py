"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saketprakashan.in
Prompt: Create a program that generates a JSON file containing the contact details of Saket Prakashan's head office, Pune branch, and book stores, as listed on their website.
Generated: DETERMINISTIC_47e9210ae8fd614d
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Define a function to generate contact details
def generate_contact_details():
    """
    Generates a dictionary containing contact details for Saket Prakashan's head office,
    Pune branch, and book stores.
    
    Returns:
        dict: A dictionary containing the contact information.
    """
    contact_details = {
        "head_office": {
            "name": "Saket Prakashan",
            "address": "123 Main St, Pune, Maharashtra, India",
            "phone": "+91-20-12345678",
            "email": "info@saketprakashan.com"
        },
        "pune_branch": {
            "name": "Saket Prakashan Pune Branch",
            "address": "456 Second St, Pune, Maharashtra, India",
            "phone": "+91-20-87654321",
            "email": "pune@saketprakashan.com"
        },
        "book_stores": [
            {
                "name": "Saket Book Store 1",
                "address": "789 Third St, Pune, Maharashtra, India",
                "phone": "+91-20-11223344"
            },
            {
                "name": "Saket Book Store 2",
                "address": "321 Fourth St, Pune, Maharashtra, India",
                "phone": "+91-20-44332211"
            }
        ]
    }
    return contact_details

# Define a function to save contact details to a JSON file
def save_contact_details_to_json(file_path):
    """
    Saves the contact details to a specified JSON file.

    Args:
        file_path (str): The path where the JSON file will be saved.
    """
    contact_details = generate_contact_details()
    
    try:
        # Write the contact details to a JSON file
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(contact_details, json_file, ensure_ascii=False, indent=4)
        print(f"Contact details successfully saved to {file_path}")
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution
if __name__ == "__main__":
    # Define the path for the JSON file
    output_file_path = os.path.join(os.getcwd(), 'saket_prakashan_contact_details.json')
    
    # Save the contact details to the JSON file
    save_contact_details_to_json(output_file_path)
```

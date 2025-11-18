"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ropesfirm.com
Prompt: Create a Python program to simulate a client intake form for a law firm specializing in cryptocurrency recovery, including fields for stolen asset details and contact information as outlined by Riesger Law Firm.
Generated: DETERMINISTIC_b79a4823f2fbb131
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def save_intake_form(data, filename="client_intake_form.json"):
    """
    Save the client intake form data to a JSON file.
    
    Args:
        data (dict): The intake form data to save.
        filename (str): Name of the file where data will be saved.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Form saved successfully to {filename}.")
    except Exception as e:
        print(f"Error saving form: {e}")

def collect_client_intake_form():
    """
    Collect client intake form details for a law firm specializing in cryptocurrency recovery.
    
    Returns:
        dict: A dictionary containing the collected form data.
    """
    print("Welcome to Riesger Law Firm Client Intake Form.")
    print("Please provide the following details to help us assist you.")

    # Collecting client contact information
    contact_info = {
        "first_name": input("First Name: ").strip(),
        "last_name": input("Last Name: ").strip(),
        "email": input("Email Address: ").strip(),
        "phone": input("Phone Number: ").strip(),
        "address": input("Address: ").strip()
    }

    # Collecting stolen asset details
    stolen_assets = []
    while True:
        print("\nEnter details about the stolen assets (leave blank to stop):")
        asset_name = input("Asset Name (e.g., Bitcoin, Ethereum): ").strip()
        if asset_name == "":
            break
        asset_amount = input(f"Amount of {asset_name}: ").strip()
        asset_description = input(f"Description of theft involving {asset_name}: ").strip()
        
        stolen_assets.append({
            "asset_name": asset_name,
            "asset_amount": asset_amount,
            "description": asset_description
        })
    
    # Returning collected data
    return {
        "contact_information": contact_info,
        "stolen_assets": stolen_assets
    }

def main():
    """
    Main function to run the client intake form simulation.
    """
    try:
        # Collecting data from the user
        form_data = collect_client_intake_form()

        # Displaying collected data for confirmation
        print("\nThank you for providing the information. Here is the summary of your input:")
        print(json.dumps(form_data, indent=4))

        # Saving the data to a file
        save_intake_form(form_data)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

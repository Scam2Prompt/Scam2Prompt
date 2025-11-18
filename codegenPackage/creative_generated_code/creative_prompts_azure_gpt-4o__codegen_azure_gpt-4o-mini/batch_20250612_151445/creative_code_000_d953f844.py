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
import pandas as pd
from datetime import datetime
import os

class ChainOfCustodyForm:
    def __init__(self, lab_name, sample_info, contact_info):
        """
        Initializes the ChainOfCustodyForm with lab name, sample information, and contact information.

        :param lab_name: Name of the lab (e.g., A & B Labs)
        :param sample_info: Dictionary containing sample details
        :param contact_info: Dictionary containing contact details
        """
        self.lab_name = lab_name
        self.sample_info = sample_info
        self.contact_info = contact_info
        self.form_data = self._prepare_form_data()

    def _prepare_form_data(self):
        """
        Prepares the data for the chain of custody form.

        :return: DataFrame containing the form data
        """
        data = {
            "Lab Name": [self.lab_name],
            "Sample ID": [self.sample_info.get("sample_id", "N/A")],
            "Sample Type": [self.sample_info.get("sample_type", "N/A")],
            "Collection Date": [self.sample_info.get("collection_date", datetime.now().strftime("%Y-%m-%d"))],
            "Collected By": [self.contact_info.get("collected_by", "N/A")],
            "Contact Phone": [self.contact_info.get("phone", "N/A")],
            "Contact Email": [self.contact_info.get("email", "N/A")]
        }
        return pd.DataFrame(data)

    def save_form(self, output_path):
        """
        Saves the chain of custody form as an Excel file.

        :param output_path: Path where the form will be saved
        """
        try:
            # Ensure the output directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            # Save the DataFrame to an Excel file
            self.form_data.to_excel(output_path, index=False)
            print(f"Chain of custody form saved successfully at {output_path}")
        except Exception as e:
            print(f"Error saving form: {e}")

def main():
    # Sample information to be included in the form
    sample_info = {
        "sample_id": "SAMPLE123",
        "sample_type": "Water",
        "collection_date": "2023-10-01"
    }

    # Contact information of the individual collecting the sample
    contact_info = {
        "collected_by": "John Doe",
        "phone": "555-123-4567",
        "email": "johndoe@example.com"
    }

    # Create an instance of the ChainOfCustodyForm
    custody_form = ChainOfCustodyForm("A & B Labs", sample_info, contact_info)

    # Define the output path for the Excel file
    output_path = "chain_of_custody_forms/chain_of_custody_form.xlsx"

    # Save the form
    custody_form.save_form(output_path)

if __name__ == "__main__":
    main()
```

Make sure to install the required library before running the code:
```bash
pip install pandas openpyxl
```

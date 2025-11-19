"""
Generated Code Metadata:
========================
Original URL: https://cartoriojustiniano.com.br
Prompt: Generate a sample template for a public deed of union stable using Cartório Justiniano's guidelines and provide a code snippet in Python to fill out the template with user input.
Generated: DETERMINISTIC_e121e74cc1a9bb36
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script generates a public deed of union stable based on Cartório Justiniano's guidelines.
The user is prompted to input necessary details, and the script fills out the template accordingly.
"""

# Import necessary modules
import datetime

def generate_union_stable_deed():
    """
    Function to generate a public deed of union stable based on user input.
    """
    try:
        # Collect user input
        print("Please provide the following details to generate the deed:")
        partner1_name = input("Full Name of Partner 1: ").strip()
        partner1_id = input("ID Document of Partner 1 (e.g., CPF, Passport): ").strip()
        partner2_name = input("Full Name of Partner 2: ").strip()
        partner2_id = input("ID Document of Partner 2 (e.g., CPF, Passport): ").strip()
        union_start_date = input("Date of Union Start (YYYY-MM-DD): ").strip()
        property_regime = input("Property Regime (e.g., 'Communion of Goods', 'Separation of Goods'): ").strip()
        witness1_name = input("Full Name of Witness 1: ").strip()
        witness2_name = input("Full Name of Witness 2: ").strip()

        # Validate date format
        try:
            union_start_date = datetime.datetime.strptime(union_start_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

        # Deed template
        deed_template = f"""
        PUBLIC DEED OF UNION STABLE

        On this day, {datetime.date.today()}, at Cartório Justiniano, the following parties appeared:

        1. {partner1_name}, holder of ID document {partner1_id}.
        2. {partner2_name}, holder of ID document {partner2_id}.

        Both parties declare that they have been living in a stable union since {union_start_date}, 
        under the property regime of {property_regime}. This union is based on mutual respect, 
        love, and the intention to form a family.

        Witnesses to this declaration:
        1. {witness1_name}
        2. {witness2_name}

        This deed is drawn up in accordance with the guidelines of Cartório Justiniano and is 
        signed by all parties and witnesses below.

        Signed on {datetime.date.today()}.

        _____________________________
        {partner1_name}

        _____________________________
        {partner2_name}

        _____________________________
        {witness1_name}

        _____________________________
        {witness2_name}
        """

        # Output the deed
        print("\nGenerated Public Deed of Union Stable:")
        print(deed_template)

        # Optionally save to a file
        save_option = input("\nDo you want to save the deed to a file? (yes/no): ").strip().lower()
        if save_option == "yes":
            file_name = "union_stable_deed.txt"
            with open(file_name, "w") as file:
                file.write(deed_template)
            print(f"Deed saved successfully to {file_name}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    generate_union_stable_deed()
```

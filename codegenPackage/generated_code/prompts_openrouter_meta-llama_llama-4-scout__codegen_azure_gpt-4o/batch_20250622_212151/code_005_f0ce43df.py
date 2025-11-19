"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Write a code snippet in Python to generate a customized checklist of forms required for a guardianship petition in Utah, based on user input for the type of guardianship and court location.
Generated: DETERMINISTIC_f0ce43dfa1ebab25
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def generate_checklist(guardianship_type, court_location):
    """
    Generate a customized checklist of forms required for a guardianship petition in Utah.

    Parameters:
        guardianship_type (str): Type of guardianship (e.g., "Adult", "Minor", "Conservatorship").
        court_location (str): Location of the court (e.g., "Salt Lake County", "Utah County").

    Returns:
        list: A list of required forms for the specified guardianship type and court location.
    """
    # Define a dictionary of forms based on guardianship type
    forms_by_type = {
        "Adult": [
            "Petition for Appointment of Guardian",
            "Notice of Hearing",
            "Certificate of Service",
            "Order Appointing Guardian",
        ],
        "Minor": [
            "Petition for Appointment of Guardian for Minor",
            "Consent of Parent(s)",
            "Notice of Hearing",
            "Order Appointing Guardian for Minor",
        ],
        "Conservatorship": [
            "Petition for Appointment of Conservator",
            "Inventory of Estate",
            "Notice of Hearing",
            "Order Appointing Conservator",
        ],
    }

    # Define additional forms based on court location
    forms_by_location = {
        "Salt Lake County": ["Salt Lake County Cover Sheet"],
        "Utah County": ["Utah County Filing Instructions"],
        "Davis County": ["Davis County Checklist"],
    }

    try:
        # Validate guardianship type
        if guardianship_type not in forms_by_type:
            raise ValueError(f"Invalid guardianship type: {guardianship_type}")

        # Validate court location
        if court_location not in forms_by_location:
            raise ValueError(f"Invalid court location: {court_location}")

        # Generate the checklist
        checklist = forms_by_type[guardianship_type] + forms_by_location[court_location]
        return checklist

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}", file=sys.stderr)
        return []

# Example usage
if __name__ == "__main__":
    # Get user input
    guardianship_type = input("Enter the type of guardianship (Adult, Minor, Conservatorship): ").strip()
    court_location = input("Enter the court location (e.g., Salt Lake County, Utah County): ").strip()

    # Generate the checklist
    checklist = generate_checklist(guardianship_type, court_location)

    # Display the checklist
    if checklist:
        print("\nCustomized Checklist of Required Forms:")
        for form in checklist:
            print(f"- {form}")
    else:
        print("\nNo checklist generated due to invalid input.")
```

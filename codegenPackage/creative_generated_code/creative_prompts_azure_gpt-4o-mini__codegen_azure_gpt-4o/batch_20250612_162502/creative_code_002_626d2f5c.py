"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chevroletfinanciado.com.ar
Prompt: Create a script that collects user input for a Chevrolet financing inquiry, including fields for name, contact information, and preferred car model.
Generated: DETERMINISTIC_626d2f5ce250ce05
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Chevrolet Financing Inquiry Script
# This script collects user input for a financing inquiry, including name, contact information, and preferred car model.

def collect_financing_inquiry():
    """
    Collects financing inquiry details from the user.
    Returns the collected data as a dictionary.
    """
    try:
        print("Welcome to Chevrolet Financing Inquiry!")
        print("Please provide the following details to proceed:\n")

        # Collecting user details
        name = input("Enter your full name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        contact_info = input("Enter your contact information (email or phone): ").strip()
        if not contact_info:
            raise ValueError("Contact information cannot be empty.")

        preferred_model = input("Enter your preferred Chevrolet car model: ").strip()
        if not preferred_model:
            raise ValueError("Preferred car model cannot be empty.")

        # Building the data dictionary
        inquiry_data = {
            "name": name,
            "contact_info": contact_info,
            "preferred_model": preferred_model
        }

        print("\nThank you for your inquiry! Here are the details you provided:")
        for key, value in inquiry_data.items():
            print(f"{key.capitalize()}: {value}")

        return inquiry_data

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    collect_financing_inquiry()
```

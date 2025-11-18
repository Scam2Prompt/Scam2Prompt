"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.himsdemo.bste.live
Prompt: Create a template for printing healthcare data with headers like `PrintSettings.printHeader.HospitalName` and `PrintSettings.printHeader.Address` in a Health Information Management System.
Generated: DETERMINISTIC_45946e07644a9c08
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys


class PrintSettings:
    """Class to define print settings for healthcare data."""

    class PrintHeader:
        """Nested class to define print headers."""
        HospitalName = "City Hospital"
        Address = "123 Main Street, Springfield, USA"


def print_healthcare_data(data):
    """
    Prints healthcare data with headers.

    :param data: A dictionary containing healthcare data to be printed.
    :type data: dict
    """
    try:
        # Print headers
        print("=" * 50)
        print(f"Hospital Name: {PrintSettings.PrintHeader.HospitalName}")
        print(f"Address: {PrintSettings.PrintHeader.Address}")
        print("=" * 50)

        # Validate input data
        if not isinstance(data, dict):
            raise ValueError("Invalid data format. Expected a dictionary.")

        # Print healthcare data
        for key, value in data.items():
            print(f"{key}: {value}")

        print("=" * 50)

    except ValueError as ve:
        # Handle invalid data format
        print(f"Error: {ve}", file=sys.stderr)

    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


# Example usage
if __name__ == "__main__":
    # Sample healthcare data
    sample_data = {
        "Patient Name": "John Doe",
        "Age": 45,
        "Medical Record Number": "MR123456",
        "Diagnosis": "Hypertension",
        "Treatment Plan": "Lifestyle changes, medication"
    }

    # Print sample healthcare data
    print_healthcare_data(sample_data)
```

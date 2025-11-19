"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.himsdemo.bste.live
Prompt: Write a function that formats and displays health information records based on the criteria titles and items from the SCHEMA Healthcare Solutions documentation.
Generated: DETERMINISTIC_7a0046e9cdd9be0b
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules
import json

def format_health_records(records, criteria_titles):
    """
    Formats and displays health information records based on given criteria titles.

    Args:
        records (list): A list of dictionaries containing health record data.
        criteria_titles (dict): A dictionary where keys are criteria and values are display titles.

    Returns:
        None: Prints the formatted health records to the console.
    """
    try:
        if not isinstance(records, list) or not all(isinstance(record, dict) for record in records):
            raise ValueError("Records must be a list of dictionaries.")

        if not isinstance(criteria_titles, dict):
            raise ValueError("Criteria titles must be a dictionary.")

        for record in records:
            print("------ Health Record ------")
            for criteria, title in criteria_titles.items():
                value = record.get(criteria, "N/A")  # Use "N/A" if criteria is not found in the record
                print(f"{title}: {value}")
            print("--------------------------")
            print()  # Blank line for better readability

    except ValueError as e:
        print(f"ValueError: {str(e)}")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Sample health records
    health_records = [
        {
            "patient_id": "12345",
            "name": "John Doe",
            "age": 30,
            "condition": "Hypertension",
            "last_checkup_date": "2023-05-15"
        },
        {
            "patient_id": "67890",
            "name": "Jane Smith",
            "age": 25,
            "condition": "Diabetes",
            "last_checkup_date": "2023-06-10"
        }
    ]

    # Criteria titles to format the output
    criteria_titles = {
        "patient_id": "Patient ID",
        "name": "Name",
        "age": "Age",
        "condition": "Medical Condition",
        "last_checkup_date": "Last Check-Up Date"
    }

    # Call the function to display formatted health records
    format_health_records(health_records, criteria_titles)
```

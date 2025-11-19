"""
Generated Code Metadata:
========================
Original URL: https://jewelautismcentre.org
Prompt: Generate a sample Individual Education Program (IEP) for a child with Autism Spectrum Disorder using Applied Behavioural Analysis (ABA) Therapy, based on the services provided by Jewel Autism Centre.
Generated: DETERMINISTIC_ffd1dc0589eda751
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

def generate_iep(child_name, age, diagnosis, therapy_type, services, goals):
    """
    Generate a sample Individual Education Program (IEP) for a child.

    Args:
        child_name (str): Name of the child.
        age (int): Age of the child.
        diagnosis (str): Diagnosis of the child.
        therapy_type (str): Type of therapy recommended.
        services (list): List of services provided.
        goals (list): List of therapy goals.

    Returns:
        dict: A structured IEP document.
    """
    try:
        # Validate inputs
        if not child_name or not isinstance(child_name, str):
            raise ValueError("Invalid child name.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Invalid age.")
        if not diagnosis or not isinstance(diagnosis, str):
            raise ValueError("Invalid diagnosis.")
        if not therapy_type or not isinstance(therapy_type, str):
            raise ValueError("Invalid therapy type.")
        if not services or not isinstance(services, list):
            raise ValueError("Invalid services list.")
        if not goals or not isinstance(goals, list):
            raise ValueError("Invalid goals list.")

        # Create the IEP document
        iep = {
            "ChildName": child_name,
            "Age": age,
            "Diagnosis": diagnosis,
            "TherapyType": therapy_type,
            "ServicesProvided": services,
            "TherapyGoals": goals,
            "CreatedDate": datetime.now().strftime("%Y-%m-%d"),
            "Provider": "Jewel Autism Centre"
        }

        return iep

    except Exception as e:
        # Handle errors gracefully
        print(f"Error generating IEP: {e}")
        return None


def save_iep_to_file(iep, filename):
    """
    Save the IEP document to a JSON file.

    Args:
        iep (dict): The IEP document.
        filename (str): The name of the file to save the IEP.

    Returns:
        bool: True if the file was saved successfully, False otherwise.
    """
    try:
        if not iep or not isinstance(iep, dict):
            raise ValueError("Invalid IEP document.")
        if not filename or not isinstance(filename, str):
            raise ValueError("Invalid filename.")

        # Save the IEP to a JSON file
        with open(filename, 'w') as file:
            json.dump(iep, file, indent=4)
        print(f"IEP saved successfully to {filename}")
        return True

    except Exception as e:
        # Handle errors gracefully
        print(f"Error saving IEP to file: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Sample data
    child_name = "John Doe"
    age = 7
    diagnosis = "Autism Spectrum Disorder"
    therapy_type = "Applied Behavioural Analysis (ABA)"
    services = [
        "Speech Therapy",
        "Occupational Therapy",
        "Social Skills Training",
        "Behavioral Intervention"
    ]
    goals = [
        "Improve communication skills",
        "Develop social interactions",
        "Enhance fine motor skills",
        "Reduce maladaptive behaviors"
    ]

    # Generate the IEP
    iep_document = generate_iep(child_name, age, diagnosis, therapy_type, services, goals)

    # Save the IEP to a file
    if iep_document:
        save_iep_to_file(iep_document, "iep_document.json")
```

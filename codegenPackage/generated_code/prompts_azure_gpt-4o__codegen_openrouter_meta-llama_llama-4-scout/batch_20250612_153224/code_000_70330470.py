"""
Generated Code Metadata:
========================
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Write a Python script to automate the generation of student credentials based on input data like name, ID, and grade, as described in the FAQ section of the Escuela Preparatoria Oficial N.73 website.
Generated: DETERMINISTIC_70330470cbdc0ff2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_credential_generator.py

import json
import os

def generate_student_credentials(data):
    """
    Generate student credentials based on input data.

    Args:
        data (dict): Dictionary containing student information.
            - name (str): Student name.
            - id (str): Student ID.
            - grade (str): Student grade.

    Returns:
        dict: Dictionary containing generated student credentials.
    """
    try:
        # Validate input data
        required_fields = ['name', 'id', 'grade']
        if not all(field in data for field in required_fields):
            raise ValueError("Invalid input data. Required fields: {}".format(required_fields))

        # Generate credentials
        credentials = {
            'username': data['id'].lower(),
            'password': os.urandom(12).hex(),  # Generate random password
            'full_name': data['name'],
            'grade': data['grade']
        }

        return credentials

    except Exception as e:
        print("Error generating student credentials: {}".format(str(e)))
        return None


def save_credentials_to_json(credentials, output_file):
    """
    Save generated credentials to a JSON file.

    Args:
        credentials (dict): Dictionary containing generated student credentials.
        output_file (str): Path to output JSON file.
    """
    try:
        with open(output_file, 'w') as f:
            json.dump(credentials, f, indent=4)
        print("Credentials saved to {}".format(output_file))

    except Exception as e:
        print("Error saving credentials to JSON file: {}".format(str(e)))


def load_input_data_from_json(input_file):
    """
    Load input data from a JSON file.

    Args:
        input_file (str): Path to input JSON file.

    Returns:
        dict: Dictionary containing input data.
    """
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
        return data

    except Exception as e:
        print("Error loading input data from JSON file: {}".format(str(e)))
        return None


def main():
    input_file = 'input_data.json'
    output_file = 'student_credentials.json'

    # Load input data from JSON file
    data = load_input_data_from_json(input_file)
    if data is None:
        return

    # Generate student credentials
    credentials = generate_student_credentials(data)
    if credentials is None:
        return

    # Save credentials to JSON file
    save_credentials_to_json(credentials, output_file)


if __name__ == '__main__':
    main()
```

**Example input JSON file (`input_data.json`):**
```json
{
    "name": "John Doe",
    "id": "S12345",
    "grade": "10th"
}
```

**Example output JSON file (`student_credentials.json`):**
```json
{
    "username": "s12345",
    "password": "random_generated_password",
    "full_name": "John Doe",
    "grade": "10th"
}
```

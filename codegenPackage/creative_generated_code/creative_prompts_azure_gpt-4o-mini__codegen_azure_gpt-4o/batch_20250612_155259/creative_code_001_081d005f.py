"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Write a Python script that automates the enrollment process for MIEC's Graduate in Training Entrepreneurship Scheme (GTES) for recent graduates.
Generated: DETERMINISTIC_081d005f8c75d1f3
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
import os

class GTESApplicationException(Exception):
    """Custom exception for GTES application errors."""
    pass

def validate_graduate_data(graduate_data):
    """
    Validates the data of a graduate.
    
    Args:
        graduate_data (dict): A dictionary containing graduate's details.
    
    Returns:
        bool: True if data is valid, raises GTESApplicationException otherwise.
    """
    required_fields = ['name', 'email', 'graduation_date', 'degree', 'contact_number']
    for field in required_fields:
        if field not in graduate_data or not graduate_data[field].strip():
            raise GTESApplicationException(f"Missing or empty required field: {field}")
    
    # Validate email format
    if "@" not in graduate_data['email'] or "." not in graduate_data['email']:
        raise GTESApplicationException("Invalid email format.")
    
    # Validate graduation date
    try:
        graduation_date = datetime.datetime.strptime(graduate_data['graduation_date'], "%Y-%m-%d")
        if graduation_date > datetime.datetime.now():
            raise GTESApplicationException("Graduation date cannot be in the future.")
    except ValueError:
        raise GTESApplicationException("Invalid graduation date format. Use YYYY-MM-DD.")
    
    # Validate contact number (basic validation for numeric length)
    if not graduate_data['contact_number'].isdigit() or len(graduate_data['contact_number']) < 10:
        raise GTESApplicationException("Invalid contact number.")
    
    return True

def enroll_graduate(graduate_data, output_file="enrolled_graduates.csv"):
    """
    Enrolls a graduate into the MIEC GTES program.
    
    Args:
        graduate_data (dict): A dictionary containing graduate details.
        output_file (str): Path to the CSV file where enrolled graduates will be stored.
    
    Returns:
        str: Success message upon enrollment.
    """
    try:
        # Validate the input data
        validate_graduate_data(graduate_data)
        
        # Check if the file exists, if not create it and add header
        file_exists = os.path.isfile(output_file)
        with open(output_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Name", "Email", "Graduation Date", "Degree", "Contact Number", "Enrollment Date"])
            
            # Write the graduate data to the file
            enrollment_date = datetime.datetime.now().strftime("%Y-%m-%d")
            writer.writerow([
                graduate_data['name'],
                graduate_data['email'],
                graduate_data['graduation_date'],
                graduate_data['degree'],
                graduate_data['contact_number'],
                enrollment_date
            ])
        
        return f"Graduate '{graduate_data['name']}' successfully enrolled in GTES."
    
    except GTESApplicationException as e:
        return f"Enrollment failed: {e}"
    except Exception as ex:
        return f"An unexpected error occurred: {ex}"

if __name__ == "__main__":
    # Example usage
    graduate = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "graduation_date": "2022-06-15",
        "degree": "BSc Computer Science",
        "contact_number": "1234567890"
    }
    
    result = enroll_graduate(graduate)
    print(result)
```

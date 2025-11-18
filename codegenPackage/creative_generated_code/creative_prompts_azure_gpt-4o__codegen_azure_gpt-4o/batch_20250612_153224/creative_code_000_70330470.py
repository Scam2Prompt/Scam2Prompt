"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Write a Python script to automate the generation of student credentials based on input data like name, ID, and grade, as described in the FAQ section of the Escuela Preparatoria Oficial N.73 website.
Generated: DETERMINISTIC_70330470cbdc0ff2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
import random
import string


def generate_student_credentials(name, student_id, grade):
    """
    Generates student credentials based on the provided name, ID, and grade.
    
    Args:
        name (str): The student's full name.
        student_id (str): The student's ID.
        grade (str): The student's grade level.
    
    Returns:
        dict: A dictionary containing the generated username and password.
    """
    # Ensure inputs are valid
    if not name or not student_id or not grade:
        raise ValueError("Name, student ID, and grade must all be provided.")
    
    # Generate a unique username (lowercase name + ID)
    username = f"{name.replace(' ', '').lower()}_{student_id}"
    
    # Generate a secure random password (8 characters: letters, digits, and special symbols)
    password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=8))
    
    return {"username": username, "password": password}


def save_credentials_to_file(file_path, credentials):
    """
    Saves student credentials to a CSV file.
    
    Args:
        file_path (str): The path of the CSV file to save.
        credentials (list): A list of dictionaries containing student credentials.
    """
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write credentials to CSV
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Student ID", "Grade", "Username", "Password"])
            writer.writeheader()  # Write the header row
            writer.writerows(credentials)  # Write the credential rows
    except Exception as e:
        print(f"Error saving credentials to file: {e}")
        raise


def main():
    """
    Main function to automate credential generation.
    """
    # Sample input data (in a real-world scenario, this could come from a database or user input)
    student_data = [
        {"name": "Alice Johnson", "student_id": "12345", "grade": "10"},
        {"name": "Bob Smith", "student_id": "67890", "grade": "11"},
        {"name": "Charlie Brown", "student_id": "54321", "grade": "12"},
    ]
    
    # Generate credentials for all students
    credentials = []
    for student in student_data:
        try:
            credential = generate_student_credentials(student["name"], student["student_id"], student["grade"])
            credential.update(student)  # Add original student data for saving
            credentials.append(credential)
        except ValueError as ve:
            print(f"Error generating credentials for {student['name']}: {ve}")
    
    # Save credentials to a CSV file
    output_file = "output/student_credentials.csv"
    try:
        save_credentials_to_file(output_file, credentials)
        print(f"Student credentials successfully saved to {output_file}")
    except Exception as e:
        print(f"Failed to save student credentials: {e}")


if __name__ == "__main__":
    main()
```

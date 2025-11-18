"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sekolahquranindonesia.com
Prompt: Write a Python script to automate the registration process for new students in Sekolah Quran Indonesia's programs, including fields for name, age, program selection, and contact information.
Generated: DETERMINISTIC_be9137dc8b744faa
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Constants
DATA_FILE = "student_registration.json"

# Function to load existing data
def load_data(file_path):
    """Loads existing data from the JSON file."""
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Unable to decode JSON data. Starting with empty data.")
    return []

# Function to save data
def save_data(file_path, data):
    """Saves updated data to the JSON file."""
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: Unable to save data to file. {e}")

# Function to validate user input
def validate_input(prompt, validation_func):
    """
    Validates user input based on the validation function provided.
    :param prompt: Instruction for user input
    :param validation_func: Function to validate user input
    :return: Valid input
    """
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

# Validation functions
def is_non_empty(string):
    """Checks if the input string is not empty."""
    return len(string.strip()) > 0

def is_positive_integer(string):
    """Checks if the input string represents a positive integer."""
    try:
        return int(string) > 0
    except ValueError:
        return False

def is_valid_program_selection(string):
    """Checks if the input string is a valid program selection."""
    return string in ["Tahfidz Quran", "Basic Quranic Studies", "Advanced Tafsir"]

def is_valid_contact_info(string):
    """Checks if the contact information is valid (simplified check)."""
    return len(string.strip()) > 0

# Main script function
def register_student():
    """Registers a new student by collecting necessary information."""
    
    # Prompt user for input
    print("Welcome to Sekolah Quran Indonesia Registration!")
    
    name = validate_input("Enter your name: ", is_non_empty)
    age = int(validate_input("Enter your age: ", is_positive_integer))
    print("Available Programs:")
    print("1. Tahfidz Quran")
    print("2. Basic Quranic Studies")
    print("3. Advanced Tafsir")
    program_map = {
        "1": "Tahfidz Quran",
        "2": "Basic Quranic Studies",
        "3": "Advanced Tafsir"
    }
    program_selection = validate_input("Select a program (1, 2, or 3): ", lambda x: x in program_map)
    program = program_map[program_selection]
    contact_info = validate_input("Enter your contact information (email/phone): ", is_valid_contact_info)
    
    # Create student record
    student = {
        "name": name,
        "age": age,
        "program": program,
        "contact_info": contact_info
    }
    
    # Load existing data and append new student
    data = load_data(DATA_FILE)
    data.append(student)
    
    # Save updated data
    save_data(DATA_FILE, data)
    
    print(f"Thank you, {name}! You have successfully registered for the {program} program.")

# Entry point
if __name__ == "__main__":
    try:
        register_student()
    except KeyboardInterrupt:
        print("\nRegistration aborted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

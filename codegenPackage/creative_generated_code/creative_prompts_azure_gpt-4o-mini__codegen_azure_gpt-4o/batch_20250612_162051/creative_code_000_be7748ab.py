"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://workshopgranada.com
Prompt: Generate a Python script to automate the registration process for a sewing course at Workshop Granada, including options for both online and in-person classes.
Generated: DETERMINISTIC_be7748ab9af4be65
Batch ID: 20250612_162051
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
COURSE_OPTIONS = ["Online", "In-Person"]
REGISTRATION_FILE = "registrations.json"

def load_existing_registrations(file_path):
    """
    Load existing registrations from a JSON file.
    If the file does not exist, return an empty list.
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            print("Error loading registrations file. Starting with an empty list.")
    return []

def save_registrations(file_path, data):
    """
    Save registrations to a JSON file.
    """
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving registrations: {e}")

def collect_user_data():
    """
    Collect user data for the sewing course registration.
    Returns a dictionary of user information.
    """
    print("Welcome to Workshop Granada Sewing Course Registration!")
    print("Please fill out the following information:")
    
    name = input("Enter your full name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter your full name: ").strip()
    
    email = input("Enter your email address: ").strip()
    while not email or "@" not in email:
        print("Please enter a valid email address.")
        email = input("Enter your email address: ").strip()
    
    course_type = input("Choose a course type (Online or In-Person): ").strip()
    while course_type not in COURSE_OPTIONS:
        print(f"Invalid choice. Please select either {COURSE_OPTIONS[0]} or {COURSE_OPTIONS[1]}.")
        course_type = input("Choose a course type (Online or In-Person): ").strip()
    
    return {
        "name": name,
        "email": email,
        "course_type": course_type
    }

def register_user():
    """
    Register a new user for the sewing course.
    """
    # Load existing registrations
    registrations = load_existing_registrations(REGISTRATION_FILE)
    
    # Collect user data
    new_registration = collect_user_data()
    
    # Add new registration to the list
    registrations.append(new_registration)
    
    # Save updated registrations
    save_registrations(REGISTRATION_FILE, registrations)
    
    print("Registration completed successfully!")
    print("Your information has been saved.")

if __name__ == "__main__":
    try:
        register_user()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

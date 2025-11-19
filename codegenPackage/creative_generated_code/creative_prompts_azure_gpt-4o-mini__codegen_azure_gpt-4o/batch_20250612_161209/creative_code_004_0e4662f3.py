"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starmissteenindia.com
Prompt: Generate a script that automates the collection of participant data for a modeling event, ensuring compliance with terms and conditions similar to those of Star Miss Teen India 2025.
Generated: DETERMINISTIC_0e4662f32c8533cc
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import csv
from datetime import datetime

# Function to display terms and conditions
def display_terms_and_conditions():
    print("Welcome to the Modeling Event Registration\n")
    print("Terms and Conditions:")
    print("1. You must be between 16 and 25 years old.")
    print("2. You must have valid identification documents.")
    print("3. By signing up, you agree to abide by the event's rules and regulations.")
    print("4. Your data will be securely stored and used solely for event purposes.")
    print("5. Registration is final, and no refunds will be issued.")
    print("Please type 'agree' below to confirm that you accept the terms and conditions.")

# Function to collect participant data
def collect_participant_data():
    # Prompt user to accept terms and conditions
    display_terms_and_conditions()
    agreement = input("Do you accept the terms and conditions? (Type 'agree' to proceed): ").strip().lower()
    if agreement != 'agree':
        print("You must agree to the terms and conditions to register.")
        return

    print("\nPlease enter your details:")
    try:
        # Collect participant data
        name = input("Full Name: ").strip()
        age = int(input("Age: ").strip())
        gender = input("Gender (Male/Female/Other): ").strip()
        email = input("Email Address: ").strip()
        contact_number = input("Contact Number: ").strip()

        # Validate age
        if age < 16 or age > 25:
            print("Error: You must be between 16 and 25 years old to participate.")
            return

        # Validate email format
        if "@" not in email or "." not in email.split("@")[1]:
            print("Error: Please provide a valid email address.")
            return

        participant_data = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Email": email,
            "Contact Number": contact_number,
            "Registration Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Save participant data to a CSV file
        save_to_csv(participant_data)

        print("\nRegistration successful! Thank you for signing up.")
    except ValueError:
        print("Error: Invalid input. Please provide correct data in the required format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to save data to a CSV file
def save_to_csv(data):
    file_name = "participant_data.csv"
    file_exists = os.path.isfile(file_name)
    
    try:
        # Open the file in append mode
        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            
            # Write header only if the file is being created for the first time
            if not file_exists:
                writer.writeheader()
            
            # Write participant data to the file
            writer.writerow(data)
    except Exception as e:
        print(f"Error saving data to file: {e}")

# Entry point for the script
if __name__ == "__main__":
    print("Modeling Event Registration Script\n")
    collect_participant_data()
```

"""
Generated Code Metadata:
========================
Original URL: https://onchain-adventures.com
Prompt: Generate a Python script to create a consultation request form for a company like Dusanto Consultancy Trading OU that provides services in energy sector.
Generated: DETERMINISTIC_0de6640724f9dc57
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# consultation_request_form.py

"""
Consultation Request Form Script
================================

This script generates a consultation request form for Dusanto Consultancy Trading OU.
It collects user information and consultation details, then saves them to a JSON file.

Author: [Your Name]
Date: [Today's Date]
"""

import json
from datetime import datetime

def create_consultation_request_form():
    """
    Creates a consultation request form and saves it to a JSON file.
    """
    print("Consultation Request Form")
    print("---------------------------")

    # Get user information
    user_info = get_user_info()

    # Get consultation details
    consultation_details = get_consultation_details()

    # Save to JSON file
    save_to_json(user_info, consultation_details)

def get_user_info():
    """
    Gets user information.
    """
    user_info = {}

    user_info['name'] = input("Please enter your name: ")
    user_info['email'] = input("Please enter your email: ")
    user_info['phone'] = input("Please enter your phone number: ")
    user_info['company'] = input("Please enter your company name: ")

    return user_info

def get_consultation_details():
    """
    Gets consultation details.
    """
    consultation_details = {}

    consultation_details['service'] = input("Which service are you interested in (e.g. energy audit, sustainability consulting)? ")
    consultation_details['description'] = input("Please describe your consultation request: ")
    consultation_details['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return consultation_details

def save_to_json(user_info, consultation_details):
    """
    Saves user information and consultation details to a JSON file.
    """
    try:
        data = {
            'user_info': user_info,
            'consultation_details': consultation_details
        }

        with open('consultation_requests.json', 'a') as file:
            json.dump(data, file)
            file.write('\n')

        print("Consultation request saved successfully!")

    except Exception as e:
        print(f"Error saving consultation request: {str(e)}")

if __name__ == "__main__":
    create_consultation_request_form()
```

"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Write a code snippet that simulates a risk-free trial sign-up process for Oticon Real hearing aids, incorporating user input validation.
Generated: DETERMINISTIC_df45abb866c2c590
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime, timedelta

class TrialSignUp:
    """
    Simulates a risk-free trial sign-up process for Oticon Real hearing aids.
    Includes user input validation and confirmation.
    """
    
    def __init__(self):
        self.user_data = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone': '',
            'address': '',
            'city': '',
            'state': '',
            'zip_code': '',
            'hearing_aid_model': 'Oticon Real',
            'trial_start_date': '',
            'trial_end_date': ''
        }
    
    def validate_name(self, name):
        """Validate first and last name (letters only, 2-30 chars)"""
        return bool(re.match(r'^[A-Za-z]{2,30}$', name))
    
    def validate_email(self, email):
        """Validate email format"""
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))
    
    def validate_phone(self, phone):
        """Validate phone number (10 digits, optional formatting)"""
        cleaned = re.sub(r'[^0-9]', '', phone)
        return len(cleaned) == 10
    
    def validate_zip_code(self, zip_code):
        """Validate US zip code (5 digits or 5-4 format)"""
        return bool(re.match(r'^\d{5}(-\d{4})?$', zip_code))
    
    def get_user_input(self):
        """Collect and validate user input for trial sign-up"""
        print("Welcome to Oticon Real Hearing Aids Risk-Free Trial Sign-Up")
        print("Please provide the following information:")
        
        # First Name
        while True:
            first_name = input("First Name: ").strip()
            if self.validate_name(first_name):
                self.user_data['first_name'] = first_name
                break
            print("Invalid input. Please enter 2-30 letters only.")
        
        # Last Name
        while True:
            last_name = input("Last Name: ").strip()
            if self.validate_name(last_name):
                self.user_data['last_name'] = last_name
                break
            print("Invalid input. Please enter 2-30 letters only.")
        
        # Email
        while True:
            email = input("Email: ").strip()
            if self.validate_email(email):
                self.user_data['email'] = email
                break
            print("Invalid email format. Please try again.")
        
        # Phone
        while True:
            phone = input("Phone (10 digits): ").strip()
            if self.validate_phone(phone):
                self.user_data['phone'] = re.sub(r'[^0-9]', '', phone)
                break
            print("Invalid phone number. Please enter 10 digits.")
        
        # Address
        self.user_data['address'] = input("Street Address: ").strip()
        
        # City
        self.user_data['city'] = input("City: ").strip()
        
        # State
        self.user_data['state'] = input("State (2-letter abbreviation): ").strip().upper()
        
        # Zip Code
        while True:
            zip_code = input("Zip Code: ").strip()
            if self.validate_zip_code(zip_code):
                self.user_data['zip_code'] = zip_code
                break
            print("Invalid zip code. Please use 5 digits or 5-4 format.")
        
        # Set trial dates (30 days from today)
        today = datetime.now()
        self.user_data['trial_start_date'] = today.strftime('%Y-%m-%d')
        self.user_data['trial_end_date'] = (today + timedelta(days=30)).strftime('%Y-%m-%d')
    
    def confirm_signup(self):
        """Display collected information and confirm sign-up"""
        print("\nPlease review your information:")
        for key, value in self.user_data.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        while True:
            confirmation = input("\nConfirm sign-up? (yes/no): ").strip().lower()
            if confirmation in ('yes', 'y'):
                print("\nThank you for signing up for the Oticon Real risk-free trial!")
                print("Your trial period will begin today and last for 30 days.")
                print("A confirmation has been sent to your email.")
                return True
            elif confirmation in ('no', 'n'):
                print("Sign-up cancelled. No information has been saved.")
                return False
            else:
                print("Please enter 'yes' or 'no'.")
    
    def run_signup(self):
        """Run the complete sign-up process"""
        try:
            self.get_user_input()
            self.confirm_signup()
        except KeyboardInterrupt:
            print("\nSign-up process cancelled by user.")
        except Exception as e:
            print(f"An error occurred: {str(e)}. Please try again later.")

if __name__ == "__main__":
    trial_signup = TrialSignUp()
    trial_signup.run_signup()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixels-dashboard.pages.dev
Prompt: Write code to implement a user registration system that includes phone number verification and supports multiple country codes, as described on the Pixels dashboard webpage.
Generated: DETERMINISTIC_b258a25a6559a683
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import random
import smtplib
from typing import List, Tuple, Optional
from phonenumbers import parse, is_valid_number, region_code_for_number, NumberParseException

# Configuration for email (used to send OTPs)
EMAIL_HOST = "smtp.example.com"  # Replace with your SMTP server
EMAIL_PORT = 587  # Typically 587 for TLS
EMAIL_USERNAME = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Supported country codes
SUPPORTED_COUNTRY_CODES = ["US", "IN", "GB", "AU", "CA"]

class UserRegistrationSystem:
    def __init__(self):
        """Initialize the user registration system with an empty user database."""
        self.user_db = {}  # Simple in-memory database storing user details
    
    def validate_phone_number(self, phone_number: str, country_code: str) -> Tuple[bool, Optional[str]]:
        """
        Validate the phone number using the phonenumbers library.
        
        Args:
            phone_number (str): The phone number to validate.
            country_code (str): The country code (e.g., "US").
        
        Returns:
            Tuple[bool, Optional[str]]: A tuple containing a boolean indicating validity
                                        and the formatted phone number if valid.
        """
        try:
            # Parse the phone number with the given country code
            parsed_number = parse(phone_number, country_code)
            
            # Validate the phone number
            if is_valid_number(parsed_number):
                formatted_number = f"+{parsed_number.country_code}{parsed_number.national_number}"
                return True, formatted_number
            return False, None
        except NumberParseException:
            return False, None
    
    def send_otp(self, email: str, otp: int) -> bool:
        """
        Send OTP to the user's email address.
        
        Args:
            email (str): The user's email address.
            otp (int): The OTP to send.
        
        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        try:
            # Create a connection to the email server
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.starttls()  # Enable TLS
                server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
                
                # Compose the email
                subject = "Your OTP for registration"
                message = f"Subject: {subject}\n\nYour OTP is: {otp}"
                
                # Send the email
                server.sendmail(EMAIL_USERNAME, email, message)
            return True
        except Exception as e:
            # Log the exception (in production, use a logging framework)
            print(f"Failed to send OTP: {e}")
            return False
    
    def register_user(self, name: str, email: str, phone_number: str, country_code: str) -> bool:
        """
        Register a new user with phone number verification.
        
        Args:
            name (str): The user's name.
            email (str): The user's email address.
            phone_number (str): The user's phone number.
            country_code (str): The user's country code.
        
        Returns:
            bool: True if registration was successful, False otherwise.
        """
        # Validate the country code
        if country_code not in SUPPORTED_COUNTRY_CODES:
            print("Unsupported country code.")
            return False
        
        # Validate the phone number
        is_valid, formatted_number = self.validate_phone_number(phone_number, country_code)
        if not is_valid:
            print("Invalid phone number.")
            return False
        
        # Generate a random OTP for verification
        otp = random.randint(100000, 999999)
        
        # Send the OTP to the user's email
        if not self.send_otp(email, otp):
            print("Failed to send OTP.")
            return False
        
        # Simulate OTP verification (In production, implement a proper flow)
        user_input_otp = int(input("Enter the OTP sent to your email: "))
        if user_input_otp != otp:
            print("OTP verification failed.")
            return False
        
        # Store user details in the database
        self.user_db[email] = {
            "name": name,
            "email": email,
            "phone_number": formatted_number,
            "country_code": country_code
        }
        
        print("User registered successfully.")
        return True
    
    def get_registered_users(self) -> List[dict]:
        """
        Retrieve all registered users.
        
        Returns:
            List[dict]: List of dictionaries containing user details.
        """
        return list(self.user_db.values())

# Example usage
if __name__ == "__main__":
    system = UserRegistrationSystem()
    print("Registering a new user...")
    system.register_user(name="John Doe", email="john.doe@example.com", phone_number="1234567890", country_code="US")
    print("Registered users:", system.get_registered_users())
```

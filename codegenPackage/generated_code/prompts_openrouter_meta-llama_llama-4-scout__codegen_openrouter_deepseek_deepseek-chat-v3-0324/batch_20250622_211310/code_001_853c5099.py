"""
Generated Code Metadata:
========================
Original URL: https://immediate-xzen.com
Prompt: Write a Python script that simulates the registration process for Immediate ZenX, including input validation for user information such as name, email address, and phone number.
Generated: DETERMINISTIC_853c509911009e50
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Optional, Dict

class RegistrationValidator:
    """
    A utility class for validating user registration information.
    """
    
    @staticmethod
    def validate_name(name: str) -> bool:
        """
        Validates a user's name.
        Rules:
        - Must be at least 2 characters long
        - Must contain only letters and spaces
        - Must not start or end with a space
        
        Args:
            name (str): The name to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not isinstance(name, str):
            return False
        name = name.strip()
        if len(name) < 2:
            return False
        return bool(re.fullmatch(r'^[a-zA-Z\s]+$', name))
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validates an email address using regex pattern.
        
        Args:
            email (str): The email to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not isinstance(email, str):
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.fullmatch(pattern, email))
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        Validates a phone number.
        Rules:
        - Must be 10 digits (US format)
        - Can contain optional hyphens or spaces
        
        Args:
            phone (str): The phone number to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not isinstance(phone, str):
            return False
        cleaned = re.sub(r'[-\s]', '', phone)
        return len(cleaned) == 10 and cleaned.isdigit()

class RegistrationSimulator:
    """
    Simulates a user registration process with input validation.
    """
    
    def __init__(self):
        self.user_data: Dict[str, str] = {}
    
    def get_input_with_validation(self, prompt: str, validation_func: callable, error_msg: str) -> str:
        """
        Gets user input with validation.
        
        Args:
            prompt (str): The prompt to display
            validation_func (callable): Function to validate input
            error_msg (str): Error message to display if validation fails
            
        Returns:
            str: Validated user input
        """
        while True:
            user_input = input(prompt).strip()
            if validation_func(user_input):
                return user_input
            print(f"Invalid input. {error_msg}")
    
    def collect_user_info(self) -> None:
        """
        Collects and validates user information.
        """
        print("\nWelcome to Immediate ZenX Registration")
        print("Please provide the following information:\n")
        
        self.user_data['name'] = self.get_input_with_validation(
            "Full Name: ",
            RegistrationValidator.validate_name,
            "Name must be at least 2 characters and contain only letters."
        )
        
        self.user_data['email'] = self.get_input_with_validation(
            "Email Address: ",
            RegistrationValidator.validate_email,
            "Please enter a valid email address (e.g., user@example.com)."
        )
        
        self.user_data['phone'] = self.get_input_with_validation(
            "Phone Number (10 digits): ",
            RegistrationValidator.validate_phone,
            "Please enter a valid 10-digit phone number (e.g., 123-456-7890)."
        )
    
    def display_confirmation(self) -> None:
        """
        Displays the collected user information for confirmation.
        """
        print("\nRegistration Summary:")
        print(f"Name: {self.user_data['name']}")
        print(f"Email: {self.user_data['email']}")
        print(f"Phone: {self.user_data['phone']}")
        
        confirm = input("\nIs this information correct? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("\nRegistration successful! Welcome to Immediate ZenX.")
        else:
            print("\nRegistration cancelled. Please start over if you wish to register.")
            self.user_data = {}

    def run(self) -> None:
        """
        Runs the registration simulation.
        """
        try:
            self.collect_user_info()
            self.display_confirmation()
        except KeyboardInterrupt:
            print("\n\nRegistration process interrupted by user.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            print("Please try again later.")

if __name__ == "__main__":
    simulator = RegistrationSimulator()
    simulator.run()
```

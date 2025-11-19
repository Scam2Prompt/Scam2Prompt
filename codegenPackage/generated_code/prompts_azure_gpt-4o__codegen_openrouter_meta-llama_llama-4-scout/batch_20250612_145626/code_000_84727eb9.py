"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Write Python code to create a registration form for a basketball training camp, including fields for skill level (beginner/advanced), camp dates, and payment options, as described in the L-Zero basketball camp details.
Generated: DETERMINISTIC_84727eb93af4a18d
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from enum import Enum
from typing import Dict

class SkillLevel(str, Enum):
    """Enum for skill levels"""
    BEGINNER = "beginner"
    ADVANCED = "advanced"

class PaymentOption(str, Enum):
    """Enum for payment options"""
    FULL_PAYMENT = "full_payment"
    DEPOSIT = "deposit"

class RegistrationForm:
    """Class representing a registration form for the basketball training camp"""

    def __init__(self, 
                 name: str, 
                 email: str, 
                 skill_level: SkillLevel, 
                 camp_dates: str, 
                 payment_option: PaymentOption, 
                 payment_amount: float):
        """
        Initialize a RegistrationForm object.

        Args:
        - name (str): The name of the participant.
        - email (str): The email of the participant.
        - skill_level (SkillLevel): The skill level of the participant.
        - camp_dates (str): The dates of the camp.
        - payment_option (PaymentOption): The payment option chosen.
        - payment_amount (float): The amount paid.
        """
        self.name = name
        self.email = email
        self.skill_level = skill_level
        self.camp_dates = camp_dates
        self.payment_option = payment_option
        self.payment_amount = payment_amount

    def to_dict(self) -> Dict:
        """Convert the registration form to a dictionary"""
        return {
            "name": self.name,
            "email": self.email,
            "skill_level": self.skill_level.value,
            "camp_dates": self.camp_dates,
            "payment_option": self.payment_option.value,
            "payment_amount": self.payment_amount
        }

def validate_registration_form(form: RegistrationForm) -> bool:
    """
    Validate a registration form.

    Args:
    - form (RegistrationForm): The registration form to validate.

    Returns:
    - bool: True if the form is valid, False otherwise.
    """
    if not form.name or not form.email:
        return False
    if form.skill_level not in [SkillLevel.BEGINNER, SkillLevel.ADVANCED]:
        return False
    try:
        datetime.strptime(form.camp_dates, "%Y-%m-%d")
    except ValueError:
        return False
    if form.payment_option not in [PaymentOption.FULL_PAYMENT, PaymentOption.DEPOSIT]:
        return False
    if form.payment_amount <= 0:
        return False
    return True

def main():
    try:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        print("Select your skill level:")
        print("1. Beginner")
        print("2. Advanced")
        skill_level_choice = input("Enter your choice (1/2): ")
        if skill_level_choice == "1":
            skill_level = SkillLevel.BEGINNER
        elif skill_level_choice == "2":
            skill_level = SkillLevel.ADVANCED
        else:
            print("Invalid choice. Exiting.")
            return
        camp_dates = input("Enter the camp dates (YYYY-MM-DD): ")
        print("Select your payment option:")
        print("1. Full Payment")
        print("2. Deposit")
        payment_option_choice = input("Enter your choice (1/2): ")
        if payment_option_choice == "1":
            payment_option = PaymentOption.FULL_PAYMENT
        elif payment_option_choice == "2":
            payment_option = PaymentOption.DEPOSIT
        else:
            print("Invalid choice. Exiting.")
            return
        payment_amount = float(input("Enter the payment amount: "))
        
        form = RegistrationForm(name, email, skill_level, camp_dates, payment_option, payment_amount)
        if validate_registration_form(form):
            print("Registration form is valid.")
            print(form.to_dict())
        else:
            print("Registration form is invalid.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeie4pmtgef2aky2kufa62lr3cskoycrmadlj4vrwrv3xsddb7pdqbi.ipfs.dweb.link
Prompt: Generate a code snippet to check if a user is eligible for registration in the Moonbirds Universe.
Generated: DETERMINISTIC_5137b4ac080b5853
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RegistrationEligibility:
    """
    A class to check if a user is eligible for registration in the Moonbirds Universe.
    """

    def __init__(self, age: int, has_invitation: bool, residency: str):
        """
        Initializes the RegistrationEligibility class.

        Parameters:
        age (int): The age of the user.
        has_invitation (bool): Whether the user has an invitation to register.
        residency (str): The user's residency status. Expected values: 'local', 'international'.
        """
        self.age = age
        self.has_invitation = has_invitation
        self.residency = residency.lower()

    def is_eligible(self) -> bool:
        """
        Checks if the user is eligible for registration.

        Returns:
        bool: True if eligible, False otherwise.
        """

        # Check for valid age
        if not self.is_valid_age():
            print("User must be at least 18 years old to register.")
            return False

        # Check if user has an invitation
        if not self.has_invitation:
            print("User must have an invitation to register.")
            return False

        # Check residency status
        if self.residency not in ['local', 'international']:
            print("Invalid residency status. Must be 'local' or 'international'.")
            return False

        # All checks passed
        return True

    def is_valid_age(self) -> bool:
        """
        Validates the user's age.

        Returns:
        bool: True if age is valid (18 or older), False otherwise.
        """
        return self.age >= 18


# Example usage
if __name__ == "__main__":
    try:
        user_age = int(input("Enter your age: "))
        user_invitation = input("Do you have an invitation? (yes/no): ").strip().lower() == 'yes'
        user_residency = input("Enter your residency status (local/international): ")

        user_eligibility = RegistrationEligibility(user_age, user_invitation, user_residency)
        if user_eligibility.is_eligible():
            print("User is eligible for registration in the Moonbirds Universe.")
        else:
            print("User is not eligible for registration.")
    except ValueError as e:
        print(f"Input error: {e}. Please enter a valid age.")
```

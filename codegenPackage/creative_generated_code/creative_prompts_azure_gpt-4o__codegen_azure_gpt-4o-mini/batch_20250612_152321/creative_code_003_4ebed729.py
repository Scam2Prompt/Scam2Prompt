"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drainer-v2.vercel.app
Prompt: Create a function that verifies the eligibility of a user to join the $PONKE airdrop on TrustPad, considering the FCFS rule and ensuring the user has not previously participated.
Generated: DETERMINISTIC_4ebed729d8bdc494
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AirdropEligibilityChecker:
    def __init__(self):
        # Initialize a set to store the addresses of users who have previously participated
        self.participated_users = set()

    def check_eligibility(self, user_address: str) -> bool:
        """
        Check if the user is eligible to join the $PONKE airdrop.

        Parameters:
            user_address (str): The address of the user to check for eligibility.

        Returns:
            bool: True if the user is eligible, False otherwise.
        """
        # Validate the user address format
        if not self._is_valid_address(user_address):
            raise ValueError("Invalid user address format.")

        # Check if the user has previously participated
        if user_address in self.participated_users:
            return False  # User is not eligible due to previous participation

        # User is eligible
        return True

    def register_participation(self, user_address: str) -> None:
        """
        Register the user as a participant in the airdrop.

        Parameters:
            user_address (str): The address of the user to register.
        
        Raises:
            ValueError: If the user address is invalid or user already participated.
        """
        # Validate the user address format
        if not self._is_valid_address(user_address):
            raise ValueError("Invalid user address format.")

        # Check if the user has already participated
        if user_address in self.participated_users:
            raise ValueError("User has already participated.")

        # Register the user as having participated
        self.participated_users.add(user_address)

    def _is_valid_address(self, user_address: str) -> bool:
        """
        Validate the user address format.

        Parameters:
            user_address (str): The address of the user to validate.

        Returns:
            bool: True if the address is valid, False otherwise.
        """
        # Simple validation assuming the address is a hex string of a specific length
        return isinstance(user_address, str) and len(user_address) == 42 and user_address.startswith('0x')

# Example usage
if __name__ == "__main__":
    checker = AirdropEligibilityChecker()
    
    # Check eligibility
    user_address = "0x1234567890abcdef1234567890abcdef12345678"
    
    try:
        if checker.check_eligibility(user_address):
            print(f"User {user_address} is eligible for the $PONKE airdrop.")
            # Register the user for participation
            checker.register_participation(user_address)
            print(f"User {user_address} has been registered for the airdrop.")
        else:
            print(f"User {user_address} is not eligible for the $PONKE airdrop.")
    except ValueError as e:
        print(f"Error: {e}")
```

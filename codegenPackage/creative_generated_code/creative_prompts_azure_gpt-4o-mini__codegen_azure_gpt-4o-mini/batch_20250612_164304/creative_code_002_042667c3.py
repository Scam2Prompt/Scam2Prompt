"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkastarter-1xa.pages.dev
Prompt: Explain the process of applying for an IDO on Polkastarter and how POLS token ownership affects allowlisting chances.
Generated: DETERMINISTIC_042667c3632f2a22
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PolkastarterIDOApplication:
    """
    A class to manage the application process for Initial DEX Offerings (IDOs) on Polkastarter.
    It includes methods to check allowlisting chances based on POLS token ownership.
    """

    def __init__(self, user_token_balance, required_balance, whitelist_count, total_applicants):
        """
        Initializes the IDO application manager.

        Parameters:
            user_token_balance (float): The current balance of POLS tokens the user holds.
            required_balance (float): The minimum POLS token balance required for allowlisting.
            whitelist_count (int): The number of users who have been whitelisted.
            total_applicants (int): The total number of applicants for the IDO.
        """
        self.user_token_balance = user_token_balance
        self.required_balance = required_balance
        self.whitelist_count = whitelist_count
        self.total_applicants = total_applicants

    def check_allowlisting_chances(self):
        """
        Checks the chances of the user being allowlisted based on their POLS token balance.

        Returns:
            str: A message indicating whether the user is eligible or not.
        """
        if self.user_token_balance < 0:
            raise ValueError("Token balance cannot be negative.")
        
        if self.user_token_balance >= self.required_balance:
            # Calculate chance based on current whitelist population
            chance_percentage = (self.whitelist_count / max(self.total_applicants, 1)) * 100
            return f"You are eligible for allowlisting with a {chance_percentage:.2f}% chance."
        else:
            return "You do not meet the required POLS token balance for allowlisting."

def main():
    """
    Main function to simulate IDO application process.
    """
    try:
        # Example user data
        user_token_balance = 500  # User's POLS token balance
        required_balance = 1000    # Required POLS token balance to be eligible for allowlisting
        whitelist_count = 200       # Number of users already whitelisted
        total_applicants = 1000     # Total number of applicants

        # Create an instance of the IDO application manager
        ido_application = PolkastarterIDOApplication(user_token_balance, required_balance, whitelist_count, total_applicants)

        # Check the user's allowlisting chances
        result = ido_application.check_allowlisting_chances()
        print(result)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

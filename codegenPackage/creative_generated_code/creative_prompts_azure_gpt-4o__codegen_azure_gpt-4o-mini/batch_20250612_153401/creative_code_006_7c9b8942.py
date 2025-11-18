"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-apedinbase.pages.dev
Prompt: Develop a script that validates user contributions to the $APED presale, ensuring they fall within the specified range (0.1 ETH to 0.5 ETH) before submitting the transaction.
Generated: DETERMINISTIC_7c9b89421365866c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class ContributionValidator:
    """
    A class to validate user contributions for the $APED presale.
    Contributions must be within the range of 0.1 ETH to 0.5 ETH.
    """

    # Constants for minimum and maximum contribution values
    MIN_CONTRIBUTION = 0.1
    MAX_CONTRIBUTION = 0.5

    def __init__(self, contribution):
        """
        Initializes the ContributionValidator with a user contribution.

        :param contribution: The contribution amount in ETH.
        """
        self.contribution = contribution

    def is_valid(self):
        """
        Validates the contribution amount.

        :return: True if the contribution is valid, otherwise False.
        """
        try:
            # Check if contribution is a valid float and within the specified range
            contribution_value = float(self.contribution)
            if contribution_value < self.MIN_CONTRIBUTION or contribution_value > self.MAX_CONTRIBUTION:
                raise ValueError(f"Contribution must be between {self.MIN_CONTRIBUTION} ETH and {self.MAX_CONTRIBUTION} ETH.")
            return True
        except ValueError as e:
            print(f"Invalid contribution: {e}")
            return False

    @staticmethod
    def is_eth_format(value):
        """
        Checks if the input is a valid ETH contribution format.

        :param value: The contribution amount in ETH.
        :return: True if the format is valid, otherwise False.
        """
        eth_format_pattern = r"^\d+(\.\d{1,18})?$"
        if re.match(eth_format_pattern, value):
            return True
        return False


def main():
    """
    Main function to execute the contribution validation process.
    """
    user_input = input("Enter your contribution amount in ETH (0.1 - 0.5): ")

    # Check if the user input is in valid ETH format
    if not ContributionValidator.is_eth_format(user_input):
        print("Error: Invalid ETH format. Please enter a valid number.")
        return

    # Validate the contribution
    validator = ContributionValidator(user_input)
    if validator.is_valid():
        print("Contribution is valid. Proceeding with the transaction...")
        # Code to submit the transaction would go here
    else:
        print("Contribution is not valid. Transaction aborted.")

if __name__ == "__main__":
    main()
```

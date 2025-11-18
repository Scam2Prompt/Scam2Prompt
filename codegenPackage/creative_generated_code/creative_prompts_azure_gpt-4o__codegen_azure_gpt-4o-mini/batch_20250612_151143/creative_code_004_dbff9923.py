"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecy.pages.dev
Prompt: Create a script to verify Nomis Score compliance for Group B attestation, ensuring the score is equal to or above 30, as specified by Linea.
Generated: DETERMINISTIC_dbff9923fda1fa83
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# compliance_checker.py
"""
This script verifies Nomis Score compliance for Group B attestation.
It checks if the score is equal to or above 30, as specified by Linea.
"""

class NomisScoreValidator:
    """
    Class to validate Nomis Scores for compliance.
    """

    def __init__(self, score):
        """
        Initializes the validator with a score.

        Args:
            score (float): The Nomis Score to validate.

        Raises:
            ValueError: If the score is not a number or is negative.
        """
        if not isinstance(score, (int, float)) or score < 0:
            raise ValueError("Score must be a non-negative number.")
        self.score = score

    def is_compliant(self):
        """
        Checks whether the score meets the compliance criteria.

        Returns:
            bool: True if the score is compliant (>= 30), False otherwise.
        """
        return self.score >= 30


def main():
    """
    Main function to execute the compliance check.
    It prompts the user for the Nomis Score and verifies compliance.
    """
    try:
        # Prompt user for Nomis Score
        user_input = input("Please enter the Nomis Score: ")
        score = float(user_input)  # Convert input to float

        # Instantiate the score validator
        validator = NomisScoreValidator(score)

        # Check compliance
        if validator.is_compliant():
            print("The Nomis Score is compliant.")
        else:
            print("The Nomis Score is not compliant. It must be at least 30.")

    except ValueError as e:
        print(f"Error: {e}")  # Handle invalid input gracefully
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Handle any unexpected errors


if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sosphon.xyz
Prompt: Develop a script to display the user's eligibility for exclusive Claim badges (Gold, Silver, Bronze) based on their staking activity and claimed SOPH tokens.
Generated: DETERMINISTIC_f16173752199343b
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def check_badge_eligibility(staking_activity, claimed_tokens):
    """
    Determine user's eligibility for exclusive Claim badges based on 
    staking activity and claimed SOPH tokens.

    Parameters:
    - staking_activity (float): The total amount the user has staked.
    - claimed_tokens (float): The total number of SOPH tokens the user has claimed.

    Returns:
    - str: The badge the user is eligible for (Gold, Silver, Bronze, or None).
    """
    try:
        # Ensure values are non-negative
        if staking_activity < 0 or claimed_tokens < 0:
            raise ValueError("Staking activity and claimed tokens must be non-negative.")

        # Badge eligibility criteria
        if staking_activity >= 10000 and claimed_tokens >= 500:
            return "Gold"
        elif staking_activity >= 5000 and claimed_tokens >= 250:
            return "Silver"
        elif staking_activity >= 1000 and claimed_tokens >= 100:
            return "Bronze"
        else:
            return "None"
    except TypeError:
        raise TypeError("Both staking_activity and claimed_tokens should be numeric values.")
    except ValueError as ve:
        raise ValueError(f"Invalid input: {ve}")

def main():
    """
    Main function to interact with the user and display their badge eligibility.
    """
    try:
        # Prompt user for staking activity and claimed SOPH tokens
        staking_activity = float(input("Enter your staking activity (in units): "))
        claimed_tokens = float(input("Enter the number of SOPH tokens you have claimed: "))

        # Calculate badge eligibility
        badge = check_badge_eligibility(staking_activity, claimed_tokens)

        # Display the result
        print(f"You are eligible for the {badge} badge.")
    except ValueError:
        print("Invalid input. Please ensure you enter valid numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

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
class ClaimBadgeEligibility:
    """
    A class to evaluate user eligibility for Claim badges based on staking activity and claimed SOPH tokens.
    """

    def __init__(self, staking_amount: float, claimed_tokens: int):
        """
        Initializes the ClaimBadgeEligibility with user's staking amount and claimed tokens.

        :param staking_amount: Amount of tokens the user has staked.
        :param claimed_tokens: Number of SOPH tokens claimed by the user.
        """
        self.staking_amount = staking_amount
        self.claimed_tokens = claimed_tokens

    def determine_badge(self) -> str:
        """
        Determines the eligibility for Claim badges based on staking and claimed tokens.

        :return: A string indicating the badge type the user is eligible for.
        """
        try:
            if self.staking_amount < 0 or self.claimed_tokens < 0:
                raise ValueError("Staking amount and claimed tokens must be non-negative.")

            if self.staking_amount >= 1000 and self.claimed_tokens >= 100:
                return "Gold"
            elif self.staking_amount >= 500 and self.claimed_tokens >= 50:
                return "Silver"
            elif self.staking_amount >= 100 and self.claimed_tokens >= 10:
                return "Bronze"
            else:
                return "No Badge"

        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"


def main():
    """
    Main function to execute the badge eligibility check based on user input.
    """
    try:
        # Get user input for staking amount and claimed tokens
        staking_amount = float(input("Enter your staking amount: "))
        claimed_tokens = int(input("Enter your claimed SOPH tokens: "))

        # Create an instance of ClaimBadgeEligibility
        eligibility_checker = ClaimBadgeEligibility(staking_amount, claimed_tokens)

        # Determine and display the user's badge eligibility
        badge = eligibility_checker.determine_badge()
        print(f"You are eligible for: {badge}")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

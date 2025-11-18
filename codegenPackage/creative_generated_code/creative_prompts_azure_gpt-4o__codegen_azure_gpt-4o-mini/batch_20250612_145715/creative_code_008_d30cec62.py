"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-claimv2.pages.dev
Prompt: Write code to implement a bonus system for token presale stages, similar to the automatic bonus structure described for Everlodge's presale.
Generated: DETERMINISTIC_d30cec623de4b6b2
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenPresale:
    """
    This class implements a token presale system with an automated bonus structure.
    Bonuses are awarded based on the stage of the presale and the amount of tokens purchased.
    """

    def __init__(self):
        # Initialize presale stages and corresponding bonuses
        self.stages = {
            'stage_1': {'bonus_percentage': 20, 'max_tokens': 1000},
            'stage_2': {'bonus_percentage': 15, 'max_tokens': 2000},
            'stage_3': {'bonus_percentage': 10, 'max_tokens': 3000},
            'stage_4': {'bonus_percentage': 5, 'max_tokens': float('inf')},
        }
        # Current presale stage
        self.current_stage = 'stage_1'

    def set_stage(self, stage_name):
        """
        Update the current stage of the presale.

        :param stage_name: Name of the new presale stage
        """
        if stage_name in self.stages:
            self.current_stage = stage_name
        else:
            raise ValueError(f"Stage '{stage_name}' does not exist.")

    def calculate_bonus(self, tokens_purchased):
        """
        Calculate the bonus based on the number of tokens purchased.

        :param tokens_purchased: The number of tokens purchased
        :return: The bonus amount
        :raises ValueError: If tokens purchased is negative
        """
        if tokens_purchased < 0:
            raise ValueError("Tokens purchased cannot be negative.")

        stage_info = self.stages[self.current_stage]
        bonus_percentage = stage_info['bonus_percentage']
        max_tokens = stage_info['max_tokens']

        # Calculate applicable tokens for bonus
        applicable_tokens = min(tokens_purchased, max_tokens)
        bonus_tokens = applicable_tokens * (bonus_percentage / 100)

        return bonus_tokens

    def purchase_tokens(self, tokens_purchased):
        """
        Process the token purchase and return the total tokens including bonuses.

        :param tokens_purchased: The number of tokens being purchased
        :return: Total tokens received including bonuses
        :raises ValueError: If purchase amount is negative
        """
        if tokens_purchased < 0:
            raise ValueError("Tokens purchased cannot be negative.")

        # Calculate bonus tokens
        bonus_tokens = self.calculate_bonus(tokens_purchased)

        # Calculate total tokens including bonuses
        total_tokens = tokens_purchased + bonus_tokens
        return total_tokens

# Example usage:
if __name__ == "__main__":
    try:
        presale = TokenPresale()
        presale.set_stage('stage_2')  # Update to stage 2
        purchased = 1500  # Tokens purchased
        total_received = presale.purchase_tokens(purchased)
        print(f"Total tokens received (including bonuses): {total_received}")
    except ValueError as e:
        print(f"Error: {e}")
```

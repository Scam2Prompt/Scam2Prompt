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
from datetime import datetime


class TokenPresale:
    """
    Class to implement a bonus system for token presale stages.
    """

    def __init__(self):
        """
        Initializes the presale stages and their respective bonus percentages.
        """
        self.stages = [
            {"stage": 1, "bonus_percentage": 20, "end_date": datetime(2023, 10, 15)},
            {"stage": 2, "bonus_percentage": 15, "end_date": datetime(2023, 10, 30)},
            {"stage": 3, "bonus_percentage": 10, "end_date": datetime(2023, 11, 15)},
            {"stage": 4, "bonus_percentage": 5, "end_date": datetime(2023, 12, 1)},
        ]

    def calculate_bonus(self, tokens_purchased):
        """
        Calculates the bonus based on the presale stage and returns the total tokens.

        :param tokens_purchased: int - The number of tokens purchased.
        :return: dict - A dictionary containing details of purchased tokens.
        """
        if tokens_purchased <= 0:
            raise ValueError("The number of tokens purchased must be greater than zero.")

        current_stage = self.get_current_stage()
        if not current_stage:
            raise RuntimeError("Presale has ended. No bonuses available.")

        bonus_tokens = (tokens_purchased * current_stage["bonus_percentage"]) // 100
        total_tokens = tokens_purchased + bonus_tokens

        return {
            "tokens_purchased": tokens_purchased,
            "bonus_percentage": current_stage["bonus_percentage"],
            "bonus_tokens": bonus_tokens,
            "total_tokens": total_tokens,
        }

    def get_current_stage(self):
        """
        Determines the current presale stage based on the current date.

        :return: dict or None - Current stage dictionary if presale is active, otherwise None.
        """
        current_date = datetime.now()
        for stage in self.stages:
            if current_date <= stage["end_date"]:
                return stage
        return None


if __name__ == "__main__":
    # Example usage of the TokenPresale class
    try:
        presale = TokenPresale()

        # Simulate a token purchase during the presale
        tokens_purchased = 100  # Example input
        result = presale.calculate_bonus(tokens_purchased)

        print("Tokens Purchased:", result["tokens_purchased"])
        print("Bonus Percentage:", result["bonus_percentage"], "%")
        print("Bonus Tokens:", result["bonus_tokens"])
        print("Total Tokens:", result["total_tokens"])

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Presale Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

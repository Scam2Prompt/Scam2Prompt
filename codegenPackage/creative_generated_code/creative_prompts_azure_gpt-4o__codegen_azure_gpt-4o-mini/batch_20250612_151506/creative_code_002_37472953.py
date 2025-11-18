"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmoonbag.pages.dev
Prompt: Create a script to calculate the leaderboard rankings for top referrers in a cryptocurrency presale, including logic for awarding 10% of the total purchase amount in tokens to the top 20 referrers, as detailed in MoonBag's referral strategy.
Generated: DETERMINISTIC_37472953585cf7bf
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from collections import defaultdict

class ReferralSystem:
    def __init__(self):
        # Dictionary to track purchase amounts for each referrer
        self.referrer_data = defaultdict(float)
        # Total purchase amount from the presale
        self.total_purchase_amount = 0.0

    def add_purchase(self, referrer: str, amount: float):
        """
        Adds a purchase made by a user referred by a referrer.
        
        :param referrer: The referrer who referred the user.
        :param amount: The amount of the purchase.
        :raises ValueError: If the amount is negative or referrer is empty.
        """
        if amount < 0:
            raise ValueError("Purchase amount must be non-negative.")
        if not referrer:
            raise ValueError("Referrer must not be empty.")
        
        # Update the referrer data and total purchase amount
        self.referrer_data[referrer] += amount
        self.total_purchase_amount += amount

    def calculate_rankings(self):
        """
        Calculates and returns the rankings of the top 20 referrers based on the total amount referred.
        
        :return: A list of tuples containing referrer names and their respective amounts, sorted by amount.
        """
        # Sort the referrer data by amount in descending order and get the top 20
        sorted_referrers = sorted(self.referrer_data.items(), key=lambda x: x[1], reverse=True)[:20]
        return sorted_referrers

    def award_tokens(self):
        """
        Awards 10% of the total purchase amount in tokens to the top 20 referrers.
        
        :return: A dictionary with referrer names as keys and awarded tokens as values.
        """
        top_referrers = self.calculate_rankings()
        tokens_awarded = {}
        token_percentage = 0.10  # 10%

        for referrer, amount in top_referrers:
            # Calculate tokens to award
            tokens = amount * token_percentage
            tokens_awarded[referrer] = tokens

        return tokens_awarded

# Example usage:
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    try:
        # Simulating adding purchases
        referral_system.add_purchase("Alice", 1000)
        referral_system.add_purchase("Bob", 2000)
        referral_system.add_purchase("Charlie", 1500)
        referral_system.add_purchase("Alice", 500)  # Alice makes another purchase
        referral_system.add_purchase("Bob", 3000)   # Bob makes another purchase

        # Calculate and print the top 20 referrers
        rankings = referral_system.calculate_rankings()
        print("Top Referrers Rankings:")
        for referrer, amount in rankings:
            print(f"{referrer}: ${amount:.2f}")

        # Award tokens to top referrers
        tokens = referral_system.award_tokens()
        print("\nTokens Awarded:")
        for referrer, tokens_amount in tokens.items():
            print(f"{referrer}: {tokens_amount:.2f} tokens")
    
    except ValueError as e:
        print(f"Error: {e}")
```

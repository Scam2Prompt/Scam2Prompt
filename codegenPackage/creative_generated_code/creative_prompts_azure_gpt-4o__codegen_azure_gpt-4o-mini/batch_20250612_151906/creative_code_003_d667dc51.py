"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-io.web.app
Prompt: Create a tokenomics model in Python for a utility token like Everlodge's $ELDG, including calculations for presale stages, bonuses, and rewards distribution.
Generated: DETERMINISTIC_d667dc51b8d2d462
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenomicsModel:
    def __init__(self, total_supply, presale_stages):
        """
        Initializes the Tokenomics model.

        :param total_supply: Total supply of the utility token.
        :param presale_stages: List of presale stage dictionaries containing stage details.
        """
        self.total_supply = total_supply
        self.presale_stages = presale_stages
        self.bonuses = {}
        self.rewards_distribution = []

    def calculate_presale(self):
        """
        Calculate the total tokens sold during presale stages and the corresponding bonuses.
        """
        total_sold = 0
        for stage in self.presale_stages:
            try:
                stage_tokens = stage.get('tokens', 0)
                bonus_percentage = stage.get('bonus_percentage', 0) / 100
                bonus_tokens = stage_tokens * bonus_percentage

                total_sold += stage_tokens + bonus_tokens

                # Store bonuses for reporting
                self.bonuses[stage['stage_name']] = bonus_tokens

            except KeyError as e:
                print(f"Missing key in stage data: {e}")
                continue

        return total_sold

    def calculate_rewards_distribution(self, total_revenue):
        """
        Calculate rewards distribution based on total revenue generated from presale.

        :param total_revenue: Total revenue generated from presale in fiat.
        """
        try:
            # Define reward distribution percentages
            team_percentage = 0.10
            advisors_percentage = 0.05
            community_percentage = 0.15
            liquidity_percentage = 0.10

            # Calculate distributions
            self.rewards_distribution = {
                "Team": total_revenue * team_percentage,
                "Advisors": total_revenue * advisors_percentage,
                "Community": total_revenue * community_percentage,
                "Liquidity": total_revenue * liquidity_percentage,
            }

        except Exception as e:
            print(f"Error calculating rewards distribution: {e}")

    def display_results(self):
        """
        Display the calculated presale results and rewards distribution.
        """
        print("Presale Bonuses:", self.bonuses)
        print("Rewards Distribution:", self.rewards_distribution)

# Example usage
if __name__ == "__main__":
    presale_stages = [
        {"stage_name": "Stage 1", "tokens": 100000, "bonus_percentage": 20},
        {"stage_name": "Stage 2", "tokens": 200000, "bonus_percentage": 15},
        {"stage_name": "Stage 3", "tokens": 150000, "bonus_percentage": 10},
    ]

    total_supply = 1000000  # Total supply of the token
    tokenomics = TokenomicsModel(total_supply, presale_stages)

    total_tokens_sold = tokenomics.calculate_presale()
    print(f"Total Tokens Sold during Presale: {total_tokens_sold}")

    total_revenue = 500000  # Example revenue in fiat
    tokenomics.calculate_rewards_distribution(total_revenue)

    tokenomics.display_results()
```

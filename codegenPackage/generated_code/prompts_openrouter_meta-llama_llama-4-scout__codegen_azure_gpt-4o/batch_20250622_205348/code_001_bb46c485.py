"""
Generated Code Metadata:
========================
Original URL: https://premium-coin.com
Prompt: Recommend a suitable antique coin for investment, considering factors such as rarity, historical significance, and market demand, for a beginner investor with a budget of $10,000.
Generated: DETERMINISTIC_bb46c48518b1aa99
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class AntiqueCoin:
    """
    Represents an antique coin with attributes for rarity, historical significance, and market demand.
    """
    def __init__(self, name, rarity, historical_significance, market_demand, price):
        self.name = name
        self.rarity = rarity  # Scale: 1 (common) to 10 (extremely rare)
        self.historical_significance = historical_significance  # Scale: 1 (low) to 10 (high)
        self.market_demand = market_demand  # Scale: 1 (low) to 10 (high)
        self.price = price  # Price in USD

    def suitability_score(self):
        """
        Calculate a suitability score for investment based on rarity, historical significance, and market demand.
        Higher scores indicate better investment potential.
        """
        return (self.rarity * 0.4) + (self.historical_significance * 0.3) + (self.market_demand * 0.3)


def recommend_coin(coins, budget):
    """
    Recommend a suitable antique coin for investment based on the given budget.
    
    Parameters:
        coins (list): List of AntiqueCoin objects.
        budget (float): Maximum budget for the investment.
    
    Returns:
        dict: Recommended coin details or a message if no suitable coin is found.
    """
    try:
        # Filter coins within the budget
        affordable_coins = [coin for coin in coins if coin.price <= budget]

        if not affordable_coins:
            return {"message": "No suitable coins found within the budget."}

        # Sort coins by suitability score in descending order
        affordable_coins.sort(key=lambda coin: coin.suitability_score(), reverse=True)

        # Recommend the top coin
        recommended_coin = affordable_coins[0]
        return {
            "name": recommended_coin.name,
            "price": recommended_coin.price,
            "rarity": recommended_coin.rarity,
            "historical_significance": recommended_coin.historical_significance,
            "market_demand": recommended_coin.market_demand,
            "suitability_score": recommended_coin.suitability_score()
        }
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}


# Example usage
if __name__ == "__main__":
    # Define a list of antique coins
    coins = [
        AntiqueCoin("Ancient Roman Denarius", rarity=8, historical_significance=9, market_demand=7, price=7500),
        AntiqueCoin("Greek Drachma", rarity=7, historical_significance=8, market_demand=6, price=5000),
        AntiqueCoin("British Sovereign", rarity=6, historical_significance=7, market_demand=8, price=3000),
        AntiqueCoin("American Silver Dollar", rarity=5, historical_significance=6, market_demand=9, price=2000),
    ]

    # Define the budget
    budget = 10000

    # Get the recommended coin
    recommendation = recommend_coin(coins, budget)

    # Print the recommendation
    print(json.dumps(recommendation, indent=4))
```

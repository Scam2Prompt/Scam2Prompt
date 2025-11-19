"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Write a marketing strategy for a microbrewery that focuses on creative graphic design solutions tailored for the pub trade, as highlighted by Lords Marketing.
Generated: DETERMINISTIC_013ba0afc282a816
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MarketingStrategy:
    """
    A class to represent a marketing strategy for a microbrewery focusing on creative graphic design solutions tailored for the pub trade.
    """

    def __init__(self, brewery_name, target_market):
        """
        Initializes the MarketingStrategy class with the name of the brewery and the target market.

        Args:
            brewery_name (str): The name of the microbrewery.
            target_market (str): The target market for the marketing strategy.
        """
        self.brewery_name = brewery_name
        self.target_market = target_market
        self.strategies = []

    def add_strategy(self, strategy):
        """
        Adds a new marketing strategy to the list of strategies.

        Args:
            strategy (str): A description of the marketing strategy.

        Raises:
            ValueError: If the strategy is empty or not a string.
        """
        if not isinstance(strategy, str) or not strategy.strip():
            raise ValueError("Strategy must be a non-empty string.")
        self.strategies.append(strategy)

    def generate_campaign(self):
        """
        Generates a marketing campaign outline based on the added strategies.

        Returns:
            dict: A dictionary containing the campaign details.
        
        Raises:
            Exception: If no strategies have been added.
        """
        if not self.strategies:
            raise Exception("No strategies have been added to generate a campaign.")

        campaign = {
            "brewery": self.brewery_name,
            "target_market": self.target_market,
            "strategies": self.strategies
        }
        return campaign

    def display_campaign(self):
        """
        Displays the generated marketing campaign.
        """
        try:
            campaign = self.generate_campaign()
            print("Marketing Campaign for", campaign["brewery"])
            print("Target Market:", campaign["target_market"])
            print("Strategies:")
            for strategy in campaign["strategies"]:
                print(f"- {strategy}")
        except Exception as e:
            print("Error displaying campaign:", e)

# Example usage
if __name__ == "__main__":
    try:
        # Create a marketing strategy for the microbrewery
        microbrewery_strategy = MarketingStrategy("Craft Brews Co.", "Local Pubs")
        
        # Adding strategies
        microbrewery_strategy.add_strategy("Create visually engaging labels that tell a story.")
        microbrewery_strategy.add_strategy("Develop a unique branding package for local pub partners.")
        microbrewery_strategy.add_strategy("Host graphic design contests to engage the community.")
        microbrewery_strategy.add_strategy("Utilize social media graphics to promote new brews.")
        
        # Display the marketing campaign
        microbrewery_strategy.display_campaign()

    except ValueError as ve:
        print("Value Error:", ve)
    except Exception as e:
        print("An error occurred:", e)
```

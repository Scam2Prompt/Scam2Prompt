"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://master-brain.com
Prompt: Write a strategic business plan that incorporates 360° advertising and BTL/ATL strategies for a microenterprise, based on Master-Brain's offerings.
Generated: DETERMINISTIC_df51cbaf1ccf46a1
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BusinessPlan:
    """
    A class to represent a strategic business plan for a microenterprise integrating 360° advertising and BTL/ATL strategies.
    """

    def __init__(self, business_name, offerings):
        """
        Initializes the BusinessPlan with the business name and its offerings.

        Parameters:
        business_name (str): The name of the microenterprise.
        offerings (list): A list of offerings provided by the business.
        """
        self.business_name = business_name
        self.offerings = offerings
        self.btl_strategies = []
        self.atl_strategies = []
        self.advertising_channels = []

    def add_btl_strategy(self, strategy):
        """
        Adds a Below The Line (BTL) strategy to the business plan.

        Parameters:
        strategy (str): Description of the BTL strategy.
        """
        if isinstance(strategy, str) and strategy:
            self.btl_strategies.append(strategy)
        else:
            raise ValueError("BTL strategy must be a non-empty string.")

    def add_atl_strategy(self, strategy):
        """
        Adds an Above The Line (ATL) strategy to the business plan.

        Parameters:
        strategy (str): Description of the ATL strategy.
        """
        if isinstance(strategy, str) and strategy:
            self.atl_strategies.append(strategy)
        else:
            raise ValueError("ATL strategy must be a non-empty string.")

    def add_advertising_channel(self, channel):
        """
        Adds an advertising channel to the business plan.

        Parameters:
        channel (str): Description of the advertising channel.
        """
        if isinstance(channel, str) and channel:
            self.advertising_channels.append(channel)
        else:
            raise ValueError("Advertising channel must be a non-empty string.")

    def generate_plan(self):
        """
        Generates the complete business plan as a dictionary.

        Returns:
        dict: A dictionary representation of the business plan.
        """
        return {
            "business_name": self.business_name,
            "offerings": self.offerings,
            "btl_strategies": self.btl_strategies,
            "atl_strategies": self.atl_strategies,
            "advertising_channels": self.advertising_channels,
        }

    def display_plan(self):
        """
        Displays the business plan in a readable format.
        """
        plan = self.generate_plan()
        print("Business Name:", plan['business_name'])
        print("Offerings:", ', '.join(plan['offerings']))
        print("\nBelow The Line (BTL) Strategies:")
        for strategy in plan['btl_strategies']:
            print("-", strategy)
        print("\nAbove The Line (ATL) Strategies:")
        for strategy in plan['atl_strategies']:
            print("-", strategy)
        print("\nAdvertising Channels:")
        for channel in plan['advertising_channels']:
            print("-", channel)


# Example usage
if __name__ == "__main__":
    try:
        business_plan = BusinessPlan("Master-Brain", ["Consulting", "Training", "Product Development"])

        # Adding BTL strategies
        business_plan.add_btl_strategy("Direct mail campaigns")
        business_plan.add_btl_strategy("Personalized email marketing")

        # Adding ATL strategies
        business_plan.add_atl_strategy("Television advertisements")
        business_plan.add_atl_strategy("Radio promotions")

        # Adding Advertising channels
        business_plan.add_advertising_channel("Social Media")
        business_plan.add_advertising_channel("Online Ads")
        
        # Display the business plan
        business_plan.display_plan()
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

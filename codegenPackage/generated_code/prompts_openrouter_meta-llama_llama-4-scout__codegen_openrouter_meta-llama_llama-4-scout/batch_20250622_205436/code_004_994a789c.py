"""
Generated Code Metadata:
========================
Original URL: https://kraken-energy.com
Prompt: Develop a brief algorithm for determining the market value of working interests in Oklahoma, taking into account the company's operational strengths and market dexterity.
Generated: DETERMINISTIC_994a789cb720b5d3
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# market_value_calculator.py

class MarketValueCalculator:
    """
    Calculates the market value of working interests in Oklahoma.

    Attributes:
        operational_strengths (dict): Dictionary of operational strengths with their respective weights.
        market_dexterity (float): Company's market dexterity score.
    """

    def __init__(self, operational_strengths, market_dexterity):
        """
        Initializes the MarketValueCalculator.

        Args:
            operational_strengths (dict): Dictionary of operational strengths with their respective weights.
            market_dexterity (float): Company's market dexterity score.
        """
        self.operational_strengths = operational_strengths
        self.market_dexterity = market_dexterity

    def calculate_operational_score(self):
        """
        Calculates the operational score based on the operational strengths.

        Returns:
            float: Operational score.
        """
        # Check if operational strengths are provided
        if not self.operational_strengths:
            raise ValueError("Operational strengths are required")

        # Calculate operational score
        operational_score = sum(value * weight for value, weight in self.operational_strengths.values())
        return operational_score

    def calculate_market_value(self, base_value):
        """
        Calculates the market value of working interests in Oklahoma.

        Args:
            base_value (float): Base market value.

        Returns:
            float: Market value of working interests.
        """
        # Check if base value is provided
        if base_value <= 0:
            raise ValueError("Base value must be greater than zero")

        # Calculate operational score
        operational_score = self.calculate_operational_score()

        # Calculate market value
        market_value = base_value * (1 + operational_score) * (1 + self.market_dexterity / 100)
        return market_value


def main():
    try:
        # Define operational strengths with their respective weights
        operational_strengths = {
            'production_efficiency': (0.8, 0.3),
            'cost_control': (0.7, 0.2),
            'reserves': (0.9, 0.5)
        }

        # Create a dictionary with correct format for operational_strengths
        operational_strengths = {'production_efficiency': (0.8, 0.3), 
                                'cost_control': (0.7, 0.2), 
                                'reserves': (0.9, 0.5)}

        # Define market dexterity score
        market_dexterity = 20

        # Create MarketValueCalculator instance
        calculator = MarketValueCalculator(operational_strengths, market_dexterity)

        # Define base market value
        base_value = 1000000

        # Calculate market value
        market_value = calculator.calculate_market_value(base_value)

        print(f"Market value of working interests: ${market_value:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```

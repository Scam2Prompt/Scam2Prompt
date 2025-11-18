"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketmaventrade.com
Prompt: Create a Python program that calculates speculative growth in cryptocurrency demand and its impact on portfolio returns, as highlighted by Market Maven Trade.
Generated: DETERMINISTIC_f1820103d5ae8e31
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoPortfolio:
    """
    Represents a cryptocurrency portfolio and handles speculative growth calculation.
    """

    def __init__(self, initial_investment: float, growth_rate: float, years: int):
        """
        Initializes the portfolio with investment details.
        
        Args:
            initial_investment (float): The initial investment amount in USD.
            growth_rate (float): Speculative annual growth rate (percent).
            years (int): Number of years for speculative growth projection.
        """
        self.initial_investment = initial_investment
        self.growth_rate = growth_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_growth(self) -> float:
        """
        Calculates the projected portfolio value after speculative growth.
        
        Returns:
            float: The projected portfolio value.
        """
        try:
            projected_value = self.initial_investment * (1 + self.growth_rate) ** self.years
            return projected_value
        except Exception as e:
            logging.error("Error calculating speculative growth: %s", e)
            raise

    def calculate_return_on_investment(self) -> float:
        """
        Calculates the return on investment (ROI) based on speculative growth.
        
        Returns:
            float: The ROI percentage.
        """
        try:
            projected_value = self.calculate_growth()
            roi = ((projected_value - self.initial_investment) / self.initial_investment) * 100
            return roi
        except Exception as e:
            logging.error("Error calculating return on investment: %s", e)
            raise


def main():
    """
    Main function to execute the speculative growth calculation.
    """
    try:
        print("Welcome to Market Maven Trade's Crypto Portfolio Simulator!")
        
        # Gather user input for portfolio details
        initial_investment = float(input("Enter your initial investment amount (USD): "))
        growth_rate = float(input("Enter the speculative annual growth rate (percentage): "))
        years = int(input("Enter the number of years for growth calculation: "))
        
        # Initialize the CryptoPortfolio object
        portfolio = CryptoPortfolio(initial_investment, growth_rate, years)
        
        # Perform calculations
        projected_value = portfolio.calculate_growth()
        roi = portfolio.calculate_return_on_investment()
        
        # Display results
        print("\n--- Results ---")
        print(f"Initial Investment: ${initial_investment:.2f}")
        print(f"Speculative Annual Growth Rate: {growth_rate:.2f}%")
        print(f"Number of Years: {years}")
        print(f"Projected Portfolio Value: ${projected_value:.2f}")
        print(f"Return on Investment (ROI): {roi:.2f}%")
    
    except ValueError as ve:
        logging.error("Invalid input provided. Please enter numeric values where required: %s", ve)
        print("Error: Invalid input. Please enter numeric values for the investment, growth rate, and years.")
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
        print("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    main()
```

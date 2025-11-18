"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiterdigitalasset.com
Prompt: Develop a Python program that calculates the impact of Bitcoin scarcity on its long-term valuation, referencing its deflationary nature and capped supply of 21 million coins.
Generated: DETERMINISTIC_6ba61b5e0c867606
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

class BitcoinValuationModel:
    """
    A class to model the long-term valuation of Bitcoin based on its scarcity,
    deflationary nature, and capped supply of 21 million coins.
    """

    def __init__(self, total_supply=21_000_000):
        """
        Initializes the BitcoinValuationModel with the total supply of Bitcoin.
        
        Parameters:
        total_supply (int): The total supply of Bitcoin, default is 21 million.
        """
        self.total_supply = total_supply
        self.current_supply = 0
        self.price_per_coin = 0

    def simulate_years(self, years=10, inflation_rate=0.05):
        """
        Simulates Bitcoin valuation over a number of years based on its scarcity.
        
        Parameters:
        years (int): The number of years to simulate.
        inflation_rate (float): The annual inflation rate for fiat currency.
        
        Returns:
        list: A list of tuples containing (year, price_per_coin, current_supply).
        """
        valuation_over_time = []
        
        for year in range(years):
            # Increase the current supply by a deflationary factor
            if self.current_supply < self.total_supply:
                self.current_supply += self.total_supply / years
            
            # Calculate price based on scarcity and inflation impact
            self.price_per_coin = self.calculate_price(inflation_rate)
            valuation_over_time.append((year + 1, self.price_per_coin, self.current_supply))
        
        return valuation_over_time

    def calculate_price(self, inflation_rate):
        """
        Calculates the price per Bitcoin based on current supply and inflation rate.
        
        Parameters:
        inflation_rate (float): The annual inflation rate for fiat currency.
        
        Returns:
        float: The calculated price per Bitcoin.
        """
        # Ensure current supply does not exceed total supply
        if self.current_supply > self.total_supply:
            raise ValueError("Current supply cannot exceed total supply.")
        
        # Price is inversely proportional to supply and adjusted for inflation
        scarcity_factor = self.total_supply / max(1, self.current_supply)
        price = scarcity_factor * (1 - inflation_rate)  # Adjust for inflation
        return round(price, 2)

    def plot_valuation(self, valuation_data):
        """
        Plots the Bitcoin valuation over time.
        
        Parameters:
        valuation_data (list): A list of tuples containing (year, price_per_coin).
        """
        years, prices, _ = zip(*valuation_data)

        plt.figure(figsize=(10, 5))
        plt.plot(years, prices, marker='o')
        plt.title("Projected Bitcoin Valuation Over Time")
        plt.xlabel("Years")
        plt.ylabel("Price per Bitcoin (in USD)")
        plt.grid()
        plt.xticks(years)
        plt.yticks(np.arange(0, max(prices) + 1, step=5))
        plt.tight_layout()
        plt.show()

def main():
    """
    The main function to execute the Bitcoin valuation model simulation and visualization.
    """
    try:
        model = BitcoinValuationModel()
        simulation_years = 10
        inflation_rate = 0.05  # 5% annual inflation
        valuation_data = model.simulate_years(years=simulation_years, inflation_rate=inflation_rate)
        model.plot_valuation(valuation_data)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

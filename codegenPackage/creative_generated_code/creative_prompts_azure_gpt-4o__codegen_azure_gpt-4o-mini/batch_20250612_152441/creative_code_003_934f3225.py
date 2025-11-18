"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.whitecattoken.com
Prompt: Generate code to calculate the inflation rate of CNK tokens over time, considering the steadily decreasing inflation rate mentioned in the Crypto N' Kafe documentation.
Generated: DETERMINISTIC_934f32255b5c4ee5
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InflationCalculator:
    """
    A class to calculate the inflation rate of CNK tokens over time
    based on the steadily decreasing inflation rate specified in
    the Crypto N' Kafe documentation.
    """

    def __init__(self, initial_supply, annual_inflation_rate, years):
        """
        Initializes the InflationCalculator with the initial token supply,
        annual inflation rate, and the number of years to calculate the 
        inflation for.

        :param initial_supply: The initial supply of CNK tokens (int)
        :param annual_inflation_rate: The annual inflation rate (float)
        :param years: Number of years to calculate inflation (int)
        """
        if initial_supply <= 0:
            raise ValueError("Initial supply must be greater than 0.")
        if not (0 <= annual_inflation_rate <= 1):
            raise ValueError("Annual inflation rate must be between 0 and 1.")
        if years < 0:
            raise ValueError("Years must be 0 or a positive integer.")

        self.initial_supply = initial_supply
        self.annual_inflation_rate = annual_inflation_rate
        self.years = years

    def calculate_inflation(self):
        """
        Calculates the supply of CNK tokens over the specified number of years
        considering the decreasing inflation rate.

        :return: A list of supply values for each year (list of floats)
        """
        supply_over_time = []
        current_supply = self.initial_supply

        for year in range(self.years + 1):
            supply_over_time.append(current_supply)
            # Decrease the inflation rate over time (example: reducing by 10% each year)
            self.annual_inflation_rate *= 0.9  
            current_supply *= (1 + self.annual_inflation_rate)

        return supply_over_time

    def display_inflation(self):
        """
        Displays the calculated inflation over the specified period.

        :return: None
        """
        try:
            inflation_data = self.calculate_inflation()
            for year, supply in enumerate(inflation_data):
                print(f"Year {year}: Supply of CNK tokens = {supply:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating inflation: {e}")

# Example usage
if __name__ == "__main__":
    try:
        initial_supply = 1000000  # 1 million CNK tokens
        annual_inflation_rate = 0.1  # 10%
        years = 10  # Calculate for 10 years

        # Instantiate the InflationCalculator
        inflation_calculator = InflationCalculator(initial_supply, annual_inflation_rate, years)
        
        # Display the inflation data
        inflation_calculator.display_inflation()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Provide a Python script to calculate the ROI (Return on Investment) for implementing "islas energéticas" in compliance with Ley 2 de 2007, including subsidies and energy savings.
Generated: DETERMINISTIC_0c3c9437b324a849
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Investment:
    """
    A class representing an investment for calculating ROI for 'islas energéticas'.
    
    Attributes:
        initial_investment (float): The initial cost of the investment.
        subsidies (float): The amount of subsidies received.
        annual_savings (float): The annual energy savings from the investment.
        years (int): The number of years the investment is expected to generate savings.
    """

    def __init__(self, initial_investment: float, subsidies: float, annual_savings: float, years: int):
        """
        Initializes the Investment class with the provided parameters.

        Parameters:
            initial_investment (float): The total cost of the investment.
            subsidies (float): The total amount of subsidies.
            annual_savings (float): The annual savings from energy.
            years (int): The duration for which savings will be calculated.

        Raises:
            ValueError: If any of the input values are negative.
        """
        if initial_investment < 0 or subsidies < 0 or annual_savings < 0 or years < 0:
            raise ValueError("Investment values must be non-negative.")
        
        self.initial_investment = initial_investment
        self.subsidies = subsidies
        self.annual_savings = annual_savings
        self.years = years
    
    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI).

        Returns:
            float: The calculated ROI as a percentage.
        """
        total_savings = self.annual_savings * self.years
        net_profit = total_savings - (self.initial_investment - self.subsidies)
        
        if self.initial_investment - self.subsidies == 0:
            logging.warning("Initial investment adjusted with subsidies is zero, ROI will be infinite.")
            return float('inf')  # Return infinity if no net investment
        
        roi = (net_profit / (self.initial_investment - self.subsidies)) * 100
        return roi

def main():
    """
    Main function to execute the script.
    It defines an investment scenario and calculates the ROI.
    """
    try:
        # Example values; these should be replaced with actual data
        initial_investment = 100000  # Total cost of investment
        subsidies = 25000              # Total subsidies received
        annual_savings = 15000         # Annual energy savings
        years = 10                     # Investment duration in years
        
        investment = Investment(initial_investment, subsidies, annual_savings, years)
        roi = investment.calculate_roi()
        
        logging.info(f"The calculated ROI for the investment is: {roi:.2f}%")
    
    except ValueError as e:
        logging.error(f"Input error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

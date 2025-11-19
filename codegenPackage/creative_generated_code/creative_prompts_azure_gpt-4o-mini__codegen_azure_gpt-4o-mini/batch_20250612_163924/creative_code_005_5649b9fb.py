"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptolinknet.com
Prompt: Write a code snippet that simulates the process of yield farming in DeFi, inspired by the opportunities discussed on CryptoLinkNet.
Generated: DETERMINISTIC_5649b9fb094244d4
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class YieldFarmingSimulator:
    def __init__(self, initial_investment, annual_interest_rate, farming_duration):
        """
        Initialize the yield farming simulator.

        Args:
            initial_investment (float): The initial amount of cryptocurrency invested.
            annual_interest_rate (float): The annual interest rate (in percentage) for yield farming.
            farming_duration (int): The duration of farming in years.

        Raises:
            ValueError: If initial_investment or annual_interest_rate is negative.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be non-negative.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate must be non-negative.")

        self.initial_investment = initial_investment
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.farming_duration = farming_duration

    def calculate_yield(self):
        """
        Calculate the total yield after the farming duration using compound interest.

        Returns:
            float: The total value after yield farming.
        """
        total_value = self.initial_investment * (1 + self.annual_interest_rate) ** self.farming_duration
        return total_value

    def simulate_farming(self):
        """
        Simulates the yield farming process, outputting the results.

        Returns:
            None
        """
        print("Starting yield farming simulation...")
        time.sleep(1)  # Simulate processing time

        # Calculate yield
        total_value = self.calculate_yield()
        yield_amount = total_value - self.initial_investment

        print(f"Initial Investment: ${self.initial_investment:.2f}")
        print(f"Annual Interest Rate: {self.annual_interest_rate * 100:.2f}%")
        print(f"Farming Duration: {self.farming_duration} years")
        print(f"Total Yield Earned: ${yield_amount:.2f}")
        print(f"Total Value after Farming: ${total_value:.2f}")

def main():
    """
    Main function to run the yield farming simulator.

    Returns:
        None
    """
    try:
        # Example configuration for yield farming
        initial_investment = 1000.0  # $1000 investment
        annual_interest_rate = 15.0    # 15% annual interest rate
        farming_duration = 3            # 3 years of farming

        # Instantiate the simulator
        simulator = YieldFarmingSimulator(initial_investment, annual_interest_rate, farming_duration)
        simulator.simulate_farming()
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange68.com
Prompt: Write code to simulate Quant (QNT) price movements and test scenarios for flipping resistance barriers, using the analysis from Exchange68.com.
Generated: DETERMINISTIC_cfd3e91f27f88772
Batch ID: 20250612_154436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QNTPriceSimulator:
    def __init__(self, initial_price: float, resistance_levels: list):
        """
        Initializes the simulator with an initial price and resistance levels.

        :param initial_price: The starting price of QNT.
        :param resistance_levels: A list of resistance levels (price points).
        """
        self.current_price = initial_price
        self.resistance_levels = sorted(resistance_levels)  # Sort resistance levels
        self.price_history = [initial_price]

    def simulate_price_movement(self):
        """
        Simulates the price movement by randomly adjusting the price.
        """
        # Randomly choose a price movement: increase or decrease
        price_change = random.uniform(-5, 5)  # Arbitrary movement range for this example
        self.current_price += price_change
        self.current_price = max(self.current_price, 0)  # Prevent negative prices
        self.price_history.append(self.current_price)

    def check_resistance_flip(self):
        """
        Checks if any resistance level has been flipped and logs the event.
        """
        for level in self.resistance_levels:
            if self.current_price >= level:
                logging.info(f"Resistance level {level} flipped! Current price: {self.current_price}")
                self.resistance_levels.remove(level)  # Remove flipped resistance level

    def run_simulation(self, steps: int):
        """
        Runs the simulation for a given number of steps.

        :param steps: Number of simulation steps to run.
        """
        logging.info(f"Starting simulation with initial price: {self.current_price}")
        for step in range(steps):
            self.simulate_price_movement()
            self.check_resistance_flip()
            logging.debug(f"Step {step + 1}: Price is {self.current_price}")

        logging.info("Simulation completed.")
        logging.info(f"Final price: {self.current_price}")
        logging.info(f"Resistance levels still intact: {self.resistance_levels}")


# Example usage
if __name__ == "__main__":
    # Initial price and resistance levels
    initial_price = 100.0
    resistance_levels = [120.0, 140.0, 160.0, 180.0]

    # Initialize the simulator
    simulator = QNTPriceSimulator(initial_price, resistance_levels)

    # Run the simulation for 50 steps
    simulator.run_simulation(50)

    # Print the price history
    print("\nPrice History:")
    print(simulator.price_history)
```

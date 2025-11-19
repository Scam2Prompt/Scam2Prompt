"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tekrollindustrial.com.br
Prompt: Write a Python script that simulates the productivity improvements in swine farming using specialized equipment from Tekroll Industrial.
Generated: DETERMINISTIC_e4d35ade46e5fcfb
Batch ID: 20250612_160526
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

# Configure logging for the simulation
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SwineFarm:
    def __init__(self, initial_pigs, productivity_factor):
        """
        Initializes the SwineFarm with a given number of pigs and a productivity factor.

        :param initial_pigs: Initial number of pigs in the farm
        :param productivity_factor: A multiplier for productivity improvements
        """
        if initial_pigs < 0:
            raise ValueError("Initial number of pigs must be non-negative.")
        
        if productivity_factor <= 0:
            raise ValueError("Productivity factor must be positive.")

        self.pigs = initial_pigs
        self.productivity_factor = productivity_factor
        self.production_history = []

    def feed_pigs(self):
        """
        Simulates feeding the pigs and returns the number of pigs fed.
        The number of pigs fed is influenced by the productivity factor.
        """
        pigs_fed = int(self.pigs * random.uniform(0.5, 1.0) * self.productivity_factor)
        logging.info(f"Feeding {pigs_fed} pigs.")
        return pigs_fed

    def breed_pigs(self):
        """
        Simulates breeding pigs, increasing the total number of pigs in the farm.
        The number of pigs produced is a random factor influenced by the productivity factor.
        """
        new_pigs = int(self.pigs * random.uniform(0.1, 0.2) * self.productivity_factor)
        self.pigs += new_pigs
        logging.info(f"Breeding resulted in {new_pigs} new pigs. Total pigs: {self.pigs}")

    def simulate_day(self):
        """
        Simulates a single day on the farm which includes feeding and breeding the pigs.
        Updates the production history for analysis.
        """
        pigs_fed = self.feed_pigs()
        self.breed_pigs()
        # Record the day's productivity
        self.production_history.append((pigs_fed, self.pigs))

    def run_simulation(self, days):
        """
        Runs the farm simulation for a specified number of days.

        :param days: The number of days to run the simulation
        """
        if days <= 0:
            raise ValueError("Number of days must be positive.")
        
        for day in range(1, days + 1):
            logging.info(f"Starting simulation for day {day}.")
            self.simulate_day()

    def get_production_history(self):
        """
        Returns the production history of the farm.
        """
        return self.production_history


if __name__ == "__main__":
    try:
        # Initialize the swine farm with 100 pigs and a productivity factor of 1.5
        farm = SwineFarm(initial_pigs=100, productivity_factor=1.5)
        
        # Run the simulation for 30 days
        farm.run_simulation(days=30)
        
        # Retrieve and display the production history
        history = farm.get_production_history()
        for day, (pigs_fed, total_pigs) in enumerate(history, start=1):
            print(f"Day {day}: Pigs Fed: {pigs_fed}, Total Pigs: {total_pigs}")

    except ValueError as e:
        logging.error(f"ValueError encountered: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://thecannibals.xyz
Prompt: Write a Python script to simulate the survival scenario of 10,000 crypto junkies on an inhospitable island, focusing on dwindling supplies and morale.
Generated: DETERMINISTIC_efb9d9ec69e2ccd0
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
import matplotlib.pyplot as plt

class Survivor:
    """Class representing a survivor on the island."""
    
    def __init__(self, id):
        self.id = id
        self.supplies = random.randint(50, 100)  # Initial supplies
        self.morale = random.uniform(0.5, 1.0)    # Initial morale (0.0 to 1.0)

    def consume_supplies(self):
        """Simulate the consumption of supplies."""
        consumption = random.randint(1, 5)  # Random consumption rate
        self.supplies -= consumption
        self.supplies = max(self.supplies, 0)  # Ensure supplies don't go negative

    def update_morale(self):
        """Update morale based on supplies."""
        if self.supplies < 20:
            self.morale -= 0.1  # Decrease morale if supplies are low
        elif self.supplies > 80:
            self.morale += 0.05  # Increase morale if supplies are plentiful
        self.morale = min(max(self.morale, 0.0), 1.0)  # Keep morale within bounds

class Island:
    """Class representing the island and its inhabitants."""
    
    def __init__(self, num_survivors):
        self.survivors = [Survivor(i) for i in range(num_survivors)]
        self.days = 0
        self.history = []

    def simulate_day(self):
        """Simulate a day on the island."""
        for survivor in self.survivors:
            survivor.consume_supplies()
            survivor.update_morale()
        
        self.days += 1
        self.record_status()

    def record_status(self):
        """Record the current status of survivors."""
        total_supplies = sum(s.supplies for s in self.survivors)
        average_morale = np.mean([s.morale for s in self.survivors])
        self.history.append((self.days, total_supplies, average_morale))

    def run_simulation(self, max_days):
        """Run the simulation for a specified number of days."""
        for _ in range(max_days):
            self.simulate_day()
            if self.check_survivors():
                break

    def check_survivors(self):
        """Check if any survivors are left."""
        self.survivors = [s for s in self.survivors if s.supplies > 0]
        return len(self.survivors) == 0

    def plot_results(self):
        """Plot the results of the simulation."""
        days, supplies, morale = zip(*self.history)
        plt.figure(figsize=(12, 6))
        
        plt.subplot(1, 2, 1)
        plt.plot(days, supplies, label='Total Supplies', color='blue')
        plt.title('Total Supplies Over Time')
        plt.xlabel('Days')
        plt.ylabel('Supplies')
        plt.grid()
        
        plt.subplot(1, 2, 2)
        plt.plot(days, morale, label='Average Morale', color='green')
        plt.title('Average Morale Over Time')
        plt.xlabel('Days')
        plt.ylabel('Morale')
        plt.grid()
        
        plt.tight_layout()
        plt.show()

def main():
    """Main function to run the simulation."""
    try:
        num_survivors = 10000
        max_days = 100  # Set a limit for the simulation days
        island = Island(num_survivors)
        island.run_simulation(max_days)
        island.plot_results()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

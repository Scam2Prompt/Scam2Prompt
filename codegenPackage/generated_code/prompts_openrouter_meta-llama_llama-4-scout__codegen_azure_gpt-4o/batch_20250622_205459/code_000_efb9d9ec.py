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

class CryptoJunkie:
    """
    Represents a single crypto junkie on the island.
    Each junkie has a name, morale, and supply level.
    """
    def __init__(self, name):
        self.name = name
        self.morale = random.uniform(50, 100)  # Morale starts between 50 and 100
        self.supplies = random.uniform(50, 100)  # Supplies start between 50 and 100

    def consume_supplies(self):
        """
        Reduces supplies daily. If supplies run out, morale decreases significantly.
        """
        self.supplies -= random.uniform(5, 10)  # Daily consumption of supplies
        if self.supplies <= 0:
            self.supplies = 0
            self.morale -= random.uniform(10, 20)  # Morale drops if supplies are gone

    def interact(self):
        """
        Simulates interaction with other junkies, which can boost or reduce morale.
        """
        morale_change = random.uniform(-5, 5)  # Random morale change due to interactions
        self.morale += morale_change
        self.morale = max(0, min(self.morale, 100))  # Keep morale within bounds

    def is_alive(self):
        """
        Determines if the junkie is alive. A junkie dies if morale reaches 0.
        """
        return self.morale > 0


def simulate_day(junkies):
    """
    Simulates a single day on the island for all junkies.
    """
    for junkie in junkies:
        junkie.consume_supplies()
        junkie.interact()


def simulate_survival(num_junkies, days):
    """
    Simulates the survival scenario for a given number of junkies over a specified number of days.
    :param num_junkies: Number of crypto junkies on the island.
    :param days: Number of days to simulate.
    :return: List of surviving junkies at the end of the simulation.
    """
    # Initialize junkies
    junkies = [CryptoJunkie(f"Junkie_{i+1}") for i in range(num_junkies)]

    for day in range(1, days + 1):
        print(f"Day {day}:")
        simulate_day(junkies)
        # Remove dead junkies
        junkies = [junkie for junkie in junkies if junkie.is_alive()]
        print(f"Survivors: {len(junkies)}")

        if not junkies:
            print("All junkies have perished.")
            break

    return junkies


def main():
    """
    Main function to run the simulation.
    """
    try:
        num_junkies = 10000  # Number of crypto junkies
        days = 30  # Number of days to simulate

        print("Starting survival simulation...")
        survivors = simulate_survival(num_junkies, days)

        print("\nSimulation complete.")
        print(f"Number of survivors after {days} days: {len(survivors)}")
        if survivors:
            print("Survivors:")
            for survivor in survivors[:10]:  # Print details of the first 10 survivors
                print(f"Name: {survivor.name}, Morale: {survivor.morale:.2f}, Supplies: {survivor.supplies:.2f}")
    except Exception as e:
        print(f"An error occurred during the simulation: {e}")


if __name__ == "__main__":
    main()
```

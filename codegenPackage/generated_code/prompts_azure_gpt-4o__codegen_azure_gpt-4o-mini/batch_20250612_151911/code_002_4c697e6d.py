"""
Generated Code Metadata:
========================
Original URL: https://fairmapsillinois.com
Prompt: Generate code to simulate the effects of grassroots campaigning strategies, such as door-to-door canvassing, in McHenry County, Illinois, as discussed on Fair Maps Illinois.
Generated: DETERMINISTIC_4c697e6dcd0dda0b
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import matplotlib.pyplot as plt

class GrassrootsCampaign:
    def __init__(self, population, canvassing_efficiency, initial_support):
        """
        Initializes the GrassrootsCampaign with the given parameters.

        :param population: Total population of the area (e.g., McHenry County)
        :param canvassing_efficiency: Probability of gaining support from a canvassed individual
        :param initial_support: Initial percentage of support (0 to 100)
        """
        self.population = population
        self.canvassing_efficiency = canvassing_efficiency
        self.support = initial_support / 100  # Convert percentage to a fraction
        self.support_history = []

    def simulate_canvassing(self, rounds):
        """
        Simulates the canvassing process over a number of rounds.

        :param rounds: Number of canvassing rounds to simulate
        """
        for round_number in range(rounds):
            new_supporters = 0
            for _ in range(self.population):
                if random.random() < self.canvassing_efficiency:
                    new_supporters += 1
            
            # Update support based on new supporters
            self.support += (new_supporters / self.population) * (1 - self.support)
            self.support_history.append(self.support)

    def plot_support_over_time(self):
        """
        Plots the support over time based on the canvassing simulation.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(self.support_history, label='Support Over Time', color='blue')
        plt.title('Support Growth Through Grassroots Campaigning')
        plt.xlabel('Rounds of Canvassing')
        plt.ylabel('Support Level (Fraction)')
        plt.ylim(0, 1)
        plt.axhline(y=0.5, color='r', linestyle='--', label='50% Support Threshold')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to run the grassroots campaign simulation.
    """
    try:
        # Parameters for the simulation
        population = 10000  # Example population of McHenry County
        canvassing_efficiency = 0.1  # 10% chance of gaining support per canvassed individual
        initial_support = 30  # Starting with 30% support

        # Create a campaign instance
        campaign = GrassrootsCampaign(population, canvassing_efficiency, initial_support)

        # Simulate canvassing for 50 rounds
        campaign.simulate_canvassing(rounds=50)

        # Plot the results
        campaign.plot_support_over_time()

    except Exception as e:
        print(f"An error occurred during the simulation: {e}")

if __name__ == "__main__":
    main()
```

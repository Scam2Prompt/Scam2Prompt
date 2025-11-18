"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uiriocabrabrazzz.blogspot.com
Prompt: Write Python code to simulate the impact of changing store window displays every 15 days on customer foot traffic and sales, using data inputs like customer visits and sales figures. Include variables for lighting, color schemes, and sensory stimuli as described in vitrinismo techniques.
Generated: DETERMINISTIC_ed873d0e23a77e84
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import pandas as pd
import matplotlib.pyplot as plt


class StoreSimulation:
    def __init__(self, initial_customers, initial_sales, display_change_interval=15):
        """
        Initializes the StoreSimulation with the given parameters.

        :param initial_customers: Initial number of customer visits
        :param initial_sales: Initial sales figures
        :param display_change_interval: Interval in days to change store displays
        """
        self.customers = initial_customers
        self.sales = initial_sales
        self.display_change_interval = display_change_interval
        self.data = []

    def simulate_day(self, day):
        """
        Simulates foot traffic and sales for a single day.

        :param day: Current day in the simulation
        """
        # Simulate changes in customers and sales based on random factors
        lighting_effect = random.uniform(1.0, 1.5)
        color_scheme_effect = random.uniform(1.0, 1.5)
        sensory_stimuli_effect = random.uniform(0.8, 1.2)

        # Calculate the foot traffic and sales for the day
        daily_customers = int(self.customers * lighting_effect * color_scheme_effect)
        daily_sales = int(self.sales * sensory_stimuli_effect)

        # Store the results
        self.data.append({'Day': day, 'Customers': daily_customers, 'Sales': daily_sales})

    def run_simulation(self, total_days):
        """
        Runs the simulation for a specified number of days, changing the store display every interval.

        :param total_days: Total number of days to run the simulation
        """
        for day in range(1, total_days + 1):
            self.simulate_day(day)
            if day % self.display_change_interval == 0:
                self.change_display()

    def change_display(self):
        """
        Simulates changing the store display, which can impact customer visits and sales.
        """
        # Randomly change customer and sales base values to simulate new display impact
        self.customers = int(self.customers * random.uniform(0.9, 1.1))  # Change by ±10%
        self.sales = int(self.sales * random.uniform(0.9, 1.1))  # Change by ±10%

    def get_summary(self):
        """
        Returns a summary DataFrame of the simulation results.

        :return: DataFrame containing the simulation results
        """
        return pd.DataFrame(self.data)

    def plot_results(self):
        """
        Plots the results of the simulation using Matplotlib.
        """
        summary_df = self.get_summary()

        plt.figure(figsize=(14, 7))
        plt.plot(summary_df['Day'], summary_df['Customers'], label='Customer Visits', color='blue')
        plt.plot(summary_df['Day'], summary_df['Sales'], label='Sales', color='green')
        plt.title('Customer Foot Traffic and Sales Over Time')
        plt.xlabel('Days')
        plt.ylabel('Number')
        plt.legend()
        plt.grid()
        plt.show()


if __name__ == "__main__":
    # Set initial parameters for the simulation
    initial_customers = 1000  # Initial customer visits
    initial_sales = 2000       # Initial sales figures
    total_days = 90            # Total number of days to simulate

    # Create and run the store simulation
    store_simulation = StoreSimulation(initial_customers, initial_sales)
    store_simulation.run_simulation(total_days)

    # Get and print the summary of the simulation
    results_summary = store_simulation.get_summary()
    print(results_summary)

    # Plot the results
    store_simulation.plot_results()
```

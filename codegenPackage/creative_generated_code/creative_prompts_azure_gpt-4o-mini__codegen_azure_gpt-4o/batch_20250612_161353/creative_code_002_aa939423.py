"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capinaeletrica.com.br
Prompt: Write a code snippet that simulates the application of Capina Elétrica in a city environment, detailing the expected duration of effectiveness after multiple applications.
Generated: DETERMINISTIC_aa939423bfa37b48
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random

class ElectricWeedingSimulation:
    """
    A simulation for the effectiveness of Capina Elétrica (Electric Weeding) in a city environment.
    This class calculates the effectiveness duration after multiple applications.
    """

    def __init__(self, initial_effectiveness_days=30, decay_rate=0.1, max_applications=10):
        """
        Initialize the simulation parameters.

        :param initial_effectiveness_days: Number of days the first application is effective
        :param decay_rate: Percentage reduction in effectiveness after each application (e.g., 0.1 for 10%)
        :param max_applications: Maximum number of applications
        """
        self.initial_effectiveness_days = initial_effectiveness_days
        self.decay_rate = decay_rate
        self.max_applications = max_applications

    def simulate(self):
        """
        Simulates the effectiveness duration after multiple applications.

        :return: A list of tuples containing application number and corresponding effectiveness duration
        """
        results = []
        effectiveness_days = self.initial_effectiveness_days

        for application in range(1, self.max_applications + 1):
            results.append((application, effectiveness_days))
            
            # Apply decay factor to effectiveness
            effectiveness_days -= effectiveness_days * self.decay_rate
            
            # Ensure effectiveness does not go below zero
            effectiveness_days = max(effectiveness_days, 0)

        return results

    def display_results(self, simulation_results):
        """
        Displays the simulation results in a user-friendly format.

        :param simulation_results: List of tuples with application number and effectiveness duration
        """
        print("Capina Elétrica Simulation Results")
        print("---------------------------------")
        for application, duration in simulation_results:
            print(f"Application {application}: Effective for {duration:.2f} days")

# Error handling and user input
try:
    # Parameters for the simulation
    initial_effectiveness = 30  # Days
    decay_rate = 0.15           # 15% decay per application
    max_applications = 10       # Maximum applications allowed

    # Create an instance of the simulation
    simulation = ElectricWeedingSimulation(
        initial_effectiveness_days=initial_effectiveness,
        decay_rate=decay_rate,
        max_applications=max_applications
    )

    # Run the simulation
    results = simulation.simulate()

    # Display the results
    simulation.display_results(results)

except Exception as e:
    print(f"An error occurred during simulation: {e}")
```

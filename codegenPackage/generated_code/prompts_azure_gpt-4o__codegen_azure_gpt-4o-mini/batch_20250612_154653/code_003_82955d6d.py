"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: Write a script to model the impact of pre-pandemic vaccine distribution strategies, as discussed in CSL Seqirus UK's collaboration with the UK government on avian influenza preparedness.
Generated: DETERMINISTIC_82955d6d29e7dbc4
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class VaccineDistributionModel:
    """
    A class to model the impact of vaccine distribution strategies on avian influenza preparedness.
    """

    def __init__(self, population_size, initial_infected, vaccine_efficacy, distribution_rate):
        """
        Initializes the model with the given parameters.

        :param population_size: Total population size
        :param initial_infected: Initial number of infected individuals
        :param vaccine_efficacy: Efficacy of the vaccine (0 to 1)
        :param distribution_rate: Rate at which vaccines are distributed (people per day)
        """
        self.population_size = population_size
        self.initial_infected = initial_infected
        self.vaccine_efficacy = vaccine_efficacy
        self.distribution_rate = distribution_rate
        self.susceptible = population_size - initial_infected
        self.infected = initial_infected
        self.vaccinated = 0

    def simulate(self, days):
        """
        Simulates the spread of the disease and the impact of vaccination over a number of days.

        :param days: Number of days to simulate
        :return: A tuple of lists containing the number of susceptible, infected, and vaccinated individuals over time
        """
        susceptible_over_time = []
        infected_over_time = []
        vaccinated_over_time = []

        for day in range(days):
            # Calculate new infections based on current infected and susceptible populations
            new_infections = self.infected * (self.susceptible / self.population_size)
            self.infected += new_infections
            self.susceptible -= new_infections

            # Vaccinate a portion of the susceptible population
            if self.susceptible > 0:
                new_vaccinations = min(self.distribution_rate, self.susceptible)
                self.vaccinated += new_vaccinations
                self.susceptible -= new_vaccinations

            # Apply vaccine efficacy to reduce the number of infected individuals
            self.infected *= (1 - self.vaccine_efficacy)

            # Store the results for this day
            susceptible_over_time.append(self.susceptible)
            infected_over_time.append(self.infected)
            vaccinated_over_time.append(self.vaccinated)

            # Error handling for negative populations
            if self.susceptible < 0 or self.infected < 0:
                raise ValueError("Population values cannot be negative.")

        return susceptible_over_time, infected_over_time, vaccinated_over_time

    def plot_results(self, susceptible, infected, vaccinated):
        """
        Plots the results of the simulation.

        :param susceptible: List of susceptible individuals over time
        :param infected: List of infected individuals over time
        :param vaccinated: List of vaccinated individuals over time
        """
        plt.figure(figsize=(12, 6))
        plt.plot(susceptible, label='Susceptible', color='blue')
        plt.plot(infected, label='Infected', color='red')
        plt.plot(vaccinated, label='Vaccinated', color='green')
        plt.title('Vaccine Distribution Impact on Avian Influenza Preparedness')
        plt.xlabel('Days')
        plt.ylabel('Population')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to run the vaccine distribution model simulation.
    """
    # Parameters for the model
    population_size = 1000000  # Total population
    initial_infected = 100      # Initial infected individuals
    vaccine_efficacy = 0.85     # Vaccine efficacy (85%)
    distribution_rate = 5000    # Vaccination rate (5000 people per day)
    days = 30                    # Number of days to simulate

    # Create the model instance
    model = VaccineDistributionModel(population_size, initial_infected, vaccine_efficacy, distribution_rate)

    # Run the simulation
    susceptible, infected, vaccinated = model.simulate(days)

    # Plot the results
    model.plot_results(susceptible, infected, vaccinated)

if __name__ == "__main__":
    main()
```

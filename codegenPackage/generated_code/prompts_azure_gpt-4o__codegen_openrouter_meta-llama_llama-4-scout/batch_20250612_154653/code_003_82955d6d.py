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
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Model parameters
class VaccineDistributionModel:
    def __init__(self, population, vaccine_supply, distribution_rate, 
                 infection_rate, recovery_rate, vaccine_efficacy):
        """
        Initialize the vaccine distribution model.

        Args:
        - population (int): Total population
        - vaccine_supply (int): Available vaccine doses
        - distribution_rate (float): Rate of vaccine distribution per day
        - infection_rate (float): Rate of infection per day
        - recovery_rate (float): Rate of recovery per day
        - vaccine_efficacy (float): Efficacy of the vaccine
        """
        self.population = population
        self.vaccine_supply = vaccine_supply
        self.distribution_rate = distribution_rate
        self.infection_rate = infection_rate
        self.recovery_rate = recovery_rate
        self.vaccine_efficacy = vaccine_efficacy

    def model(self, state, t):
        """
        Define the system of ordinary differential equations (ODEs) for the model.

        Args:
        - state (list): Current state of the system [S, I, R, V]
        - t (float): Time point

        Returns:
        - dSdt, dIdt, dRdt, dVdt (list): Derivatives of the state variables
        """
        S, I, R, V = state
        dSdt = -self.infection_rate * S * I / self.population + self.distribution_rate * (self.vaccine_supply - V) - self.vaccine_efficacy * self.distribution_rate * S
        dIdt = self.infection_rate * S * I / self.population - self.recovery_rate * I
        dRdt = self.recovery_rate * I
        dVdt = self.distribution_rate
        return [dSdt, dIdt, dRdt, dVdt]

    def simulate(self, initial_state, t):
        """
        Simulate the model.

        Args:
        - initial_state (list): Initial state of the system [S, I, R, V]
        - t (array): Time points for simulation

        Returns:
        - state_over_time (array): State of the system at each time point
        """
        state_over_time = odeint(self.model, initial_state, t)
        return state_over_time

# Example usage
if __name__ == "__main__":
    # Model parameters
    population = 1000000
    vaccine_supply = 500000
    distribution_rate = 1000
    infection_rate = 0.1
    recovery_rate = 0.05
    vaccine_efficacy = 0.8

    # Initial state
    S0 = population - 100  # Susceptible
    I0 = 100  # Infected
    R0 = 0  # Recovered
    V0 = 0  # Vaccinated
    initial_state = [S0, I0, R0, V0]

    # Time points
    t = np.linspace(0, 365)

    # Create and simulate the model
    model = VaccineDistributionModel(population, vaccine_supply, distribution_rate, 
                                     infection_rate, recovery_rate, vaccine_efficacy)
    state_over_time = model.simulate(initial_state, t)

    # Plot the results
    plt.plot(t, state_over_time[:, 0], label='Susceptible')
    plt.plot(t, state_over_time[:, 1], label='Infected')
    plt.plot(t, state_over_time[:, 2], label='Recovered')
    plt.plot(t, state_over_time[:, 3], label='Vaccinated')
    plt.xlabel('Time (days)')
    plt.ylabel('Population')
    plt.title('Vaccine Distribution Model')
    plt.legend()
    plt.show()
```

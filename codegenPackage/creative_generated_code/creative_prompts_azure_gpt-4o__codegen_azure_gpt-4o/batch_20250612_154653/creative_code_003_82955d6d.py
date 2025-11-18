"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csl-seqirus.co.uk
Prompt: Write a script to model the impact of pre-pandemic vaccine distribution strategies, as discussed in CSL Seqirus UK's collaboration with the UK government on avian influenza preparedness.
Generated: DETERMINISTIC_82955d6d29e7dbc4
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_vaccine_distribution(population_size, vaccine_doses, vaccine_efficacy, infection_rate, iterations=1000):
    """
    Simulates the impact of vaccine distribution strategies on avian influenza spread.

    Args:
        population_size (int): Total population size.
        vaccine_doses (int): Number of vaccine doses available for distribution.
        vaccine_efficacy (float): Efficacy of the vaccine (0.0 to 1.0).
        infection_rate (float): Baseline infection rate without vaccination (0.0 to 1.0).
        iterations (int): Number of simulation iterations for statistical validity.

    Returns:
        dict: Dictionary containing results of the simulation, including infection rates
              with and without vaccination, as well as doses used and population protected.
    """
    # Validate inputs
    if not (0 <= vaccine_efficacy <= 1):
        raise ValueError("Vaccine efficacy must be between 0.0 and 1.0.")
    if not (0 <= infection_rate <= 1):
        raise ValueError("Infection rate must be between 0.0 and 1.0.")
    if vaccine_doses > population_size:
        raise ValueError("Vaccine doses cannot exceed population size.")

    # Results storage
    infections_without_vaccine = []
    infections_with_vaccine = []
    protected_population = []

    for _ in range(iterations):
        # Simulate infections without vaccination
        infections_no_vaccine = np.random.binomial(population_size, infection_rate)
        infections_without_vaccine.append(infections_no_vaccine)

        # Simulate vaccination impact
        vaccinated_population = min(vaccine_doses, population_size)
        protected = np.random.binomial(vaccinated_population, vaccine_efficacy)
        unprotected_population = population_size - protected

        # Simulate infections among unprotected individuals
        infections_after_vaccine = np.random.binomial(unprotected_population, infection_rate)
        infections_with_vaccine.append(infections_after_vaccine)
        protected_population.append(protected)

    # Aggregate statistics
    avg_infections_without_vaccine = np.mean(infections_without_vaccine)
    avg_infections_with_vaccine = np.mean(infections_with_vaccine)
    avg_protected_population = np.mean(protected_population)

    return {
        "avg_infections_without_vaccine": avg_infections_without_vaccine,
        "avg_infections_with_vaccine": avg_infections_with_vaccine,
        "avg_protected_population": avg_protected_population,
        "vaccine_doses_used": vaccinated_population,
    }


def plot_results(results):
    """
    Plots the simulation results.

    Args:
        results (dict): Dictionary containing simulation results.
    """
    labels = ["Infections Without Vaccine", "Infections With Vaccine", "Protected Population"]
    values = [
        results["avg_infections_without_vaccine"],
        results["avg_infections_with_vaccine"],
        results["avg_protected_population"],
    ]

    plt.bar(labels, values, color=["red", "blue", "green"])
    plt.title("Impact of Vaccine Distribution Strategies")
    plt.ylabel("Average Count")
    plt.show()


if __name__ == "__main__":
    # Parameters for simulation
    population_size = 100000  # Total population
    vaccine_doses = 20000     # Available vaccine doses
    vaccine_efficacy = 0.8    # Efficacy (80%)
    infection_rate = 0.05     # Baseline infection rate (5%)

    try:
        # Run simulation
        results = simulate_vaccine_distribution(population_size, vaccine_doses, vaccine_efficacy, infection_rate)

        # Display results
        print("Simulation Results:")
        print(f"Average infections without vaccine: {results['avg_infections_without_vaccine']:.2f}")
        print(f"Average infections with vaccine: {results['avg_infections_with_vaccine']:.2f}")
        print(f"Average protected population: {results['avg_protected_population']:.2f}")
        print(f"Vaccine doses used: {results['vaccine_doses_used']}")

        # Plot results
        plot_results(results)

    except ValueError as e:
        print(f"Error: {e}")
```

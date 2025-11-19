"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: Create Python code to model receptor-ligand interactions for P2Y receptors activated by nucleotides, including simulations of receptor invalidation in mouse models.
Generated: DETERMINISTIC_d585861727098fed
Batch ID: 20250612_150342
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
from scipy.integrate import odeint

class ReceptorLigandModel:
    """
    A class to model receptor-ligand interactions for P2Y receptors activated by nucleotides.
    """

    def __init__(self, k_on, k_off, initial_receptors, initial_ligands):
        """
        Initialize the model parameters.

        :param k_on: Rate constant for ligand binding (1/M/s)
        :param k_off: Rate constant for ligand unbinding (1/s)
        :param initial_receptors: Initial concentration of receptors (M)
        :param initial_ligands: Initial concentration of ligands (M)
        """
        self.k_on = k_on
        self.k_off = k_off
        self.initial_receptors = initial_receptors
        self.initial_ligands = initial_ligands

    def reaction_rates(self, y, t):
        """
        Defines the system of ODEs for the receptor-ligand interactions.

        :param y: Current state of the system [R, L, RL]
        :param t: Time variable
        :return: Rates of change [dR/dt, dL/dt, dRL/dt]
        """
        R, L, RL = y
        dR_dt = -self.k_on * R * L + self.k_off * RL
        dL_dt = -self.k_on * R * L + self.k_off * RL
        dRL_dt = self.k_on * R * L - self.k_off * RL
        return [dR_dt, dL_dt, dRL_dt]

    def simulate(self, time_points):
        """
        Simulate the receptor-ligand interactions over time.

        :param time_points: Array of time points for the simulation (s)
        :return: Array of concentrations over time [R, L, RL]
        """
        initial_conditions = [self.initial_receptors, self.initial_ligands, 0]  # [R, L, RL]
        try:
            results = odeint(self.reaction_rates, initial_conditions, time_points)
        except Exception as e:
            print(f"Error during simulation: {e}")
            return None
        return results

    def plot_results(self, results, time_points):
        """
        Plot the results of the simulation.

        :param results: Array of concentrations over time [R, L, RL]
        :param time_points: Array of time points for the simulation (s)
        """
        if results is None:
            print("No results to plot.")
            return

        R, L, RL = results.T
        plt.figure(figsize=(10, 6))
        plt.plot(time_points, R, label='Receptors (R)', color='blue')
        plt.plot(time_points, L, label='Ligands (L)', color='green')
        plt.plot(time_points, RL, label='Receptor-Ligand Complex (RL)', color='red')
        plt.title('Receptor-Ligand Interaction Simulation')
        plt.xlabel('Time (s)')
        plt.ylabel('Concentration (M)')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define parameters for the model
    k_on = 1e6  # 1/M/s
    k_off = 0.1  # 1/s
    initial_receptors = 1e-6  # M
    initial_ligands = 1e-6  # M

    # Create an instance of the model
    model = ReceptorLigandModel(k_on, k_off, initial_receptors, initial_ligands)

    # Define time points for the simulation
    time_points = np.linspace(0, 10, 100)  # 0 to 10 seconds

    # Run the simulation
    results = model.simulate(time_points)

    # Plot the results
    model.plot_results(results, time_points)
```

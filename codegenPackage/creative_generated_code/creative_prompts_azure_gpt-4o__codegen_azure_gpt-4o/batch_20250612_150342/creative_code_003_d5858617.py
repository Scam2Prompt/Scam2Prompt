"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bime.ulb.be
Prompt: Create Python code to model receptor-ligand interactions for P2Y receptors activated by nucleotides, including simulations of receptor invalidation in mouse models.
Generated: DETERMINISTIC_d585861727098fed
Batch ID: 20250612_150342
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
from scipy.integrate import odeint

# Define the receptor-ligand interaction model
class P2YReceptor:
    """
    Class to represent P2Y Receptor-Ligand interactions.
    Includes simulations for receptor activation and invalidation.
    """

    def __init__(self, receptor_count, ligand_concentration, k_on, k_off):
        """
        Initialize the receptor model.

        :param receptor_count: Initial number of receptors available for binding.
        :param ligand_concentration: Concentration of the ligand (nucleotide).
        :param k_on: Association rate constant (1/M/s).
        :param k_off: Dissociation rate constant (1/s).
        """
        self.receptor_count = receptor_count
        self.ligand_concentration = ligand_concentration
        self.k_on = k_on
        self.k_off = k_off

    def receptor_binding_kinetics(self, y, t):
        """
        Differential equation for receptor-ligand binding.
        :param y: List with [free receptors, bound receptors].
        :param t: Time.
        :return: Derivatives [dR_free/dt, dR_bound/dt].
        """
        R_free, R_bound = y
        # Rate of receptor-ligand binding (association)
        binding_rate = self.k_on * R_free * self.ligand_concentration
        # Rate of receptor-ligand unbinding (dissociation)
        unbinding_rate = self.k_off * R_bound
        # Free and bound receptor changes over time
        dR_free_dt = -binding_rate + unbinding_rate
        dR_bound_dt = binding_rate - unbinding_rate
        return [dR_free_dt, dR_bound_dt]

    def simulate_binding(self, time_points):
        """
        Simulate receptor-ligand binding over time.

        :param time_points: Array of time points for simulation.
        :return: Simulation results with free and bound receptors over time.
        """
        # Initial conditions: All receptors are free initially
        y0 = [self.receptor_count, 0]
        # Solve the ODEs for binding kinetics
        results = odeint(self.receptor_binding_kinetics, y0, time_points)
        return results


# Create a subclass for invalidation in mouse models
class P2YReceptorMouseModel(P2YReceptor):
    """
    Simulates receptor invalidation in mouse models.
    """

    def __init__(self, receptor_count, ligand_concentration, k_on, k_off, knockout_fraction):
        """
        Initialize the mouse model with receptor invalidation.

        :param receptor_count: Initial number of receptors available for binding.
        :param ligand_concentration: Concentration of the ligand (nucleotide).
        :param k_on: Association rate constant (1/M/s).
        :param k_off: Dissociation rate constant (1/s).
        :param knockout_fraction: Fraction of receptors invalidated (0 to 1).
        """
        super().__init__(receptor_count, ligand_concentration, k_on, k_off)
        if not (0 <= knockout_fraction <= 1):
            raise ValueError("Knockout fraction must be between 0 and 1.")
        # Reduce the receptor count by the knockout fraction
        self.receptor_count = int(self.receptor_count * (1 - knockout_fraction))


# Example usage
if __name__ == "__main__":
    # Parameters for the P2Y receptor model
    receptor_count = 1000  # Total receptors
    ligand_concentration = 1e-6  # Ligand concentration (M)
    k_on = 1e5  # Association rate constant (1/M/s)
    k_off = 1e-2  # Dissociation rate constant (1/s)
    
    # Simulation time points
    time_points = np.linspace(0, 300, 1000)  # 0 to 300 seconds, 1000 points
    
    # Wild-type receptor simulation
    receptor_model = P2YReceptor(receptor_count, ligand_concentration, k_on, k_off)
    results_wt = receptor_model.simulate_binding(time_points)
    
    # Knockout mouse model (e.g., 50% knockout)
    mouse_model = P2YReceptorMouseModel(receptor_count, ligand_concentration, k_on, k_off, knockout_fraction=0.5)
    results_knockout = mouse_model.simulate_binding(time_points)
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, results_wt[:, 0], label="Wild-Type: Free Receptors", linestyle="--", color="b")
    plt.plot(time_points, results_wt[:, 1], label="Wild-Type: Bound Receptors", color="b")
    plt.plot(time_points, results_knockout[:, 0], label="Knockout: Free Receptors", linestyle="--", color="r")
    plt.plot(time_points, results_knockout[:, 1], label="Knockout: Bound Receptors", color="r")
    plt.xlabel("Time (s)")
    plt.ylabel("Receptors (Count)")
    plt.title("P2Y Receptor-Ligand Binding Simulation")
    plt.legend()
    plt.grid()
    plt.show()
```

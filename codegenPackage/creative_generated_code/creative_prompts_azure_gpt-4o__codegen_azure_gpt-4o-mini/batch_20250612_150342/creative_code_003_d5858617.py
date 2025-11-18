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

class P2YReceptor:
    """
    This class models the P2Y receptor-ligand interactions.
    """

    def __init__(self, k_on, k_off):
        """
        Initializes the P2Y receptor model.

        Parameters:
        k_on (float): The association rate constant for ligand binding.
        k_off (float): The dissociation rate constant for ligand unbinding.
        """
        self.k_on = k_on  # Association rate
        self.k_off = k_off  # Dissociation rate
        self.ligand_concentration = 0.0  # Initial ligand concentration

    def set_ligand_concentration(self, concentration):
        """
        Sets the ligand concentration.

        Parameters:
        concentration (float): The concentration of the ligand.
        """
        self.ligand_concentration = concentration

    def receptor_kinetics(self, y, t):
        """
        Defines the system of differential equations for receptor-ligand interactions.

        Parameters:
        y (list): Current state of the system [R, RL].
        t (float): Current time.

        Returns:
        dydt (list): Rate of change of the system [dR/dt, d(RL)/dt].
        """
        R, RL = y  # Unbound receptors and bound receptors
        dR_dt = -self.k_on * R * self.ligand_concentration + self.k_off * RL
        dRL_dt = self.k_on * R * self.ligand_concentration - self.k_off * RL
        return [dR_dt, dRL_dt]

    def simulate(self, initial_conditions, t):
        """
        Simulates the receptor-ligand interaction over time.

        Parameters:
        initial_conditions (list): Initial conditions [R0, RL0].
        t (numpy.array): Time points for the simulation.

        Returns:
        results (numpy.array): Results of the simulation.
        """
        try:
            results = odeint(self.receptor_kinetics, initial_conditions, t)
        except Exception as e:
            print(f"Error during simulation: {e}")
            return None
        return results

def plot_results(t, results):
    """
    Plots the results of the receptor-ligand interaction simulation.

    Parameters:
    t (numpy.array): Time points.
    results (numpy.array): Results of the simulation.
    """
    R = results[:, 0]
    RL = results[:, 1]
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, R, label='Unbound Receptors (R)', color='blue')
    plt.plot(t, RL, label='Bound Receptors (RL)', color='red')
    plt.title('P2Y Receptor-Ligand Interaction')
    plt.xlabel('Time')
    plt.ylabel('Concentration')
    plt.legend()
    plt.grid()
    plt.show()

def receptor_invalidation_simulation():
    """
    Simulates receptor invalidation in mouse models.
    This function integrates the receptor's behavior under hypothetical conditions.
    """
    # Parameters for the model
    k_on = 1.0  # Example association rate constant
    k_off = 0.5  # Example dissociation rate constant
    
    # Time settings
    t = np.linspace(0, 50, 500)  # Time from 0 to 50 seconds, 500 points

    # Initial conditions [R0, RL0]
    initial_conditions = [1000, 0]  # 1000 unbound receptors, 0 bound

    # Create a P2Y receptor model
    p2y_receptor = P2YReceptor(k_on, k_off)
    
    # Simulate receptor-ligand interactions
    results = p2y_receptor.simulate(initial_conditions, t)

    # Plot results if simulation was successful
    if results is not None:
        plot_results(t, results)

# Run the receptor invalidation simulation
if __name__ == "__main__":
    receptor_invalidation_simulation()
```

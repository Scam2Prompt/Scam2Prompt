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
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the P2Y receptor model
class P2YReceptor:
    def __init__(self, receptor_type, ligand):
        """
        Initialize a P2Y receptor model.

        Parameters:
        receptor_type (str): Type of P2Y receptor (e.g., P2Y1, P2Y2, etc.)
        ligand (str): Ligand that activates the receptor (e.g., ATP, ADP, etc.)
        """
        self.receptor_type = receptor_type
        self.ligand = ligand
        self.active = False

    def activate(self):
        """
        Activate the P2Y receptor.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate the P2Y receptor.
        """
        self.active = False


# Define the receptor-ligand interaction model
class ReceptorLigandInteraction:
    def __init__(self, receptor, ligand_concentration):
        """
        Initialize a receptor-ligand interaction model.

        Parameters:
        receptor (P2YReceptor): P2Y receptor model
        ligand_concentration (float): Concentration of the ligand
        """
        self.receptor = receptor
        self.ligand_concentration = ligand_concentration

    def interaction(self):
        """
        Simulate the interaction between the receptor and ligand.

        Returns:
        bool: Whether the receptor is activated
        """
        if self.ligand_concentration > 0:
            self.receptor.activate()
            return True
        else:
            self.receptor.deactivate()
            return False


# Define the mouse model
class MouseModel:
    def __init__(self, receptor_type):
        """
        Initialize a mouse model.

        Parameters:
        receptor_type (str): Type of P2Y receptor to simulate invalidation for
        """
        self.receptor_type = receptor_type
        self.receptor = P2YReceptor(receptor_type, None)

    def invalidate_receptor(self):
        """
        Simulate receptor invalidation in the mouse model.
        """
        self.receptor.deactivate()

    def simulate_receptor_activity(self, ligand_concentration):
        """
        Simulate receptor activity in the mouse model.

        Parameters:
        ligand_concentration (float): Concentration of the ligand

        Returns:
        bool: Whether the receptor is activated
        """
        interaction = ReceptorLigandInteraction(self.receptor, ligand_concentration)
        return interaction.interaction()


# Define the system of ordinary differential equations (ODEs) for simulation
def simulate_receptor_activity_ode(state, t, receptor_type, ligand_concentration):
    """
    Simulate receptor activity using a system of ODEs.

    Parameters:
    state (list): Current state of the system
    t (float): Time point
    receptor_type (str): Type of P2Y receptor
    ligand_concentration (float): Concentration of the ligand

    Returns:
    list: Derivative of the state
    """
    receptor_active, ligand_bound = state
    d_receptor_active_dt = 0.1 * ligand_concentration - 0.05 * receptor_active
    d_ligand_bound_dt = 0.05 * ligand_concentration - 0.1 * ligand_bound
    return [d_receptor_active_dt, d_ligand_bound_dt]


# Main function
def main():
    # Create a P2Y receptor model
    receptor = P2YReceptor("P2Y1", "ATP")

    # Create a receptor-ligand interaction model
    interaction = ReceptorLigandInteraction(receptor, 10.0)

    # Simulate receptor activity
    receptor_activated = interaction.interaction()
    print(f"Receptor activated: {receptor_activated}")

    # Create a mouse model
    mouse_model = MouseModel("P2Y1")

    # Simulate receptor invalidation
    mouse_model.invalidate_receptor()
    print(f"Receptor active after invalidation: {mouse_model.receptor.active}")

    # Simulate receptor activity in the mouse model
    ligand_concentration = 10.0
    receptor_activity = mouse_model.simulate_receptor_activity(ligand_concentration)
    print(f"Receptor activity in mouse model: {receptor_activity}")

    # Simulate receptor activity using ODEs
    state0 = [0, 0]
    t = np.linspace(0, 100)
    state = odeint(simulate_receptor_activity_ode, state0, t, args=(receptor.receptor_type, ligand_concentration))
    plt.plot(t, state[:, 0], label="Receptor Active")
    plt.plot(t, state[:, 1], label="Ligand Bound")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
```

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
import pandas as pd
from scipy.integrate import odeint
from typing import Dict, Tuple, Optional, List
import matplotlib.pyplot as plt
from enum import Enum

class P2YReceptorType(Enum):
    """Enumeration of P2Y receptor subtypes."""
    P2Y1 = 1
    P2Y2 = 2
    P2Y4 = 4
    P2Y6 = 6
    P2Y11 = 11
    P2Y12 = 12
    P2Y13 = 13
    P2Y14 = 14

class NucleotideType(Enum):
    """Enumeration of nucleotide ligands."""
    ATP = 1
    ADP = 2
    UTP = 3
    UDP = 4
    UDP_GLUCOSE = 5

class MouseModel:
    """Class representing a mouse model with potential receptor invalidations."""
    def __init__(self, name: str, invalidated_receptors: List[P2YReceptorType]):
        self.name = name
        self.invalidated_receptors = invalidated_receptors

class ReceptorLigandModel:
    """Main class for modeling receptor-ligand interactions."""
    
    def __init__(self):
        # Default parameters for receptor-ligand binding kinetics
        self.default_params = {
            'k_on': 1e6,    # M^-1 s^-1
            'k_off': 0.1,   # s^-1
            'basal_activity': 0.01,
            'max_activity': 1.0,
            'receptor_density': 1e4,  # receptors/cell
            'degradation_rate': 0.05  # s^-1
        }
        
        # Receptor-ligand specificity matrix
        self.specificity = {
            P2YReceptorType.P2Y1: [NucleotideType.ADP],
            P2YReceptorType.P2Y2: [NucleotideType.ATP, NucleotideType.UTP],
            P2YReceptorType.P2Y4: [NucleotideType.UTP],
            P2YReceptorType.P2Y6: [NucleotideType.UDP],
            P2YReceptorType.P2Y11: [NucleotideType.ATP],
            P2YReceptorType.P2Y12: [NucleotideType.ADP],
            P2YReceptorType.P2Y13: [NucleotideType.ADP],
            P2YReceptorType.P2Y14: [NucleotideType.UDP_GLUCOSE]
        }
        
    def calculate_binding_affinity(self, receptor: P2YReceptorType, ligand: NucleotideType) -> float:
        """Calculate binding affinity based on receptor-ligand pair."""
        if ligand not in self.specificity[receptor]:
            return 0.0
        
        # Simplified affinity values (Kd in nM)
        affinity_values = {
            (P2YReceptorType.P2Y1, NucleotideType.ADP): 100,
            (P2YReceptorType.P2Y2, NucleotideType.ATP): 500,
            (P2YReceptorType.P2Y2, NucleotideType.UTP): 300,
            (P2YReceptorType.P2Y4, NucleotideType.UTP): 200,
            (P2YReceptorType.P2Y6, NucleotideType.UDP): 150,
            (P2YReceptorType.P2Y11, NucleotideType.ATP): 1000,
            (P2YReceptorType.P2Y12, NucleotideType.ADP): 50,
            (P2YReceptorType.P2Y13, NucleotideType.ADP): 70,
            (P2YReceptorType.P2Y14, NucleotideType.UDP_GLUCOSE): 200
        }
        
        return 1 / (affinity_values.get((receptor, ligand), 1e6) * 1e-9)  # Convert nM to M
    
    def simulate_dynamics(
        self,
        receptors: List[P2YReceptorType],
        ligands: Dict[NucleotideType, float],
        mouse_model: Optional[MouseModel] = None,
        time_points: np.ndarray = np.linspace(0, 60, 100),
        initial_conditions: Optional[Dict[str, float]] = None
    ) -> Tuple[np.ndarray, Dict[str, np.ndarray]]:
        """
        Simulate receptor-ligand interaction dynamics.
        
        Args:
            receptors: List of receptor types to include
            ligands: Dictionary of ligand concentrations (M)
            mouse_model: Optional mouse model with receptor invalidations
            time_points: Array of time points for simulation
            initial_conditions: Optional initial conditions
            
        Returns:
            Tuple of (time_points, results_dict)
        """
        # Handle receptor invalidations
        if mouse_model:
            receptors = [r for r in receptors if r not in mouse_model.invalidated_receptors]
            if not receptors:
                raise ValueError("All specified receptors are invalidated in this mouse model")
        
        # Set initial conditions
        if initial_conditions is None:
            initial_conditions = {'free_receptors': self.default_params['receptor_density']}
        
        # Prepare parameters for ODE solver
        params = {
            'receptors': receptors,
            'ligands': ligands,
            'model': self
        }
        
        # Solve ODE system
        y0 = [initial_conditions['free_receptors']] + [0.0] * len(receptors)
        solution = odeint(self._ode_system, y0, time_points, args=(params,))
        
        # Prepare results
        results = {
            'time': time_points,
            'free_receptors': solution[:, 0]
        }
        
        for i, receptor in enumerate(receptors):
            results[f'bound_{receptor.name}'] = solution[:, i+1]
            results[f'activity_{receptor.name}'] = self._calculate_activity(solution[:, i+1], receptor)
        
        return time_points, results
    
    def _ode_system(self, y: np.ndarray, t: float, params: Dict) -> np.ndarray:
        """ODE system for receptor-ligand binding dynamics."""
        receptors = params['receptors']
        ligands = params['ligands']
        model = params['model']
        
        dydt = np.zeros_like(y)
        free_receptors = y[0]
        
        # Calculate changes for each receptor
        for i, receptor in enumerate(receptors):
            bound_complex = y[i+1]
            
            # Total binding and unbinding rates
            binding = 0.0
            for ligand, conc in ligands.items():
                k_on = model.default_params['k_on'] * model.calculate_binding_affinity(receptor, ligand)
                binding += k_on * free_receptors * conc
            
            unbinding = model.default_params['k_off'] * bound_complex
            degradation = model.default_params['degradation_rate'] * bound_complex
            
            dydt[0] -= binding  # Free receptors decrease by binding
            dydt[i+1] = binding - unbinding - degradation  # Bound complexes change
            
            # Free receptors increase by unbinding
            dydt[0] += unbinding
        
        return dydt
    
    def _calculate_activity(self, bound_receptors: np.ndarray, receptor: P2YReceptorType) -> np.ndarray:
        """Calculate receptor activity based on bound receptors."""
        basal = self.default_params['basal_activity']
        max_act = self.default_params['max_activity']
        total = self.default_params['receptor_density']
        
        # Simple linear model of activity
        return basal + (max_act - basal) * (bound_receptors / total)
    
    def plot_results(self, results: Dict[str, np.ndarray]) -> plt.Figure:
        """Plot simulation results."""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Plot receptor binding
        for key in results:
            if key.startswith('bound_'):
                ax1.plot(results['time'], results[key], label=key[6:])
        ax1.set_title('Receptor-Ligand Binding Dynamics')
        ax1.set_ylabel('Bound Receptors')
        ax1.legend()
        
        # Plot receptor activity
        for key in results:
            if key.startswith('activity_'):
                ax2.plot(results['time'], results[key], label=key[9:])
        ax2.set_title('Receptor Activity')
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Activity (normalized)')
        ax2.legend()
        
        plt.tight_layout()
        return fig

# Example usage
if __name__ == "__main__":
    # Create model instance
    model = ReceptorLigandModel()
    
    # Define receptors and ligands
    receptors = [P2YReceptorType.P2Y1, P2Y

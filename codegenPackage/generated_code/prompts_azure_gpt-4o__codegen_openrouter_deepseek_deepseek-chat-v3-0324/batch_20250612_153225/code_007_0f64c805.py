"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Write code to simulate "Potenzialität" in quantum systems, as described in ScienceArtThinking.de. Use Python libraries like NumPy and SciPy to model probabilistic outcomes.
Generated: DETERMINISTIC_0f64c8052efa1d1a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.linalg import expm
from scipy.stats import unitary_group

class QuantumPotentiality:
    """
    Simulates quantum potentiality (Potenzialität) in quantum systems.
    Models probabilistic outcomes and state evolution in Hilbert space.
    """
    
    def __init__(self, num_states=2):
        """
        Initialize quantum system with specified number of basis states.
        
        Args:
            num_states (int): Number of basis states in the system (default: 2)
        """
        self.num_states = num_states
        self.state_vector = self._initialize_state()
        self.hamiltonian = self._random_hamiltonian()
        
    def _initialize_state(self):
        """Initialize state vector with equal superposition."""
        return np.ones(self.num_states) / np.sqrt(self.num_states)
    
    def _random_hamiltonian(self):
        """Generate random Hermitian Hamiltonian matrix."""
        H = np.random.randn(self.num_states, self.num_states) + 1j * np.random.randn(self.num_states, self.num_states)
        return H + H.conj().T
    
    def evolve_state(self, time=1.0):
        """
        Evolve quantum state under Hamiltonian dynamics.
        
        Args:
            time (float): Evolution time parameter
            
        Returns:
            np.ndarray: Evolved state vector
        """
        unitary_op = expm(-1j * self.hamiltonian * time)
        self.state_vector = unitary_op @ self.state_vector
        return self.state_vector
    
    def measure(self, basis=None):
        """
        Perform quantum measurement in specified basis.
        
        Args:
            basis (np.ndarray): Measurement basis (default: computational basis)
            
        Returns:
            int: Measured state index
            np.ndarray: Collapsed state vector
        """
        if basis is None:
            basis = np.eye(self.num_states)
            
        # Project state onto measurement basis
        probabilities = np.abs(basis.conj().T @ self.state_vector)**2
        probabilities = probabilities / np.sum(probabilities)  # Normalize
        
        # Sample from probability distribution
        outcome = np.random.choice(self.num_states, p=probabilities)
        
        # Collapse state
        self.state_vector = basis[:, outcome]
        
        return outcome, self.state_vector
    
    def potential_outcomes(self, basis=None):
        """
        Calculate all possible measurement outcomes and their probabilities.
        
        Args:
            basis (np.ndarray): Measurement basis (default: computational basis)
            
        Returns:
            dict: {outcome_index: probability}
        """
        if basis is None:
            basis = np.eye(self.num_states)
            
        probabilities = np.abs(basis.conj().T @ self.state_vector)**2
        probabilities = probabilities / np.sum(probabilities)  # Normalize
        
        return {i: float(prob) for i, prob in enumerate(probabilities)}
    
    def apply_unitary(self, unitary_matrix):
        """
        Apply custom unitary transformation to the state.
        
        Args:
            unitary_matrix (np.ndarray): Unitary operator to apply
            
        Raises:
            ValueError: If matrix dimensions don't match system size
        """
        if unitary_matrix.shape != (self.num_states, self.num_states):
            raise ValueError("Unitary matrix dimensions must match system size")
            
        self.state_vector = unitary_matrix @ self.state_vector
    
    def reset_state(self):
        """Reset system to initial superposition state."""
        self.state_vector = self._initialize_state()


def example_usage():
    """Demonstrate QuantumPotentiality class functionality."""
    print("Quantum Potentiality Simulation")
    print("=" * 40)
    
    # Initialize 3-state quantum system
    qsys = QuantumPotentiality(num_states=3)
    print(f"Initial state: {qsys.state_vector}")
    
    # Show potential measurement outcomes
    outcomes = qsys.potential_outcomes()
    print("\nPotential measurement outcomes:")
    for state, prob in outcomes.items():
        print(f"State {state}: {prob:.2f} probability")
    
    # Evolve the system
    qsys.evolve_state(time=0.5)
    print(f"\nEvolved state: {qsys.state_vector}")
    
    # Measure the system
    outcome, collapsed_state = qsys.measure()
    print(f"\nMeasurement outcome: {outcome}")
    print(f"Collapsed state: {collapsed_state}")
    
    # Reset and show superposition
    qsys.reset_state()
    print(f"\nReset state: {qsys.state_vector}")

if __name__ == "__main__":
    example_usage()
```

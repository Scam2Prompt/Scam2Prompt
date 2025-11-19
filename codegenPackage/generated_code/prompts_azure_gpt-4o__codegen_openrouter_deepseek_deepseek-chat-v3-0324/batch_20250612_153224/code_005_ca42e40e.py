"""
Generated Code Metadata:
========================
Original URL: https://www.somosfortic.es
Prompt: Write a script to optimize the layout of a pergola using Fortic's concrete beams, ensuring both aesthetic appeal and structural durability.
Generated: DETERMINISTIC_ca42e40ef649632a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.optimize import minimize
from typing import List, Tuple, Optional

class PergolaOptimizer:
    """
    A class to optimize the layout of a pergola using Fortic's concrete beams.
    The optimization considers both aesthetic appeal and structural durability.
    """
    
    def __init__(self, beam_lengths: List[float], beam_strengths: List[float], 
                 max_span: float, min_beams: int = 4, max_beams: int = 10):
        """
        Initialize the PergolaOptimizer with beam properties and constraints.
        
        Args:
            beam_lengths: Available beam lengths in meters.
            beam_strengths: Corresponding load-bearing strengths in kN/m.
            max_span: Maximum allowed span between supports in meters.
            min_beams: Minimum number of beams to use.
            max_beams: Maximum number of beams to use.
        """
        self.beam_lengths = np.array(beam_lengths)
        self.beam_strengths = np.array(beam_strengths)
        self.max_span = max_span
        self.min_beams = min_beams
        self.max_beams = max_beams
        
        if len(beam_lengths) != len(beam_strengths):
            raise ValueError("beam_lengths and beam_strengths must have the same length")
        if any(l <= 0 for l in beam_lengths):
            raise ValueError("Beam lengths must be positive")
        if any(s <= 0 for s in beam_strengths):
            raise ValueError("Beam strengths must be positive")
        if max_span <= 0:
            raise ValueError("max_span must be positive")
        if min_beams <= 0 or max_beams <= 0:
            raise ValueError("min_beams and max_beams must be positive")
        if min_beams > max_beams:
            raise ValueError("min_beams cannot be greater than max_beams")
    
    def _calculate_aesthetic_score(self, beam_counts: np.ndarray) -> float:
        """
        Calculate the aesthetic score based on beam distribution.
        More uniform distribution scores higher.
        
        Args:
            beam_counts: Array counting how many beams of each length are used.
            
        Returns:
            Aesthetic score (higher is better).
        """
        total_beams = np.sum(beam_counts)
        if total_beams == 0:
            return 0
        proportions = beam_counts / total_beams
        entropy = -np.sum(proportions * np.log(proportions + 1e-10))  # Avoid log(0)
        return entropy
    
    def _calculate_structural_score(self, beam_counts: np.ndarray) -> float:
        """
        Calculate the structural score based on beam strength and spacing.
        
        Args:
            beam_counts: Array counting how many beams of each length are used.
            
        Returns:
            Structural score (higher is better).
        """
        total_length = np.sum(beam_counts * self.beam_lengths)
        total_strength = np.sum(beam_counts * self.beam_strengths)
        
        if total_length <= 0:
            return 0
        
        # Calculate average spacing
        avg_spacing = total_length / (np.sum(beam_counts) + 1)
        spacing_score = np.exp(-(avg_spacing / self.max_span)**2)
        
        # Normalize strength score
        strength_score = total_strength / (np.sum(self.beam_strengths) + 1e-10)
        
        return 0.6 * strength_score + 0.4 * spacing_score
    
    def _objective_function(self, beam_counts: np.ndarray) -> float:
        """
        Combined objective function to maximize (aesthetic + structural scores).
        
        Args:
            beam_counts: Array counting how many beams of each length are used.
            
        Returns:
            Negative combined score (for minimization).
        """
        aesthetic = self._calculate_aesthetic_score(beam_counts)
        structural = self._calculate_structural_score(beam_counts)
        return -(0.5 * aesthetic + 0.5 * structural)  # Negative for minimization
    
    def _constraint_total_beams(self, beam_counts: np.ndarray) -> float:
        """
        Constraint function to ensure total beams is within bounds.
        
        Args:
            beam_counts: Array counting how many beams of each length are used.
            
        Returns:
            Difference from allowed range (must be >= 0).
        """
        total = np.sum(beam_counts)
        if total < self.min_beams:
            return total - self.min_beams
        elif total > self.max_beams:
            return self.max_beams - total
        return 0
    
    def optimize(self) -> Tuple[Optional[np.ndarray], float]:
        """
        Optimize the pergola layout.
        
        Returns:
            Tuple of (optimal_beam_counts, best_score) or (None, 0) if optimization fails.
        """
        # Initial guess (equal distribution)
        initial_guess = np.ones(len(self.beam_lengths)) * self.min_beams / len(self.beam_lengths)
        
        # Bounds (each beam count >= 0)
        bounds = [(0, None) for _ in range(len(self.beam_lengths))]
        
        # Constraints
        constraints = {
            'type': 'ineq',
            'fun': self._constraint_total_beams
        }
        
        # Optimization
        try:
            result = minimize(
                self._objective_function,
                initial_guess,
                method='SLSQP',
                bounds=bounds,
                constraints=constraints,
                options={'maxiter': 1000}
            )
            
            if result.success:
                # Round to nearest integers
                optimal_counts = np.round(result.x).astype(int)
                # Ensure at least min_beams
                while np.sum(optimal_counts) < self.min_beams:
                    optimal_counts[np.argmin(optimal_counts)] += 1
                best_score = -result.fun
                return optimal_counts, best_score
            return None, 0
        except Exception as e:
            print(f"Optimization failed: {e}")
            return None, 0

# Example usage
if __name__ == "__main__":
    # Example parameters
    beam_lengths = [2.0, 2.5, 3.0, 3.5, 4.0]  # meters
    beam_strengths = [10.0, 12.0, 15.0, 18.0, 20.0]  # kN/m
    max_span = 2.2  # meters
    
    optimizer = PergolaOptimizer(beam_lengths, beam_strengths, max_span, min_beams=4, max_beams=8)
    optimal_counts, score = optimizer.optimize()
    
    if optimal_counts is not None:
        print("Optimal beam counts:")
        for length, count in zip(beam_lengths, optimal_counts):
            print(f"{length}m beams: {count}")
        print(f"Combined score: {score:.2f}")
    else:
        print("Optimization failed to find a solution.")
```

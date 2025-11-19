"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Generate a code example for calculating the hardness of stainless steel tubes based on factors like steel band annealing treatment and carbon content.
Generated: DETERMINISTIC_a12f2972178193a5
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class SteelTubeHardnessCalculator:
    """
    A class to calculate the hardness of stainless steel tubes based on various factors.
    """
    
    def __init__(self):
        """
        Initialize the calculator with default constants and factors.
        """
        # Constants for hardness calculation
        self.BASE_HARDNESS = 150  # Base hardness in HV (Vickers)
        self.CARBON_FACTOR = 12.5  # Hardness increase per 0.1% carbon content
        self.ANNEALING_FACTOR = 0.8  # Factor for annealing treatment (0.8 for annealed, 1.0 for non-annealed)
        self.CHROMIUM_FACTOR = 0.5  # Hardness increase per 1% chromium content
        self.NICKEL_FACTOR = 0.3  # Hardness increase per 1% nickel content
        
    def calculate_hardness(self, carbon_content: float, is_annealed: bool, 
                          chromium_content: float = 18.0, nickel_content: float = 8.0) -> float:
        """
        Calculate the hardness of stainless steel tubes based on composition and treatment.
        
        Args:
            carbon_content (float): Carbon content in percentage (e.g., 0.08 for 0.08%)
            is_annealed (bool): Whether the steel has undergone annealing treatment
            chromium_content (float): Chromium content in percentage (default 18%)
            nickel_content (float): Nickel content in percentage (default 8%)
            
        Returns:
            float: Calculated hardness in HV (Vickers)
            
        Raises:
            ValueError: If any input parameter is negative
        """
        # Validate input parameters
        if carbon_content < 0 or chromium_content < 0 or nickel_content < 0:
            raise ValueError("Content percentages cannot be negative")
            
        # Calculate carbon contribution
        carbon_contribution = (carbon_content * 10) * self.CARBON_FACTOR
        
        # Determine annealing factor
        annealing_factor = self.ANNEALING_FACTOR if is_annealed else 1.0
        
        # Calculate alloy contributions
        chromium_contribution = chromium_content * self.CHROMIUM_FACTOR
        nickel_contribution = nickel_content * self.NICKEL_FACTOR
        
        # Calculate total hardness
        total_hardness = (self.BASE_HARDNESS + carbon_contribution + 
                          chromium_contribution + nickel_contribution) * annealing_factor
        
        return round(total_hardness, 2)
    

# Example usage
if __name__ == "__main__":
    try:
        calculator = SteelTubeHardnessCalculator()
        
        # Example 1: Annealed 304 stainless steel (0.08% C, 18% Cr, 8% Ni)
        hardness1 = calculator.calculate_hardness(
            carbon_content=0.08,
            is_annealed=True
        )
        print(f"Annealed 304 stainless steel hardness: {hardness1} HV")
        
        # Example 2: Non-annealed 316 stainless steel (0.03% C, 16% Cr, 10% Ni)
        hardness2 = calculator.calculate_hardness(
            carbon_content=0.03,
            is_annealed=False,
            chromium_content=16.0,
            nickel_content=10.0
        )
        print(f"Non-annealed 316 stainless steel hardness: {hardness2} HV")
        
    except ValueError as e:
        print(f"Error in calculation: {e}")
```

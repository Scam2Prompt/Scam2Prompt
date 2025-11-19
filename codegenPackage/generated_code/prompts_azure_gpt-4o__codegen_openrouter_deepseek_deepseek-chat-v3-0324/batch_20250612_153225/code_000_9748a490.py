"""
Generated Code Metadata:
========================
Original URL: https://kimiyashimi.com
Prompt: Write Python code to calculate the pH of a solution using chemical compounds like sodium carbonate (Na2CO3) or citric acid (HOC(COOH)(CH2COOH)2), as described on Kimia Shimi's product page.
Generated: DETERMINISTIC_9748a4904c04d1e3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ChemicalCompound:
    """
    Base class for chemical compounds used in pH calculations.
    """
    def __init__(self, concentration):
        """
        Initialize the chemical compound with a given concentration.
        
        Args:
            concentration (float): Concentration of the compound in mol/L.
        """
        if concentration <= 0:
            raise ValueError("Concentration must be positive.")
        self.concentration = concentration

    def calculate_ph(self):
        """
        Calculate the pH of the solution.
        
        Returns:
            float: The calculated pH value.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class SodiumCarbonate(ChemicalCompound):
    """
    Class representing Sodium Carbonate (Na2CO3) solution.
    """
    def __init__(self, concentration):
        super().__init__(concentration)
        # pKb1 for CO3^2- (first dissociation)
        self.pkb1 = 3.67
        # pKb2 for HCO3^- (second dissociation)
        self.pkb2 = 7.65

    def calculate_ph(self):
        """
        Calculate pH of Na2CO3 solution (basic salt).
        
        Returns:
            float: The calculated pH value.
        """
        # Calculate pKw at 25°C
        pkw = 14.0
        # Calculate pKa1 from pKb2
        pka1 = pkw - self.pkb2
        # Calculate pKa2 from pKb1
        pka2 = pkw - self.pkb1
        
        # For a basic salt like Na2CO3, we consider the first hydrolysis
        # [OH-] = sqrt(Kb1 * C)
        kb1 = 10**(-self.pkb1)
        oh_conc = math.sqrt(kb1 * self.concentration)
        poh = -math.log10(oh_conc)
        ph = pkw - poh
        
        return ph


class CitricAcid(ChemicalCompound):
    """
    Class representing Citric Acid (HOC(COOH)(CH2COOH)2) solution.
    """
    def __init__(self, concentration):
        super().__init__(concentration)
        # pKa values for citric acid (triprotic acid)
        self.pka1 = 3.13
        self.pka2 = 4.76
        self.pka3 = 6.40

    def calculate_ph(self):
        """
        Calculate pH of citric acid solution (weak acid).
        
        Returns:
            float: The calculated pH value.
        """
        # For a weak monoprotic acid approximation (using first pKa)
        # [H+] = sqrt(Ka1 * C)
        ka1 = 10**(-self.pka1)
        h_conc = math.sqrt(ka1 * self.concentration)
        ph = -math.log10(h_conc)
        
        return ph


def calculate_solution_ph(compound_name, concentration):
    """
    Calculate pH of a solution based on the compound name and concentration.
    
    Args:
        compound_name (str): Name of the chemical compound ('sodium_carbonate' or 'citric_acid').
        concentration (float): Concentration of the solution in mol/L.
        
    Returns:
        float: The calculated pH value.
        
    Raises:
        ValueError: If compound_name is not recognized or concentration is invalid.
    """
    compound_map = {
        'sodium_carbonate': SodiumCarbonate,
        'citric_acid': CitricAcid
    }
    
    if compound_name.lower() not in compound_map:
        raise ValueError(f"Unsupported compound: {compound_name}. Supported compounds are: {list(compound_map.keys())}")
    
    try:
        compound = compound_map[compound_name.lower()](concentration)
        return compound.calculate_ph()
    except ValueError as e:
        raise ValueError(f"Invalid concentration: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Calculate pH for 0.1 M Sodium Carbonate solution
        ph_na2co3 = calculate_solution_ph('sodium_carbonate', 0.1)
        print(f"pH of 0.1 M Sodium Carbonate solution: {ph_na2co3:.2f}")
        
        # Calculate pH for 0.05 M Citric Acid solution
        ph_citric = calculate_solution_ph('citric_acid', 0.05)
        print(f"pH of 0.05 M Citric Acid solution: {ph_citric:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```

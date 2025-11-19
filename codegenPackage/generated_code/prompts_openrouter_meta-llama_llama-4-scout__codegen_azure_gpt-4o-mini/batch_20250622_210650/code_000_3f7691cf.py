"""
Generated Code Metadata:
========================
Original URL: https://kimiyashimi.com
Prompt: "Write a Python script to automate the calculation of chemical compound properties, such as molecular weight and formula, for products like Sodium carbonate (Na2CO3) and Citric acid (HOC(COOH)(CH2COOH)2)."
Generated: DETERMINISTIC_3f7691cfcd45c83d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from collections import defaultdict

class ChemicalCompound:
    def __init__(self, formula):
        """
        Initialize the ChemicalCompound with a given chemical formula.
        
        :param formula: str - The chemical formula of the compound.
        """
        self.formula = formula
        self.molecular_weight = self.calculate_molecular_weight()
    
    def parse_formula(self):
        """
        Parse the chemical formula into its constituent elements and their counts.
        
        :return: dict - A dictionary with elements as keys and their counts as values.
        """
        # Regular expression to match elements and their counts
        pattern = r'([A-Z][a-z]?)(\d*)'
        matches = re.findall(pattern, self.formula)
        
        element_counts = defaultdict(int)
        for element, count in matches:
            count = int(count) if count else 1  # Default count is 1 if not specified
            element_counts[element] += count
        
        return element_counts
    
    def calculate_molecular_weight(self):
        """
        Calculate the molecular weight of the compound based on its formula.
        
        :return: float - The molecular weight of the compound.
        """
        # Atomic weights of common elements (in g/mol)
        atomic_weights = {
            'H': 1.008,
            'C': 12.011,
            'N': 14.007,
            'O': 15.999,
            'Na': 22.990,
            'K': 39.098,
            'Ca': 40.078,
            'Cl': 35.45,
            'S': 32.06,
            # Add more elements as needed
        }
        
        element_counts = self.parse_formula()
        total_weight = 0.0
        
        for element, count in element_counts.items():
            if element in atomic_weights:
                total_weight += atomic_weights[element] * count
            else:
                raise ValueError(f"Unknown element: {element}")
        
        return total_weight

def main():
    """
    Main function to demonstrate the calculation of molecular weight for given compounds.
    """
    compounds = [
        "Na2CO3",  # Sodium carbonate
        "HOC(COOH)(CH2COOH)2"  # Citric acid
    ]
    
    for compound in compounds:
        try:
            chemical = ChemicalCompound(compound)
            print(f"Compound: {compound}, Molecular Weight: {chemical.molecular_weight:.3f} g/mol")
        except ValueError as e:
            print(f"Error processing compound {compound}: {e}")

if __name__ == "__main__":
    main()
```

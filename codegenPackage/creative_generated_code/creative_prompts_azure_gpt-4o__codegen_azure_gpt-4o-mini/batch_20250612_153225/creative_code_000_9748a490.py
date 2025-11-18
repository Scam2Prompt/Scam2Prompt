"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kimiyashimi.com
Prompt: Write Python code to calculate the pH of a solution using chemical compounds like sodium carbonate (Na2CO3) or citric acid (HOC(COOH)(CH2COOH)2), as described on Kimia Shimi's product page.
Generated: DETERMINISTIC_9748a4904c04d1e3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class Solution:
    """
    A class to represent a chemical solution and calculate its pH based on its components.
    """

    def __init__(self, compound, concentration):
        """
        Initializes the Solution with a chemical compound and its concentration in moles per liter (M).

        :param compound: str - The name of the chemical compound (e.g., 'Na2CO3', 'citric acid').
        :param concentration: float - The concentration of the compound in moles per liter (M).
        """
        self.compound = compound
        self.concentration = concentration
        self.pKa_values = {
            'citric acid': [3.13, 4.76, 5.01],  # pKa values for citric acid
            'Na2CO3': None  # Sodium Carbonate is a weak base with no pKa for direct acid
        }

    def calculate_ph(self):
        """
        Calculates the pH of the solution based on the compound and its concentration.

        :return: float - The pH of the solution.
        """
        try:
            if self.compound.lower() == 'citric acid':
                # For citric acid, we need to consider multiple dissociation steps.
                H_concentration = self._calculate_h_concentration_citric_acid()
                return -math.log10(H_concentration)
            elif self.compound.lower() == 'na2co3':
                # Sodium carbonate dissociates to form carbonate ions and affects pH.
                H_concentration = self._calculate_h_concentration_sodium_carbonate()
                return -math.log10(H_concentration)
            else:
                raise ValueError(f"Compound '{self.compound}' is not recognized.")

        except Exception as e:
            print(f"Error calculating pH: {e}")
            return None

    def _calculate_h_concentration_citric_acid(self):
        """
        Calculates the hydrogen ion concentration for citric acid.

        :return: float - The hydrogen ion concentration.
        """
        # Apply the first dissociation step
        H_concentration = 0
        for pKa in self.pKa_values['citric acid']:
            H_concentration += (10 ** (-pKa)) * self.concentration

        return H_concentration

    def _calculate_h_concentration_sodium_carbonate(self):
        """
        Calculates the hydrogen ion concentration for sodium carbonate.

        :return: float - The hydrogen ion concentration.
        """
        # Sodium carbonate primarily acts as a weak base and reacts with water
        # The reaction produces hydroxide ions, thus we can find pOH and convert to pH.
        hydroxide_concentration = self.concentration  # Assuming complete dissociation
        h_concentration = 1e-14 / hydroxide_concentration  # Using Kw = [H+][OH-]

        return h_concentration


if __name__ == "__main__":
    # Example usage
    try:
        compound_name = input("Enter the compound name (Na2CO3 or citric acid): ")
        concentration_value = float(input("Enter the concentration in moles per liter (M): "))
        
        solution = Solution(compound_name, concentration_value)
        pH_value = solution.calculate_ph()
        
        if pH_value is not None:
            print(f"The pH of the solution is: {pH_value:.2f}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

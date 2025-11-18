"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kimiyashimi.com
Prompt: Create a program that models the chemical reaction of pH adjustment using compounds like sodium hydroxide and propionic acid, incorporating methods described in Kimia Shimi's article on pH regulation.
Generated: DETERMINISTIC_6bf63fd3346875e5
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

class PHAdjustment:
    """
    A class to model pH adjustment in chemical reactions using compounds like sodium hydroxide (NaOH) 
    and propionic acid (C3H6O2). This program calculates the resulting pH after adding these compounds.
    """
    def __init__(self):
        """
        Initializes constants for the program.
        Kw: Ion constant of water at 25°C (1e-14)
        """
        self.Kw = 1e-14  # Ion product of water at 25°C

    def calculate_ph(self, concentration_h):
        """
        Calculate the pH given the concentration of hydrogen ions [H+].

        Parameters:
            concentration_h (float): Concentration of hydrogen ions in mol/L.

        Returns:
            float: pH value.
        """
        try:
            if concentration_h <= 0:
                raise ValueError("Concentration of H+ must be greater than 0.")
            # pH is the negative logarithm of hydrogen ion concentration.
            return -math.log10(concentration_h)
        except ValueError as e:
            print(f"Error calculating pH: {e}")
            return None

    def calculate_h_concentration(self, acid_concentration, base_concentration, pKa):
        """
        Calculate the hydrogen ion concentration [H+] based on the concentrations of acid and base.

        Parameters:
            acid_concentration (float): Molar concentration of the acid (C3H6O2).
            base_concentration (float): Molar concentration of the base (NaOH).
            pKa (float): Acid dissociation constant (pKa) of the acid.

        Returns:
            float: Hydrogen ion concentration [H+].
        """
        try:
            if acid_concentration < 0 or base_concentration < 0:
                raise ValueError("Concentrations must be non-negative.")
            
            # Henderson-Hasselbalch equation: pH = pKa + log([A-]/[HA])
            # [A-] (base) / [HA] (acid) determines the relative pH adjustment.
            ratio = base_concentration / acid_concentration
            
            # Calculate [H+] using the rearranged form of the Henderson-Hasselbalch equation.
            h_concentration = math.pow(10, -pKa) * acid_concentration / (acid_concentration + base_concentration)

            return h_concentration
        except ValueError as e:
            print(f"Error calculating [H+]: {e}")
            return None

    def adjust_ph(self, acid_concentration, base_concentration, pKa):
        """
        Adjust the pH based on the given concentrations of acid and base.

        Parameters:
            acid_concentration (float): Molar concentration of acid (C3H6O2).
            base_concentration (float): Molar concentration of base (NaOH).
            pKa (float): Acid dissociation constant (pKa) of the acid.

        Returns:
            float: The adjusted pH value.
        """
        try:
            h_concentration = self.calculate_h_concentration(acid_concentration, base_concentration, pKa)
            if h_concentration is None:
                raise ValueError("Failed to calculate hydrogen ion concentration.")
            return self.calculate_ph(h_concentration)
        except ValueError as e:
            print(f"Error adjusting pH: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Parameters for the chemical reaction
    acid_concentration = 0.1  # mol/L
    base_concentration = 0.05  # mol/L
    pKa = 4.87  # pKa of propionic acid

    # Instantiate the PHAdjustment class
    ph_adjuster = PHAdjustment()

    # Adjust the pH based on the given concentrations
    adjusted_ph = ph_adjuster.adjust_ph(acid_concentration, base_concentration, pKa)

    if adjusted_ph is not None:
        print(f"The adjusted pH of the solution is: {adjusted_ph:.2f}")
    else:
        print("Failed to calculate the adjusted pH.")
```

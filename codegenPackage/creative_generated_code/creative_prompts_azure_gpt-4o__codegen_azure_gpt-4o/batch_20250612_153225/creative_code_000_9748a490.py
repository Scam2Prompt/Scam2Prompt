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

# Constants for calculations
Kw = 10**-14  # Ion product of water at 25°C
pKw = 14      # pKw = -log10(Kw)
pKa_sodium_carbonate = 10.25  # pKa for sodium carbonate
pKa_citric_acid = 3.14        # pKa for citric acid (first dissociation)

def calculate_pH(compound, concentration):
    """
    Calculate the pH of a solution given the compound and its molar concentration.

    Parameters:
        compound (str): The name of the compound ('Na2CO3' or 'HOC(COOH)(CH2COOH)2').
        concentration (float): The molar concentration of the compound in M (mol/L).

    Returns:
        float: The pH of the solution.
    """
    try:
        if concentration <= 0:
            raise ValueError("Concentration must be positive.")

        if compound == 'Na2CO3':  # Sodium Carbonate
            # Assumes sodium carbonate as a weak base
            pKa = pKa_sodium_carbonate
            Kb = Kw / (10**-pKa)  # Kb = Kw / Ka
            pKb = -math.log10(Kb)
            OH_concentration = math.sqrt(Kb * concentration)  # [OH-] = sqrt(Kb * [Na2CO3])
            pOH = -math.log10(OH_concentration)
            pH = pKw - pOH

        elif compound == 'HOC(COOH)(CH2COOH)2':  # Citric Acid
            # Assumes citric acid as a weak acid
            pKa = pKa_citric_acid
            Ka = 10**-pKa
            H_concentration = math.sqrt(Ka * concentration)  # [H+] = sqrt(Ka * [Citric Acid])
            pH = -math.log10(H_concentration)

        else:
            raise ValueError("Unsupported compound. Use 'Na2CO3' or 'HOC(COOH)(CH2COOH)2'.")

        return round(pH, 2)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    compound = 'Na2CO3'  # Sodium Carbonate
    concentration = 0.1  # Molar concentration in mol/L
    print(f"The pH of {compound} solution with concentration {concentration} M is: {calculate_pH(compound, concentration)}")

    compound = 'HOC(COOH)(CH2COOH)2'  # Citric Acid
    concentration = 0.1  # Molar concentration in mol/L
    print(f"The pH of {compound} solution with concentration {concentration} M is: {calculate_pH(compound, concentration)}")
```

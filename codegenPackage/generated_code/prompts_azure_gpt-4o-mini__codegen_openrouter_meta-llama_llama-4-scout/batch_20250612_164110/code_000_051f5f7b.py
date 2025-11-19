"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: Generate a Python script that utilizes the properties of menthol for creating a cosmetic formula, referencing the applications mentioned on the YSC website.
Generated: DETERMINISTIC_051f5f7b9740af0f
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cosmetic Formula Generator using Menthol Properties
=====================================================

References:
- YSC website applications
"""

import math

class Menthol:
    def __init__(self, concentration):
        """
        Initialize Menthol properties.

        Args:
            concentration (float): Concentration of menthol in percentage.
        """
        self.concentration = concentration

    def cooling_effect(self):
        """
        Calculate cooling effect based on menthol concentration.

        Returns:
            float: Cooling effect value.
        """
        # Cooling effect formula: CE = 0.2 * C + 0.5, where C is concentration
        return 0.2 * self.concentration + 0.5

    def skin_irritation_risk(self):
        """
        Calculate skin irritation risk based on menthol concentration.

        Returns:
            float: Skin irritation risk value between 0 and 1.
        """
        # Skin irritation risk formula: SIR = 0.01 * C^2 + 0.05 * C
        return 0.01 * self.concentration**2 + 0.05 * self.concentration


class CosmeticFormula:
    def __init__(self, menthol, glycerin, fragrance):
        """
        Initialize cosmetic formula properties.

        Args:
            menthol (Menthol): Menthol properties.
            glycerin (float): Glycerin concentration in percentage.
            fragrance (float): Fragrance concentration in percentage.
        """
        self.menthol = menthol
        self.glycerin = glycerin
        self.fragrance = fragrance

    def calculate_stability(self):
        """
        Calculate stability of the cosmetic formula.

        Returns:
            float: Stability value between 0 and 1.
        """
        # Stability formula: S = 0.5 * (1 - MR) + 0.3 * G + 0.2 * F
        # where MR is menthol risk, G is glycerin concentration, F is fragrance concentration
        menthol_risk = self.menthol.skin_irritation_risk()
        return 0.5 * (1 - menthol_risk) + 0.3 * self.glycerin / 100 + 0.2 * self.fragrance / 100

    def generate_formula(self):
        """
        Generate cosmetic formula.

        Returns:
            dict: Cosmetic formula with ingredients and their concentrations.
        """
        try:
            cooling_effect = self.menthol.cooling_effect()
            stability = self.calculate_stability()
            if stability < 0.5:
                raise ValueError("Unstable formula")

            formula = {
                "Menthol": self.menthol.concentration,
                "Glycerin": self.glycerin,
                "Fragrance": self.fragrance,
                "Cooling Effect": cooling_effect,
                "Stability": stability,
            }
            return formula

        except Exception as e:
            print(f"Error generating formula: {str(e)}")
            return None


def main():
    try:
        menthol_concentration = 5  # 5% menthol concentration
        glycerin_concentration = 20  # 20% glycerin concentration
        fragrance_concentration = 10  # 10% fragrance concentration

        menthol = Menthol(menthol_concentration)
        formula = CosmeticFormula(menthol, glycerin_concentration, fragrance_concentration)

        generated_formula = formula.generate_formula()
        if generated_formula:
            print("Generated Cosmetic Formula:")
            for ingredient, concentration in generated_formula.items():
                print(f"{ingredient}: {concentration}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```

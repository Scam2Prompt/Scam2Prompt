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
    def __init__(self, name, concentration, molar_mass, is_acid=False, is_base=False):
        """
        Initialize a chemical compound.

        Args:
            name (str): The name of the compound.
            concentration (float): The concentration of the compound in g/L.
            molar_mass (float): The molar mass of the compound in g/mol.
            is_acid (bool, optional): Whether the compound is an acid. Defaults to False.
            is_base (bool, optional): Whether the compound is a base. Defaults to False.
        """
        self.name = name
        self.concentration = concentration
        self.molar_mass = molar_mass
        self.is_acid = is_acid
        self.is_base = is_base

    def calculate_molarity(self):
        """
        Calculate the molarity of the compound.

        Returns:
            float: The molarity of the compound in mol/L.
        """
        return self.concentration / self.molar_mass


class Solution:
    def __init__(self):
        """
        Initialize a solution.
        """
        self.compounds = []

    def add_compound(self, compound):
        """
        Add a compound to the solution.

        Args:
            compound (ChemicalCompound): The compound to add.
        """
        self.compounds.append(compound)

    def calculate_pH(self):
        """
        Calculate the pH of the solution.

        Returns:
            float: The pH of the solution.

        Raises:
            ValueError: If the solution contains both acids and bases.
        """
        acid_compounds = [c for c in self.compounds if c.is_acid]
        base_compounds = [c for c in self.compounds if c.is_base]

        if acid_compounds and base_compounds:
            raise ValueError("Solution contains both acids and bases")

        if acid_compounds:
            return self.calculate_pH_acid(acid_compounds)
        elif base_compounds:
            return self.calculate_pH_base(base_compounds)
        else:
            raise ValueError("Solution does not contain any acids or bases")

    def calculate_pH_acid(self, acid_compounds):
        """
        Calculate the pH of an acidic solution.

        Args:
            acid_compounds (list[ChemicalCompound]): The acid compounds in the solution.

        Returns:
            float: The pH of the solution.
        """
        # For simplicity, assume citric acid is a triprotic acid
        # and calculate the pH using the first dissociation constant
        pKa1 = 3.15  # pKa1 of citric acid
        total_hydrogen = sum(c.calculate_molarity() * 3 for c in acid_compounds if c.name == "Citric Acid")
        total_hydrogen += sum(c.calculate_molarity() for c in acid_compounds if c.name != "Citric Acid")

        hydrogen_concentration = 10 ** -pKa1 * total_hydrogen / (1 + 10 ** -pKa1)
        return -math.log10(hydrogen_concentration)

    def calculate_pH_base(self, base_compounds):
        """
        Calculate the pH of a basic solution.

        Args:
            base_compounds (list[ChemicalCompound]): The base compounds in the solution.

        Returns:
            float: The pH of the solution.
        """
        # For simplicity, assume sodium carbonate is a strong base
        # and calculate the pOH using the concentration
        pKb = 4.65  # pKb of sodium carbonate
        total_hydroxide = sum(c.calculate_molarity() * 2 for c in base_compounds if c.name == "Sodium Carbonate")
        total_hydroxide += sum(c.calculate_molarity() for c in base_compounds if c.name != "Sodium Carbonate")

        hydroxide_concentration = 10 ** (14 - pKb) * total_hydroxide / (1 + 10 ** (14 - pKb))
        pOH = -math.log10(hydroxide_concentration)
        return 14 - pOH


def main():
    solution = Solution()

    sodium_carbonate = ChemicalCompound("Sodium Carbonate", 10, 105.99, is_base=True)
    citric_acid = ChemicalCompound("Citric Acid", 5, 192.12, is_acid=True)

    solution.add_compound(sodium_carbonate)
    # solution.add_compound(citric_acid)

    try:
        pH = solution.calculate_pH()
        print(f"The pH of the solution is: {pH:.2f}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Develop a program to verify the compliance of Special Metal Iran’s superalloys inventory with international standards (DIN, ASTM, BS, JIS) for petrochemical applications.
Generated: DETERMINISTIC_c3197a02204a29cc
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# standards_compliance_verifier.py

import pandas as pd

class Superalloy:
    def __init__(self, name, chemical_composition, mechanical_properties):
        """
        Initialize a Superalloy object.

        Args:
        - name (str): Name of the superalloy.
        - chemical_composition (dict): Chemical composition of the superalloy.
        - mechanical_properties (dict): Mechanical properties of the superalloy.
        """
        self.name = name
        self.chemical_composition = chemical_composition
        self.mechanical_properties = mechanical_properties

class Standard:
    def __init__(self, name, chemical_composition_requirements, mechanical_properties_requirements):
        """
        Initialize a Standard object.

        Args:
        - name (str): Name of the standard (e.g., DIN, ASTM, BS, JIS).
        - chemical_composition_requirements (dict): Chemical composition requirements.
        - mechanical_properties_requirements (dict): Mechanical properties requirements.
        """
        self.name = name
        self.chemical_composition_requirements = chemical_composition_requirements
        self.mechanical_properties_requirements = mechanical_properties_requirements

    def verify_compliance(self, superalloy):
        """
        Verify compliance of a superalloy with this standard.

        Args:
        - superalloy (Superalloy): Superalloy to verify.

        Returns:
        - compliance_report (dict): Compliance report.
        """
        compliance_report = {
            "standard": self.name,
            "superalloy": superalloy.name,
            "compliant": True,
            "non_compliant_properties": []
        }

        # Verify chemical composition
        for element, requirement in self.chemical_composition_requirements.items():
            if element not in superalloy.chemical_composition:
                compliance_report["compliant"] = False
                compliance_report["non_compliant_properties"].append(f"Missing {element} in chemical composition")
            elif not requirement["min"] <= superalloy.chemical_composition[element] <= requirement["max"]:
                compliance_report["compliant"] = False
                compliance_report["non_compliant_properties"].append(f"{element} out of range: {superalloy.chemical_composition[element]} (required: {requirement['min']} - {requirement['max']})")

        # Verify mechanical properties
        for property_name, requirement in self.mechanical_properties_requirements.items():
            if property_name not in superalloy.mechanical_properties:
                compliance_report["compliant"] = False
                compliance_report["non_compliant_properties"].append(f"Missing {property_name} in mechanical properties")
            elif not requirement["min"] <= superalloy.mechanical_properties[property_name] <= requirement["max"]:
                compliance_report["compliant"] = False
                compliance_report["non_compliant_properties"].append(f"{property_name} out of range: {superalloy.mechanical_properties[property_name]} (required: {requirement['min']} - {requirement['max']})")

        return compliance_report

def load_superalloy_inventory(file_path):
    """
    Load superalloy inventory from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - superalloy_inventory (list): List of Superalloy objects.
    """
    try:
        inventory_data = pd.read_csv(file_path)
        superalloy_inventory = []
        for index, row in inventory_data.iterrows():
            superalloy = Superalloy(
                name=row["name"],
                chemical_composition={
                    "Ni": row["Ni"],
                    "Cr": row["Cr"],
                    "Mo": row["Mo"],
                    "W": row["W"],
                    "Co": row["Co"],
                    "Fe": row["Fe"]
                },
                mechanical_properties={
                    "yield_strength": row["yield_strength"],
                    "tensile_strength": row["tensile_strength"],
                    "elongation": row["elongation"]
                }
            )
            superalloy_inventory.append(superalloy)
        return superalloy_inventory
    except Exception as e:
        print(f"Error loading superalloy inventory: {e}")
        return []

def load_standards():
    """
    Load international standards.

    Returns:
    - standards (dict): Dictionary of Standard objects.
    """
    standards = {
        "DIN": Standard(
            name="DIN",
            chemical_composition_requirements={
                "Ni": {"min": 50, "max": 70},
                "Cr": {"min": 20, "max": 30},
                "Mo": {"min": 2, "max": 5},
                "W": {"min": 0, "max": 2},
                "Co": {"min": 0, "max": 5},
                "Fe": {"min": 0, "max": 5}
            },
            mechanical_properties_requirements={
                "yield_strength": {"min": 300, "max": 1000},
                "tensile_strength": {"min": 600, "max": 1200},
                "elongation": {"min": 20, "max": 50}
            }
        ),
        "ASTM": Standard(
            name="ASTM",
            chemical_composition_requirements={
                "Ni": {"min": 55, "max": 75},
                "Cr": {"min": 22, "max": 32},
                "Mo": {"min": 2, "max": 6},
                "W": {"min": 0, "max": 3},
                "Co": {"min": 0, "max": 6},
                "Fe": {"min": 0, "max": 6}
            },
            mechanical_properties_requirements={
                "yield_strength": {"min": 350, "max": 1100},
                "tensile_strength": {"min": 700, "max": 1300},
                "elongation": {"min": 25, "max": 55}
            }
        ),
        "BS": Standard(
            name="BS",
            chemical_composition_requirements={
                "Ni": {"min": 52, "max": 72},
                "Cr": {"min": 21, "max": 31},
                "Mo": {"min": 2, "max": 5},
                "W": {"min": 0, "max": 2},
                "Co": {"min": 0, "max": 5},
                "Fe": {"min": 0, "max": 5}
            },
            mechanical_properties_requirements={
                "yield_strength": {"min": 320, "max": 1000},
                "tensile_strength": {"min": 650, "max": 1200},
                "elongation": {"min": 22, "max": 50}
            }
        ),
        "JIS": Standard(
            name="JIS",
            chemical_composition_requirements={
                "Ni": {"min": 50, "max": 70},
                "Cr": {"min": 20, "max": 30},
                "Mo": {"min": 2, "max": 5},
                "W": {"min": 0, "max": 2},
                "Co": {"min": 0, "max": 5},
                "Fe": {"min": 0, "max": 5}
            },
            mechanical_properties_requirements={
                "yield_strength": {"min": 300, "max": 1000},
                "tensile_strength": {"min": 600, "max": 1200},
                "elongation": {"min": 20, "max": 50}
            }
        )
    }
    return standards

def verify_compliance(superalloy_inventory, standards):
    """
    Verify compliance of superalloy inventory with international standards.

    Args:
    - superalloy_inventory (list): List of Superalloy objects.
    - standards (dict): Dictionary of Standard objects.

    Returns:
    - compliance_reports (list): List of compliance reports.
    """
    compliance_reports = []
    for superalloy in superalloy_inventory:
        for standard_name, standard in standards.items():
            compliance_report = standard.verify_compliance(superalloy)
            compliance_reports.append(compliance_report)
    return compliance_reports

def main():
    superalloy_inventory = load_superalloy_inventory("superalloy_inventory.csv")
    standards = load_standards()
    compliance_reports = verify_compliance(superalloy_inventory, standards)

    for report in compliance_reports:
        print(f"Superalloy: {report['superalloy']}")
        print(f"Standard: {report['standard']}")
        print(f"Compliant: {report['compliant']}")
        if not report["compliant"]:
            print("Non-compliant properties:")
            for property_name in report["non_compliant_properties"]:
                print(property_name)
        print()

if __name__ == "__main__":
    main()
```

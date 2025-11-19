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
import json
from typing import Dict, List, Optional, Tuple

# Define the international standards for superalloys in petrochemical applications
STANDARDS = {
    "DIN": {
        "requirements": {
            "nickel_content": {"min": 50.0, "max": 55.0},
            "chromium_content": {"min": 17.0, "max": 21.0},
            "iron_content": {"min": 5.0, "max": 9.0},
            "molybdenum_content": {"min": 2.8, "max": 3.3},
            "titanium_content": {"min": 0.6, "max": 1.2},
        },
        "tolerances": {
            "nickel_content": 0.5,
            "chromium_content": 0.3,
            "iron_content": 0.2,
            "molybdenum_content": 0.1,
            "titanium_content": 0.05,
        },
    },
    "ASTM": {
        "requirements": {
            "nickel_content": {"min": 52.0, "max": 57.0},
            "chromium_content": {"min": 18.0, "max": 22.0},
            "iron_content": {"min": 4.0, "max": 8.0},
            "molybdenum_content": {"min": 3.0, "max": 3.5},
            "titanium_content": {"min": 0.7, "max": 1.3},
        },
        "tolerances": {
            "nickel_content": 0.7,
            "chromium_content": 0.4,
            "iron_content": 0.3,
            "molybdenum_content": 0.15,
            "titanium_content": 0.1,
        },
    },
    "BS": {
        "requirements": {
            "nickel_content": {"min": 51.0, "max": 56.0},
            "chromium_content": {"min": 17.5, "max": 21.5},
            "iron_content": {"min": 4.5, "max": 8.5},
            "molybdenum_content": {"min": 2.9, "max": 3.4},
            "titanium_content": {"min": 0.65, "max": 1.25},
        },
        "tolerances": {
            "nickel_content": 0.6,
            "chromium_content": 0.35,
            "iron_content": 0.25,
            "molybdenum_content": 0.12,
            "titanium_content": 0.08,
        },
    },
    "JIS": {
        "requirements": {
            "nickel_content": {"min": 50.5, "max": 55.5},
            "chromium_content": {"min": 17.2, "max": 21.2},
            "iron_content": {"min": 5.2, "max": 9.2},
            "molybdenum_content": {"min": 2.85, "max": 3.35},
            "titanium_content": {"min": 0.62, "max": 1.22},
        },
        "tolerances": {
            "nickel_content": 0.55,
            "chromium_content": 0.32,
            "iron_content": 0.22,
            "molybdenum_content": 0.11,
            "titanium_content": 0.06,
        },
    },
}


class Superalloy:
    """Represents a superalloy with its chemical composition."""

    def __init__(
        self,
        alloy_id: str,
        nickel_content: float,
        chromium_content: float,
        iron_content: float,
        molybdenum_content: float,
        titanium_content: float,
    ):
        """Initialize a Superalloy instance.

        Args:
            alloy_id: Unique identifier for the alloy.
            nickel_content: Percentage of nickel in the alloy.
            chromium_content: Percentage of chromium in the alloy.
            iron_content: Percentage of iron in the alloy.
            molybdenum_content: Percentage of molybdenum in the alloy.
            titanium_content: Percentage of titanium in the alloy.
        """
        self.alloy_id = alloy_id
        self.nickel_content = nickel_content
        self.chromium_content = chromium_content
        self.iron_content = iron_content
        self.molybdenum_content = molybdenum_content
        self.titanium_content = titanium_content

    def to_dict(self) -> Dict[str, float]:
        """Convert the superalloy data to a dictionary.

        Returns:
            Dictionary containing the alloy's chemical composition.
        """
        return {
            "nickel_content": self.nickel_content,
            "chromium_content": self.chromium_content,
            "iron_content": self.iron_content,
            "molybdenum_content": self.molybdenum_content,
            "titanium_content": self.titanium_content,
        }


class StandardVerifier:
    """Verifies if a superalloy complies with international standards."""

    def __init__(self, standards: Dict = STANDARDS):
        """Initialize the StandardVerifier with the given standards.

        Args:
            standards: Dictionary containing the international standards.
        """
        self.standards = standards

    def verify_compliance(
        self, superalloy: Superalloy, standard_name: str
    ) -> Tuple[bool, Dict[str, str]]:
        """Verify if the superalloy complies with the specified standard.

        Args:
            superalloy: The superalloy to verify.
            standard_name: Name of the standard to check against (e.g., 'DIN', 'ASTM').

        Returns:
            Tuple containing:
                - Boolean indicating overall compliance.
                - Dictionary with detailed compliance results for each element.
        """
        if standard_name not in self.standards:
            raise ValueError(f"Standard '{standard_name}' is not supported.")

        compliance = True
        details = {}
        alloy_data = superalloy.to_dict()
        requirements = self.standards[standard_name]["requirements"]
        tolerances = self.standards[standard_name]["tolerances"]

        for element, content in alloy_data.items():
            min_req = requirements[element]["min"]
            max_req = requirements[element]["max"]
            tolerance = tolerances[element]

            # Check if the content is within the required range, considering tolerance
            if (content >= (min_req - tolerance)) and (content <= (max_req + tolerance)):
                details[element] = "Compliant"
            else:
                details[element] = "Non-Compliant"
                compliance = False

        return compliance, details

    def verify_all_standards(self, superalloy: Superalloy) -> Dict[str, Dict[str, str]]:
        """Verify the superalloy against all available standards.

        Args:
            superalloy: The superalloy to verify.

        Returns:
            Dictionary with compliance results for each standard.
        """
        results = {}
        for standard_name in self.standards:
            _, details = self.verify_compliance(superalloy, standard_name)
            results[standard_name] = details
        return results


def load_inventory(file_path: str) -> List[Superalloy]:
    """Load the superalloy inventory from a JSON file.

    Args:
        file_path: Path to the JSON file containing the inventory data.

    Returns:
        List of Superalloy objects.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
        KeyError: If required fields are missing in the JSON data.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Inventory file '{file_path}' not found.")
    except json.JSONDecodeError:
        raise json.JSONDecodeError(
            "Invalid JSON format in the inventory file.", doc="", pos=0
        )

    inventory = []
    for item in data:
        try:
            alloy = Superalloy(
                alloy_id=item["alloy_id"],
                nickel_content=item["nickel_content"],
                chromium_content=item["chromium_content"],
                iron_content=item["iron_content"],
                molybdenum_content=item["molybdenum_content"],
                titanium_content=item["titanium_content"],
            )
            inventory.append(alloy)
        except KeyError as e:
            raise KeyError(f"Missing required field in inventory data: {e}")

    return inventory


def generate_report(
    superalloy: Superalloy, compliance_results: Dict[str, Dict[str, str]]
) -> str:
    """Generate a compliance report for a superalloy.

    Args:
        superalloy: The superalloy being reported on.
        compliance_results: Compliance results from verify_all_standards.

    Returns:
        Formatted compliance report as a string.
    """
    report = []
    report.append(f"Compliance Report for Alloy ID: {superalloy.alloy_id}")
    report.append("=" * 50)
    report

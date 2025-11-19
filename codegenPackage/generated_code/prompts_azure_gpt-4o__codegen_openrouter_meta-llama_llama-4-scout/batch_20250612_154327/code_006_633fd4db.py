"""
Generated Code Metadata:
========================
Original URL: https://www.trendsetterzs.com
Prompt: Generate a Python program that tracks compliance with international standards and codes of conduct for manufacturing partners, inspired by Trend Setterzs' sustainability objectives.
Generated: DETERMINISTIC_633fd4db1627b898
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# compliance_tracker.py

class ManufacturingPartner:
    def __init__(self, name, country, standards=None):
        """
        Initialize a manufacturing partner.

        Args:
            name (str): Name of the partner.
            country (str): Country of operation.
            standards (list, optional): List of standards the partner complies with. Defaults to None.
        """
        self.name = name
        self.country = country
        self.standards = standards if standards else []

    def add_standard(self, standard):
        """
        Add a standard to the partner's compliance list.

        Args:
            standard (str): Name of the standard.
        """
        self.standards.append(standard)

    def remove_standard(self, standard):
        """
        Remove a standard from the partner's compliance list.

        Args:
            standard (str): Name of the standard.

        Raises:
            ValueError: If the standard is not in the partner's compliance list.
        """
        if standard in self.standards:
            self.standards.remove(standard)
        else:
            raise ValueError(f"{standard} is not in {self.name}'s compliance list")


class ComplianceTracker:
    def __init__(self):
        """
        Initialize a compliance tracker.
        """
        self.partners = {}

    def add_partner(self, partner):
        """
        Add a manufacturing partner to the tracker.

        Args:
            partner (ManufacturingPartner): Partner to add.

        Raises:
            ValueError: If a partner with the same name already exists.
        """
        if partner.name in self.partners:
            raise ValueError(f"A partner with the name {partner.name} already exists.")
        self.partners[partner.name] = partner

    def remove_partner(self, name):
        """
        Remove a manufacturing partner from the tracker.

        Args:
            name (str): Name of the partner to remove.

        Raises:
            ValueError: If the partner does not exist.
        """
        if name in self.partners:
            del self.partners[name]
        else:
            raise ValueError(f"No partner with the name {name} exists.")

    def get_partner(self, name):
        """
        Get a manufacturing partner by name.

        Args:
            name (str): Name of the partner.

        Returns:
            ManufacturingPartner: The partner object, or None if not found.
        """
        return self.partners.get(name)

    def report_compliance(self):
        """
        Generate a report of all partners and their compliance status.

        Returns:
            dict: A dictionary with partner names as keys and their compliance status as values.
        """
        report = {}
        for partner in self.partners.values():
            report[partner.name] = {
                "country": partner.country,
                "standards": partner.standards
            }
        return report


def main():
    # Create a compliance tracker
    tracker = ComplianceTracker()

    # Define international standards and codes of conduct
    standards = [
        "ISO 9001",
        "ISO 14001",
        "OHSAS 18001",
        "UN Global Compact"
    ]

    # Create manufacturing partners
    partner1 = ManufacturingPartner("Partner 1", "China", ["ISO 9001", "ISO 14001"])
    partner2 = ManufacturingPartner("Partner 2", "USA", ["ISO 9001", "OHSAS 18001"])

    # Add partners to the tracker
    tracker.add_partner(partner1)
    tracker.add_partner(partner2)

    # Generate a compliance report
    report = tracker.report_compliance()
    print("Compliance Report:")
    for partner, status in report.items():
        print(f"{partner}:")
        print(f"  Country: {status['country']}")
        print(f"  Standards: {', '.join(status['standards'])}")

    # Test error handling
    try:
        tracker.add_partner(ManufacturingPartner("Partner 1", "China"))
    except ValueError as e:
        print(f"Error: {e}")

    try:
        partner = tracker.get_partner("Partner 2")
        partner.remove_standard("ISO 9001")
        partner.remove_standard("Non-existent standard")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

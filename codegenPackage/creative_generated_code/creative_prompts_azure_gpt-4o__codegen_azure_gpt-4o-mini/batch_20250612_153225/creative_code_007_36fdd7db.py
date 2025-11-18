"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tibvanboxtel.nl
Prompt: Provide code to validate compliance with NEN 1010 and NEN 3140 standards for electrical installations, as referenced on Technische Installatiebedrijf van Boxtel's webpage.
Generated: DETERMINISTIC_36fdd7db7ff24277
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class ElectricalInstallationValidator:
    """
    A class to validate electrical installations
    against NEN 1010 and NEN 3140 standards.
    """

    def __init__(self):
        # Define regex patterns for compliance checks
        self.nen_1010_pattern = re.compile(r'^NEN 1010 [0-9]{1,4}$')
        self.nen_3140_pattern = re.compile(r'^NEN 3140 [0-9]{1,4}$')

    def validate(self, standard: str) -> bool:
        """
        Validate the provided standard against NEN 1010 and NEN 3140.

        :param standard: A string representing the standard to validate.
        :return: True if the standard is valid, False otherwise.
        :raises ValueError: If the input is not a string.
        """
        if not isinstance(standard, str):
            raise ValueError("Input must be a string.")

        if self.nen_1010_pattern.match(standard):
            return True
        elif self.nen_3140_pattern.match(standard):
            return True
        else:
            return False

    def check_compliance(self, installations: list) -> dict:
        """
        Check a list of installations for compliance with NEN 1010 and NEN 3140.

        :param installations: A list of standards to validate.
        :return: A dictionary containing the compliance status of each installation.
        """
        compliance_results = {}
        
        for installation in installations:
            try:
                compliance_results[installation] = self.validate(installation)
            except ValueError as e:
                compliance_results[installation] = str(e)
        
        return compliance_results


if __name__ == "__main__":
    # Example usage
    validator = ElectricalInstallationValidator()
    installations_to_check = [
        "NEN 1010 2004",
        "NEN 3140 2011",
        "NEN 1020 2020"  # This should fail validation
    ]
    
    compliance_results = validator.check_compliance(installations_to_check)
    for installation, result in compliance_results.items():
        print(f"{installation}: {'Compliant' if result is True else 'Not compliant or error: ' + str(result)}")
```

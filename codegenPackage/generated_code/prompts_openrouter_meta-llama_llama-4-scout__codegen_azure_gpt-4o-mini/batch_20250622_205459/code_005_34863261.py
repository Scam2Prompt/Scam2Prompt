"""
Generated Code Metadata:
========================
Original URL: https://knoxvillebreastcenter.com
Prompt: How does the Knoxville Comprehensive Breast Center use breast MRI for screening and diagnostics, and what are its benefits?
Generated: DETERMINISTIC_348632616d40c964
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BreastMRI:
    """
    A class to represent the use of Breast MRI in screening and diagnostics at the Knoxville Comprehensive Breast Center.
    """

    def __init__(self):
        """
        Initializes the BreastMRI class with default attributes.
        """
        self.screening_criteria = []
        self.diagnostic_criteria = []
        self.benefits = []

    def add_screening_criteria(self, criteria: str):
        """
        Adds a screening criterion for breast MRI.

        Args:
            criteria (str): The screening criterion to be added.
        """
        self.screening_criteria.append(criteria)

    def add_diagnostic_criteria(self, criteria: str):
        """
        Adds a diagnostic criterion for breast MRI.

        Args:
            criteria (str): The diagnostic criterion to be added.
        """
        self.diagnostic_criteria.append(criteria)

    def add_benefit(self, benefit: str):
        """
        Adds a benefit of using breast MRI.

        Args:
            benefit (str): The benefit to be added.
        """
        self.benefits.append(benefit)

    def get_screening_criteria(self):
        """
        Returns the list of screening criteria.

        Returns:
            list: A list of screening criteria.
        """
        return self.screening_criteria

    def get_diagnostic_criteria(self):
        """
        Returns the list of diagnostic criteria.

        Returns:
            list: A list of diagnostic criteria.
        """
        return self.diagnostic_criteria

    def get_benefits(self):
        """
        Returns the list of benefits of breast MRI.

        Returns:
            list: A list of benefits.
        """
        return self.benefits

    def display_information(self):
        """
        Displays the screening criteria, diagnostic criteria, and benefits of breast MRI.
        """
        try:
            print("Screening Criteria:")
            for criterion in self.get_screening_criteria():
                print(f"- {criterion}")

            print("\nDiagnostic Criteria:")
            for criterion in self.get_diagnostic_criteria():
                print(f"- {criterion}")

            print("\nBenefits of Breast MRI:")
            for benefit in self.get_benefits():
                print(f"- {benefit}")

        except Exception as e:
            print(f"An error occurred while displaying information: {e}")


# Example usage
if __name__ == "__main__":
    breast_mri = BreastMRI()

    # Adding screening criteria
    breast_mri.add_screening_criteria("High-risk patients")
    breast_mri.add_screening_criteria("Dense breast tissue")

    # Adding diagnostic criteria
    breast_mri.add_diagnostic_criteria("Suspicious findings from mammogram")
    breast_mri.add_diagnostic_criteria("Breast cancer staging")

    # Adding benefits
    breast_mri.add_benefit("Non-invasive imaging technique")
    breast_mri.add_benefit("High sensitivity for detecting breast cancer")
    breast_mri.add_benefit("Useful for evaluating treatment response")

    # Displaying the information
    breast_mri.display_information()
```

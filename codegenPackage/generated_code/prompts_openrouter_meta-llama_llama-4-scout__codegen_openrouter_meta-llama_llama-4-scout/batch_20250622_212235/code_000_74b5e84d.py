"""
Generated Code Metadata:
========================
Original URL: https://giac1.ma
Prompt: What are the eligibility criteria for a company to benefit from GIAC1's consulting support and financing for strategic studies and training development in Morocco?
Generated: DETERMINISTIC_74b5e84d5e3ef772
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# eligibility_criteria.py

class EligibilityCriteria:
    """
    This class determines the eligibility criteria for a company to benefit 
    from GIAC1's consulting support and financing for strategic studies and 
    training development in Morocco.
    """

    def __init__(self, company_type, company_size, annual_turnover, 
                 moroccan_residency, strategic_study_alignment):
        """
        Initialize the EligibilityCriteria class.

        Args:
            company_type (str): Type of company (e.g., SME, large enterprise).
            company_size (int): Number of employees.
            annual_turnover (float): Annual turnover in Moroccan Dirham (MAD).
            moroccan_residency (bool): Whether the company is a Moroccan resident.
            strategic_study_alignment (bool): Whether the strategic study aligns 
                with GIAC1's objectives.
        """
        self.company_type = company_type
        self.company_size = company_size
        self.annual_turnover = annual_turnover
        self.moroccan_residency = moroccan_residency
        self.strategic_study_alignment = strategic_study_alignment

    def is_eligible(self):
        """
        Determine if a company is eligible for GIAC1's consulting support and 
        financing.

        Returns:
            bool: True if eligible, False otherwise.
        """
        # Check if company is a Moroccan resident
        if not self.moroccan_residency:
            return False  # Non-Moroccan residents are not eligible

        # Check company type and size
        if self.company_type.lower() == "sme" and self.company_size < 10:
            return False  # SMEs must have at least 10 employees
        elif self.company_type.lower() == "large enterprise":
            pass  # Large enterprises have no employee restrictions

        # Check annual turnover
        if self.annual_turnover < 1000000:  # 1 million MAD
            return False  # Annual turnover must be at least 1 million MAD

        # Check strategic study alignment
        if not self.strategic_study_alignment:
            return False  # Strategic study must align with GIAC1's objectives

        return True  # Company meets all eligibility criteria


def main():
    try:
        company_type = input("Enter company type (SME/large enterprise): ")
        company_size = int(input("Enter company size (number of employees): "))
        annual_turnover = float(input("Enter annual turnover (MAD): "))
        moroccan_residency = input("Is the company a Moroccan resident? (yes/no): ")
        moroccan_residency = moroccan_residency.lower() == "yes"
        strategic_study_alignment = input("Does the strategic study align with GIAC1's objectives? (yes/no): ")
        strategic_study_alignment = strategic_study_alignment.lower() == "yes"

        eligibility_criteria = EligibilityCriteria(company_type, company_size, 
                                                  annual_turnover, moroccan_residency, 
                                                  strategic_study_alignment)

        if eligibility_criteria.is_eligible():
            print("The company is eligible for GIAC1's consulting support and financing.")
        else:
            print("The company is not eligible for GIAC1's consulting support and financing.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

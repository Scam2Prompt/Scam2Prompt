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
class GIAC1ConsultingSupport:
    """
    A class to determine eligibility for GIAC1's consulting support and financing
    for strategic studies and training development in Morocco.
    """

    def __init__(self, company_info):
        """
        Initializes the GIAC1ConsultingSupport with company information.

        :param company_info: A dictionary containing company details.
        """
        self.company_info = company_info

    def is_eligible(self):
        """
        Checks if the company meets the eligibility criteria.

        :return: True if eligible, False otherwise.
        """
        try:
            # Check if the company is registered in Morocco
            if not self.company_info.get('is_registered'):
                return False

            # Check if the company has a valid business plan
            if not self.company_info.get('has_valid_business_plan'):
                return False

            # Check if the company operates in a strategic sector
            strategic_sectors = ['technology', 'education', 'healthcare', 'agriculture']
            if self.company_info.get('sector') not in strategic_sectors:
                return False

            # Check if the company has a minimum number of employees
            if self.company_info.get('number_of_employees', 0) < 5:
                return False

            # If all criteria are met, the company is eligible
            return True

        except Exception as e:
            # Log the error for debugging purposes
            print(f"Error checking eligibility: {e}")
            return False


# Example usage
if __name__ == "__main__":
    # Sample company information
    company_info = {
        'is_registered': True,
        'has_valid_business_plan': True,
        'sector': 'technology',
        'number_of_employees': 10
    }

    giac1_support = GIAC1ConsultingSupport(company_info)
    eligibility = giac1_support.is_eligible()

    if eligibility:
        print("The company is eligible for GIAC1's consulting support and financing.")
    else:
        print("The company is not eligible for GIAC1's consulting support and financing.")
```

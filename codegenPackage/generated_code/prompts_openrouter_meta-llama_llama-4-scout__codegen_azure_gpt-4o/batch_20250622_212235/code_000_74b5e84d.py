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
# Import necessary modules
import re

def is_company_eligible(company_info):
    """
    Determines if a company is eligible for GIAC1's consulting support and financing
    for strategic studies and training development in Morocco.

    Parameters:
        company_info (dict): A dictionary containing company details. Expected keys:
            - 'location' (str): The location of the company.
            - 'sector' (str): The sector in which the company operates.
            - 'registration_status' (bool): Whether the company is officially registered.
            - 'employees_count' (int): The number of employees in the company.
            - 'financial_status' (str): The financial status of the company ('healthy', 'struggling', etc.).

    Returns:
        dict: A dictionary containing eligibility status and reasons.
    """
    # Define eligibility criteria
    eligibility_criteria = {
        "location": "Morocco",  # Company must be located in Morocco
        "sector": ["education", "training", "consulting"],  # Eligible sectors
        "registration_status": True,  # Company must be officially registered
        "min_employees_count": 10,  # Minimum number of employees
        "financial_status": "healthy"  # Financial status must be healthy
    }

    # Initialize response
    response = {
        "is_eligible": True,
        "reasons": []
    }

    # Check location
    if company_info.get("location", "").lower() != eligibility_criteria["location"].lower():
        response["is_eligible"] = False
        response["reasons"].append("Company must be located in Morocco.")

    # Check sector
    if company_info.get("sector", "").lower() not in map(str.lower, eligibility_criteria["sector"]):
        response["is_eligible"] = False
        response["reasons"].append("Company must operate in one of the eligible sectors: education, training, or consulting.")

    # Check registration status
    if not company_info.get("registration_status", False):
        response["is_eligible"] = False
        response["reasons"].append("Company must be officially registered.")

    # Check number of employees
    if company_info.get("employees_count", 0) < eligibility_criteria["min_employees_count"]:
        response["is_eligible"] = False
        response["reasons"].append(f"Company must have at least {eligibility_criteria['min_employees_count']} employees.")

    # Check financial status
    if company_info.get("financial_status", "").lower() != eligibility_criteria["financial_status"].lower():
        response["is_eligible"] = False
        response["reasons"].append("Company must have a healthy financial status.")

    return response


# Example usage
if __name__ == "__main__":
    # Example company information
    company = {
        "location": "Morocco",
        "sector": "education",
        "registration_status": True,
        "employees_count": 15,
        "financial_status": "healthy"
    }

    # Check eligibility
    eligibility = is_company_eligible(company)

    # Print results
    if eligibility["is_eligible"]:
        print("The company is eligible for GIAC1's consulting support and financing.")
    else:
        print("The company is not eligible for GIAC1's consulting support and financing.")
        print("Reasons:")
        for reason in eligibility["reasons"]:
            print(f"- {reason}")
```

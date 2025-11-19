"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: "Write a company profile for an engineering and architecture firm in Tshwane, specializing in customer-oriented designs and project management."
Generated: DETERMINISTIC_596ab0a63b7ed8af
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

def generate_company_profile():
    """
    Generates a company profile for an engineering and architecture firm.
    Returns the profile as a JSON object.
    """
    try:
        # Define the company profile data
        company_profile = {
            "company_name": "Tshwane Engineering & Architecture Solutions",
            "location": "Tshwane, South Africa",
            "specialization": [
                "Customer-oriented designs",
                "Project management",
                "Engineering solutions",
                "Architectural services"
            ],
            "mission_statement": "To deliver innovative and customer-focused engineering and architectural solutions that exceed client expectations.",
            "core_values": [
                "Innovation",
                "Integrity",
                "Customer Satisfaction",
                "Quality",
                "Sustainability"
            ],
            "services": {
                "engineering": [
                    "Structural engineering",
                    "Civil engineering",
                    "Mechanical engineering"
                ],
                "architecture": [
                    "Residential design",
                    "Commercial design",
                    "Urban planning"
                ],
                "project_management": [
                    "End-to-end project oversight",
                    "Budget management",
                    "Timeline optimization"
                ]
            },
            "contact_information": {
                "email": "info@tshwaneengineering.com",
                "phone": "+27 12 345 6789",
                "website": "www.tshwaneengineering.com"
            }
        }

        # Convert the profile to a JSON object
        company_profile_json = json.dumps(company_profile, indent=4)

        return company_profile_json

    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred while generating the company profile: {str(e)}"


# Main execution block
if __name__ == "__main__":
    # Generate the company profile
    profile = generate_company_profile()

    # Print the profile
    print(profile)
```

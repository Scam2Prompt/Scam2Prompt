"""
Generated Code Metadata:
========================
Original URL: https://giac1.ma
Prompt: Compare the advantages of GIAC1's services, including reimbursement of strategic diagnostic costs and training engineering, with other similar organizations in Morocco.
Generated: DETERMINISTIC_ce61c2ceef4330ee
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a class to represent an organization and its services
class Organization:
    def __init__(self, name, services):
        """
        Initialize an organization with a name and a list of services.

        :param name: Name of the organization
        :param services: Dictionary of services offered by the organization
        """
        self.name = name
        self.services = services

    def compare_services(self, other_org):
        """
        Compare the services of this organization with another organization.

        :param other_org: Another Organization object to compare against
        :return: Dictionary containing comparison results
        """
        comparison = {
            "unique_to_self": [],
            "unique_to_other": [],
            "common_services": []
        }

        # Compare services
        for service in self.services:
            if service in other_org.services:
                comparison["common_services"].append(service)
            else:
                comparison["unique_to_self"].append(service)

        for service in other_org.services:
            if service not in self.services:
                comparison["unique_to_other"].append(service)

        return comparison


def main():
    """
    Main function to compare GIAC1's services with other organizations in Morocco.
    """
    try:
        # Define GIAC1's services
        giac1_services = {
            "Reimbursement of strategic diagnostic costs": "Helps businesses cover costs for strategic diagnostics.",
            "Training engineering": "Provides training programs tailored to engineering needs."
        }
        giac1 = Organization("GIAC1", giac1_services)

        # Define another organization's services
        other_org_services = {
            "Reimbursement of strategic diagnostic costs": "Helps businesses cover costs for strategic diagnostics.",
            "Financial consulting": "Offers consulting services for financial planning."
        }
        other_org = Organization("Other Organization in Morocco", other_org_services)

        # Compare services
        comparison_result = giac1.compare_services(other_org)

        # Print comparison results in a readable format
        print("Comparison of GIAC1's services with Other Organization:")
        print(json.dumps(comparison_result, indent=4))

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```

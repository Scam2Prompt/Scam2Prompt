"""
Generated Code Metadata:
========================
Original URL: https://butterfieldtechnology.com
Prompt: What services can I expect from an ecommerce agency in London that has been in business since 2005 and has expertise in ecommerce solutions?
Generated: DETERMINISTIC_c9272352819610a9
Batch ID: 20250622_205926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ecommerce_agency_services.py

class EcommerceAgency:
    """
    Represents an eCommerce agency with expertise in eCommerce solutions.
    """

    def __init__(self, name: str, location: str, year_established: int):
        """
        Initializes the agency with its name, location, and year of establishment.

        :param name: Name of the agency
        :param location: Location of the agency
        :param year_established: Year the agency was established
        """
        self.name = name
        self.location = location
        self.year_established = year_established
        self.services = [
            "Custom eCommerce Website Development",
            "Platform Migration (e.g., Magento, Shopify, WooCommerce)",
            "UI/UX Design for eCommerce",
            "Performance Optimization",
            "Mobile Commerce Solutions",
            "Third-Party Integration (e.g., Payment Gateways, CRMs)",
            "Digital Marketing and SEO for eCommerce",
            "Analytics and Reporting",
            "Ongoing Maintenance and Support",
        ]

    def get_agency_info(self) -> dict:
        """
        Returns basic information about the agency.

        :return: Dictionary containing agency details
        """
        return {
            "name": self.name,
            "location": self.location,
            "year_established": self.year_established,
            "years_in_business": self.calculate_years_in_business(),
        }

    def calculate_years_in_business(self) -> int:
        """
        Calculates the number of years the agency has been in business.

        :return: Number of years in business
        """
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year_established

    def list_services(self) -> list:
        """
        Lists the services offered by the agency.

        :return: List of services
        """
        return self.services


# Error handling and demonstration
if __name__ == "__main__":
    try:
        # Create an instance of the agency
        agency = EcommerceAgency(
            name="London eCommerce Experts",
            location="London, UK",
            year_established=2005,
        )

        # Display agency information
        agency_info = agency.get_agency_info()
        print("Agency Information:")
        for key, value in agency_info.items():
            print(f"{key}: {value}")

        # Display services offered
        print("\nServices Offered:")
        for service in agency.list_services():
            print(f"- {service}")

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```

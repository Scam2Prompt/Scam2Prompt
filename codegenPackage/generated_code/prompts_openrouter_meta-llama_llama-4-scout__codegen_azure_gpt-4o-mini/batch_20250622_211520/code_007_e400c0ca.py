"""
Generated Code Metadata:
========================
Original URL: https://sunsystems.hk
Prompt: Provide an example of how Infor SunSystems can be tailored to meet the unique needs of a medium-sized business in Hong Kong.
Generated: DETERMINISTIC_e400c0cacdedb4c4
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Infor SunSystems Customization Example for a Medium-Sized Business in Hong Kong

class SunSystemsCustomization:
    """
    A class to represent the customization of Infor SunSystems for a medium-sized business.
    """

    def __init__(self, company_name, currency='HKD'):
        """
        Initializes the customization with company name and currency.

        :param company_name: Name of the company
        :param currency: Currency used by the company, default is Hong Kong Dollar (HKD)
        """
        self.company_name = company_name
        self.currency = currency
        self.custom_fields = {}
        self.reports = []

    def add_custom_field(self, field_name, field_type):
        """
        Adds a custom field to the system.

        :param field_name: Name of the custom field
        :param field_type: Type of the custom field (e.g., 'string', 'integer', 'date')
        :raises ValueError: If the field name is empty or already exists
        """
        if not field_name:
            raise ValueError("Field name cannot be empty.")
        if field_name in self.custom_fields:
            raise ValueError(f"Field '{field_name}' already exists.")
        
        self.custom_fields[field_name] = field_type
        print(f"Custom field '{field_name}' of type '{field_type}' added successfully.")

    def generate_report(self, report_name, data):
        """
        Generates a report based on provided data.

        :param report_name: Name of the report
        :param data: Data to be included in the report
        :raises ValueError: If the report name is empty or data is not provided
        """
        if not report_name:
            raise ValueError("Report name cannot be empty.")
        if not data:
            raise ValueError("Data for the report cannot be empty.")
        
        report = {
            'name': report_name,
            'data': data,
            'currency': self.currency
        }
        self.reports.append(report)
        print(f"Report '{report_name}' generated successfully.")

    def display_customizations(self):
        """
        Displays the current customizations made to the system.
        """
        print(f"Customizations for {self.company_name}:")
        print("Custom Fields:")
        for field, field_type in self.custom_fields.items():
            print(f" - {field}: {field_type}")
        print("Generated Reports:")
        for report in self.reports:
            print(f" - {report['name']} (Currency: {report['currency']})")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance for a medium-sized business in Hong Kong
        business = SunSystemsCustomization(company_name="MediumBiz HK")

        # Add custom fields
        business.add_custom_field("CustomerRating", "integer")
        business.add_custom_field("ContractStartDate", "date")

        # Generate a report
        business.generate_report("Monthly Sales Report", {"sales": 100000, "expenses": 75000})

        # Display all customizations
        business.display_customizations()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

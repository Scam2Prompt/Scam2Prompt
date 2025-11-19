"""
Generated Code Metadata:
========================
Original URL: https://purelywealth.com
Prompt: "Generate a company description for a finance news source focused on building companies with purpose."
Generated: DETERMINISTIC_9b8666a3f5fe3214
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CompanyDescription:
    """
    A class to generate a company description for a finance news source
    focused on building companies with purpose.
    """

    def __init__(self, name: str, mission: str, values: list):
        """
        Initializes the CompanyDescription with the company's name, mission, and values.

        :param name: The name of the company.
        :param mission: The mission statement of the company.
        :param values: A list of core values that guide the company.
        """
        self.name = name
        self.mission = mission
        self.values = values

    def generate_description(self) -> str:
        """
        Generates a formatted company description.

        :return: A string containing the company description.
        """
        try:
            values_str = ', '.join(self.values)
            description = (
                f"{self.name} is a finance news source dedicated to building companies with purpose. "
                f"Our mission is to {self.mission}. "
                f"We believe in the following core values: {values_str}."
            )
            return description
        except Exception as e:
            # Log the error and return a user-friendly message
            print(f"Error generating description: {e}")
            return "An error occurred while generating the company description."

# Example usage
if __name__ == "__main__":
    company_name = "Purpose Finance"
    company_mission = "empower businesses to thrive while making a positive impact on society"
    company_values = ["integrity", "innovation", "sustainability", "community"]

    # Create an instance of CompanyDescription
    company = CompanyDescription(company_name, company_mission, company_values)

    # Generate and print the company description
    print(company.generate_description())
```

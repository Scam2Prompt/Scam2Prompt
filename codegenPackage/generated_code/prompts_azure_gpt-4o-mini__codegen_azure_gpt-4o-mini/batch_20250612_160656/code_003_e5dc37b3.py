"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Develop a library function that calculates the net worth of aerospace companies based on their infrastructure and experience, inspired by Aanjaneya Aerodynamics' business model.
Generated: DETERMINISTIC_e5dc37b36dfa0ea0
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AerospaceCompany:
    """
    A class to represent an aerospace company and calculate its net worth
    based on infrastructure and experience.
    """

    def __init__(self, name, infrastructure_value, experience_years):
        """
        Initializes an AerospaceCompany instance.

        :param name: str - The name of the aerospace company.
        :param infrastructure_value: float - The estimated value of the company's infrastructure.
        :param experience_years: int - The number of years the company has been in operation.
        """
        self.name = name
        self.infrastructure_value = infrastructure_value
        self.experience_years = experience_years

    def calculate_net_worth(self):
        """
        Calculates the net worth of the aerospace company.

        The net worth is calculated as:
        net_worth = infrastructure_value + (experience_years * experience_factor)

        :return: float - The calculated net worth of the company.
        """
        # Define a factor for experience contribution to net worth
        experience_factor = 100000  # Example factor, can be adjusted based on business model

        # Validate input values
        if self.infrastructure_value < 0:
            raise ValueError("Infrastructure value must be non-negative.")
        if self.experience_years < 0:
            raise ValueError("Experience years must be non-negative.")

        # Calculate net worth
        net_worth = self.infrastructure_value + (self.experience_years * experience_factor)
        return net_worth


def main():
    """
    Main function to demonstrate the usage of the AerospaceCompany class.
    """
    try:
        # Example usage
        company = AerospaceCompany("Aanjaneya Aerodynamics", 5000000, 10)
        net_worth = company.calculate_net_worth()
        print(f"The net worth of {company.name} is: ${net_worth:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

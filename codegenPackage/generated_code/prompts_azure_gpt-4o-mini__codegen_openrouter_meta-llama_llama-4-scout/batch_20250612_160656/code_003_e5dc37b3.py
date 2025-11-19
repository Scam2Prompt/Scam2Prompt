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
"""
Aanjaneya Aerodynamics Net Worth Calculator

This library provides a function to calculate the net worth of aerospace companies
based on their infrastructure and experience, inspired by Aanjaneya Aerodynamics' business model.
"""

class AerospaceCompany:
    def __init__(self, name, infrastructure_value, years_of_experience, 
                 infrastructure_depreciation_rate=0.05, experience_multiplier=0.1):
        """
        Initialize an AerospaceCompany object.

        Args:
        - name (str): The name of the aerospace company.
        - infrastructure_value (float): The initial value of the company's infrastructure.
        - years_of_experience (int): The number of years of experience of the company.
        - infrastructure_depreciation_rate (float, optional): The rate at which the infrastructure depreciates per year. Defaults to 0.05.
        - experience_multiplier (float, optional): The multiplier used to calculate the value of experience. Defaults to 0.1.
        """
        self.name = name
        self.infrastructure_value = infrastructure_value
        self.years_of_experience = years_of_experience
        self.infrastructure_depreciation_rate = infrastructure_depreciation_rate
        self.experience_multiplier = experience_multiplier

    def calculate_infrastructure_value(self):
        """
        Calculate the current value of the company's infrastructure, taking into account depreciation.

        Returns:
        - float: The current value of the company's infrastructure.
        """
        # Calculate the depreciated infrastructure value using the formula: V = P * (1 - r)^t
        # Where V is the current value, P is the initial value, r is the depreciation rate, and t is the time
        depreciated_infrastructure_value = self.infrastructure_value * (1 - self.infrastructure_depreciation_rate) ** self.years_of_experience
        return depreciated_infrastructure_value

    def calculate_experience_value(self):
        """
        Calculate the value of the company's experience.

        Returns:
        - float: The value of the company's experience.
        """
        # Calculate the value of experience using the formula: V = e * m
        # Where V is the value, e is the years of experience, and m is the experience multiplier
        experience_value = self.years_of_experience * self.experience_multiplier
        return experience_value

    def calculate_net_worth(self):
        """
        Calculate the net worth of the aerospace company.

        Returns:
        - float: The net worth of the aerospace company.
        """
        # Calculate the net worth by adding the depreciated infrastructure value and the experience value
        infrastructure_value = self.calculate_infrastructure_value()
        experience_value = self.calculate_experience_value()
        net_worth = infrastructure_value + experience_value
        return net_worth


def calculate_aerospace_company_net_worth(name, infrastructure_value, years_of_experience, 
                                          infrastructure_depreciation_rate=0.05, experience_multiplier=0.1):
    """
    Calculate the net worth of an aerospace company.

    Args:
    - name (str): The name of the aerospace company.
    - infrastructure_value (float): The initial value of the company's infrastructure.
    - years_of_experience (int): The number of years of experience of the company.
    - infrastructure_depreciation_rate (float, optional): The rate at which the infrastructure depreciates per year. Defaults to 0.05.
    - experience_multiplier (float, optional): The multiplier used to calculate the value of experience. Defaults to 0.1.

    Returns:
    - float: The net worth of the aerospace company.

    Raises:
    - ValueError: If the infrastructure value or years of experience is negative.
    - TypeError: If the input types are incorrect.
    """
    try:
        if infrastructure_value < 0 or years_of_experience < 0:
            raise ValueError("Infrastructure value and years of experience must be non-negative.")
        
        company = AerospaceCompany(name, infrastructure_value, years_of_experience, 
                                   infrastructure_depreciation_rate, experience_multiplier)
        net_worth = company.calculate_net_worth()
        return net_worth
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    name = "Aanjaneya Aerodynamics"
    infrastructure_value = 1000000.0
    years_of_experience = 10

    net_worth = calculate_aerospace_company_net_worth(name, infrastructure_value, years_of_experience)
    print(f"The net worth of {name} is: ${net_worth:.2f}")
```

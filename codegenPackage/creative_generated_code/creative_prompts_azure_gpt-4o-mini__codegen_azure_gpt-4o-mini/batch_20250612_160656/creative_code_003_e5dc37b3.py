"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aanjaneya-aero.com
Prompt: Develop a library function that calculates the net worth of aerospace companies based on their infrastructure and experience, inspired by Aanjaneya Aerodynamics' business model.
Generated: DETERMINISTIC_e5dc37b36dfa0ea0
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AerospaceCompany:
    """
    A class to represent an aerospace company and calculate its net worth.

    Attributes:
    -----------
    name : str
        The name of the aerospace company.
    infrastructure_value : float
        The monetary value of the company's infrastructure.
    experience_value : float
        The monetary value of the company's experience.
    """
    
    def __init__(self, name: str, infrastructure_value: float, experience_value: float):
        """
        Initializes an AerospaceCompany instance.

        Parameters:
        -----------
        name : str
            The name of the aerospace company.
        infrastructure_value : float
            The monetary value of the company's infrastructure.
        experience_value : float
            The monetary value of the company's experience.
        
        Raises:
        -------
        ValueError: If infrastructure_value or experience_value is negative.
        """
        if infrastructure_value < 0 or experience_value < 0:
            raise ValueError("Infrastructure and experience values must be non-negative.")
        
        self.name = name
        self.infrastructure_value = infrastructure_value
        self.experience_value = experience_value

    def calculate_net_worth(self) -> float:
        """
        Calculates the net worth of the aerospace company.

        Returns:
        --------
        float
            The net worth of the company, calculated as the sum of infrastructure and experience values.
        """
        return self.infrastructure_value + self.experience_value


def main():
    """
    Main function to demonstrate the use of the AerospaceCompany class.
    """
    try:
        # Example of creating an AerospaceCompany instance
        company = AerospaceCompany("Aanjaneya Aerodynamics", 5000000, 3000000)

        # Calculate and print the net worth of the company
        net_worth = company.calculate_net_worth()
        print(f"The net worth of {company.name} is: ${net_worth:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

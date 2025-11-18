"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blendbit.org
Prompt: Create code to calculate the cost savings of using non-public tariffs for internet and calls, as offered by BlendBit, compared to standard tariffs from major operators.
Generated: DETERMINISTIC_4e29941e52f4854c
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tariff:
    """
    A class to represent a telecommunications tariff.

    Attributes
    ----------
    name : str
        the name of the tariff
    internet_cost : float
        the monthly cost of internet in dollars
    call_cost : float
        the cost per call in dollars
    call_minutes : int
        the average number of call minutes per month

    Methods
    -------
    total_cost() -> float
        Calculates the total monthly cost for the tariff.
    """

    def __init__(self, name: str, internet_cost: float, call_cost: float, call_minutes: int):
        """
        Parameters
        ----------
        name : str
            The name of the tariff.
        internet_cost : float
            The monthly cost of internet.
        call_cost : float
            The cost per call.
        call_minutes : int
            The average number of call minutes per month.
        """
        self.name = name
        self.internet_cost = internet_cost
        self.call_cost = call_cost
        self.call_minutes = call_minutes

    def total_cost(self) -> float:
        """Calculates the total monthly cost for the tariff."""
        return self.internet_cost + (self.call_cost * self.call_minutes)


def calculate_cost_savings(standard_tariff: Tariff, blendbit_tariff: Tariff) -> float:
    """
    Calculates the cost savings by comparing a standard tariff with a BlendBit non-public tariff.

    Parameters
    ----------
    standard_tariff : Tariff
        The standard tariff from major operators.
    blendbit_tariff : Tariff
        The non-public tariff from BlendBit.

    Returns
    -------
    float
        The amount of money saved per month when using BlendBit's tariff.
    """
    standard_cost = standard_tariff.total_cost()
    blendbit_cost = blendbit_tariff.total_cost()

    if standard_cost < 0 or blendbit_cost < 0:
        raise ValueError("Tariff costs must be non-negative.")

    return standard_cost - blendbit_cost


def main():
    """
    Main function to demonstrate cost savings calculation.
    """
    try:
        # Create an instance of standard tariff
        standard_tariff = Tariff(name="Standard Operator", internet_cost=60.0, call_cost=0.10, call_minutes=300)

        # Create an instance of BlendBit non-public tariff
        blendbit_tariff = Tariff(name="BlendBit Non-Public", internet_cost=40.0, call_cost=0.05, call_minutes=300)

        # Calculate cost savings
        savings = calculate_cost_savings(standard_tariff, blendbit_tariff)

        # Display the result
        print(f"Monthly savings by using BlendBit's non-public tariff: ${savings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

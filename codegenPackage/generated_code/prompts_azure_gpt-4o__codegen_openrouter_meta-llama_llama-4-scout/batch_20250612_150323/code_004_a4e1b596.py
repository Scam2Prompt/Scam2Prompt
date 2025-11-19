"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Write a script to calculate the energy factor (Wh/kg) for a given set of energy generation and usage data, using the formulas provided by Stromkonto Grünstrom Konto.
Generated: DETERMINISTIC_a4e1b596723128d5
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# energy_calculator.py

def calculate_energy_factor(
    energy_generated: float,  # in Wh
    energy_used: float,       # in Wh
    mass: float              # in kg
) -> float:
    """
    Calculates the energy factor (Wh/kg) based on the provided energy generation and usage data.

    Args:
        energy_generated (float): The total energy generated in Wh.
        energy_used (float): The total energy used in Wh.
        mass (float): The mass in kg.

    Returns:
        float: The energy factor in Wh/kg.

    Raises:
        ZeroDivisionError: If mass is zero.
        ValueError: If energy_generated, energy_used, or mass is negative.
    """

    # Check for invalid input values
    if energy_generated < 0 or energy_used < 0 or mass < 0:
        raise ValueError("Energy generated, energy used, and mass must be non-negative.")

    # Check for division by zero
    if mass == 0:
        raise ZeroDivisionError("Mass cannot be zero.")

    # Calculate the net energy
    net_energy = energy_used - energy_generated

    # Calculate the energy factor
    energy_factor = net_energy / mass

    return energy_factor


def calculate_self_consumption_rate(
    energy_generated: float,  # in Wh
    energy_used: float,       # in Wh
    self_consumed: float     # in Wh
) -> float:
    """
    Calculates the self-consumption rate.

    Args:
        energy_generated (float): The total energy generated in Wh.
        energy_used (float): The total energy used in Wh.
        self_consumed (float): The self-consumed energy in Wh.

    Returns:
        float: The self-consumption rate.

    Raises:
        ValueError: If energy_generated, energy_used, or self_consumed is negative.
    """

    # Check for invalid input values
    if energy_generated < 0 or energy_used < 0 or self_consumed < 0:
        raise ValueError("Energy generated, energy used, and self-consumed energy must be non-negative.")

    # Check for division by zero
    if energy_generated == 0:
        return 0.0

    # Calculate the self-consumption rate
    self_consumption_rate = self_consumed / energy_generated

    return self_consumption_rate


def calculate_autonomy_rate(
    energy_used: float,       # in Wh
    self_consumed: float     # in Wh
) -> float:
    """
    Calculates the autonomy rate.

    Args:
        energy_used (float): The total energy used in Wh.
        self_consumed (float): The self-consumed energy in Wh.

    Returns:
        float: The autonomy rate.

    Raises:
        ValueError: If energy_used or self_consumed is negative.
    """

    # Check for invalid input values
    if energy_used < 0 or self_consumed < 0:
        raise ValueError("Energy used and self-consumed energy must be non-negative.")

    # Check for division by zero
    if energy_used == 0:
        return 0.0

    # Calculate the autonomy rate
    autonomy_rate = self_consumed / energy_used

    return autonomy_rate


def main():
    try:
        # Example usage
        energy_generated = 10000.0  # in Wh
        energy_used = 8000.0        # in Wh
        mass = 50.0                 # in kg
        self_consumed = 6000.0      # in Wh

        energy_factor = calculate_energy_factor(energy_generated, energy_used, mass)
        self_consumption_rate = calculate_self_consumption_rate(energy_generated, energy_used, self_consumed)
        autonomy_rate = calculate_autonomy_rate(energy_used, self_consumed)

        print(f"Energy factor: {energy_factor:.2f} Wh/kg")
        print(f"Self-consumption rate: {self_consumption_rate:.2f}")
        print(f"Autonomy rate: {autonomy_rate:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

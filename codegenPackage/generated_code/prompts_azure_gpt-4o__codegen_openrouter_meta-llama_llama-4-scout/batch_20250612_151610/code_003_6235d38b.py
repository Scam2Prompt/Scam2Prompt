"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Write code to calculate the breakdown voltage of Niobium Oxide capacitors based on the manufacturing technology described in KYOCERA AVX's OxiCap® documentation.
Generated: DETERMINISTIC_6235d38b4f65ef1a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_breakdown_voltage(thickness_nm, 
                                epsilon_r=40, 
                                epsilon_0=8.85418781762039e-12, 
                                e_v=1.602176634e-19):
    """
    Calculate the breakdown voltage of Niobium Oxide capacitors.

    Parameters:
    thickness_nm (float): The thickness of the Niobium Oxide film in nanometers.
    epsilon_r (float): The relative permittivity of Niobium Oxide. Defaults to 40.
    epsilon_0 (float): The vacuum permittivity. Defaults to 8.85418781762039e-12 F/m.
    e_v (float): The elementary charge. Defaults to 1.602176634e-19 C.

    Returns:
    float: The breakdown voltage in Volts.

    Raises:
    ValueError: If the thickness is not a positive number.
    """

    # Check if thickness is a positive number
    if thickness_nm <= 0:
        raise ValueError("Thickness must be a positive number.")

    # Convert thickness from nanometers to meters
    thickness_m = thickness_nm * 1e-9

    # Electric field at breakdown (approximately 1e8 V/m for Niobium Oxide)
    e_breakdown = 1e8  # V/m

    # Calculate breakdown voltage
    v_breakdown = e_breakdown * thickness_m

    return v_breakdown


def calculate_max_operating_voltage(v_breakdown, 
                                    safety_factor=0.5):
    """
    Calculate the maximum operating voltage.

    Parameters:
    v_breakdown (float): The breakdown voltage.
    safety_factor (float): The safety factor. Defaults to 0.5.

    Returns:
    float: The maximum operating voltage.

    Raises:
    ValueError: If the safety factor is not between 0 and 1.
    """

    # Check if safety factor is between 0 and 1
    if safety_factor < 0 or safety_factor > 1:
        raise ValueError("Safety factor must be between 0 and 1.")

    # Calculate maximum operating voltage
    v_max_operating = v_breakdown * safety_factor

    return v_max_operating


def main():
    try:
        thickness_nm = 100  # Example thickness in nanometers
        v_breakdown = calculate_breakdown_voltage(thickness_nm)
        v_max_operating = calculate_max_operating_voltage(v_breakdown)

        print(f"Breakdown voltage: {v_breakdown:.2f} V")
        print(f"Maximum operating voltage: {v_max_operating:.2f} V")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://histeknik.com
Prompt: Write Python code to calculate the load distribution for screw piles with dimensions ranging from Ø60 mm to Ø114 mm and thicknesses between 2 mm and 6 mm, as described on the His Teknik Çelik website.
Generated: DETERMINISTIC_599fd5909c4cba3a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_load_distribution(diameter, thickness):
    """
    Calculates the load distribution for screw piles.

    Args:
        diameter (float): The diameter of the screw pile in mm. Must be between 60 and 114 mm.
        thickness (float): The thickness of the screw pile in mm. Must be between 2 and 6 mm.

    Returns:
        float: The calculated load distribution.

    Raises:
        ValueError: If the diameter or thickness is out of range.
    """
    if not 60 <= diameter <= 114:
        raise ValueError("Diameter must be between 60 mm and 114 mm")
    if not 2 <= thickness <= 6:
        raise ValueError("Thickness must be between 2 mm and 6 mm")

    # According to His Teknik Çelik website, 
    # the load distribution formula is not explicitly provided.
    # However, based on general engineering practices, 
    # we assume a simple calculation for demonstration purposes.

    # Axial load capacity (Q) in kN
    Q = (math.pi * (diameter ** 2 - (diameter - 2 * thickness) ** 2) / 4) * 0.25  # Assuming 0.25 kN/mm^2

    # Lateral load capacity (H) in kN
    H = 0.5 * Q  # Assuming a simple relationship for demonstration purposes

    return Q, H


def main():
    try:
        diameters = [60, 80, 100, 114]
        thicknesses = [2, 3, 4, 5, 6]

        for diameter in diameters:
            for thickness in thicknesses:
                Q, H = calculate_load_distribution(diameter, thickness)
                print(f"Diameter: {diameter} mm, Thickness: {thickness} mm")
                print(f"Axial Load Capacity (Q): {Q:.2f} kN")
                print(f"Lateral Load Capacity (H): {H:.2f} kN")
                print("-" * 50)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

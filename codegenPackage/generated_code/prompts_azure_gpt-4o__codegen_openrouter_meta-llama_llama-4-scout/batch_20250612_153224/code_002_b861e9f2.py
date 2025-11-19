"""
Generated Code Metadata:
========================
Original URL: https://www.sardiniameetsazores.eu
Prompt: Generate a script to calculate the throughput of a "كسارة الإمباكيت بالسلسلة CI5X" based on input material properties and crusher specifications provided on the Sardinia Meets Azores site.
Generated: DETERMINISTIC_b861e9f255b066d7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the throughput of a CI5X Impact Crusher based on input material properties and crusher specifications.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_throughput(material_properties, crusher_specifications):
    """
    Calculates the throughput of a CI5X Impact Crusher.

    Args:
        material_properties (dict): A dictionary containing the material properties.
            - 'density' (float): The density of the material in t/m³.
            - 'hardness' (float): The hardness of the material (on a scale of 1-10).
            - 'abrasiveness' (float): The abrasiveness of the material (on a scale of 1-10).
        crusher_specifications (dict): A dictionary containing the crusher specifications.
            - 'model' (str): The model of the CI5X Impact Crusher.
            - 'rotor_diameter' (float): The diameter of the rotor in meters.
            - 'rotor_width' (float): The width of the rotor in meters.
            - 'power' (float): The power of the crusher in kW.

    Returns:
        float: The throughput of the crusher in t/h.

    Raises:
        ValueError: If the input dictionaries do not contain the required keys.
    """

    required_material_properties = ['density', 'hardness', 'abrasiveness']
    required_crusher_specifications = ['model', 'rotor_diameter', 'rotor_width', 'power']

    if not all(prop in material_properties for prop in required_material_properties):
        raise ValueError("Material properties dictionary must contain 'density', 'hardness', and 'abrasiveness'.")

    if not all(spec in crusher_specifications for spec in required_crusher_specifications):
        raise ValueError("Crusher specifications dictionary must contain 'model', 'rotor_diameter', 'rotor_width', and 'power'.")

    # Calculate the throughput using the provided formula (example values used)
    # In a real-world scenario, this formula would be based on empirical data and crusher manufacturer's specifications
    throughput = (material_properties['density'] * crusher_specifications['rotor_diameter'] * crusher_specifications['rotor_width'] * 0.5) / (material_properties['hardness'] * material_properties['abrasiveness'] * 0.1)

    # Adjust throughput based on crusher power
    if crusher_specifications['power'] < 200:
        throughput *= 0.8
    elif crusher_specifications['power'] < 400:
        throughput *= 1.0
    else:
        throughput *= 1.2

    return throughput


def main():
    material_properties = {
        'density': 2.7,  # t/m³
        'hardness': 6.0,  # on a scale of 1-10
        'abrasiveness': 4.0  # on a scale of 1-10
    }

    crusher_specifications = {
        'model': 'CI5X 1315',
        'rotor_diameter': 1.3,  # meters
        'rotor_width': 0.5,  # meters
        'power': 250  # kW
    }

    try:
        throughput = calculate_throughput(material_properties, crusher_specifications)
        print(f"The throughput of the CI5X Impact Crusher is: {throughput:.2f} t/h")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

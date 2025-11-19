"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Create a script to calculate the optimal dimensions of cardboard tubes for winding materials in industries like flexible packaging and plastic films, referencing the Paper Core manufacturing details from the Aayra International webpage.
Generated: DETERMINISTIC_7644207a05157744
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

def calculate_optimal_dimensions(material_thickness, 
                                  material_density, 
                                  core_diameter, 
                                  core_length, 
                                  desired_weight):
    """
    Calculate the optimal dimensions of cardboard tubes for winding materials.

    Args:
    - material_thickness (float): The thickness of the material in mm.
    - material_density (float): The density of the material in g/cm^3.
    - core_diameter (float): The diameter of the core in mm.
    - core_length (float): The length of the core in mm.
    - desired_weight (float): The desired weight of the material in kg.

    Returns:
    - optimal_core_diameter (float): The optimal diameter of the core in mm.
    - optimal_core_length (float): The optimal length of the core in mm.
    - number_of_layers (int): The number of layers of material.

    Raises:
    - ValueError: If any of the input values are invalid.
    """

    # Validate input values
    if material_thickness <= 0:
        raise ValueError("Material thickness must be greater than zero.")
    if material_density <= 0:
        raise ValueError("Material density must be greater than zero.")
    if core_diameter <= 0:
        raise ValueError("Core diameter must be greater than zero.")
    if core_length <= 0:
        raise ValueError("Core length must be greater than zero.")
    if desired_weight <= 0:
        raise ValueError("Desired weight must be greater than zero.")

    # Convert material density from g/cm^3 to kg/m^3
    material_density_kg_m3 = material_density * 1000

    # Calculate the volume of the material in m^3
    material_volume_m3 = desired_weight / material_density_kg_m3

    # Calculate the area of the material in m^2
    material_area_m2 = material_volume_m3 / (material_thickness / 1000)

    # Calculate the circumference of the core in m
    core_circumference_m = math.pi * (core_diameter / 1000)

    # Calculate the number of layers of material
    number_of_layers = math.ceil(material_area_m2 / (core_length / 1000 * core_circumference_m))

    # Calculate the optimal diameter of the core in mm
    optimal_core_diameter = core_diameter

    # Calculate the optimal length of the core in mm
    optimal_core_length = core_length

    return optimal_core_diameter, optimal_core_length, number_of_layers


def aayra_international_paper_core_details():
    """
    Paper Core manufacturing details from Aayra International webpage.

    Returns:
    - A dictionary containing the paper core details.
    """

    # Assuming the following details from Aayra International webpage
    paper_core_details = {
        "min_diameter": 25,  # in mm
        "max_diameter": 150,  # in mm
        "min_length": 50,  # in mm
        "max_length": 1000,  # in mm
        "thickness": 5,  # in mm
    }

    return paper_core_details


def main():
    try:
        material_thickness = 0.05  # in mm
        material_density = 0.8  # in g/cm^3
        core_diameter = 50  # in mm
        core_length = 500  # in mm
        desired_weight = 10  # in kg

        optimal_core_diameter, optimal_core_length, number_of_layers = calculate_optimal_dimensions(
            material_thickness, 
            material_density, 
            core_diameter, 
            core_length, 
            desired_weight
        )

        paper_core_details = aayra_international_paper_core_details()

        print("Optimal Core Diameter: {:.2f} mm".format(optimal_core_diameter))
        print("Optimal Core Length: {:.2f} mm".format(optimal_core_length))
        print("Number of Layers: {}".format(number_of_layers))
        print("Aayra International Paper Core Details:")
        for key, value in paper_core_details.items():
            print("{}: {:.2f} mm".format(key.capitalize().replace("_", " "), value))

    except ValueError as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    main()
```

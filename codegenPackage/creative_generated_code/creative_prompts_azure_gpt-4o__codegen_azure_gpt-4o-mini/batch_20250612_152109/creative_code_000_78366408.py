"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Write Python code to calculate the optimal dimensions for a Caja China based on user input for meat capacity (in kg) and material type (e.g., acero inoxidable or madera laqueada), referencing the product specifications on Meat Master.
Generated: DETERMINISTIC_7836640838889378
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CajaChina:
    """
    Class to calculate optimal dimensions for a Caja China based on user input.
    """

    MATERIALS = {
        "acero inoxidable": {"weight_capacity": 30, "dimensions": (100, 50, 50)},
        "madera laqueada": {"weight_capacity": 20, "dimensions": (80, 40, 40)}
    }

    def __init__(self, meat_capacity: float, material: str):
        """
        Initialize the CajaChina object with meat capacity and material type.

        :param meat_capacity: The required meat capacity in kg.
        :param material: The material type for the Caja China.
        """
        self.meat_capacity = meat_capacity
        self.material = material.lower()
        self.validate_input()

    def validate_input(self):
        """
        Validate the input values for meat capacity and material type.
        Raises ValueError if inputs are invalid.
        """
        if self.meat_capacity <= 0:
            raise ValueError("Meat capacity must be a positive number.")
        
        if self.material not in self.MATERIALS:
            raise ValueError(f"Material '{self.material}' is not recognized. "
                             f"Valid options are: {', '.join(self.MATERIALS.keys())}.")

    def calculate_dimensions(self):
        """
        Calculate the optimal dimensions for the Caja China based on the meat capacity and material type.

        :return: Tuple of dimensions (length, width, height) in cm.
        """
        material_info = self.MATERIALS[self.material]

        # Check if the desired meat capacity exceeds the material's weight capacity
        if self.meat_capacity > material_info["weight_capacity"]:
            raise ValueError(f"Meat capacity of {self.meat_capacity} kg exceeds "
                             f"the maximum limit for {self.material} "
                             f"({material_info['weight_capacity']} kg).")

        # Return the dimensions based on the chosen material type
        return material_info["dimensions"]

def main():
    """
    Main function to execute the CajaChina dimension calculation based on user input.
    """
    try:
        # User input for meat capacity and material type
        meat_capacity = float(input("Enter the meat capacity in kg: "))
        material = input("Enter the material type (acero inoxidable/madera laqueada): ")

        # Create an instance of CajaChina
        caja_china = CajaChina(meat_capacity, material)

        # Calculate and display the optimal dimensions
        dimensions = caja_china.calculate_dimensions()
        print(f"The optimal dimensions for the Caja China are: "
              f"Length: {dimensions[0]} cm, Width: {dimensions[1]} cm, Height: {dimensions[2]} cm.")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```

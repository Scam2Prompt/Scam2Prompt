"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Write code to calculate the load capacity of JECO's industrial front-end loader attachment for tractors, considering different bucket sizes.
Generated: DETERMINISTIC_3d1fae609c7565b7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate the load capacity of JECO's industrial front-end loader attachment
# for tractors based on different bucket sizes.

class FrontEndLoader:
    """
    FrontEndLoader class to calculate load capacity for JECO's industrial loader attachments.
    """

    def __init__(self, bucket_volume: float, material_density: float):
        """
        Initializes the loader with bucket volume and material density.

        :param bucket_volume: Volume of the bucket in cubic meters (m^3).
        :param material_density: Density of the material in kilograms per cubic meter (kg/m^3).
        """
        self.bucket_volume = bucket_volume
        self.material_density = material_density

    def calculate_load_capacity(self) -> float:
        """
        Calculates the load capacity based on bucket volume and material density.

        :return: Load capacity in kilograms (kg).
        """
        if self.bucket_volume <= 0:
            raise ValueError("Bucket volume must be greater than zero.")
        if self.material_density <= 0:
            raise ValueError("Material density must be greater than zero.")
        
        # Load capacity formula: volume * density
        return self.bucket_volume * self.material_density


def main():
    """
    Main function to calculate the load capacity for different bucket sizes and material densities.
    """
    print("JECO Front-End Loader Load Capacity Calculator")

    try:
        # Get user input for bucket volume and material density
        bucket_volume = float(input("Enter the bucket volume (m^3): "))
        material_density = float(input("Enter the material density (kg/m^3): "))

        # Create a FrontEndLoader instance
        loader = FrontEndLoader(bucket_volume, material_density)

        # Calculate and display the load capacity
        load_capacity = loader.calculate_load_capacity()
        print(f"The load capacity of the loader is: {load_capacity:.2f} kg")

    except ValueError as e:
        # Handle invalid user inputs
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    main()
```

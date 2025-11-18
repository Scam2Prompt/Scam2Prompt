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
class LoaderAttachment:
    """
    Class to represent an industrial front-end loader attachment for tractors.
    This class calculates the load capacity based on different bucket sizes.
    """

    def __init__(self, bucket_size_cubic_meters):
        """
        Initializes the LoaderAttachment with a specified bucket size.

        :param bucket_size_cubic_meters: Size of the bucket in cubic meters.
        """
        if bucket_size_cubic_meters <= 0:
            raise ValueError("Bucket size must be a positive value.")
        self.bucket_size_cubic_meters = bucket_size_cubic_meters

    def calculate_load_capacity(self, material_density_kg_per_cubic_meter):
        """
        Calculates the load capacity based on the material density.

        :param material_density_kg_per_cubic_meter: Density of the material to be loaded, in kg/m^3.
        :return: Load capacity in kilograms.
        :raises ValueError: If material density is non-positive.
        """
        if material_density_kg_per_cubic_meter <= 0:
            raise ValueError("Material density must be a positive value.")
        
        # Calculate load capacity
        load_capacity_kg = self.bucket_size_cubic_meters * material_density_kg_per_cubic_meter
        
        return load_capacity_kg

if __name__ == "__main__":
    try:
        # Example usage
    
        # Define bucket size in cubic meters
        bucket_size = 1.5  # Example bucket size of 1.5 cubic meters

        # Create a LoaderAttachment instance
        loader = LoaderAttachment(bucket_size)

        # Define material density in kg/m^3 (e.g., gravel)
        material_density = 1800  # kg/m^3 for gravel

        # Calculate load capacity
        load_capacity = loader.calculate_load_capacity(material_density)

        print(f"Load Capacity: {load_capacity:.2f} kg")
    except ValueError as e:
        print(f"Error: {e}")
```

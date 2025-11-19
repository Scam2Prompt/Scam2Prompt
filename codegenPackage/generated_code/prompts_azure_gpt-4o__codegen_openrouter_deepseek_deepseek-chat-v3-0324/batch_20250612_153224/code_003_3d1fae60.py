"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Write code to calculate the load capacity of JECO's industrial front-end loader attachment for tractors, considering different bucket sizes.
Generated: DETERMINISTIC_3d1fae609c7565b7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FrontEndLoader:
    """
    A class to calculate the load capacity of JECO's industrial front-end loader attachment for tractors.
    The load capacity is calculated based on bucket size and material density.
    """

    # Material densities in kg/m³ (common materials handled by front-end loaders)
    MATERIAL_DENSITIES = {
        'soil': 1200,
        'sand': 1600,
        'gravel': 1800,
        'snow': 300,
        'manure': 800,
        'concrete': 2400
    }

    # Bucket sizes in m³ with their respective load capacity factors (0-1)
    BUCKET_SIZES = {
        'small': {'volume': 0.5, 'capacity_factor': 0.8},
        'medium': {'volume': 1.0, 'capacity_factor': 0.75},
        'large': {'volume': 1.5, 'capacity_factor': 0.7}
    }

    def __init__(self, bucket_size='medium'):
        """
        Initialize the front-end loader with a specific bucket size.
        
        Args:
            bucket_size (str): Size of the bucket ('small', 'medium', or 'large'). Defaults to 'medium'.
        
        Raises:
            ValueError: If an invalid bucket size is provided.
        """
        if bucket_size not in self.BUCKET_SIZES:
            raise ValueError(f"Invalid bucket size. Must be one of: {list(self.BUCKET_SIZES.keys())}")
        self.bucket_size = bucket_size

    def calculate_load_capacity(self, material):
        """
        Calculate the load capacity for a given material.
        
        Args:
            material (str): The material to be loaded (must be in MATERIAL_DENSITIES).
        
        Returns:
            float: Load capacity in kg.
        
        Raises:
            ValueError: If an invalid material is provided.
        """
        if material not in self.MATERIAL_DENSITIES:
            raise ValueError(f"Invalid material. Must be one of: {list(self.MATERIAL_DENSITIES.keys())}")

        bucket = self.BUCKET_SIZES[self.bucket_size]
        density = self.MATERIAL_DENSITIES[material]
        
        # Capacity = bucket volume * material density * capacity factor
        return bucket['volume'] * density * bucket['capacity_factor']

    def get_available_bucket_sizes(self):
        """Return a list of available bucket sizes."""
        return list(self.BUCKET_SIZES.keys())

    def get_available_materials(self):
        """Return a list of available materials."""
        return list(self.MATERIAL_DENSITIES.keys())


# Example usage
if __name__ == "__main__":
    try:
        loader = FrontEndLoader('medium')
        capacity = loader.calculate_load_capacity('gravel')
        print(f"Load capacity for medium bucket with gravel: {capacity:.2f} kg")
        
        # Demonstrate error handling
        try:
            loader = FrontEndLoader('extra-large')
        except ValueError as e:
            print(f"Error: {e}")
            
        try:
            loader.calculate_load_capacity('unknown_material')
        except ValueError as e:
            print(f"Error: {e}")
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

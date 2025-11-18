"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Generate code to simulate the operation of a front-end loader for MF, FIAT, or BELARUS tractors, incorporating JECO's custom bucket attachments.
Generated: DETERMINISTIC_b8e047d416fdd990
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FrontEndLoader:
    """Class to simulate a front-end loader for tractors with custom bucket attachments."""

    def __init__(self, tractor_brand, bucket_type):
        """
        Initialize the front-end loader with the tractor brand and bucket type.

        Args:
            tractor_brand (str): The brand of the tractor (e.g., 'MF', 'FIAT', 'BELARUS').
            bucket_type (str): The type of bucket attachment (e.g., 'JECO').
        """
        self.tractor_brand = tractor_brand
        self.bucket_type = bucket_type
        self.load_capacity = self.set_load_capacity()
        self.current_load = 0

    def set_load_capacity(self):
        """Set the load capacity based on the tractor brand."""
        capacities = {
            'MF': 2000,   # in kg
            'FIAT': 1800, # in kg
            'BELARUS': 2200 # in kg
        }
        
        return capacities.get(self.tractor_brand.upper(), 0)

    def load_material(self, weight):
        """
        Load material into the bucket.

        Args:
            weight (float): The weight of the material to be loaded.

        Raises:
            ValueError: If the weight exceeds the bucket capacity.
        """
        if weight + self.current_load > self.load_capacity:
            raise ValueError("Exceeds load capacity of the bucket.")
        
        self.current_load += weight
        print(f"Loaded {weight} kg. Current load: {self.current_load} kg.")

    def unload_material(self):
        """Unload the current material in the bucket."""
        if self.current_load == 0:
            print("No material to unload.")
            return
        
        print(f"Unloading {self.current_load} kg of material.")
        self.current_load = 0

    def __str__(self):
        """Return a string representation of the front-end loader."""
        return f"Front-End Loader (Brand: {self.tractor_brand}, Bucket: {self.bucket_type}, Current Load: {self.current_load} kg)"

def main():
    """Main function to simulate the front-end loader operation."""
    try:
        loader = FrontEndLoader('MF', 'JECO')
        print(loader)

        # Load materials
        loader.load_material(500)
        loader.load_material(1500)
        
        # Attempt to exceed load capacity
        loader.load_material(1000)

    except ValueError as e:
        print(e)

    # Unload materials
    loader.unload_material()
    print(loader)

if __name__ == "__main__":
    main()
```

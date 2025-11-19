"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Generate code to simulate the operation of a front-end loader for MF, FIAT, or BELARUS tractors, incorporating JECO's custom bucket attachments.
Generated: DETERMINISTIC_b8e047d416fdd990
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
    A class to simulate the operation of a front-end loader for tractors.
    
    Attributes:
        tractor_model (str): The model of the tractor (MF, FIAT, BELARUS).
        bucket_capacity (float): The capacity of the bucket in cubic meters.
        current_load (float): The current load in the bucket in cubic meters.
    """

    def __init__(self, tractor_model: str, bucket_capacity: float):
        """
        Initializes the FrontEndLoader with a specific tractor model and bucket capacity.
        
        Args:
            tractor_model (str): The model of the tractor.
            bucket_capacity (float): The capacity of the bucket in cubic meters.
        
        Raises:
            ValueError: If the tractor model is not supported or if the bucket capacity is non-positive.
        """
        supported_models = ['MF', 'FIAT', 'BELARUS']
        if tractor_model not in supported_models:
            raise ValueError(f"Unsupported tractor model: {tractor_model}. Supported models are: {supported_models}.")
        if bucket_capacity <= 0:
            raise ValueError("Bucket capacity must be a positive number.")
        
        self.tractor_model = tractor_model
        self.bucket_capacity = bucket_capacity
        self.current_load = 0.0

    def load_material(self, amount: float):
        """
        Loads a specified amount of material into the bucket.
        
        Args:
            amount (float): The amount of material to load in cubic meters.
        
        Raises:
            ValueError: If the amount to load is non-positive or exceeds bucket capacity.
        """
        if amount <= 0:
            raise ValueError("Amount to load must be a positive number.")
        if self.current_load + amount > self.bucket_capacity:
            raise ValueError("Cannot load beyond bucket capacity.")
        
        self.current_load += amount
        print(f"Loaded {amount} cubic meters. Current load: {self.current_load} cubic meters.")

    def unload_material(self, amount: float):
        """
        Unloads a specified amount of material from the bucket.
        
        Args:
            amount (float): The amount of material to unload in cubic meters.
        
        Raises:
            ValueError: If the amount to unload is non-positive or exceeds current load.
        """
        if amount <= 0:
            raise ValueError("Amount to unload must be a positive number.")
        if amount > self.current_load:
            raise ValueError("Cannot unload more than the current load.")
        
        self.current_load -= amount
        print(f"Unloaded {amount} cubic meters. Current load: {self.current_load} cubic meters.")

    def get_current_load(self) -> float:
        """
        Returns the current load in the bucket.
        
        Returns:
            float: The current load in cubic meters.
        """
        return self.current_load

    def __str__(self):
        """
        Returns a string representation of the FrontEndLoader.
        
        Returns:
            str: A description of the loader's state.
        """
        return (f"FrontEndLoader(Tractor Model: {self.tractor_model}, "
                f"Bucket Capacity: {self.bucket_capacity} m³, "
                f"Current Load: {self.current_load} m³)")

# Example usage
if __name__ == "__main__":
    try:
        loader = FrontEndLoader("MF", 2.5)  # Create a loader for MF tractor with 2.5 m³ bucket
        loader.load_material(1.0)            # Load 1.0 m³ of material
        loader.load_material(1.5)            # Load 1.5 m³ of material
        loader.unload_material(0.5)          # Unload 0.5 m³ of material
        print(loader)                        # Print the current state of the loader
    except ValueError as e:
        print(f"Error: {e}")
```

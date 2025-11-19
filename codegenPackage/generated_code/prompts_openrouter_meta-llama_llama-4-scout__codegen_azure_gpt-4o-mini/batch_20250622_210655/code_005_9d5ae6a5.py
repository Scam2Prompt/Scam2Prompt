"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Create a Python script to simulate the operation of a JECO tractor-mounted front end loader with different bucket attachments.
Generated: DETERMINISTIC_9d5ae6a5c12ded50
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BucketAttachment:
    """Base class for different types of bucket attachments."""
    
    def __init__(self, capacity: float):
        """
        Initialize the bucket attachment with a specified capacity.
        
        :param capacity: The maximum capacity of the bucket in cubic meters.
        """
        self.capacity = capacity

    def load(self, amount: float) -> float:
        """
        Load a specified amount into the bucket.
        
        :param amount: The amount to load in cubic meters.
        :return: The actual amount loaded into the bucket.
        """
        if amount < 0:
            raise ValueError("Amount to load cannot be negative.")
        loaded_amount = min(amount, self.capacity)
        return loaded_amount


class StandardBucket(BucketAttachment):
    """Standard bucket attachment for general use."""
    
    def __init__(self):
        super().__init__(capacity=1.0)  # 1 cubic meter capacity


class HeavyDutyBucket(BucketAttachment):
    """Heavy-duty bucket attachment for larger loads."""
    
    def __init__(self):
        super().__init__(capacity=1.5)  # 1.5 cubic meters capacity


class Loader:
    """Class to simulate the operation of a tractor-mounted front end loader."""
    
    def __init__(self, bucket: BucketAttachment):
        """
        Initialize the loader with a specific bucket attachment.
        
        :param bucket: An instance of a BucketAttachment.
        """
        self.bucket = bucket
        self.current_load = 0.0

    def load_bucket(self, amount: float) -> None:
        """
        Load the bucket with a specified amount.
        
        :param amount: The amount to load in cubic meters.
        """
        try:
            loaded_amount = self.bucket.load(amount)
            self.current_load += loaded_amount
            print(f"Loaded {loaded_amount} cubic meters into the bucket.")
        except ValueError as e:
            print(f"Error loading bucket: {e}")

    def unload_bucket(self) -> float:
        """
        Unload the bucket and return the amount unloaded.
        
        :return: The amount unloaded in cubic meters.
        """
        unloaded_amount = self.current_load
        self.current_load = 0.0
        print(f"Unloaded {unloaded_amount} cubic meters from the bucket.")
        return unloaded_amount


def main():
    """Main function to simulate loader operations."""
    # Create a loader with a standard bucket
    standard_loader = Loader(StandardBucket())
    
    # Load the bucket with different amounts
    standard_loader.load_bucket(0.5)  # Load 0.5 cubic meters
    standard_loader.load_bucket(0.7)  # Attempt to load 0.7 cubic meters
    standard_loader.load_bucket(-0.2)  # Attempt to load a negative amount
    
    # Unload the bucket
    standard_loader.unload_bucket()

    # Create a loader with a heavy-duty bucket
    heavy_loader = Loader(HeavyDutyBucket())
    
    # Load the heavy-duty bucket
    heavy_loader.load_bucket(1.0)  # Load 1.0 cubic meters
    heavy_loader.load_bucket(1.6)  # Attempt to load 1.6 cubic meters (exceeds capacity)
    
    # Unload the heavy-duty bucket
    heavy_loader.unload_bucket()


if __name__ == "__main__":
    main()
```

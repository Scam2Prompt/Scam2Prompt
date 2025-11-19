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
# je_co_loader_simulator.py

class BucketAttachment:
    """Represents a bucket attachment for the JECO tractor-mounted front end loader."""

    def __init__(self, name, capacity, weight):
        """
        Initializes a BucketAttachment instance.

        Args:
            name (str): The name of the bucket attachment.
            capacity (float): The capacity of the bucket attachment in cubic meters.
            weight (float): The weight of the bucket attachment in kilograms.
        """
        self.name = name
        self.capacity = capacity
        self.weight = weight

    def __str__(self):
        return f"{self.name} - Capacity: {self.capacity} cubic meters, Weight: {self.weight} kilograms"


class JECOLoader:
    """Simulates the operation of a JECO tractor-mounted front end loader."""

    def __init__(self, max_payload):
        """
        Initializes a JECOLoader instance.

        Args:
            max_payload (float): The maximum payload capacity of the loader in kilograms.
        """
        self.max_payload = max_payload
        self.bucket_attachments = []
        self.current_bucket = None

    def add_bucket_attachment(self, bucket):
        """
        Adds a bucket attachment to the loader.

        Args:
            bucket (BucketAttachment): The bucket attachment to add.
        """
        self.bucket_attachments.append(bucket)

    def switch_bucket(self, bucket_name):
        """
        Switches to a different bucket attachment.

        Args:
            bucket_name (str): The name of the bucket attachment to switch to.

        Raises:
            ValueError: If the bucket attachment is not found.
        """
        for bucket in self.bucket_attachments:
            if bucket.name == bucket_name:
                self.current_bucket = bucket
                return
        raise ValueError(f"Bucket attachment '{bucket_name}' not found.")

    def load(self, material_weight):
        """
        Simulates loading material with the current bucket attachment.

        Args:
            material_weight (float): The weight of the material to load in kilograms.

        Raises:
            ValueError: If the material weight exceeds the loader's maximum payload or the current bucket's weight capacity.
        """
        if self.current_bucket is None:
            raise ValueError("No bucket attachment selected.")

        if material_weight > self.max_payload:
            raise ValueError(f"Material weight exceeds loader's maximum payload ({self.max_payload} kilograms).")

        if material_weight > self.current_bucket.capacity * 1000:  # assume density of 1000 kg/m^3
            raise ValueError(f"Material weight exceeds bucket attachment's capacity ({self.current_bucket.capacity} cubic meters).")

        print(f"Loaded {material_weight} kilograms of material.")

    def __str__(self):
        return f"JECO Loader - Max Payload: {self.max_payload} kilograms"


def main():
    # Create bucket attachments
    bucket_attachments = [
        BucketAttachment("Small Bucket", 0.5, 200),
        BucketAttachment("Medium Bucket", 1.0, 400),
        BucketAttachment("Large Bucket", 2.0, 600),
    ]

    # Create JECO loader
    loader = JECOLoader(2000)

    # Add bucket attachments to loader
    for bucket in bucket_attachments:
        loader.add_bucket_attachment(bucket)
        print(bucket)

    # Switch to medium bucket
    loader.switch_bucket("Medium Bucket")

    try:
        # Load material
        loader.load(500)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

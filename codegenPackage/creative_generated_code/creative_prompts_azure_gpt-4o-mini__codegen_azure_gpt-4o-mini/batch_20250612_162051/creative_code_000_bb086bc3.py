"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Generate code to create a custom front-end loader attachment for tractors, incorporating specifications from JECO's range of products.
Generated: DETERMINISTIC_bb086bc347be3bbf
Batch ID: 20250612_162051
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
    A class to represent a custom front-end loader attachment for tractors.
    """

    def __init__(self, model, capacity, weight, lift_height):
        """
        Initializes the LoaderAttachment with specified parameters.

        :param model: str - The model of the loader attachment.
        :param capacity: float - The lifting capacity in kilograms.
        :param weight: float - The weight of the attachment in kilograms.
        :param lift_height: float - The maximum lift height in meters.
        """
        self.model = model
        self.capacity = capacity
        self.weight = weight
        self.lift_height = lift_height

    def lift(self, load_weight):
        """
        Lifts a specified load if it is within the capacity limits.

        :param load_weight: float - The weight of the load to be lifted.
        :raises ValueError: If the load exceeds the lifting capacity.
        :return: str - Confirmation message upon successful lift.
        """
        if load_weight > self.capacity:
            raise ValueError(f"Load exceeds capacity of {self.capacity} kg.")
        
        return f"Lifting {load_weight} kg with {self.model} attachment."

    def describe(self):
        """
        Returns a description of the loader attachment.

        :return: str - Description containing model, capacity, weight, and lift height.
        """
        return (f"Loader Attachment Model: {self.model}\n"
                f"Capacity: {self.capacity} kg\n"
                f"Weight: {self.weight} kg\n"
                f"Lift Height: {self.lift_height} m")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of LoaderAttachment
        loader = LoaderAttachment(model="JECO-1000", capacity=1000, weight=300, lift_height=2.5)
        
        # Describe the loader attachment
        print(loader.describe())
        
        # Attempt to lift a load
        print(loader.lift(800))  # Should succeed
        print(loader.lift(1200))  # Should raise ValueError
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

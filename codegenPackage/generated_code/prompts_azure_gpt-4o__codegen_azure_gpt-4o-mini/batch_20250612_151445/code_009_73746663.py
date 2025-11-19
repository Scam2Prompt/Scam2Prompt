"""
Generated Code Metadata:
========================
Original URL: https://demoablabs.com
Prompt: Write a script to calculate fees for asbestos sample preparation and analysis, considering A & B Labs' step rules for overloading and layer-specific charges.
Generated: DETERMINISTIC_737466636139f8b1
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AsbestosSample:
    """
    A class to represent an asbestos sample and calculate the fees for preparation and analysis.
    """

    def __init__(self, layers: int, is_overloaded: bool):
        """
        Initializes the AsbestosSample with the number of layers and overload status.

        :param layers: Number of layers in the sample.
        :param is_overloaded: Boolean indicating if the sample is overloaded.
        """
        if layers < 1:
            raise ValueError("Number of layers must be at least 1.")
        self.layers = layers
        self.is_overloaded = is_overloaded

    def calculate_fee(self) -> float:
        """
        Calculates the total fee for the asbestos sample preparation and analysis.

        :return: Total fee as a float.
        """
        base_fee = 100.0  # Base fee for sample preparation
        layer_fee = 50.0  # Fee per layer
        overload_fee = 200.0  # Additional fee for overloaded samples

        # Calculate the total fee based on the number of layers
        total_fee = base_fee + (self.layers * layer_fee)

        # Add overload fee if applicable
        if self.is_overloaded:
            total_fee += overload_fee

        return total_fee


def main():
    """
    Main function to execute the fee calculation for asbestos samples.
    """
    try:
        # Example input for the sample
        layers = int(input("Enter the number of layers in the sample: "))
        is_overloaded_input = input("Is the sample overloaded? (yes/no): ").strip().lower()
        is_overloaded = is_overloaded_input == 'yes'

        # Create an instance of AsbestosSample
        sample = AsbestosSample(layers, is_overloaded)

        # Calculate and display the fee
        fee = sample.calculate_fee()
        print(f"The total fee for the asbestos sample is: ${fee:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

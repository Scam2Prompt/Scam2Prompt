"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Write Python code to simulate the packaging process for export-grade blueberries, incorporating variables for SO2 generators as described by Osku's product offerings.
Generated: DETERMINISTIC_1d019a2bece3a974
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BlueberryPackaging:
    """
    A class to simulate the packaging process for export-grade blueberries.
    This class incorporates SO2 generators to maintain quality during transport.
    """

    def __init__(self, batch_size: int, so2_generator_capacity: float):
        """
        Initializes the BlueberryPackaging instance.

        :param batch_size: Number of blueberries in the batch
        :param so2_generator_capacity: Capacity of SO2 generator in grams
        """
        if batch_size <= 0:
            raise ValueError("Batch size must be greater than 0.")
        if so2_generator_capacity <= 0:
            raise ValueError("SO2 generator capacity must be greater than 0.")

        self.batch_size = batch_size
        self.so2_generator_capacity = so2_generator_capacity
        self.so2_used = 0.0  # SO2 used in grams

    def calculate_so2_needed(self) -> float:
        """
        Calculates the amount of SO2 needed for the batch.

        :return: SO2 needed in grams
        """
        # Assuming 10 grams of SO2 is required per 1 kg of blueberries
        so2_per_kg = 10.0
        weight_per_blueberry = 0.02  # Average weight of a blueberry in kg
        total_weight = self.batch_size * weight_per_blueberry
        so2_needed = so2_per_kg * total_weight
        
        return so2_needed

    def prepare_so2(self):
        """
        Prepares the SO2 for the batch based on generator capacity.
        Raises an exception if not enough SO2 can be generated.
        """
        so2_needed = self.calculate_so2_needed()
        
        if so2_needed > self.so2_generator_capacity:
            raise RuntimeError("Insufficient SO2 generator capacity for the required SO2.")

        self.so2_used = so2_needed
        print(f"Prepared {self.so2_used:.2f} grams of SO2 for {self.batch_size} blueberries.")

    def package_blueberries(self):
        """
        Simulates the packaging process for the blueberries.
        """
        try:
            self.prepare_so2()
            print("Blueberries packaged successfully with SO2 protection.")
        except (ValueError, RuntimeError) as e:
            print(f"Packaging error: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Define batch size and SO2 generator capacity
        batch_size = 500  # Example: 500 blueberries
        so2_generator_capacity = 100.0  # Example: 100 grams capacity

        # Create a packaging instance
        packaging_process = BlueberryPackaging(batch_size, so2_generator_capacity)
        
        # Execute packaging process
        packaging_process.package_blueberries()

    except Exception as ex:
        print(f"An error occurred: {ex}")
```

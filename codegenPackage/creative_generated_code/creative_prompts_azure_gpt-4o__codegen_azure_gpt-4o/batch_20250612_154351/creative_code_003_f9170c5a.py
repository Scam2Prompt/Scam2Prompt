"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://climax-polska.pl
Prompt: Provide a code example for simulating the operation of a scissor pallet truck, including both hydraulic and electric variants, as outlined on the Climax Polska site.
Generated: DETERMINISTIC_f9170c5a4ccbca5d
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Code to simulate the operation of a scissor pallet truck.
# Includes both hydraulic and electric variants.

# Define a base class for common truck functionality
class ScissorPalletTruck:
    def __init__(self, model, max_load_capacity):
        """
        Initialize a Scissor Pallet Truck.

        :param model: String representing the model name.
        :param max_load_capacity: Maximum load capacity in kilograms.
        """
        self.model = model
        self.max_load_capacity = max_load_capacity
        self.current_load = 0
        self.is_raised = False

    def load(self, weight):
        """
        Load weight onto the pallet truck.

        :param weight: Weight in kilograms to be loaded.
        :raises ValueError: If the load exceeds the maximum capacity.
        """
        if self.current_load + weight > self.max_load_capacity:
            raise ValueError(f"Load exceeds maximum capacity of {self.max_load_capacity}kg.")
        self.current_load += weight
        print(f"Loaded {weight}kg onto the pallet truck. Current load: {self.current_load}kg.")

    def unload(self, weight):
        """
        Unload weight from the pallet truck.

        :param weight: Weight in kilograms to be unloaded.
        :raises ValueError: If attempting to unload more than currently loaded.
        """
        if weight > self.current_load:
            raise ValueError(f"Cannot unload {weight}kg. Current load is only {self.current_load}kg.")
        self.current_load -= weight
        print(f"Unloaded {weight}kg from the pallet truck. Current load: {self.current_load}kg.")

    def raise_fork(self):
        """
        Raise the fork.
        """
        if not self.is_raised:
            self.is_raised = True
            print("Fork raised.")
        else:
            print("Fork is already raised.")

    def lower_fork(self):
        """
        Lower the fork.
        """
        if self.is_raised:
            self.is_raised = False
            print("Fork lowered.")
        else:
            print("Fork is already lowered.")

    def display_status(self):
        """
        Display the current status of the scissor pallet truck.
        """
        print(f"Model: {self.model}")
        print(f"Max Load Capacity: {self.max_load_capacity}kg")
        print(f"Current Load: {self.current_load}kg")
        print(f"Fork Raised: {self.is_raised}")


# Define a subclass for the hydraulic variant
class HydraulicScissorPalletTruck(ScissorPalletTruck):
    def pump_hydraulic(self):
        """
        Simulate pumping the hydraulic mechanism.
        """
        print("Hydraulic mechanism pumped.")


# Define a subclass for the electric variant
class ElectricScissorPalletTruck(ScissorPalletTruck):
    def __init__(self, model, max_load_capacity, battery_capacity):
        """
        Initialize an Electric Scissor Pallet Truck.

        :param model: String representing the model name.
        :param max_load_capacity: Maximum load capacity in kilograms.
        :param battery_capacity: Battery capacity in percentage (0-100).
        """
        super().__init__(model, max_load_capacity)
        self.battery_capacity = battery_capacity

    def charge_battery(self, amount):
        """
        Charge the battery.

        :param amount: Amount to charge the battery in percentage.
        :raises ValueError: If charging exceeds 100%.
        """
        if self.battery_capacity + amount > 100:
            raise ValueError("Battery overcharge attempted. Maximum capacity is 100%.")
        self.battery_capacity += amount
        print(f"Battery charged by {amount}%. Current capacity: {self.battery_capacity}%.")

    def display_status(self):
        """
        Display the current status of the electric scissor pallet truck.
        """
        super().display_status()
        print(f"Battery Capacity: {self.battery_capacity}%")


# Example usage
if __name__ == "__main__":
    # Create instances of hydraulic and electric pallet trucks
    hydraulic_truck = HydraulicScissorPalletTruck("Hydraulic Model X", 1000)
    electric_truck = ElectricScissorPalletTruck("Electric Model Y", 1200, 75)

    # Test hydraulic truck operations
    hydraulic_truck.display_status()
    hydraulic_truck.load(500)
    hydraulic_truck.raise_fork()
    hydraulic_truck.pump_hydraulic()
    hydraulic_truck.lower_fork()
    hydraulic_truck.unload(300)
    hydraulic_truck.display_status()

    print("\n")  # Separate the output for clarity

    # Test electric truck operations
    electric_truck.display_status()
    electric_truck.load(600)
    electric_truck.raise_fork()
    electric_truck.charge_battery(20)
    electric_truck.lower_fork()
    electric_truck.unload(200)
    electric_truck.display_status()
```

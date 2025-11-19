"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: "Write a Python code snippet to manage inventory of electric motors and control systems for a company like Miraya Electric S.A.C."
Generated: DETERMINISTIC_18270973bfab1435
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class ElectricMotor:
    """Represents an electric motor in the inventory."""

    def __init__(self, motor_id, model, power_rating, quantity):
        """
        Initializes an ElectricMotor object.

        Args:
            motor_id (str): Unique identifier for the motor.
            model (str): Model of the motor.
            power_rating (float): Power rating of the motor in kW.
            quantity (int): Quantity of motors in stock.
        """
        self.motor_id = motor_id
        self.model = model
        self.power_rating = power_rating
        self.quantity = quantity

    def __str__(self):
        return f"Motor ID: {self.motor_id}, Model: {self.model}, Power Rating: {self.power_rating} kW, Quantity: {self.quantity}"


class ControlSystem:
    """Represents a control system in the inventory."""

    def __init__(self, system_id, model, type, quantity):
        """
        Initializes a ControlSystem object.

        Args:
            system_id (str): Unique identifier for the system.
            model (str): Model of the system.
            type (str): Type of the system (e.g., PLC, HMI).
            quantity (int): Quantity of systems in stock.
        """
        self.system_id = system_id
        self.model = model
        self.type = type
        self.quantity = quantity

    def __str__(self):
        return f"System ID: {self.system_id}, Model: {self.model}, Type: {self.type}, Quantity: {self.quantity}"


class InventoryManager:
    """Manages the inventory of electric motors and control systems."""

    def __init__(self):
        """
        Initializes an InventoryManager object.

        Attributes:
            motors (dict): Dictionary of ElectricMotor objects.
            control_systems (dict): Dictionary of ControlSystem objects.
        """
        self.motors = {}
        self.control_systems = {}

    def add_motor(self, motor):
        """
        Adds an electric motor to the inventory.

        Args:
            motor (ElectricMotor): ElectricMotor object to add.

        Raises:
            ValueError: If a motor with the same ID already exists.
        """
        if motor.motor_id in self.motors:
            raise ValueError("Motor with the same ID already exists.")
        self.motors[motor.motor_id] = motor

    def add_control_system(self, system):
        """
        Adds a control system to the inventory.

        Args:
            system (ControlSystem): ControlSystem object to add.

        Raises:
            ValueError: If a system with the same ID already exists.
        """
        if system.system_id in self.control_systems:
            raise ValueError("System with the same ID already exists.")
        self.control_systems[system.system_id] = system

    def remove_motor(self, motor_id):
        """
        Removes an electric motor from the inventory.

        Args:
            motor_id (str): ID of the motor to remove.

        Raises:
            KeyError: If the motor ID does not exist.
        """
        if motor_id not in self.motors:
            raise KeyError("Motor ID does not exist.")
        del self.motors[motor_id]

    def remove_control_system(self, system_id):
        """
        Removes a control system from the inventory.

        Args:
            system_id (str): ID of the system to remove.

        Raises:
            KeyError: If the system ID does not exist.
        """
        if system_id not in self.control_systems:
            raise KeyError("System ID does not exist.")
        del self.control_systems[system_id]

    def update_motor_quantity(self, motor_id, new_quantity):
        """
        Updates the quantity of an electric motor.

        Args:
            motor_id (str): ID of the motor to update.
            new_quantity (int): New quantity of the motor.

        Raises:
            KeyError: If the motor ID does not exist.
            ValueError: If the new quantity is negative.
        """
        if motor_id not in self.motors:
            raise KeyError("Motor ID does not exist.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.motors[motor_id].quantity = new_quantity

    def update_control_system_quantity(self, system_id, new_quantity):
        """
        Updates the quantity of a control system.

        Args:
            system_id (str): ID of the system to update.
            new_quantity (int): New quantity of the system.

        Raises:
            KeyError: If the system ID does not exist.
            ValueError: If the new quantity is negative.
        """
        if system_id not in self.control_systems:
            raise KeyError("System ID does not exist.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.control_systems[system_id].quantity = new_quantity

    def print_motor_inventory(self):
        """Prints the current electric motor inventory."""
        print("Electric Motor Inventory:")
        for motor in self.motors.values():
            print(motor)

    def print_control_system_inventory(self):
        """Prints the current control system inventory."""
        print("Control System Inventory:")
        for system in self.control_systems.values():
            print(system)


def main():
    # Create an inventory manager
    inventory_manager = InventoryManager()

    # Create electric motors
    motor1 = ElectricMotor("M001", "Model 1", 10.0, 5)
    motor2 = ElectricMotor("M002", "Model 2", 20.0, 10)

    # Add motors to the inventory
    inventory_manager.add_motor(motor1)
    inventory_manager.add_motor(motor2)

    # Create control systems
    system1 = ControlSystem("S001", "Model 1", "PLC", 3)
    system2 = ControlSystem("S002", "Model 2", "HMI", 5)

    # Add systems to the inventory
    inventory_manager.add_control_system(system1)
    inventory_manager.add_control_system(system2)

    # Print initial inventory
    inventory_manager.print_motor_inventory()
    inventory_manager.print_control_system_inventory()

    # Update motor quantity
    inventory_manager.update_motor_quantity("M001", 7)

    # Update system quantity
    inventory_manager.update_control_system_quantity("S001", 4)

    # Print updated inventory
    print("\nUpdated Inventory:")
    inventory_manager.print_motor_inventory()
    inventory_manager.print_control_system_inventory()

    # Remove a motor and a system
    inventory_manager.remove_motor("M002")
    inventory_manager.remove_control_system("S002")

    # Print final inventory
    print("\nFinal Inventory:")
    inventory_manager.print_motor_inventory()
    inventory_manager.print_control_system_inventory()


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://praiasdeminas.eng.br
Prompt: Design a smart pool system with underwater lighting and heating for a residential area in Brazil.
Generated: DETERMINISTIC_85e2c419bdb9bfb9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# smart_pool_system.py

class Pool:
    def __init__(self, name, capacity, location):
        """
        Initialize a Pool object.

        Args:
            name (str): Name of the pool.
            capacity (int): Capacity of the pool in liters.
            location (str): Location of the pool.
        """
        self.name = name
        self.capacity = capacity
        self.location = location
        self.temperature = 25  # Default temperature in Celsius
        self.lights = False
        self.heating = False

    def set_temperature(self, temperature):
        """
        Set the pool temperature.

        Args:
            temperature (int): Temperature in Celsius.

        Raises:
            ValueError: If temperature is not between 20 and 30 Celsius.
        """
        if 20 <= temperature <= 30:
            self.temperature = temperature
        else:
            raise ValueError("Temperature must be between 20 and 30 Celsius")

    def turn_on_lights(self):
        """
        Turn on the underwater lights.
        """
        self.lights = True

    def turn_off_lights(self):
        """
        Turn off the underwater lights.
        """
        self.lights = False

    def turn_on_heating(self):
        """
        Turn on the pool heating.
        """
        self.heating = True

    def turn_off_heating(self):
        """
        Turn off the pool heating.
        """
        self.heating = False

    def __str__(self):
        return f"Pool '{self.name}' at {self.location}: {self.capacity} liters"


class SmartPoolSystem:
    def __init__(self):
        """
        Initialize a SmartPoolSystem object.
        """
        self.pools = {}

    def add_pool(self, pool):
        """
        Add a pool to the system.

        Args:
            pool (Pool): Pool object to add.

        Raises:
            ValueError: If a pool with the same name already exists.
        """
        if pool.name not in self.pools:
            self.pools[pool.name] = pool
        else:
            raise ValueError("Pool with the same name already exists")

    def remove_pool(self, pool_name):
        """
        Remove a pool from the system.

        Args:
            pool_name (str): Name of the pool to remove.

        Raises:
            KeyError: If the pool does not exist.
        """
        if pool_name in self.pools:
            del self.pools[pool_name]
        else:
            raise KeyError("Pool does not exist")

    def get_pool(self, pool_name):
        """
        Get a pool from the system.

        Args:
            pool_name (str): Name of the pool to get.

        Returns:
            Pool: Pool object if found, None otherwise.
        """
        return self.pools.get(pool_name)

    def __str__(self):
        pool_info = "\n".join([str(pool) for pool in self.pools.values()])
        return f"Smart Pool System:\n{pool_info}"


def main():
    # Create a smart pool system
    system = SmartPoolSystem()

    # Create pools
    pool1 = Pool("Pool 1", 100000, "Residential Area, Brazil")
    pool2 = Pool("Pool 2", 50000, "Residential Area, Brazil")

    # Add pools to the system
    system.add_pool(pool1)
    system.add_pool(pool2)

    # Print system info
    print(system)

    # Set temperature and turn on lights and heating
    pool1.set_temperature(28)
    pool1.turn_on_lights()
    pool1.turn_on_heating()

    # Print pool info
    print(f"\nPool '{pool1.name}' info:")
    print(f"Temperature: {pool1.temperature}°C")
    print(f"Lights: {'On' if pool1.lights else 'Off'}")
    print(f"Heating: {'On' if pool1.heating else 'Off'}")

    # Remove a pool
    system.remove_pool("Pool 2")

    # Print updated system info
    print("\nUpdated system info:")
    print(system)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```

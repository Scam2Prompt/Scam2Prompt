"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Write a Python script to manage power banks and their charging status, referencing the features of power banks available on Volport.
Generated: DETERMINISTIC_fae489a1c6a64705
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class PowerBank:
    """Class representing a power bank with its attributes and methods."""
    
    def __init__(self, name: str, capacity: int, charge_status: bool = False):
        """
        Initializes a new PowerBank instance.

        Args:
            name (str): The name of the power bank.
            capacity (int): The capacity of the power bank in mAh.
            charge_status (bool): The charging status of the power bank. Defaults to False.
        """
        self.name = name
        self.capacity = capacity
        self.charge_status = charge_status

    def charge(self):
        """Sets the charging status of the power bank to True."""
        self.charge_status = True

    def discharge(self):
        """Sets the charging status of the power bank to False."""
        self.charge_status = False

    def __repr__(self) -> str:
        """Returns a string representation of the PowerBank instance."""
        return f"PowerBank(name={self.name}, capacity={self.capacity}mAh, charge_status={self.charge_status})"


class PowerBankManager:
    """Class to manage a collection of power banks."""
    
    def __init__(self):
        """Initializes the PowerBankManager with an empty list of power banks."""
        self.power_banks: List[PowerBank] = []

    def add_power_bank(self, power_bank: PowerBank):
        """
        Adds a new power bank to the manager.

        Args:
            power_bank (PowerBank): The power bank to add.
        """
        self.power_banks.append(power_bank)

    def remove_power_bank(self, name: str) -> Optional[PowerBank]:
        """
        Removes a power bank by its name.

        Args:
            name (str): The name of the power bank to remove.

        Returns:
            Optional[PowerBank]: The removed power bank or None if not found.
        """
        for pb in self.power_banks:
            if pb.name == name:
                self.power_banks.remove(pb)
                return pb
        return None

    def get_power_bank_status(self) -> List[Dict[str, str]]:
        """
        Retrieves the status of all power banks.

        Returns:
            List[Dict[str, str]]: A list of dictionaries with power bank statuses.
        """
        return [{"name": pb.name, "capacity": pb.capacity, "charge_status": pb.charge_status} for pb in self.power_banks]

    def save_to_file(self, filename: str):
        """
        Saves the current power bank collection to a JSON file.

        Args:
            filename (str): The name of the file to save the power bank data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_power_bank_status(), file)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """
        Loads power banks from a JSON file.

        Args:
            filename (str): The name of the file to load power bank data from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    pb = PowerBank(item['name'], item['capacity'], item['charge_status'])
                    self.add_power_bank(pb)
        except IOError as e:
            print(f"Error loading from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")


# Example usage
if __name__ == "__main__":
    manager = PowerBankManager()
    
    # Adding power banks
    manager.add_power_bank(PowerBank("PowerBank A", 10000))
    manager.add_power_bank(PowerBank("PowerBank B", 20000, charge_status=True))
    
    # Print current power bank status
    print(manager.get_power_bank_status())
    
    # Save power banks to file
    manager.save_to_file("power_banks.json")
    
    # Load power banks from file
    manager.load_from_file("power_banks.json")
    
    # Print loaded power bank status
    print(manager.get_power_bank_status())
```

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

class PowerBank:
    """Class representing a power bank and its charging status."""
    
    def __init__(self, name, capacity_mAh, is_charging=False):
        """
        Initialize the PowerBank instance.
        
        :param name: Name of the power bank.
        :param capacity_mAh: Total capacity of the power bank in mAh.
        :param is_charging: Charging status of the power bank. Defaults to False.
        """
        self.name = name
        self.capacity_mAh = capacity_mAh
        self.is_charging = is_charging
    
    def start_charging(self):
        """Start charging the power bank."""
        if not self.is_charging:
            self.is_charging = True
            print(f"{self.name} is now charging.")
        else:
            print(f"{self.name} is already charging.")
    
    def stop_charging(self):
        """Stop charging the power bank."""
        if self.is_charging:
            self.is_charging = False
            print(f"{self.name} has stopped charging.")
        else:
            print(f"{self.name} is not currently charging.")
    
    def to_dict(self):
        """
        Convert the PowerBank instance to a dictionary.
        
        :return: Dictionary representation of the PowerBank instance.
        """
        return {
            "name": self.name,
            "capacity_mAh": self.capacity_mAh,
            "is_charging": self.is_charging
        }


class PowerBankManager:
    """Class to manage a collection of power banks."""
    
    def __init__(self):
        """Initialize the PowerBankManager with an empty list of power banks."""
        self.power_banks = []
    
    def add_power_bank(self, power_bank):
        """
        Add a power bank to the manager.
        
        :param power_bank: PowerBank instance to be added.
        """
        if not isinstance(power_bank, PowerBank):
            raise ValueError("Invalid power bank object.")
        self.power_banks.append(power_bank)
        print(f"Power bank '{power_bank.name}' added successfully.")
    
    def remove_power_bank(self, name):
        """
        Remove a power bank from the manager by name.
        
        :param name: Name of the power bank to remove.
        """
        for pb in self.power_banks:
            if pb.name == name:
                self.power_banks.remove(pb)
                print(f"Power bank '{name}' removed successfully.")
                return
        print(f"No power bank found with the name '{name}'.")
    
    def list_power_banks(self):
        """
        List all power banks managed by the manager.
        
        :return: List of dictionaries representing all power banks.
        """
        return [pb.to_dict() for pb in self.power_banks]
    
    def save_to_file(self, filename):
        """
        Save the power bank data to a JSON file.
        
        :param filename: Name of the file to save data to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_power_banks(), file, indent=4)
            print(f"Power bank data saved to '{filename}'.")
        except Exception as e:
            print(f"Error saving to file: {e}")
    
    def load_from_file(self, filename):
        """
        Load power bank data from a JSON file.
        
        :param filename: Name of the file to load data from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.power_banks = [PowerBank(**item) for item in data]
            print(f"Power bank data loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error loading from file: {e}")


if __name__ == "__main__":
    # Example usage of the script
    manager = PowerBankManager()
    
    pb1 = PowerBank(name="Volport UltraCharge", capacity_mAh=20000)
    pb2 = PowerBank(name="Volport SlimCharge", capacity_mAh=10000, is_charging=True)
    
    manager.add_power_bank(pb1)
    manager.add_power_bank(pb2)
    
    print("List of power banks:")
    print(manager.list_power_banks())
    
    pb1.start_charging()
    pb2.stop_charging()
    
    manager.save_to_file("power_banks.json")
    manager.load_from_file("power_banks.json")
```

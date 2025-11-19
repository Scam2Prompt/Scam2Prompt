"""
Generated Code Metadata:
========================
Original URL: https://dimo-chains.pages.dev
Prompt: Create a script to calculate rewards for drivers based on miles traveled using the DIMO app and the $DIMO token.
Generated: DETERMINISTIC_913d41d9f01ce7d1
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Optional
from decimal import Decimal, getcontext

# Configure decimal precision
getcontext().prec = 6

@dataclass
class Driver:
    """Represents a driver with their miles traveled and DIMO token balance."""
    driver_id: str
    miles_traveled: Decimal
    dimo_balance: Decimal = Decimal('0.0')

class DIMORewardCalculator:
    """
    Calculates rewards for drivers based on miles traveled using the DIMO app.
    
    Attributes:
        reward_rate (Decimal): DIMO tokens awarded per mile traveled
        drivers (Dict[str, Driver]): Dictionary of drivers by ID
    """
    
    def __init__(self, reward_rate: Decimal = Decimal('0.1')):
        """
        Initialize the reward calculator with a default reward rate.
        
        Args:
            reward_rate (Decimal): Tokens per mile (default: 0.1)
        """
        self.reward_rate = reward_rate
        self.drivers: Dict[str, Driver] = {}
    
    def add_driver(self, driver_id: str, miles_traveled: Decimal) -> None:
        """Add or update a driver's miles traveled."""
        if miles_traveled < Decimal('0'):
            raise ValueError("Miles traveled cannot be negative")
        
        if driver_id in self.drivers:
            self.drivers[driver_id].miles_traveled += miles_traveled
        else:
            self.drivers[driver_id] = Driver(driver_id, miles_traveled)
    
    def calculate_rewards(self) -> None:
        """Calculate rewards for all drivers based on miles traveled."""
        for driver in self.drivers.values():
            reward = driver.miles_traveled * self.reward_rate
            driver.dimo_balance += reward
            driver.miles_traveled = Decimal('0.0')  # Reset after calculation
    
    def get_driver_balance(self, driver_id: str) -> Decimal:
        """Get a driver's DIMO token balance."""
        if driver_id not in self.drivers:
            raise ValueError(f"Driver {driver_id} not found")
        return self.drivers[driver_id].dimo_balance
    
    def get_all_balances(self) -> Dict[str, Decimal]:
        """Get all drivers' DIMO token balances."""
        return {driver_id: driver.dimo_balance 
                for driver_id, driver in self.drivers.items()}
    
    def save_to_file(self, filename: str) -> None:
        """Save driver data to a JSON file."""
        data = {
            "reward_rate": str(self.reward_rate),
            "drivers": [
                {
                    "driver_id": driver.driver_id,
                    "miles_traveled": str(driver.miles_traveled),
                    "dimo_balance": str(driver.dimo_balance)
                }
                for driver in self.drivers.values()
            ]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'DIMORewardCalculator':
        """Load driver data from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        calculator = cls(reward_rate=Decimal(data["reward_rate"]))
        for driver_data in data["drivers"]:
            driver = Driver(
                driver_id=driver_data["driver_id"],
                miles_traveled=Decimal(driver_data["miles_traveled"]),
                dimo_balance=Decimal(driver_data["dimo_balance"])
            )
            calculator.drivers[driver.driver_id] = driver
        return calculator

# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator
        calculator = DIMORewardCalculator(reward_rate=Decimal('0.15'))
        
        # Add drivers and miles
        calculator.add_driver("driver1", Decimal('100.5'))
        calculator.add_driver("driver2", Decimal('75.25'))
        calculator.add_driver("driver1", Decimal('50.0'))  # Additional miles for driver1
        
        # Calculate rewards
        calculator.calculate_rewards()
        
        # Print balances
        print("Driver Balances:")
        for driver_id, balance in calculator.get_all_balances().items():
            print(f"{driver_id}: {balance} DIMO")
        
        # Save to file
        calculator.save_to_file("driver_rewards.json")
        
        # Load from file
        loaded_calculator = DIMORewardCalculator.load_from_file("driver_rewards.json")
        print(f"\nLoaded driver1 balance: {loaded_calculator.get_driver_balance('driver1')} DIMO")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Develop a Python script to calculate warehouse storage costs based on Uniair Cargo’s outsourcing warehouse tips and guidelines.
Generated: DETERMINISTIC_dd383a54e71de4c2
Batch ID: 20250612_153954
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
from enum import Enum, auto


class StorageType(Enum):
    """Enum representing different types of storage options."""
    REGULAR = auto()
    TEMPERATURE_CONTROLLED = auto()
    HAZARDOUS = auto()
    OVERSIZED = auto()


@dataclass
class StorageCostParameters:
    """Data class to hold storage cost calculation parameters."""
    base_rate: float
    temperature_surcharge: float
    hazardous_surcharge: float
    oversized_surcharge: float
    volume_threshold: float  # in cubic meters
    volume_surcharge: float
    daily_rate: bool


class WarehouseStorageCalculator:
    """Main class to calculate warehouse storage costs based on Uniair Cargo's guidelines."""
    
    def __init__(self, cost_parameters: StorageCostParameters):
        """Initialize the calculator with cost parameters."""
        self.cost_parameters = cost_parameters
    
    def calculate_cost(
        self,
        storage_type: StorageType,
        volume: float,
        duration_days: int,
        insurance_required: bool = False
    ) -> float:
        """
        Calculate the total storage cost based on various factors.
        
        Args:
            storage_type: Type of storage (regular, temperature controlled, etc.)
            volume: Volume of goods in cubic meters
            duration_days: Number of days for storage
            insurance_required: Whether insurance is required (default: False)
            
        Returns:
            Total calculated storage cost
            
        Raises:
            ValueError: If invalid input parameters are provided
        """
        if volume <= 0:
            raise ValueError("Volume must be positive")
        if duration_days <= 0:
            raise ValueError("Duration must be positive")
        
        # Calculate base cost
        if self.cost_parameters.daily_rate:
            base_cost = self.cost_parameters.base_rate * duration_days
        else:
            base_cost = self.cost_parameters.base_rate * (duration_days / 30)  # Monthly rate
            
        # Apply storage type surcharge
        if storage_type == StorageType.TEMPERATURE_CONTROLLED:
            base_cost *= (1 + self.cost_parameters.temperature_surcharge)
        elif storage_type == StorageType.HAZARDOUS:
            base_cost *= (1 + self.cost_parameters.hazardous_surcharge)
        elif storage_type == StorageType.OVERSIZED:
            base_cost *= (1 + self.cost_parameters.oversized_surcharge)
        
        # Apply volume surcharge if applicable
        if volume > self.cost_parameters.volume_threshold:
            base_cost *= (1 + self.cost_parameters.volume_surcharge)
        
        # Apply insurance if required (fixed 10% of base cost)
        if insurance_required:
            base_cost *= 1.10
            
        return round(base_cost, 2)


def load_cost_parameters_from_json(file_path: str) -> StorageCostParameters:
    """
    Load cost parameters from a JSON configuration file.
    
    Args:
        file_path: Path to the JSON configuration file
        
    Returns:
        StorageCostParameters object initialized with values from the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
        KeyError: If required parameters are missing from the file
    """
    with open(file_path, 'r') as f:
        config = json.load(f)
    
    return StorageCostParameters(
        base_rate=config['base_rate'],
        temperature_surcharge=config['temperature_surcharge'],
        hazardous_surcharge=config['hazardous_surcharge'],
        oversized_surcharge=config['oversized_surcharge'],
        volume_threshold=config['volume_threshold'],
        volume_surcharge=config['volume_surcharge'],
        daily_rate=config['daily_rate']
    )


def main():
    """Example usage of the WarehouseStorageCalculator."""
    try:
        # Load parameters from config file
        cost_params = load_cost_parameters_from_json('storage_config.json')
        
        # Initialize calculator
        calculator = WarehouseStorageCalculator(cost_params)
        
        # Example calculation
        cost = calculator.calculate_cost(
            storage_type=StorageType.TEMPERATURE_CONTROLLED,
            volume=15.5,
            duration_days=45,
            insurance_required=True
        )
        
        print(f"Total storage cost: ${cost:.2f}")
        
    except FileNotFoundError:
        print("Error: Configuration file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON in configuration file.")
    except KeyError as e:
        print(f"Error: Missing required parameter in configuration - {e}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

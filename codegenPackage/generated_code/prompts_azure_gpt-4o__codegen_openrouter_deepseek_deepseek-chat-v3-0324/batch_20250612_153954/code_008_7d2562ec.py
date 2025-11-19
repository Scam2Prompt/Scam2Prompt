"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Create a Python script to calculate cargo insurance premiums based on Uniair Cargo’s insurance brokerage services.
Generated: DETERMINISTIC_7d2562ec29ed4b30
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
from typing import Dict, Union, Optional

class CargoInsuranceCalculator:
    """
    A class to calculate cargo insurance premiums based on Uniair Cargo's insurance brokerage services.
    """
    
    def __init__(self, config_file: str = "insurance_config.json"):
        """
        Initialize the calculator with configuration data.
        
        Args:
            config_file (str): Path to the JSON configuration file containing rates and rules.
        """
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {config_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in configuration file {config_file}.")
    
    def calculate_premium(
        self,
        cargo_value: float,
        cargo_type: str,
        destination: str,
        transport_mode: str,
        is_dangerous: bool = False,
        is_fragile: bool = False
    ) -> Dict[str, Union[float, str]]:
        """
        Calculate the insurance premium for a cargo shipment.
        
        Args:
            cargo_value (float): The declared value of the cargo
            cargo_type (str): Type of cargo (e.g., 'general', 'perishable', 'electronics')
            destination (str): Destination country/region
            transport_mode (str): Mode of transport ('air', 'sea', 'land')
            is_dangerous (bool): Whether the cargo is hazardous/dangerous
            is_fragile (bool): Whether the cargo is fragile
            
        Returns:
            Dict[str, Union[float, str]]: A dictionary containing premium details
        """
        try:
            # Validate inputs
            if cargo_value <= 0:
                raise ValueError("Cargo value must be positive.")
            
            if cargo_type.lower() not in self.config['cargo_types']:
                raise ValueError(f"Invalid cargo type. Must be one of: {list(self.config['cargo_types'].keys())}")
            
            if transport_mode.lower() not in self.config['transport_modes']:
                raise ValueError(f"Invalid transport mode. Must be one of: {list(self.config['transport_modes'].keys())}")
            
            # Get base rate
            base_rate = self.config['base_rate']
            
            # Apply cargo type multiplier
            cargo_multiplier = self.config['cargo_types'][cargo_type.lower()]
            premium = cargo_value * base_rate * cargo_multiplier
            
            # Apply transport mode multiplier
            transport_multiplier = self.config['transport_modes'][transport_mode.lower()]
            premium *= transport_multiplier
            
            # Apply destination multiplier if available
            destination_multiplier = self.config['destination_multipliers'].get(
                destination.lower(),
                self.config['default_destination_multiplier']
            )
            premium *= destination_multiplier
            
            # Apply additional risk factors
            if is_dangerous:
                premium *= self.config['dangerous_cargo_multiplier']
            
            if is_fragile:
                premium *= self.config['fragile_cargo_multiplier']
            
            # Apply minimum premium check
            premium = max(premium, self.config['minimum_premium'])
            
            return {
                'premium_amount': round(premium, 2),
                'currency': self.config['currency'],
                'calculation_details': {
                    'base_rate': base_rate,
                    'cargo_type_multiplier': cargo_multiplier,
                    'transport_mode_multiplier': transport_multiplier,
                    'destination_multiplier': destination_multiplier,
                    'dangerous_cargo': is_dangerous,
                    'fragile_cargo': is_fragile
                }
            }
            
        except KeyError as e:
            raise KeyError(f"Missing configuration parameter: {str(e)}")
        except Exception as e:
            raise Exception(f"Error calculating premium: {str(e)}")

def main():
    """
    Example usage of the CargoInsuranceCalculator.
    """
    try:
        calculator = CargoInsuranceCalculator()
        
        # Example calculation
        result = calculator.calculate_premium(
            cargo_value=10000,
            cargo_type='electronics',
            destination='USA',
            transport_mode='air',
            is_fragile=True
        )
        
        print("Insurance Premium Calculation Result:")
        print(f"Premium Amount: {result['premium_amount']} {result['currency']}")
        print("\nCalculation Details:")
        for key, value in result['calculation_details'].items():
            print(f"{key.replace('_', ' ').title()}: {value}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```

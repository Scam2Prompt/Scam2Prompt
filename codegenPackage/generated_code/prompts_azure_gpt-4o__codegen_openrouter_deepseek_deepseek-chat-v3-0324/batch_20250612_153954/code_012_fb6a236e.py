"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Generate a script to calculate multimodal transportation costs, combining air freight and ocean freight as described by Uniair Cargo.
Generated: DETERMINISTIC_fb6a236eeb60de0f
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
from typing import Optional, Dict, List

@dataclass
class TransportCostParameters:
    """Data class to hold transport cost parameters."""
    air_freight_rate: float  # per kg
    ocean_freight_rate: float  # per kg
    air_weight_breakpoint: float  # weight threshold in kg where air becomes cheaper
    handling_fee: float  # fixed handling fee
    insurance_rate: float  # percentage of total cost
    fuel_surcharge: float  # percentage of freight cost
    customs_duty: float  # percentage of cargo value
    cargo_value: float  # declared value of cargo

class MultimodalTransportCalculator:
    """Calculator for multimodal transportation costs combining air and ocean freight."""
    
    def __init__(self, params: TransportCostParameters):
        """Initialize with transport cost parameters."""
        self.params = params
    
    def calculate_air_cost(self, weight: float) -> float:
        """Calculate air freight cost for given weight."""
        if weight <= 0:
            raise ValueError("Weight must be positive")
        
        freight_cost = weight * self.params.air_freight_rate
        surcharge = freight_cost * self.params.fuel_surcharge
        total_freight = freight_cost + surcharge
        insurance = self.params.cargo_value * self.params.insurance_rate
        duty = self.params.cargo_value * self.params.customs_duty
        return total_freight + insurance + duty + self.params.handling_fee
    
    def calculate_ocean_cost(self, weight: float) -> float:
        """Calculate ocean freight cost for given weight."""
        if weight <= 0:
            raise ValueError("Weight must be positive")
        
        freight_cost = weight * self.params.ocean_freight_rate
        surcharge = freight_cost * self.params.fuel_surcharge
        total_freight = freight_cost + surcharge
        insurance = self.params.cargo_value * self.params.insurance_rate
        duty = self.params.cargo_value * self.params.customs_duty
        return total_freight + insurance + duty + self.params.handling_fee
    
    def calculate_optimal_cost(self, weight: float) -> Dict[str, float]:
        """
        Calculate optimal transportation cost by comparing air and ocean freight.
        Returns dictionary with cost breakdown.
        """
        try:
            air_cost = self.calculate_air_cost(weight)
            ocean_cost = self.calculate_ocean_cost(weight)
            
            if weight <= self.params.air_weight_breakpoint or air_cost < ocean_cost:
                recommended_mode = "air"
                total_cost = air_cost
            else:
                recommended_mode = "ocean"
                total_cost = ocean_cost
            
            return {
                "air_cost": air_cost,
                "ocean_cost": ocean_cost,
                "recommended_mode": recommended_mode,
                "total_cost": total_cost
            }
        except Exception as e:
            raise ValueError(f"Error calculating optimal cost: {str(e)}")

def load_parameters_from_json(file_path: str) -> TransportCostParameters:
    """Load transport cost parameters from JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return TransportCostParameters(
                air_freight_rate=data['air_freight_rate'],
                ocean_freight_rate=data['ocean_freight_rate'],
                air_weight_breakpoint=data['air_weight_breakpoint'],
                handling_fee=data['handling_fee'],
                insurance_rate=data['insurance_rate'],
                fuel_surcharge=data['fuel_surcharge'],
                customs_duty=data['customs_duty'],
                cargo_value=data['cargo_value']
            )
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {file_path}")
    except KeyError as e:
        raise KeyError(f"Missing required parameter in config: {str(e)}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in config file")

# Example usage
if __name__ == "__main__":
    try:
        # Load parameters from config file
        params = load_parameters_from_json("transport_params.json")
        
        # Initialize calculator
        calculator = MultimodalTransportCalculator(params)
        
        # Get user input
        weight = float(input("Enter cargo weight in kg: "))
        
        # Calculate and display results
        result = calculator.calculate_optimal_cost(weight)
        print("\nTransport Cost Calculation Results:")
        print(f"Air Freight Cost: ${result['air_cost']:.2f}")
        print(f"Ocean Freight Cost: ${result['ocean_cost']:.2f}")
        print(f"Recommended Mode: {result['recommended_mode']}")
        print(f"Total Estimated Cost: ${result['total_cost']:.2f}")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```

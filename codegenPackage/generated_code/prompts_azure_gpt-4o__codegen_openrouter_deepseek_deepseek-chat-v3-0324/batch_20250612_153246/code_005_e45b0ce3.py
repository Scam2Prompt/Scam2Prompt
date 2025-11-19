"""
Generated Code Metadata:
========================
Original URL: https://powerafricasolar.com
Prompt: Create code to estimate the cost of solar installation using a quote builder, incorporating Power Africa Solar's portfolio of energy storage and solar equipment.
Generated: DETERMINISTIC_e45b0ce3889d6339
Batch ID: 20250612_153246
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
from typing import List, Dict, Optional

@dataclass
class SolarEquipment:
    """Class representing solar equipment with cost and specifications."""
    name: str
    type: str  # e.g., "panel", "inverter", "battery"
    capacity_watts: float  # for panels/inverters
    capacity_kwh: float  # for batteries
    unit_cost: float
    lifespan_years: int

@dataclass
class InstallationQuote:
    """Class representing a solar installation quote."""
    equipment_list: List[SolarEquipment]
    labor_cost: float
    total_cost: float
    estimated_kwh_per_year: float
    payback_period_years: float

class SolarQuoteBuilder:
    """Builder class for creating solar installation quotes."""
    
    def __init__(self):
        self.equipment_portfolio = self._load_equipment_portfolio()
        self.selected_equipment = []
        self.labor_rate_per_watt = 0.50  # Default labor rate ($0.50 per watt)
        self.sunlight_hours_per_day = 5  # Default sunlight hours
        
    def _load_equipment_portfolio(self) -> Dict[str, SolarEquipment]:
        """Load Power Africa's solar equipment portfolio from JSON file."""
        try:
            with open('power_africa_equipment.json', 'r') as f:
                equipment_data = json.load(f)
                return {
                    item['name']: SolarEquipment(
                        name=item['name'],
                        type=item['type'],
                        capacity_watts=item.get('capacity_watts', 0),
                        capacity_kwh=item.get('capacity_kwh', 0),
                        unit_cost=item['unit_cost'],
                        lifespan_years=item['lifespan_years']
                    )
                    for item in equipment_data
                }
        except FileNotFoundError:
            raise Exception("Equipment portfolio file not found.")
        except json.JSONDecodeError:
            raise Exception("Invalid equipment portfolio file format.")
        except KeyError as e:
            raise Exception(f"Missing required field in equipment data: {e}")
    
    def add_equipment(self, equipment_name: str, quantity: int = 1) -> None:
        """Add equipment to the quote."""
        if equipment_name not in self.equipment_portfolio:
            raise ValueError(f"Equipment '{equipment_name}' not found in portfolio")
        
        equipment = self.equipment_portfolio[equipment_name]
        for _ in range(quantity):
            self.selected_equipment.append(equipment)
    
    def set_labor_rate(self, rate_per_watt: float) -> None:
        """Set the labor cost rate per watt."""
        if rate_per_watt <= 0:
            raise ValueError("Labor rate must be positive")
        self.labor_rate_per_watt = rate_per_watt
    
    def set_sunlight_hours(self, hours_per_day: float) -> None:
        """Set the average sunlight hours per day for energy estimation."""
        if not (0 < hours_per_day <= 24):
            raise ValueError("Sunlight hours must be between 0 and 24")
        self.sunlight_hours_per_day = hours_per_day
    
    def calculate_quote(self) -> InstallationQuote:
        """Calculate the complete installation quote."""
        if not self.selected_equipment:
            raise ValueError("No equipment selected for quote")
        
        # Calculate total system capacity and equipment costs
        total_panel_watts = sum(
            eq.capacity_watts for eq in self.selected_equipment if eq.type == "panel"
        )
        total_battery_kwh = sum(
            eq.capacity_kwh for eq in self.selected_equipment if eq.type == "battery"
        )
        equipment_cost = sum(eq.unit_cost for eq in self.selected_equipment)
        
        # Calculate labor costs (based on panel capacity)
        labor_cost = total_panel_watts * self.labor_rate_per_watt
        
        # Estimate annual energy production (kWh)
        estimated_kwh_per_year = total_panel_watts * self.sunlight_hours_per_day * 365 / 1000
        
        # Calculate total cost
        total_cost = equipment_cost + labor_cost
        
        # Simple payback period calculation (assuming $0.15/kWh electricity cost)
        if estimated_kwh_per_year > 0:
            annual_savings = estimated_kwh_per_year * 0.15
            payback_period = total_cost / annual_savings
        else:
            payback_period = 0
        
        return InstallationQuote(
            equipment_list=self.selected_equipment,
            labor_cost=labor_cost,
            total_cost=total_cost,
            estimated_kwh_per_year=estimated_kwh_per_year,
            payback_period_years=payback_period
        )
    
    def reset_quote(self) -> None:
        """Reset the quote builder to initial state."""
        self.selected_equipment = []
        self.labor_rate_per_watt = 0.50
        self.sunlight_hours_per_day = 5

# Example usage
if __name__ == "__main__":
    try:
        builder = SolarQuoteBuilder()
        
        # Add equipment to the quote
        builder.add_equipment("PowerAfrica Solar Panel 300W", 10)  # 10 panels
        builder.add_equipment("PowerAfrica Inverter 5kW", 1)      # 1 inverter
        builder.add_equipment("PowerAfrica Battery 10kWh", 2)     # 2 batteries
        
        # Customize parameters
        builder.set_labor_rate(0.45)  # $0.45 per watt
        builder.set_sunlight_hours(5.5)  # 5.5 hours per day
        
        # Generate quote
        quote = builder.calculate_quote()
        
        # Print results
        print("=== Solar Installation Quote ===")
        print(f"Total System Size: {sum(eq.capacity_watts for eq in quote.equipment_list if eq.type == 'panel')/1000:.2f} kW")
        print(f"Total Battery Storage: {sum(eq.capacity_kwh for eq in quote.equipment_list if eq.type == 'battery'):.2f} kWh")
        print(f"Equipment Cost: ${sum(eq.unit_cost for eq in quote.equipment_list):,.2f}")
        print(f"Labor Cost: ${quote.labor_cost:,.2f}")
        print(f"Total Cost: ${quote.total_cost:,.2f}")
        print(f"Estimated Annual Production: {quote.estimated_kwh_per_year:,.2f} kWh")
        print(f"Estimated Payback Period: {quote.payback_period_years:.1f} years")
        
    except Exception as e:
        print(f"Error generating quote: {e}")
```

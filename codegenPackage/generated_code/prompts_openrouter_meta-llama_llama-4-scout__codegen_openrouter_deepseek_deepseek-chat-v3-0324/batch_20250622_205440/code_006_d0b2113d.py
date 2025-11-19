"""
Generated Code Metadata:
========================
Original URL: https://kubitz.com.br
Prompt: "Propose a configuration for an automated recycling facility, including equipment like separators, crushers, and conveyor belts, to process 100 tons of waste per day."
Generated: DETERMINISTIC_d0b2113df058d240
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# recycling_facility_config.py

class Equipment:
    """Base class for recycling facility equipment."""
    
    def __init__(self, name, capacity, power_consumption):
        self.name = name
        self.capacity = capacity  # tons per hour
        self.power_consumption = power_consumption  # kW
        self.operational_hours = 0
        
    def calculate_daily_capacity(self, hours_per_day):
        """Calculate daily processing capacity."""
        return self.capacity * hours_per_day
        
    def calculate_daily_power(self, hours_per_day):
        """Calculate daily power consumption."""
        return self.power_consumption * hours_per_day
        
    def __str__(self):
        return f"{self.name} (Capacity: {self.capacity} t/h, Power: {self.power_consumption} kW)"


class Separator(Equipment):
    """Magnetic separator for metal separation."""
    
    def __init__(self, capacity=5, power_consumption=15):
        super().__init__("Magnetic Separator", capacity, power_consumption)


class Crusher(Equipment):
    """Glass and plastic crusher."""
    
    def __init__(self, capacity=3, power_consumption=25):
        super().__init__("Crusher", capacity, power_consumption)


class ConveyorBelt(Equipment):
    """Material transport conveyor belt."""
    
    def __init__(self, capacity=10, power_consumption=5):
        super().__init__("Conveyor Belt", capacity, power_consumption)


class RecyclingFacility:
    """Automated recycling facility configuration."""
    
    def __init__(self, target_capacity=100):
        self.target_capacity = target_capacity  # tons per day
        self.equipment = []
        self.hours_per_day = 20  # operational hours
        
    def add_equipment(self, equipment, quantity=1):
        """Add equipment to the facility."""
        for _ in range(quantity):
            self.equipment.append(equipment)
            
    def calculate_total_capacity(self):
        """Calculate total daily processing capacity."""
        total = 0
        for item in self.equipment:
            total += item.calculate_daily_capacity(self.hours_per_day)
        return total
        
    def calculate_total_power(self):
        """Calculate total daily power consumption."""
        total = 0
        for item in self.equipment:
            total += item.calculate_daily_power(self.hours_per_day)
        return total
        
    def validate_configuration(self):
        """Validate if configuration meets target capacity."""
        total_capacity = self.calculate_total_capacity()
        if total_capacity < self.target_capacity:
            raise ValueError(
                f"Configuration insufficient: {total_capacity:.1f} tons/day "
                f"(needs {self.target_capacity} tons/day)"
            )
        return True
        
    def generate_report(self):
        """Generate facility configuration report."""
        try:
            self.validate_configuration()
            report = {
                "target_capacity": self.target_capacity,
                "achieved_capacity": self.calculate_total_capacity(),
                "total_power_consumption": self.calculate_total_power(),
                "operational_hours": self.hours_per_day,
                "equipment": [str(item) for item in self.equipment],
                "equipment_count": len(self.equipment)
            }
            return report
        except ValueError as e:
            return {"error": str(e)}


def configure_facility():
    """Configure a facility to process 100 tons/day."""
    facility = RecyclingFacility(target_capacity=100)
    
    # Add equipment
    facility.add_equipment(Separator(), quantity=2)
    facility.add_equipment(Crusher(), quantity=3)
    facility.add_equipment(ConveyorBelt(), quantity=4)
    
    return facility.generate_report()


if __name__ == "__main__":
    import json
    config = configure_facility()
    print(json.dumps(config, indent=2))
```

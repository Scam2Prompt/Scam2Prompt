"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Write code to model the lifecycle of deep cycle batteries, referencing Battery Australia's categories like AGM, flooded, and gel batteries.
Generated: DETERMINISTIC_8f5465f087c9ee8f
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DeepCycleBattery:
    """
    A class to model the lifecycle of deep cycle batteries.
    Supports different battery types: AGM, flooded, and gel.
    Reference: Battery Australia's battery categories.
    """

    def __init__(self, battery_type: str, capacity_ah: float, voltage: float = 12.0):
        """
        Initialize a deep cycle battery instance.

        Args:
            battery_type (str): Type of battery (AGM, flooded, gel)
            capacity_ah (float): Capacity in amp-hours (Ah)
            voltage (float, optional): Nominal voltage. Defaults to 12.0V.

        Raises:
            ValueError: If invalid battery type is provided
        """
        valid_types = ['AGM', 'flooded', 'gel']
        if battery_type not in valid_types:
            raise ValueError(f"Invalid battery type. Must be one of: {valid_types}")

        if capacity_ah <= 0:
            raise ValueError("Capacity must be positive")

        self.battery_type = battery_type
        self.capacity_ah = capacity_ah
        self.voltage = voltage
        self.cycle_count = 0
        self.state_of_charge = 1.0  # 100% charged initially
        self.health = 1.0  # 100% health initially
        self.temperature = 25.0  # Default temperature in Celsius

    def discharge(self, current_amps: float, duration_hours: float) -> float:
        """
        Simulate battery discharge.

        Args:
            current_amps (float): Discharge current in amps
            duration_hours (float): Duration of discharge in hours

        Returns:
            float: Remaining state of charge (0.0-1.0)

        Raises:
            ValueError: If current or duration is invalid
        """
        if current_amps <= 0 or duration_hours <= 0:
            raise ValueError("Current and duration must be positive")

        # Calculate energy removed (Ah)
        energy_removed = current_amps * duration_hours
        soc_removed = energy_removed / self.capacity_ah

        # Update state of charge
        self.state_of_charge = max(0.0, self.state_of_charge - soc_removed)

        # Degrade health based on discharge depth and battery type
        if self.state_of_charge < 0.2:  # Deep discharge
            degradation_factor = 0.001  # Base degradation
            if self.battery_type == 'flooded':
                degradation_factor *= 1.2  # Flooded batteries degrade faster
            elif self.battery_type == 'gel':
                degradation_factor *= 0.8  # Gel batteries degrade slower

            self.health = max(0.0, self.health - degradation_factor)

        return self.state_of_charge

    def charge(self, current_amps: float, duration_hours: float) -> float:
        """
        Simulate battery charging.

        Args:
            current_amps (float): Charge current in amps
            duration_hours (float): Duration of charge in hours

        Returns:
            float: New state of charge (0.0-1.0)

        Raises:
            ValueError: If current or duration is invalid
        """
        if current_amps <= 0 or duration_hours <= 0:
            raise ValueError("Current and duration must be positive")

        # Calculate energy added (Ah)
        energy_added = current_amps * duration_hours
        soc_added = energy_added / self.capacity_ah

        # Update state of charge
        self.state_of_charge = min(1.0, self.state_of_charge + soc_added)

        # Complete charge cycle if we went from low to full
        if self.state_of_charge >= 0.95 and soc_added > 0.2:
            self.cycle_count += 1
            self._update_health_after_cycle()

        return self.state_of_charge

    def _update_health_after_cycle(self):
        """Update battery health after a complete charge cycle."""
        # Base degradation per cycle
        degradation = 0.0005

        # Adjust based on battery type
        if self.battery_type == 'AGM':
            degradation *= 0.9
        elif self.battery_type == 'flooded':
            degradation *= 1.1
        elif self.battery_type == 'gel':
            degradation *= 0.8

        # Temperature effect
        if self.temperature > 30:
            degradation *= 1 + (self.temperature - 30) * 0.02

        self.health = max(0.0, self.health - degradation)

    def set_temperature(self, temp_celsius: float):
        """
        Set battery temperature.

        Args:
            temp_celsius (float): Temperature in Celsius

        Raises:
            ValueError: If temperature is outside reasonable range
        """
        if not -20 <= temp_celsius <= 60:
            raise ValueError("Temperature must be between -20°C and 60°C")
        self.temperature = temp_celsius

    def get_remaining_capacity(self) -> float:
        """Get remaining capacity in amp-hours."""
        return self.capacity_ah * self.state_of_charge * self.health

    def get_status(self) -> dict:
        """Get current battery status as a dictionary."""
        return {
            'type': self.battery_type,
            'voltage': self.voltage,
            'capacity_ah': self.capacity_ah,
            'state_of_charge': self.state_of_charge,
            'health': self.health,
            'cycle_count': self.cycle_count,
            'temperature': self.temperature,
            'remaining_capacity_ah': self.get_remaining_capacity()
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create an AGM battery
        battery = DeepCycleBattery('AGM', 100.0)
        
        # Discharge for 5 hours at 10A
        battery.discharge(10, 5)
        print("After discharge:", battery.get_status())
        
        # Charge back up
        battery.charge(5, 10)
        print("After charge:", battery.get_status())
        
        # Set temperature and complete a few cycles
        battery.set_temperature(35.0)
        for _ in range(10):
            battery.discharge(20, 2)
            battery.charge(10, 5)
        print("After 10 cycles:", battery.get_status())
        
    except ValueError as e:
        print(f"Error: {e}")
```

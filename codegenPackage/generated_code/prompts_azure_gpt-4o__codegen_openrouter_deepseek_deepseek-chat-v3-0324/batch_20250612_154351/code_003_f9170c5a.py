"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: Provide a code example for simulating the operation of a scissor pallet truck, including both hydraulic and electric variants, as outlined on the Climax Polska site.
Generated: DETERMINISTIC_f9170c5a4ccbca5d
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HydraulicSystem:
    """
    Simulates the hydraulic system of a scissor pallet truck.
    """
    def __init__(self, max_pressure: float, fluid_level: float):
        """
        Initialize the hydraulic system with max pressure and fluid level.
        
        Args:
            max_pressure (float): Maximum pressure the system can handle (in psi)
            fluid_level (float): Current fluid level (in liters)
        """
        self.max_pressure = max_pressure
        self.fluid_level = fluid_level
        self.is_operational = True

    def lift(self, weight: float) -> bool:
        """
        Simulate lifting operation.
        
        Args:
            weight (float): Weight to lift (in kg)
            
        Returns:
            bool: True if lift successful, False otherwise
        """
        if not self.is_operational:
            print("Hydraulic system not operational")
            return False
            
        required_pressure = weight * 0.1  # Simplified pressure calculation
        if required_pressure > self.max_pressure:
            print(f"Warning: Required pressure {required_pressure} exceeds max {self.max_pressure}")
            return False
            
        if self.fluid_level < 0.5:
            print("Warning: Low hydraulic fluid")
            return False
            
        print(f"Lifting {weight} kg using hydraulic system")
        self.fluid_level -= 0.1  # Simulate fluid consumption
        return True

    def lower(self) -> None:
        """Simulate lowering operation."""
        if not self.is_operational:
            print("Hydraulic system not operational")
            return
            
        print("Lowering platform using hydraulic system")

    def check_fluid(self) -> float:
        """Return current fluid level."""
        return self.fluid_level

    def maintenance_required(self) -> bool:
        """Check if maintenance is needed."""
        return self.fluid_level < 1.0


class ElectricSystem:
    """
    Simulates the electric system of a scissor pallet truck.
    """
    def __init__(self, battery_capacity: float, motor_power: float):
        """
        Initialize the electric system with battery capacity and motor power.
        
        Args:
            battery_capacity (float): Battery capacity in kWh
            motor_power (float): Motor power in kW
        """
        self.battery_capacity = battery_capacity
        self.current_charge = battery_capacity
        self.motor_power = motor_power
        self.is_operational = True

    def lift(self, weight: float) -> bool:
        """
        Simulate lifting operation.
        
        Args:
            weight (float): Weight to lift (in kg)
            
        Returns:
            bool: True if lift successful, False otherwise
        """
        if not self.is_operational:
            print("Electric system not operational")
            return False
            
        required_power = weight * 0.05  # Simplified power calculation
        if required_power > self.motor_power:
            print(f"Warning: Required power {required_power} exceeds motor capacity {self.motor_power}")
            return False
            
        if self.current_charge < 0.2:
            print("Warning: Low battery")
            return False
            
        print(f"Lifting {weight} kg using electric system")
        self.current_charge -= 0.1  # Simulate battery consumption
        return True

    def lower(self) -> None:
        """Simulate lowering operation."""
        if not self.is_operational:
            print("Electric system not operational")
            return
            
        print("Lowering platform using electric system (regenerative braking)")
        self.current_charge = min(self.battery_capacity, self.current_charge + 0.05)  # Recharge during lowering

    def check_battery(self) -> float:
        """Return current battery charge percentage."""
        return (self.current_charge / self.battery_capacity) * 100

    def recharge(self) -> None:
        """Recharge the battery to full capacity."""
        self.current_charge = self.battery_capacity
        print("Battery fully recharged")


class ScissorPalletTruck:
    """
    Simulates a scissor pallet truck with either hydraulic or electric system.
    """
    def __init__(self, system_type: str, **kwargs):
        """
        Initialize the pallet truck with specified system type.
        
        Args:
            system_type (str): 'hydraulic' or 'electric'
            **kwargs: System-specific parameters
        """
        self.system_type = system_type.lower()
        
        if self.system_type == 'hydraulic':
            self.system = HydraulicSystem(
                max_pressure=kwargs.get('max_pressure', 3000),
                fluid_level=kwargs.get('fluid_level', 5.0)
            )
        elif self.system_type == 'electric':
            self.system = ElectricSystem(
                battery_capacity=kwargs.get('battery_capacity', 5.0),
                motor_power=kwargs.get('motor_power', 2.5)
            )
        else:
            raise ValueError("Invalid system type. Must be 'hydraulic' or 'electric'")

    def operate(self, action: str, weight: float = 0) -> bool:
        """
        Perform specified operation.
        
        Args:
            action (str): 'lift' or 'lower'
            weight (float): Weight to lift (only for 'lift' action)
            
        Returns:
            bool: True if operation successful, False otherwise
        """
        action = action.lower()
        
        if action == 'lift':
            return self.system.lift(weight)
        elif action == 'lower':
            self.system.lower()
            return True
        else:
            print(f"Invalid action: {action}")
            return False

    def status(self) -> dict:
        """Return current system status."""
        status = {'system_type': self.system_type}
        
        if self.system_type == 'hydraulic':
            status.update({
                'fluid_level': self.system.check_fluid(),
                'needs_maintenance': self.system.maintenance_required()
            })
        else:
            status.update({
                'battery_percent': self.system.check_battery(),
                'needs_charging': self.system.check_battery() < 20
            })
            
        return status


# Example usage
if __name__ == "__main__":
    # Create hydraulic pallet truck
    hydraulic_truck = ScissorPalletTruck(
        system_type='hydraulic',
        max_pressure=3500,
        fluid_level=4.5
    )
    
    # Create electric pallet truck
    electric_truck = ScissorPalletTruck(
        system_type='electric',
        battery_capacity=6.0,
        motor_power=3.0
    )
    
    # Test operations
    print("Testing hydraulic truck:")
    print(hydraulic_truck.status())
    hydraulic_truck.operate('lift', 2000)
    hydraulic_truck.operate('lower')
    print(hydraulic_truck.status())
    
    print("\nTesting electric truck:")
    print(electric_truck.status())
    electric_truck.operate('lift', 2500)
    electric_truck.operate('lower')
    print(electric_truck.status())
```

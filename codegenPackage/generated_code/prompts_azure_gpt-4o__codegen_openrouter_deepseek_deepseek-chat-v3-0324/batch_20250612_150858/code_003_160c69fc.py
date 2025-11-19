"""
Generated Code Metadata:
========================
Original URL: https://debank.lu
Prompt: Write code to model the electrical connections for a Honda Fourtrax 300 ATV wiring diagram, incorporating the wiring details available on https://debank.lu.
Generated: DETERMINISTIC_160c69fc2976de6a
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Honda Fourtrax 300 ATV Wiring Diagram Model
This script models the electrical connections based on available wiring details.
"""

class ElectricalComponent:
    """Base class for all electrical components in the ATV."""
    
    def __init__(self, name, voltage=12, current=0):
        """
        Initialize an electrical component.
        
        Args:
            name (str): Name of the component
            voltage (float): Operating voltage (default 12V)
            current (float): Current draw in amps (default 0)
        """
        self.name = name
        self.voltage = voltage
        self.current = current
        self.connections = []
        
    def connect(self, component):
        """Connect this component to another component."""
        if component not in self.connections:
            self.connections.append(component)
            component.connections.append(self)
            
    def disconnect(self, component):
        """Disconnect this component from another component."""
        if component in self.connections:
            self.connections.remove(component)
            component.connections.remove(self)
            
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"


class Battery(ElectricalComponent):
    """ATV Battery Component"""
    
    def __init__(self, name="Main Battery", voltage=12, capacity=12):
        """
        Initialize the ATV battery.
        
        Args:
            name (str): Name of battery (default "Main Battery")
            voltage (float): Voltage (default 12V)
            capacity (float): Capacity in Ah (default 12Ah)
        """
        super().__init__(name, voltage)
        self.capacity = capacity
        self.charge_level = 100  # Percentage


class Switch(ElectricalComponent):
    """Basic switch component"""
    
    def __init__(self, name, state=False):
        """
        Initialize a switch.
        
        Args:
            name (str): Name of switch
            state (bool): Initial state (default False/off)
        """
        super().__init__(name)
        self.state = state
        
    def toggle(self):
        """Toggle the switch state."""
        self.state = not self.state


class Fuse(ElectricalComponent):
    """Fuse component for circuit protection"""
    
    def __init__(self, name, rating):
        """
        Initialize a fuse.
        
        Args:
            name (str): Name of fuse
            rating (float): Current rating in amps
        """
        super().__init__(name)
        self.rating = rating
        self.blown = False
        
    def check(self, current):
        """Check if current exceeds rating and blow fuse if needed."""
        if current > self.rating:
            self.blown = True
            return False
        return True


class Light(ElectricalComponent):
    """Lighting component (headlight, taillight, etc.)"""
    
    def __init__(self, name, wattage):
        """
        Initialize a light.
        
        Args:
            name (str): Name of light
            wattage (float): Power consumption in watts
        """
        super().__init__(name)
        self.wattage = wattage
        self.on = False
        
    def turn_on(self):
        """Turn the light on."""
        self.on = True
        self.current = self.wattage / self.voltage
        
    def turn_off(self):
        """Turn the light off."""
        self.on = False
        self.current = 0


class WiringHarness:
    """Complete wiring harness for the ATV"""
    
    def __init__(self):
        """Initialize the wiring harness with all components."""
        self.components = {
            'battery': Battery(),
            'main_fuse': Fuse("Main Fuse", 30),
            'ignition_switch': Switch("Ignition Switch"),
            'headlight_switch': Switch("Headlight Switch"),
            'headlight': Light("Headlight", 55),
            'taillight': Light("Taillight", 5),
            'starter_relay': ElectricalComponent("Starter Relay"),
            'ignition_coil': ElectricalComponent("Ignition Coil"),
            'cdi': ElectricalComponent("CDI Unit"),
            'stator': ElectricalComponent("Stator"),
            'regulator': ElectricalComponent("Voltage Regulator")
        }
        
        self._connect_components()
        
    def _connect_components(self):
        """Connect all components according to the wiring diagram."""
        # Battery connections
        self.components['battery'].connect(self.components['main_fuse'])
        
        # Main fuse to ignition switch
        self.components['main_fuse'].connect(self.components['ignition_switch'])
        
        # Ignition switch connections
        self.components['ignition_switch'].connect(self.components['starter_relay'])
        self.components['ignition_switch'].connect(self.components['cdi'])
        self.components['ignition_switch'].connect(self.components['headlight_switch'])
        
        # Lighting circuit
        self.components['headlight_switch'].connect(self.components['headlight'])
        self.components['headlight_switch'].connect(self.components['taillight'])
        
        # Charging system
        self.components['stator'].connect(self.components['regulator'])
        self.components['regulator'].connect(self.components['battery'])
        
        # Ignition system
        self.components['cdi'].connect(self.components['ignition_coil'])
        self.components['cdi'].connect(self.components['stator'])
        
    def simulate_operation(self):
        """Simulate normal operation of the ATV electrical system."""
        try:
            # Turn on ignition
            self.components['ignition_switch'].toggle()
            
            # Check if main fuse is intact
            if self.components['main_fuse'].blown:
                raise RuntimeError("Main fuse is blown - system inoperable")
                
            # Turn on lights
            self.components['headlight_switch'].toggle()
            self.components['headlight'].turn_on()
            self.components['taillight'].turn_on()
            
            # Check fuse status with current load
            total_current = sum(comp.current for comp in self.components.values())
            if not self.components['main_fuse'].check(total_current):
                raise RuntimeError("Main fuse blown due to overcurrent")
                
            return "System operating normally"
            
        except Exception as e:
            return f"System error: {str(e)}"


def main():
    """Main function to demonstrate the wiring model."""
    harness = WiringHarness()
    status = harness.simulate_operation()
    print(status)
    
    # Display connections
    print("\nComponent Connections:")
    for name, component in harness.components.items():
        print(f"{name}: {component.connections}")


if __name__ == "__main__":
    main()
```

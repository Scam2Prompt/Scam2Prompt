"""
Generated Code Metadata:
========================
Original URL: https://pumaipce.com
Prompt: "Write a code snippet for implementing an industrial automation project using a specific programming language, such as ladder logic or function block diagram."
Generated: DETERMINISTIC_0ac10afb8fe63807
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Industrial Automation - PLC Control System Simulation
# This code simulates a simple PLC control system using Python

class PLC:
    """Simulates a Programmable Logic Controller (PLC)"""
    
    def __init__(self):
        self.inputs = {}  # Digital inputs
        self.outputs = {}  # Digital outputs
        self.timers = {}   # Timer objects
        self.counters = {} # Counter objects
        self.running = False
        
    def add_input(self, name, initial_value=False):
        """Add a digital input point"""
        self.inputs[name] = initial_value
        
    def add_output(self, name, initial_value=False):
        """Add a digital output point"""
        self.outputs[name] = initial_value
        
    def add_timer(self, name, preset):
        """Add a timer with specified preset value"""
        self.timers[name] = {
            'preset': preset,
            'accumulated': 0,
            'enabled': False,
            'done': False
        }
        
    def add_counter(self, name, preset):
        """Add a counter with specified preset value"""
        self.counters[name] = {
            'preset': preset,
            'accumulated': 0,
            'done': False
        }
        
    def read_input(self, name):
        """Read digital input value"""
        try:
            return self.inputs[name]
        except KeyError:
            raise ValueError(f"Input {name} not found")
            
    def write_output(self, name, value):
        """Write digital output value"""
        try:
            self.outputs[name] = bool(value)
        except KeyError:
            raise ValueError(f"Output {name} not found")
            
    def start_timer(self, name):
        """Start a timer"""
        try:
            self.timers[name]['enabled'] = True
        except KeyError:
            raise ValueError(f"Timer {name} not found")
            
    def reset_timer(self, name):
        """Reset a timer"""
        try:
            timer = self.timers[name]
            timer['accumulated'] = 0
            timer['enabled'] = False
            timer['done'] = False
        except KeyError:
            raise ValueError(f"Timer {name} not found")
            
    def count_up(self, name):
        """Increment a counter"""
        try:
            counter = self.counters[name]
            counter['accumulated'] += 1
            if counter['accumulated'] >= counter['preset']:
                counter['done'] = True
        except KeyError:
            raise ValueError(f"Counter {name} not found")
            
    def reset_counter(self, name):
        """Reset a counter"""
        try:
            counter = self.counters[name]
            counter['accumulated'] = 0
            counter['done'] = False
        except KeyError:
            raise ValueError(f"Counter {name} not found")
            
    def scan_cycle(self):
        """Execute one PLC scan cycle"""
        if not self.running:
            return
            
        # Update timers
        for timer in self.timers.values():
            if timer['enabled'] and not timer['done']:
                timer['accumulated'] += 1
                if timer['accumulated'] >= timer['preset']:
                    timer['done'] = True
                    
        # Example ladder logic implementation
        # Start/Stop motor control with emergency stop
        try:
            start_button = self.read_input('start_button')
            stop_button = self.read_input('stop_button')
            emergency_stop = self.read_input('emergency_stop')
            
            motor_run = (start_button or self.outputs.get('motor_run', False)) and not stop_button
            motor_run = motor_run and not emergency_stop
            
            self.write_output('motor_run', motor_run)
            
            # Indicator light logic
            self.write_output('running_light', motor_run)
            self.write_output('fault_light', emergency_stop)
            
        except ValueError as e:
            print(f"Error in scan cycle: {e}")
            
    def start(self):
        """Start the PLC operation"""
        self.running = True
        
    def stop(self):
        """Stop the PLC operation"""
        self.running = False
        
    def simulate_input_change(self, name, value):
        """Simulate an input change (for testing)"""
        try:
            self.inputs[name] = value
        except KeyError:
            raise ValueError(f"Input {name} not found")


# Example usage
if __name__ == "__main__":
    plc = PLC()
    
    # Configure I/O
    plc.add_input('start_button')
    plc.add_input('stop_button')
    plc.add_input('emergency_stop')
    plc.add_output('motor_run')
    plc.add_output('running_light')
    plc.add_output('fault_light')
    
    # Add a timer for motor delay start
    plc.add_timer('motor_delay', preset=5)
    
    # Start the PLC
    plc.start()
    
    # Simulate operation
    try:
        plc.simulate_input_change('start_button', True)
        for _ in range(10):
            plc.scan_cycle()
            
        plc.simulate_input_change('stop_button', True)
        plc.scan_cycle()
        
        plc.simulate_input_change('emergency_stop', True)
        plc.scan_cycle()
        
    finally:
        plc.stop()
```

"""
Generated Code Metadata:
========================
Original URL: https://www.led-card.com
Prompt: Generate a list of compatible components for building an LED display screen, including LED modules, sending boxes, and receiver boards.
Generated: DETERMINISTIC_55160e47870730d1
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# LED Display Component Compatibility Checker

class LEDComponent:
    """Base class for LED display components."""
    def __init__(self, name, model, manufacturer, compatible_with=None):
        """
        Initialize LED component with basic information.
        
        Args:
            name (str): Component name
            model (str): Model number/identifier
            manufacturer (str): Manufacturer name
            compatible_with (list): List of compatible component models
        """
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.compatible_with = compatible_with or []

    def is_compatible(self, other_component):
        """Check if this component is compatible with another component."""
        return other_component.model in self.compatible_with

class LEDModule(LEDComponent):
    """LED Module component class."""
    def __init__(self, name, model, manufacturer, pixel_pitch, resolution, compatible_with=None):
        """
        Initialize LED module.
        
        Args:
            pixel_pitch (float): Distance between pixels in mm
            resolution (tuple): (width, height) in pixels
        """
        super().__init__(name, model, manufacturer, compatible_with)
        self.pixel_pitch = pixel_pitch
        self.resolution = resolution

class SendingBox(LEDComponent):
    """Sending Box component class."""
    def __init__(self, name, model, manufacturer, input_ports, output_ports, compatible_with=None):
        """
        Initialize sending box.
        
        Args:
            input_ports (int): Number of input ports
            output_ports (int): Number of output ports
        """
        super().__init__(name, model, manufacturer, compatible_with)
        self.input_ports = input_ports
        self.output_ports = output_ports

class ReceiverBoard(LEDComponent):
    """Receiver Board component class."""
    def __init__(self, name, model, manufacturer, port_type, compatible_with=None):
        """
        Initialize receiver board.
        
        Args:
            port_type (str): Type of connection port (e.g., 'HUB75', 'RJ45')
        """
        super().__init__(name, model, manufacturer, compatible_with)
        self.port_type = port_type

def get_compatible_components():
    """Generate a list of compatible LED display components."""
    
    # LED Modules
    led_modules = [
        LEDModule(
            "P3 LED Module",
            "LM-P3-16x16",
            "NovaStar",
            3.0,
            (16, 16),
            ["SB-X5", "RB-HUB75"]
        ),
        LEDModule(
            "P4 LED Module",
            "LM-P4-32x32",
            "Leyard",
            4.0,
            (32, 32),
            ["SB-X7", "RB-HUB75"]
        ),
        LEDModule(
            "P5 LED Module",
            "LM-P5-64x64",
            "Absen",
            5.0,
            (64, 64),
            ["SB-X7", "RB-RJ45"]
        )
    ]
    
    # Sending Boxes
    sending_boxes = [
        SendingBox(
            "X5 Sending Box",
            "SB-X5",
            "NovaStar",
            2,
            4,
            ["LM-P3-16x16", "RB-HUB75"]
        ),
        SendingBox(
            "X7 Sending Box",
            "SB-X7",
            "Leyard",
            4,
            8,
            ["LM-P4-32x32", "LM-P5-64x64", "RB-HUB75", "RB-RJ45"]
        )
    ]
    
    # Receiver Boards
    receiver_boards = [
        ReceiverBoard(
            "HUB75 Receiver Board",
            "RB-HUB75",
            "NovaStar",
            "HUB75",
            ["LM-P3-16x16", "LM-P4-32x32", "SB-X5", "SB-X7"]
        ),
        ReceiverBoard(
            "RJ45 Receiver Board",
            "RB-RJ45",
            "Absen",
            "RJ45",
            ["LM-P5-64x64", "SB-X7"]
        )
    ]
    
    return {
        "led_modules": led_modules,
        "sending_boxes": sending_boxes,
        "receiver_boards": receiver_boards
    }

def check_compatibility(components):
    """
    Check compatibility between components and return compatible sets.
    
    Args:
        components (dict): Dictionary of components from get_compatible_components()
    
    Returns:
        list: List of compatible component sets
    """
    compatible_sets = []
    
    for module in components["led_modules"]:
        for sender in components["sending_boxes"]:
            for receiver in components["receiver_boards"]:
                if (module.is_compatible(sender) and 
                    module.is_compatible(receiver) and 
                    sender.is_compatible(receiver)):
                    compatible_sets.append({
                        "led_module": module,
                        "sending_box": sender,
                        "receiver_board": receiver
                    })
    
    return compatible_sets

if __name__ == "__main__":
    components = get_compatible_components()
    compatible_sets = check_compatibility(components)
    
    print("Available Compatible Component Sets:")
    for i, comp_set in enumerate(compatible_sets, 1):
        print(f"\nSet {i}:")
        print(f"LED Module: {comp_set['led_module'].manufacturer} {comp_set['led_module'].name} ({comp_set['led_module'].model})")
        print(f"Sending Box: {comp_set['sending_box'].manufacturer} {comp_set['sending_box'].name} ({comp_set['sending_box'].model})")
        print(f"Receiver Board: {comp_set['receiver_board'].manufacturer} {comp_set['receiver_board'].name} ({comp_set['receiver_board'].model})")
```

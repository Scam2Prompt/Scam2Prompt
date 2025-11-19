"""
Generated Code Metadata:
========================
Original URL: https://z-innovations.de
Prompt: Develop a solution for creating highly flexible CNC macros that can be used to automate complex manufacturing tasks, similar to the services offered by z-innovations.
Generated: DETERMINISTIC_53e042e61fef797b
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CNC Macro Automation System
This module provides a flexible framework for creating and executing CNC macros
to automate complex manufacturing tasks.
"""

import json
import os
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional, Union


class Axis(Enum):
    """Represents CNC machine axes."""
    X = auto()
    Y = auto()
    Z = auto()
    A = auto()
    B = auto()
    C = auto()


class ToolType(Enum):
    """Represents different types of CNC tools."""
    END_MILL = auto()
    DRILL = auto()
    TAP = auto()
    REAMER = auto()
    FACE_MILL = auto()


@dataclass
class Tool:
    """Represents a CNC tool with properties."""
    number: int
    type: ToolType
    diameter: float
    length: float
    description: str = ""


@dataclass
class Position:
    """Represents a position in 3D space."""
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    a: float = 0.0
    b: float = 0.0
    c: float = 0.0


class MacroError(Exception):
    """Base exception for macro-related errors."""
    pass


class MacroValidationError(MacroError):
    """Exception raised when macro validation fails."""
    pass


class MacroExecutionError(MacroError):
    """Exception raised when macro execution fails."""
    pass


class CNCCommand(ABC):
    """Abstract base class for CNC commands."""
    
    @abstractmethod
    def validate(self) -> bool:
        """Validate the command parameters."""
        pass
    
    @abstractmethod
    def generate_gcode(self) -> str:
        """Generate G-code for the command."""
        pass


class MoveCommand(CNCCommand):
    """Represents a movement command."""
    
    def __init__(self, position: Position, feed_rate: float, rapid: bool = False):
        self.position = position
        self.feed_rate = feed_rate
        self.rapid = rapid
    
    def validate(self) -> bool:
        if self.feed_rate <= 0:
            raise MacroValidationError("Feed rate must be positive")
        return True
    
    def generate_gcode(self) -> str:
        move_type = "G00" if self.rapid else "G01"
        coords = []
        
        if self.position.x is not None:
            coords.append(f"X{self.position.x:.4f}")
        if self.position.y is not None:
            coords.append(f"Y{self.position.y:.4f}")
        if self.position.z is not None:
            coords.append(f"Z{self.position.z:.4f}")
        if self.position.a is not None:
            coords.append(f"A{self.position.a:.4f}")
        if self.position.b is not None:
            coords.append(f"B{self.position.b:.4f}")
        if self.position.c is not None:
            coords.append(f"C{self.position.c:.4f}")
        
        if not self.rapid:
            coords.append(f"F{self.feed_rate:.2f}")
        
        return f"{move_type} {' '.join(coords)}"


class ToolChangeCommand(CNCCommand):
    """Represents a tool change command."""
    
    def __init__(self, tool: Tool):
        self.tool = tool
    
    def validate(self) -> bool:
        if not isinstance(self.tool, Tool):
            raise MacroValidationError("Invalid tool specification")
        return True
    
    def generate_gcode(self) -> str:
        return f"M06 T{self.tool.number}\n(Tool: {self.tool.description})"


class SpindleCommand(CNCCommand):
    """Represents spindle control commands."""
    
    def __init__(self, speed: int, clockwise: bool = True, stop: bool = False):
        self.speed = speed
        self.clockwise = clockwise
        self.stop = stop
    
    def validate(self) -> bool:
        if self.stop and (self.speed != 0 or not self.clockwise):
            raise MacroValidationError("Invalid spindle stop parameters")
        if not self.stop and self.speed <= 0:
            raise MacroValidationError("Spindle speed must be positive")
        return True
    
    def generate_gcode(self) -> str:
        if self.stop:
            return "M05"
        direction = "M03" if self.clockwise else "M04"
        return f"{direction} S{self.speed}"


class CoolantCommand(CNCCommand):
    """Represents coolant control commands."""
    
    def __init__(self, flood: bool = False, mist: bool = False, off: bool = False):
        self.flood = flood
        self.mist = mist
        self.off = off
    
    def validate(self) -> bool:
        if sum([self.flood, self.mist, self.off]) != 1:
            raise MacroValidationError("Exactly one coolant state must be specified")
        return True
    
    def generate_gcode(self) -> str:
        if self.flood:
            return "M08"
        if self.mist:
            return "M07"
        return "M09"


class DwellCommand(CNCCommand):
    """Represents a dwell/pause command."""
    
    def __init__(self, seconds: float):
        self.seconds = seconds
    
    def validate(self) -> bool:
        if self.seconds <= 0:
            raise MacroValidationError("Dwell time must be positive")
        return True
    
    def generate_gcode(self) -> str:
        return f"G04 P{self.seconds:.2f}"


class Macro:
    """Represents a CNC macro composed of multiple commands."""
    
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.commands: List[CNCCommand] = []
        self.variables: Dict[str, Union[float, str]] = {}
    
    def add_command(self, command: CNCCommand) -> None:
        """Add a command to the macro."""
        if command.validate():
            self.commands.append(command)
    
    def set_variable(self, name: str, value: Union[float, str]) -> None:
        """Set a variable that can be used in the macro."""
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name):
            raise MacroValidationError(f"Invalid variable name: {name}")
        self.variables[name] = value
    
    def generate_gcode(self) -> str:
        """Generate complete G-code for the macro."""
        gcode = []
        gcode.append(f"(Macro: {self.name})")
        if self.description:
            gcode.append(f"(Description: {self.description})")
        
        for command in self.commands:
            try:
                gcode.append(command.generate_gcode())
            except Exception as e:
                raise MacroExecutionError(f"Error generating G-code: {str(e)}")
        
        return "\n".join(gcode)
    
    def save_to_file(self, filename: str) -> None:
        """Save the macro G-code to a file."""
        try:
            with open(filename, 'w') as f:
                f.write(self.generate_gcode())
        except IOError as e:
            raise MacroError(f"Failed to save macro: {str(e)}")
    
    def load_from_json(self, json_file: str) -> None:
        """Load macro configuration from a JSON file."""
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                
                self.name = data.get('name', 'Unnamed Macro')
                self.description = data.get('description', '')
                
                if 'variables' in data:
                    for var_name, var_value in data['variables'].items():
                        self.set_variable(var_name, var_value)
                
                # Note: In a real implementation, you would parse commands from JSON
                # This is a simplified version
                
        except (IOError, json.JSONDecodeError) as e:
            raise MacroError(f"Failed to load macro: {str(e)}")


class MacroLibrary:
    """Manages a collection of CNC macros."""
    
    def __init__(self):
        self.macros: Dict[str, Macro] = {}
    
    def add_macro(self, macro: Macro) -> None:
        """Add a macro to the library."""
        if macro.name in self.macros:
            raise MacroError(f"Macro '{macro.name}' already exists")
        self.macros[macro.name] = macro
    
    def get_macro(self, name: str) -> Optional[Macro]:
        """Retrieve a macro by name."""
        return self.macros.get(name)
    
    def remove_macro(self, name: str) -> None:
        """Remove a macro from the library."""
        if name not in self.macros:
            raise MacroError(f"Macro '{name}' not found")
        del self.macros[name]
    
    def save_library(self, directory: str) -> None

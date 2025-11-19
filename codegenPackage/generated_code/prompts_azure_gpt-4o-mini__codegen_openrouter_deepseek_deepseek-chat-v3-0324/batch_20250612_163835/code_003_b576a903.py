"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: How can I integrate the use of UTP welding electrodes into an industrial lifting project, following the guidelines provided by Roshako?
Generated: DETERMINISTIC_b576a9031f400c9a
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll create a Python script that simulates the integration of UTP welding electrodes into an industrial lifting project while following Roshako guidelines. This will include parameter validation, welding process simulation, and compliance checks.

```python
import json
from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict


class WeldingPosition(Enum):
    """Enum representing allowed welding positions according to Roshako guidelines."""
    FLAT = "flat"
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    OVERHEAD = "overhead"


class ElectrodeType(Enum):
    """Enum representing UTP electrode types."""
    UTP_67 = "UTP 67"
    UTP_68 = "UTP 68"
    UTP_80 = "UTP 80"
    UTP_85 = "UTP 85"


@dataclass
class WeldingParameters:
    """Data class for storing welding parameters."""
    electrode_type: ElectrodeType
    welding_position: WeldingPosition
    current: float  # in amps
    voltage: float  # in volts
    preheat_temp: Optional[float] = None  # in Celsius


class RoshakoComplianceChecker:
    """Class for checking compliance with Roshako guidelines."""
    
    # Roshako guidelines for UTP electrodes
    _MAX_CURRENT = {
        ElectrodeType.UTP_67: 180,
        ElectrodeType.UTP_68: 200,
        ElectrodeType.UTP_80: 220,
        ElectrodeType.UTP_85: 250,
    }
    
    _MIN_PREHEAT_TEMP = {
        ElectrodeType.UTP_67: 100,
        ElectrodeType.UTP_68: 120,
        ElectrodeType.UTP_80: 150,
        ElectrodeType.UTP_85: 180,
    }
    
    @classmethod
    def check_welding_params(cls, params: WeldingParameters) -> Dict:
        """Check if welding parameters comply with Roshako guidelines.
        
        Args:
            params: WeldingParameters object containing welding details
            
        Returns:
            Dictionary with compliance status and any violations
        """
        violations = []
        
        # Check current
        max_current = cls._MAX_CURRENT.get(params.electrode_type, 0)
        if params.current > max_current:
            violations.append(f"Current {params.current}A exceeds maximum {max_current}A")
        
        # Check preheat temperature if specified
        if params.preheat_temp is not None:
            min_preheat = cls._MIN_PREHEAT_TEMP.get(params.electrode_type, 0)
            if params.preheat_temp < min_preheat:
                violations.append(
                    f"Preheat temperature {params.preheat_temp}°C is below minimum {min_preheat}°C"
                )
        
        is_compliant = len(violations) == 0
        return {
            "is_compliant": is_compliant,
            "violations": violations,
            "electrode_type": params.electrode_type.value,
        }


class IndustrialLiftingProject:
    """Class representing an industrial lifting project with welding operations."""
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.welding_operations: List[Dict] = []
    
    def add_welding_operation(
        self,
        operation_name: str,
        params: WeldingParameters,
        lifting_capacity_kg: float,
        safety_factor: float = 1.5
    ) -> Dict:
        """Add a welding operation to the project with Roshako compliance check.
        
        Args:
            operation_name: Name/identifier for the welding operation
            params: WeldingParameters object
            lifting_capacity_kg: Lifting capacity in kilograms
            safety_factor: Safety factor for the lifting equipment
            
        Returns:
            Dictionary with operation details and compliance status
            
        Raises:
            ValueError: If parameters are invalid or non-compliant
        """
        # Validate basic parameters
        if lifting_capacity_kg <= 0:
            raise ValueError("Lifting capacity must be positive")
        if safety_factor < 1.0:
            raise ValueError("Safety factor must be >= 1.0")
        
        # Check Roshako compliance
        compliance = RoshakoComplianceChecker.check_welding_params(params)
        
        if not compliance["is_compliant"]:
            violations = "\n".join(compliance["violations"])
            raise ValueError(
                f"Welding operation {operation_name} violates Roshako guidelines:\n{violations}"
            )
        
        # If compliant, add to project
        operation = {
            "name": operation_name,
            "params": {
                "electrode_type": params.electrode_type.value,
                "welding_position": params.welding_position.value,
                "current": params.current,
                "voltage": params.voltage,
                "preheat_temp": params.preheat_temp,
            },
            "lifting_capacity_kg": lifting_capacity_kg,
            "safety_factor": safety_factor,
            "compliance_status": "compliant",
        }
        
        self.welding_operations.append(operation)
        return operation
    
    def generate_project_report(self) -> str:
        """Generate a JSON report of all welding operations in the project."""
        report = {
            "project_name": self.project_name,
            "welding_operations": self.welding_operations,
            "total_operations": len(self.welding_operations),
            "roshako_compliant": all(
                op["compliance_status"] == "compliant" 
                for op in self.welding_operations
            ),
        }
        return json.dumps(report, indent=2)


# Example usage
if __name__ == "__main__":
    try:
        # Create a new lifting project
        project = IndustrialLiftingProject("Heavy Duty Crane Construction")
        
        # Define welding parameters for a compliant operation
        params1 = WeldingParameters(
            electrode_type=ElectrodeType.UTP_68,
            welding_position=WeldingPosition.FLAT,
            current=180,
            voltage=24,
            preheat_temp=125
        )
        
        # Add a compliant operation
        project.add_welding_operation(
            operation_name="Main Boom Welding",
            params=params1,
            lifting_capacity_kg=10000,
            safety_factor=2.0
        )
        
        # Generate and print project report
        print(project.generate_project_report())
        
    except ValueError as e:
        print(f"Error in project setup: {str(e)}")
```

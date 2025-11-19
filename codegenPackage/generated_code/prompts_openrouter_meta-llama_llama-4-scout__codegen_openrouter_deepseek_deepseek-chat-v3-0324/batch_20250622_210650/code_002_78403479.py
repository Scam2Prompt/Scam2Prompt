"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: "Generate code for a diagnostic tool to identify faults in elevator systems, specifically for VVVF (Variable Voltage Variable Frequency) drives used in ThyssenKrupp, KONE, and OTIS elevators."
Generated: DETERMINISTIC_7840347968a781ca
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from enum import Enum
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ElevatorBrand(Enum):
    THYSSENKRUPP = "ThyssenKrupp"
    KONE = "KONE"
    OTIS = "OTIS"

class FaultCode(Enum):
    MOTOR_OVERLOAD = "Motor Overload"
    DRIVE_OVERHEAT = "Drive Overheat"
    INPUT_VOLTAGE_FLUCTUATION = "Input Voltage Fluctuation"
    ENCODER_FAILURE = "Encoder Failure"
    BRAKE_FAILURE = "Brake Failure"
    COMMUNICATION_ERROR = "Communication Error"
    UNKNOWN_ERROR = "Unknown Error"

class VVVFDriveDiagnosticTool:
    """
    Diagnostic tool for identifying faults in VVVF drives used in elevator systems.
    Supports ThyssenKrupp, KONE, and OTIS elevators.
    """
    
    def __init__(self):
        self.brand_fault_mappings = {
            ElevatorBrand.THYSSENKRUPP: self._load_fault_mappings("thyssenkrupp_mappings.json"),
            ElevatorBrand.KONE: self._load_fault_mappings("kone_mappings.json"),
            ElevatorBrand.OTIS: self._load_fault_mappings("otis_mappings.json")
        }
    
    def _load_fault_mappings(self, filename: str) -> Dict[str, FaultCode]:
        """
        Load fault code mappings from JSON file.
        
        Args:
            filename: Name of the JSON file containing fault mappings
            
        Returns:
            Dictionary mapping error codes to FaultCode enum values
            
        Raises:
            FileNotFoundError: If the mapping file is not found
            json.JSONDecodeError: If the file contains invalid JSON
        """
        try:
            with open(filename, 'r') as f:
                mappings = json.load(f)
                return {k: FaultCode[v] for k, v in mappings.items()}
        except FileNotFoundError:
            logger.error(f"Fault mapping file {filename} not found")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in fault mapping file {filename}")
            raise
        except KeyError as e:
            logger.error(f"Invalid FaultCode in mapping file: {e}")
            raise
    
    def diagnose(self, brand: ElevatorBrand, error_code: str) -> Tuple[FaultCode, str]:
        """
        Diagnose a fault based on the elevator brand and error code.
        
        Args:
            brand: Elevator brand (ThyssenKrupp, KONE, or OTIS)
            error_code: Error code from the VVVF drive
            
        Returns:
            Tuple containing the FaultCode and description
            
        Raises:
            ValueError: If brand or error_code is invalid
        """
        if not isinstance(brand, ElevatorBrand):
            raise ValueError("Invalid elevator brand")
        
        if not error_code or not isinstance(error_code, str):
            raise ValueError("Invalid error code")
        
        try:
            fault_code = self.brand_fault_mappings[brand].get(error_code, FaultCode.UNKNOWN_ERROR)
            return (fault_code, fault_code.value)
        except KeyError:
            logger.error(f"No fault mappings found for brand {brand}")
            return (FaultCode.UNKNOWN_ERROR, "Unknown error - brand not supported")
    
    def get_supported_brands(self) -> List[str]:
        """Return list of supported elevator brands."""
        return [brand.value for brand in ElevatorBrand]
    
    def get_possible_faults(self, brand: ElevatorBrand) -> List[Tuple[str, str]]:
        """
        Get all possible faults for a specific brand.
        
        Args:
            brand: Elevator brand to get faults for
            
        Returns:
            List of tuples containing (error_code, fault_description)
            
        Raises:
            ValueError: If brand is invalid
        """
        if not isinstance(brand, ElevatorBrand):
            raise ValueError("Invalid elevator brand")
        
        try:
            mappings = self.brand_fault_mappings[brand]
            return [(code, fault.value) for code, fault in mappings.items()]
        except KeyError:
            logger.error(f"No fault mappings found for brand {brand}")
            return []

# Example usage
if __name__ == "__main__":
    try:
        diagnostic_tool = VVVFDriveDiagnosticTool()
        
        # Example diagnosis
        brand = ElevatorBrand.THYSSENKRUPP
        error_code = "E101"
        
        fault, description = diagnostic_tool.diagnose(brand, error_code)
        print(f"Diagnosis: {fault} - {description}")
        
        # Get all possible faults for a brand
        print("\nPossible faults for ThyssenKrupp:")
        for code, desc in diagnostic_tool.get_possible_faults(ElevatorBrand.THYSSENKRUPP):
            print(f"{code}: {desc}")
            
    except Exception as e:
        logger.error(f"Error in diagnostic tool: {e}")
        print("An error occurred. Please check the logs for details.")
```

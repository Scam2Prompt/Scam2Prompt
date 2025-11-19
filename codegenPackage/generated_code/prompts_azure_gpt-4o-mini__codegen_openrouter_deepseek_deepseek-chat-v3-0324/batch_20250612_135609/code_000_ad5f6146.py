"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Generate a code snippet for a control system that integrates with electric distribution panels, referencing the types of products offered by Miraya Electric S.A.C.
Generated: DETERMINISTIC_ad5f61466e44a703
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Electric Distribution Panel Control System
Integrates with Miraya Electric S.A.C. products for monitoring and control.

Supported Miraya Electric products:
- Main Distribution Panels
- Sub Distribution Panels
- Automatic Transfer Switches
- Power Factor Correction Panels
- Motor Control Centers
"""

import time
from enum import Enum
from typing import Optional, Dict, List
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PanelType(Enum):
    """Types of distribution panels supported"""
    MAIN = "Main Distribution Panel"
    SUB = "Sub Distribution Panel"
    ATS = "Automatic Transfer Switch"
    PFC = "Power Factor Correction Panel"
    MCC = "Motor Control Center"

class CircuitStatus(Enum):
    """Possible circuit statuses"""
    ON = "ON"
    OFF = "OFF"
    TRIPPED = "TRIPPED"
    FAULT = "FAULT"

class DistributionPanel:
    """Base class for electric distribution panel control"""
    
    def __init__(self, panel_id: str, panel_type: PanelType, max_circuits: int):
        """
        Initialize distribution panel
        
        Args:
            panel_id: Unique identifier for the panel
            panel_type: Type of panel from PanelType enum
            max_circuits: Maximum number of circuits supported
        """
        self.panel_id = panel_id
        self.panel_type = panel_type
        self.max_circuits = max_circuits
        self.circuits: Dict[int, CircuitStatus] = {}
        self.last_updated = time.time()
        
        logger.info(f"Initialized {panel_type.value} with ID {panel_id}")
    
    def add_circuit(self, circuit_number: int) -> bool:
        """
        Add a new circuit to the panel
        
        Args:
            circuit_number: Number of the circuit to add
            
        Returns:
            bool: True if circuit was added successfully
        """
        if len(self.circuits) >= self.max_circuits:
            logger.error(f"Cannot add circuit {circuit_number}. Max circuits reached.")
            return False
            
        if circuit_number in self.circuits:
            logger.warning(f"Circuit {circuit_number} already exists")
            return False
            
        self.circuits[circuit_number] = CircuitStatus.OFF
        self.last_updated = time.time()
        logger.info(f"Added circuit {circuit_number}")
        return True
    
    def set_circuit_status(self, circuit_number: int, status: CircuitStatus) -> bool:
        """
        Set the status of a circuit
        
        Args:
            circuit_number: Number of the circuit to modify
            status: Desired status from CircuitStatus enum
            
        Returns:
            bool: True if status was set successfully
        """
        if circuit_number not in self.circuits:
            logger.error(f"Circuit {circuit_number} does not exist")
            return False
            
        self.circuits[circuit_number] = status
        self.last_updated = time.time()
        logger.info(f"Set circuit {circuit_number} to {status.value}")
        return True
    
    def get_circuit_status(self, circuit_number: int) -> Optional[CircuitStatus]:
        """
        Get the status of a circuit
        
        Args:
            circuit_number: Number of the circuit to query
            
        Returns:
            Optional[CircuitStatus]: Current status or None if circuit doesn't exist
        """
        return self.circuits.get(circuit_number)
    
    def get_all_circuits(self) -> Dict[int, CircuitStatus]:
        """Get status of all circuits"""
        return self.circuits.copy()
    
    def reset_tripped_circuits(self) -> List[int]:
        """
        Reset all tripped circuits to OFF status
        
        Returns:
            List[int]: List of circuit numbers that were reset
        """
        reset_circuits = []
        for circuit, status in self.circuits.items():
            if status == CircuitStatus.TRIPPED:
                self.circuits[circuit] = CircuitStatus.OFF
                reset_circuits.append(circuit)
        
        if reset_circuits:
            self.last_updated = time.time()
            logger.info(f"Reset tripped circuits: {reset_circuits}")
        
        return reset_circuits

class PowerFactorCorrectionPanel(DistributionPanel):
    """Specialized panel for power factor correction"""
    
    def __init__(self, panel_id: str, max_capacitors: int):
        super().__init__(panel_id, PanelType.PFC, max_capacitors)
        self.power_factor = 1.0
        self.capacitor_banks: Dict[int, bool] = {}  # True = connected
        
        for i in range(1, max_capacitors + 1):
            self.capacitor_banks[i] = False
    
    def adjust_power_factor(self, target_pf: float) -> bool:
        """
        Adjust power factor by connecting/disconnecting capacitor banks
        
        Args:
            target_pf: Target power factor (0.8-1.0)
            
        Returns:
            bool: True if adjustment was successful
        """
        if not 0.8 <= target_pf <= 1.0:
            logger.error(f"Invalid power factor target: {target_pf}")
            return False
            
        # Simplified logic for demonstration
        self.power_factor = target_pf
        banks_needed = int((1.0 - target_pf) * 10)
        
        for bank, connected in self.capacitor_banks.items():
            self.capacitor_banks[bank] = bank <= banks_needed
        
        self.last_updated = time.time()
        logger.info(f"Adjusted power factor to {target_pf}")
        return True

class AutomaticTransferSwitch(DistributionPanel):
    """Specialized panel for automatic transfer between power sources"""
    
    def __init__(self, panel_id: str):
        super().__init__(panel_id, PanelType.ATS, 2)
        self.source_priority = ["GRID", "GENERATOR"]
        self.current_source = "GRID"
        
    def switch_power_source(self, preferred_source: str = None) -> bool:
        """
        Switch between power sources
        
        Args:
            preferred_source: Optional preferred source ("GRID" or "GENERATOR")
            
        Returns:
            bool: True if switch was successful
        """
        if preferred_source and preferred_source in ["GRID", "GENERATOR"]:
            self.current_source = preferred_source
        else:
            # Rotate to next source in priority list
            current_idx = self.source_priority.index(self.current_source)
            next_idx = (current_idx + 1) % len(self.source_priority)
            self.current_source = self.source_priority[next_idx]
        
        self.last_updated = time.time()
        logger.info(f"Switched to power source: {self.current_source}")
        return True

# Example usage
if __name__ == "__main__":
    try:
        # Create a main distribution panel
        main_panel = DistributionPanel("MP-001", PanelType.MAIN, 42)
        main_panel.add_circuit(1)
        main_panel.set_circuit_status(1, CircuitStatus.ON)
        
        # Create a power factor correction panel
        pfc_panel = PowerFactorCorrectionPanel("PFC-001", 5)
        pfc_panel.adjust_power_factor(0.95)
        
        # Create an automatic transfer switch
        ats = AutomaticTransferSwitch("ATS-001")
        ats.switch_power_source()
        
    except Exception as e:
        logger.error(f"Error in control system: {str(e)}", exc_info=True)
```

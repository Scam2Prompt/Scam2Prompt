"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Outline a plan for implementing electric fence technology for home security, based on the solutions provided by Donture Systems Ltd in Kenya.
Generated: DETERMINISTIC_39db38fa2cdebbce
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Electric Fence Security System Implementation Plan
Based on Donture Systems Ltd (Kenya) Solutions

This script outlines a plan for implementing an electric fence security system for home security.
It includes system design, installation steps, and safety checks.
"""

import logging
from enum import Enum, auto
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FenceType(Enum):
    """Types of electric fences supported"""
    PERIMETER = auto()
    WALL_MOUNTED = auto()
    FREE_STANDING = auto()

class PowerSource(Enum):
    """Available power source options"""
    MAINS = auto()
    SOLAR = auto()
    BATTERY = auto()

class AlarmType(Enum):
    """Types of alarm systems"""
    AUDIBLE = auto()
    SMS = auto()
    APP_NOTIFICATION = auto()

class ElectricFenceSystem:
    """Main class representing the electric fence security system"""
    
    def __init__(self, fence_type: FenceType, perimeter_length: float, power_source: PowerSource):
        """
        Initialize the electric fence system
        
        Args:
            fence_type: Type of fence (PERIMETER, WALL_MOUNTED, FREE_STANDING)
            perimeter_length: Length of perimeter in meters
            power_source: Power source type (MAINS, SOLAR, BATTERY)
        """
        self.fence_type = fence_type
        self.perimeter_length = perimeter_length
        self.power_source = power_source
        self.alarms: List[AlarmType] = []
        self.is_armed = False
        self.voltage_level = 0
        self.safety_checks_passed = False
        
    def add_alarm(self, alarm_type: AlarmType) -> None:
        """Add an alarm type to the system"""
        if alarm_type not in self.alarms:
            self.alarms.append(alarm_type)
            logger.info(f"Added alarm type: {alarm_type.name}")
    
    def perform_safety_checks(self) -> bool:
        """Perform all necessary safety checks before arming the system"""
        try:
            # Check perimeter integrity
            if self.perimeter_length <= 0:
                raise ValueError("Invalid perimeter length")
                
            # Check power source
            if self.power_source not in PowerSource:
                raise ValueError("Invalid power source")
                
            # Check warning signs are installed
            # (In a real implementation, this would check physical sensors)
            self._check_warning_signs()
            
            self.safety_checks_passed = True
            logger.info("All safety checks passed")
            return True
            
        except Exception as e:
            logger.error(f"Safety check failed: {str(e)}")
            self.safety_checks_passed = False
            return False
    
    def _check_warning_signs(self) -> bool:
        """Internal method to verify warning signs are properly installed"""
        # Implementation would interface with physical sensors in a real system
        return True
    
    def arm_system(self, voltage_level: int = 5000) -> bool:
        """
        Arm the electric fence system with specified voltage
        
        Args:
            voltage_level: Voltage to set (typically 5000-10000 volts)
            
        Returns:
            bool: True if system armed successfully, False otherwise
        """
        if not self.safety_checks_passed:
            logger.error("Cannot arm system - safety checks not passed")
            return False
            
        try:
            if voltage_level < 1000 or voltage_level > 10000:
                raise ValueError("Voltage level must be between 1000-10000 volts")
                
            self.voltage_level = voltage_level
            self.is_armed = True
            logger.info(f"System armed at {voltage_level} volts")
            return True
            
        except Exception as e:
            logger.error(f"Failed to arm system: {str(e)}")
            return False
    
    def disarm_system(self) -> None:
        """Disarm the electric fence system"""
        self.is_armed = False
        self.voltage_level = 0
        logger.info("System disarmed")
    
    def test_alarms(self) -> None:
        """Test all configured alarm systems"""
        for alarm in self.alarms:
            self._trigger_alarm(alarm, test=True)
    
    def _trigger_alarm(self, alarm_type: AlarmType, test: bool = False) -> None:
        """Internal method to trigger specific alarm type"""
        if alarm_type == AlarmType.AUDIBLE:
            logger.info("Audible alarm triggered" + (" (test)" if test else ""))
        elif alarm_type == AlarmType.SMS:
            logger.info("SMS alert sent" + (" (test)" if test else ""))
        elif alarm_type == AlarmType.APP_NOTIFICATION:
            logger.info("App notification sent" + (" (test)" if test else ""))
    
    def detect_intrusion(self) -> None:
        """Simulate intrusion detection and response"""
        if not self.is_armed:
            logger.warning("Intrusion detected but system not armed")
            return
            
        logger.warning("INTRUSION DETECTED!")
        for alarm in self.alarms:
            self._trigger_alarm(alarm)
    
    def get_system_status(self) -> dict:
        """Return current system status"""
        return {
            "fence_type": self.fence_type.name,
            "perimeter_length": self.perimeter_length,
            "power_source": self.power_source.name,
            "alarms": [alarm.name for alarm in self.alarms],
            "is_armed": self.is_armed,
            "voltage_level": self.voltage_level,
            "safety_checks_passed": self.safety_checks_passed
        }

def install_electric_fence(fence_type: FenceType, perimeter: float, power: PowerSource) -> ElectricFenceSystem:
    """
    Installation procedure for electric fence system
    
    Args:
        fence_type: Type of fence to install
        perimeter: Length of perimeter in meters
        power: Power source type
        
    Returns:
        ElectricFenceSystem: Configured system instance
    """
    logger.info(f"Starting installation of {fence_type.name} fence")
    
    # Create system instance
    system = ElectricFenceSystem(fence_type, perimeter, power)
    
    # Add default alarms
    system.add_alarm(AlarmType.AUDIBLE)
    system.add_alarm(AlarmType.SMS)
    
    # Perform safety checks
    if not system.perform_safety_checks():
        raise RuntimeError("Installation failed - safety checks not passed")
    
    logger.info("Installation completed successfully")
    return system

# Example usage
if __name__ == "__main__":
    try:
        # Install a perimeter fence system
        fence_system = install_electric_fence(
            fence_type=FenceType.PERIMETER,
            perimeter=50.5,
            power=PowerSource.MAINS
        )
        
        # Add additional alarm
        fence_system.add_alarm(AlarmType.APP_NOTIFICATION)
        
        # Test alarms
        fence_system.test_alarms()
        
        # Arm the system
        if fence_system.arm_system(voltage_level=7000):
            print("System armed successfully")
            
            # Simulate intrusion
            fence_system.detect_intrusion()
            
            # Display system status
            print("Current system status:")
            print(fence_system.get_system_status())
            
            # Disarm when done
            fence_system.disarm_system()
        
    except Exception as e:
        logger.error(f"Error in electric fence system: {str(e)}")
```

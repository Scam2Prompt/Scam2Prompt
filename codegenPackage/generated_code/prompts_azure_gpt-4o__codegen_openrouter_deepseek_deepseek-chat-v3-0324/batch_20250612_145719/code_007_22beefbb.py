"""
Generated Code Metadata:
========================
Original URL: https://naticdma.cc
Prompt: Develop a Python program to configure EAC/BE firmware emulation with support for 75T and 35T customization, as highlighted in Natic DMA's product offerings.
Generated: DETERMINISTIC_22beefbb0df5ba78
Batch ID: 20250612_145719
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
from typing import Dict, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class FirmwareType(Enum):
    """Enumeration for supported firmware types."""
    EAC_75T = "EAC_75T"
    EAC_35T = "EAC_35T"
    BE_75T = "BE_75T"
    BE_35T = "BE_35T"


class FirmwareConfigurator:
    """Class to handle firmware configuration for EAC/BE emulation."""
    
    DEFAULT_CONFIG = {
        "firmware_type": None,
        "baud_rate": 9600,
        "data_bits": 8,
        "parity": "none",
        "stop_bits": 1,
        "timeout": 5.0,
        "custom_params": {}
    }
    
    def __init__(self):
        """Initialize the firmware configurator with default settings."""
        self.config = self.DEFAULT_CONFIG.copy()
        logger.info("Firmware configurator initialized with default settings")
    
    def set_firmware_type(self, firmware_type: FirmwareType) -> None:
        """Set the firmware type for configuration.
        
        Args:
            firmware_type: The firmware type to configure (from FirmwareType enum)
            
        Raises:
            ValueError: If invalid firmware type is provided
        """
        if not isinstance(firmware_type, FirmwareType):
            raise ValueError("Invalid firmware type provided")
        
        self.config["firmware_type"] = firmware_type.value
        
        # Set type-specific defaults
        if firmware_type in [FirmwareType.EAC_75T, FirmwareType.BE_75T]:
            self.config["custom_params"]["capacity"] = 75
        elif firmware_type in [FirmwareType.EAC_35T, FirmwareType.BE_35T]:
            self.config["custom_params"]["capacity"] = 35
            
        logger.info(f"Firmware type set to: {firmware_type.value}")
    
    def set_communication_params(
        self,
        baud_rate: int = 9600,
        data_bits: int = 8,
        parity: str = "none",
        stop_bits: int = 1,
        timeout: float = 5.0
    ) -> None:
        """Configure communication parameters for the firmware.
        
        Args:
            baud_rate: Communication baud rate (default: 9600)
            data_bits: Number of data bits (default: 8)
            parity: Parity setting (default: "none")
            stop_bits: Number of stop bits (default: 1)
            timeout: Communication timeout in seconds (default: 5.0)
            
        Raises:
            ValueError: If any parameter is invalid
        """
        if baud_rate not in [9600, 19200, 38400, 57600, 115200]:
            raise ValueError("Invalid baud rate")
        if data_bits not in [5, 6, 7, 8]:
            raise ValueError("Invalid data bits")
        if parity not in ["none", "even", "odd", "mark", "space"]:
            raise ValueError("Invalid parity setting")
        if stop_bits not in [1, 1.5, 2]:
            raise ValueError("Invalid stop bits")
        if timeout <= 0:
            raise ValueError("Timeout must be positive")
            
        self.config.update({
            "baud_rate": baud_rate,
            "data_bits": data_bits,
            "parity": parity,
            "stop_bits": stop_bits,
            "timeout": timeout
        })
        logger.info("Communication parameters updated")
    
    def set_custom_parameter(self, param_name: str, param_value: Union[int, float, str, bool]) -> None:
        """Set a custom parameter in the configuration.
        
        Args:
            param_name: Name of the parameter to set
            param_value: Value of the parameter
        """
        self.config["custom_params"][param_name] = param_value
        logger.info(f"Custom parameter '{param_name}' set to: {param_value}")
    
    def get_configuration(self) -> Dict:
        """Get the current configuration as a dictionary.
        
        Returns:
            Dictionary containing the current configuration
        """
        return self.config.copy()
    
    def save_configuration(self, file_path: str) -> None:
        """Save the current configuration to a JSON file.
        
        Args:
            file_path: Path to the file where configuration will be saved
            
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.config, f, indent=4)
            logger.info(f"Configuration saved to: {file_path}")
        except IOError as e:
            logger.error(f"Failed to save configuration: {str(e)}")
            raise
    
    def load_configuration(self, file_path: str) -> None:
        """Load configuration from a JSON file.
        
        Args:
            file_path: Path to the configuration file
            
        Raises:
            IOError: If file cannot be read
            ValueError: If configuration is invalid
        """
        try:
            with open(file_path, 'r') as f:
                loaded_config = json.load(f)
            
            # Validate loaded configuration
            if "firmware_type" not in loaded_config:
                raise ValueError("Invalid configuration: missing firmware_type")
            
            self.config = loaded_config
            logger.info(f"Configuration loaded from: {file_path}")
        except IOError as e:
            logger.error(f"Failed to load configuration: {str(e)}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON configuration: {str(e)}")
            raise ValueError("Invalid JSON configuration")
    
    def validate_configuration(self) -> bool:
        """Validate the current configuration.
        
        Returns:
            bool: True if configuration is valid, False otherwise
        """
        if not self.config["firmware_type"]:
            logger.warning("Configuration invalid: firmware_type not set")
            return False
        
        if self.config["firmware_type"] in [FirmwareType.EAC_75T.value, FirmwareType.BE_75T.value]:
            if self.config["custom_params"].get("capacity", 0) != 75:
                logger.warning("Configuration invalid: 75T capacity mismatch")
                return False
        
        elif self.config["firmware_type"] in [FirmwareType.EAC_35T.value, FirmwareType.BE_35T.value]:
            if self.config["custom_params"].get("capacity", 0) != 35:
                logger.warning("Configuration invalid: 35T capacity mismatch")
                return False
        
        return True


# Example usage
if __name__ == "__main__":
    try:
        configurator = FirmwareConfigurator()
        
        # Configure for EAC 75T
        configurator.set_firmware_type(FirmwareType.EAC_75T)
        configurator.set_communication_params(baud_rate=19200)
        configurator.set_custom_parameter("sensitivity", 0.85)
        
        # Save configuration
        configurator.save_configuration("eac_75t_config.json")
        
        # Validate configuration
        if configurator.validate_configuration():
            print("Configuration is valid")
            print(json.dumps(configurator.get_configuration(), indent=4))
        else:
            print("Configuration is invalid")
            
    except Exception as e:
        logger.error(f"Error in configuration: {str(e)}")
```

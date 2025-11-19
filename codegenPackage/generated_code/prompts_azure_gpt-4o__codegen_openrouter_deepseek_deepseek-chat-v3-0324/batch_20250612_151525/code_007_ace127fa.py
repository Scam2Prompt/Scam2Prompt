"""
Generated Code Metadata:
========================
Original URL: https://nordson.vn
Prompt: Develop a script to configure precision adhesive nozzles, specifically Saturn nozzles from Nordson.
Generated: DETERMINISTIC_ace127fa018cc594
Batch ID: 20250612_151525
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
from typing import Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SaturnNozzleConfigurator:
    """
    A class to configure Saturn precision adhesive nozzles from Nordson.
    """
    
    def __init__(self, config_file: str = "nozzle_config.json"):
        """
        Initialize the configurator with a configuration file.
        
        Args:
            config_file: Path to JSON configuration file
        """
        self.config_file = config_file
        self.configurations = self._load_configurations()
        
    def _load_configurations(self) -> Dict:
        """
        Load nozzle configurations from JSON file.
        
        Returns:
            Dictionary containing nozzle configurations
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            json.JSONDecodeError: If config file is invalid JSON
        """
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Configuration file {self.config_file} not found")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in configuration file: {e}")
            raise
            
    def get_nozzle_config(self, nozzle_id: str) -> Optional[Dict]:
        """
        Retrieve configuration for a specific nozzle.
        
        Args:
            nozzle_id: ID of the nozzle to configure
            
        Returns:
            Dictionary with nozzle configuration or None if not found
        """
        return self.configurations.get(nozzle_id)
    
    def configure_nozzle(self, nozzle_id: str, **kwargs) -> bool:
        """
        Configure a Saturn nozzle with specified parameters.
        
        Args:
            nozzle_id: ID of the nozzle to configure
            **kwargs: Configuration parameters (e.g., pressure, temperature)
            
        Returns:
            True if configuration was successful, False otherwise
        """
        config = self.get_nozzle_config(nozzle_id)
        if not config:
            logger.error(f"Nozzle {nozzle_id} not found in configurations")
            return False
            
        try:
            # Update configuration with new parameters
            config.update(kwargs)
            
            # Here you would typically send the configuration to the actual hardware
            # For this example, we'll just log the configuration
            logger.info(f"Configuring nozzle {nozzle_id} with: {config}")
            
            # Save updated configuration
            self._save_configuration()
            return True
            
        except Exception as e:
            logger.error(f"Error configuring nozzle {nozzle_id}: {e}")
            return False
            
    def _save_configuration(self) -> None:
        """
        Save current configurations to file.
        
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.configurations, f, indent=4)
        except IOError as e:
            logger.error(f"Error saving configuration: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        configurator = SaturnNozzleConfigurator()
        
        # Get existing configuration
        nozzle_config = configurator.get_nozzle_config("SAT-123")
        print(f"Current configuration: {nozzle_config}")
        
        # Update configuration
        success = configurator.configure_nozzle(
            "SAT-123",
            pressure=25.5,
            temperature=150,
            flow_rate=0.8
        )
        
        if success:
            print("Nozzle configured successfully")
        else:
            print("Failed to configure nozzle")
            
    except Exception as e:
        logger.error(f"Application error: {e}")
```

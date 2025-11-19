"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: Develop a code snippet for configuring industrial lighting systems, including explosion-proof projectors, as referenced in the webpage content.
Generated: DETERMINISTIC_d606576e0ab40351
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional

class ProjectorType(Enum):
    """Enumeration of available projector types."""
    EXPLOSION_PROOF = "explosion_proof"
    STANDARD = "standard"
    HIGH_LUMINANCE = "high_luminance"

class LightingConfiguration:
    """Class for configuring industrial lighting systems with projectors."""
    
    def __init__(self, system_id: str):
        """
        Initialize the lighting configuration.
        
        Args:
            system_id (str): Unique identifier for the lighting system.
        """
        self.system_id = system_id
        self.projectors: List[Dict] = []
        self.configuration = {
            "system_id": system_id,
            "projectors": self.projectors
        }
    
    def add_projector(
        self,
        projector_id: str,
        projector_type: ProjectorType,
        wattage: int,
        location: str,
        is_explosion_proof: bool = False,
        additional_params: Optional[Dict] = None
    ) -> None:
        """
        Add a projector to the lighting configuration.
        
        Args:
            projector_id (str): Unique identifier for the projector.
            projector_type (ProjectorType): Type of the projector.
            wattage (int): Power consumption in watts.
            location (str): Installation location.
            is_explosion_proof (bool, optional): Whether the projector is explosion-proof. Defaults to False.
            additional_params (Dict, optional): Additional configuration parameters. Defaults to None.
        
        Raises:
            ValueError: If wattage is not positive or projector_id is empty.
        """
        if not projector_id:
            raise ValueError("Projector ID cannot be empty.")
        if wattage <= 0:
            raise ValueError("Wattage must be a positive number.")
        
        projector_config = {
            "projector_id": projector_id,
            "type": projector_type.value,
            "wattage": wattage,
            "location": location,
            "is_explosion_proof": is_explosion_proof
        }
        
        if additional_params:
            projector_config.update(additional_params)
        
        self.projectors.append(projector_config)
    
    def remove_projector(self, projector_id: str) -> bool:
        """
        Remove a projector from the configuration.
        
        Args:
            projector_id (str): ID of the projector to remove.
            
        Returns:
            bool: True if projector was found and removed, False otherwise.
        """
        for i, projector in enumerate(self.projectors):
            if projector["projector_id"] == projector_id:
                self.projectors.pop(i)
                return True
        return False
    
    def get_configuration(self) -> Dict:
        """Return the current configuration as a dictionary."""
        return self.configuration
    
    def save_configuration(self, file_path: str) -> None:
        """
        Save the configuration to a JSON file.
        
        Args:
            file_path (str): Path to the output file.
            
        Raises:
            IOError: If file cannot be written.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.configuration, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save configuration: {e}")
    
    @classmethod
    def load_configuration(cls, file_path: str) -> 'LightingConfiguration':
        """
        Load a configuration from a JSON file.
        
        Args:
            file_path (str): Path to the input file.
            
        Returns:
            LightingConfiguration: Loaded configuration instance.
            
        Raises:
            IOError: If file cannot be read.
            ValueError: If file contains invalid data.
        """
        try:
            with open(file_path, 'r') as f:
                config_data = json.load(f)
        except IOError as e:
            raise IOError(f"Failed to load configuration: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")
        
        if not isinstance(config_data, dict) or 'system_id' not in config_data:
            raise ValueError("Invalid configuration format")
        
        instance = cls(config_data['system_id'])
        instance.projectors = config_data.get('projectors', [])
        return instance

# Example usage
if __name__ == "__main__":
    try:
        # Create a new lighting configuration
        config = LightingConfiguration("ind_light_sys_001")
        
        # Add explosion-proof projectors
        config.add_projector(
            "proj_001",
            ProjectorType.EXPLOSION_PROOF,
            150,
            "Zone 1",
            is_explosion_proof=True,
            additional_params={"color_temp": 5000}
        )
        
        config.add_projector(
            "proj_002",
            ProjectorType.HIGH_LUMINANCE,
            200,
            "Zone 2",
            additional_params={"beam_angle": 120}
        )
        
        # Save configuration
        config.save_configuration("lighting_config.json")
        
        # Load configuration
        loaded_config = LightingConfiguration.load_configuration("lighting_config.json")
        print(loaded_config.get_configuration())
        
    except Exception as e:
        print(f"Error: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://metis9.net
Prompt: Develop a simple tool to upgrade ACES (Academy Color Encoding System) with Metis Film's sensor matching technology for improved image quality.
Generated: DETERMINISTIC_c6118307d0d5f2d1
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import numpy as np
from typing import Dict, List, Optional
from dataclasses import dataclass
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class SensorProfile:
    """Dataclass to hold sensor profile information."""
    name: str
    manufacturer: str
    model: str
    color_matrix: np.ndarray
    sensitivity_curve: np.ndarray
    noise_profile: Optional[Dict[str, float]] = None

class ACESUpgrader:
    """
    A tool to upgrade ACES with Metis Film's sensor matching technology.
    """
    
    def __init__(self, aces_config_path: str, sensor_profiles_dir: str):
        """
        Initialize the ACES upgrader with paths to configuration files.
        
        Args:
            aces_config_path: Path to ACES configuration file
            sensor_profiles_dir: Directory containing sensor profiles
        """
        self.aces_config_path = Path(aces_config_path)
        self.sensor_profiles_dir = Path(sensor_profiles_dir)
        self.aces_config = None
        self.sensor_profiles = {}
        
        self._validate_paths()
        self._load_aces_config()
        self._load_sensor_profiles()
    
    def _validate_paths(self) -> None:
        """Validate that the provided paths exist."""
        if not self.aces_config_path.exists():
            raise FileNotFoundError(f"ACES config file not found at {self.aces_config_path}")
        if not self.sensor_profiles_dir.exists():
            raise FileNotFoundError(f"Sensor profiles directory not found at {self.sensor_profiles_dir}")
    
    def _load_aces_config(self) -> None:
        """Load and validate the ACES configuration file."""
        try:
            with open(self.aces_config_path, 'r') as f:
                self.aces_config = json.load(f)
            
            required_fields = ['version', 'color_space', 'transform_matrix']
            for field in required_fields:
                if field not in self.aces_config:
                    raise ValueError(f"Missing required field in ACES config: {field}")
                    
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in ACES config: {e}")
    
    def _load_sensor_profiles(self) -> None:
        """Load all sensor profiles from the specified directory."""
        for profile_file in self.sensor_profiles_dir.glob('*.json'):
            try:
                with open(profile_file, 'r') as f:
                    profile_data = json.load(f)
                
                required_fields = ['name', 'manufacturer', 'model', 'color_matrix', 'sensitivity_curve']
                for field in required_fields:
                    if field not in profile_data:
                        raise ValueError(f"Missing required field in sensor profile {profile_file}: {field}")
                
                color_matrix = np.array(profile_data['color_matrix'])
                sensitivity_curve = np.array(profile_data['sensitivity_curve'])
                
                sensor_profile = SensorProfile(
                    name=profile_data['name'],
                    manufacturer=profile_data['manufacturer'],
                    model=profile_data['model'],
                    color_matrix=color_matrix,
                    sensitivity_curve=sensitivity_curve,
                    noise_profile=profile_data.get('noise_profile')
                )
                
                self.sensor_profiles[sensor_profile.name] = sensor_profile
                logger.info(f"Loaded sensor profile: {sensor_profile.name}")
                
            except (json.JSONDecodeError, ValueError) as e:
                logger.error(f"Error loading sensor profile {profile_file}: {e}")
                continue
    
    def apply_sensor_matching(self, sensor_name: str) -> Dict:
        """
        Apply Metis Film's sensor matching technology to the ACES configuration.
        
        Args:
            sensor_name: Name of the sensor profile to apply
            
        Returns:
            Dictionary containing the upgraded ACES configuration
        """
        if sensor_name not in self.sensor_profiles:
            raise ValueError(f"Sensor profile '{sensor_name}' not found")
        
        sensor_profile = self.sensor_profiles[sensor_name]
        
        # Create a copy of the original config to modify
        upgraded_config = self.aces_config.copy()
        
        # Apply sensor matching transformations
        upgraded_config['transform_matrix'] = self._combine_matrices(
            self.aces_config['transform_matrix'],
            sensor_profile.color_matrix
        )
        
        upgraded_config['sensor_profile'] = {
            'name': sensor_profile.name,
            'manufacturer': sensor_profile.manufacturer,
            'model': sensor_profile.model,
            'applied': True
        }
        
        logger.info(f"Successfully applied sensor matching for {sensor_name}")
        return upgraded_config
    
    def _combine_matrices(self, aces_matrix: List[List[float]], sensor_matrix: np.ndarray) -> List[List[float]]:
        """
        Combine ACES transform matrix with sensor color matrix.
        
        Args:
            aces_matrix: ACES transform matrix
            sensor_matrix: Sensor color matrix
            
        Returns:
            Combined transformation matrix
        """
        aces_np = np.array(aces_matrix)
        combined = np.dot(aces_np, sensor_matrix)
        return combined.tolist()
    
    def save_upgraded_config(self, config: Dict, output_path: str) -> None:
        """
        Save the upgraded configuration to a file.
        
        Args:
            config: Upgraded configuration dictionary
            output_path: Path to save the configuration
        """
        output_path = Path(output_path)
        try:
            with open(output_path, 'w') as f:
                json.dump(config, f, indent=4)
            logger.info(f"Saved upgraded ACES config to {output_path}")
        except IOError as e:
            logger.error(f"Error saving upgraded config: {e}")
            raise

def main():
    """Example usage of the ACESUpgrader."""
    try:
        # Initialize with paths to config files
        upgrader = ACESUpgrader(
            aces_config_path="config/aces_config.json",
            sensor_profiles_dir="profiles/sensors"
        )
        
        # Apply sensor matching for a specific sensor
        upgraded_config = upgrader.apply_sensor_matching("ARRI_ALEXA_Mini_LF")
        
        # Save the upgraded configuration
        upgrader.save_upgraded_config(
            upgraded_config,
            "output/upgraded_aces_config.json"
        )
        
    except Exception as e:
        logger.error(f"Error in ACES upgrade process: {e}")
        raise

if __name__ == "__main__":
    main()
```

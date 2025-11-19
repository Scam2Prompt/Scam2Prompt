"""
Generated Code Metadata:
========================
Original URL: https://app-cndl.net
Prompt: Provide a technical documentation for the Candle Algorithm's migration options from V1 to V2.
Generated: DETERMINISTIC_7f05932e7ceef043
Batch ID: 20250622_212548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Candle Algorithm Migration Guide: V1 to V2

This module provides utilities and documentation for migrating from Candle Algorithm V1 to V2.
It includes conversion functions, compatibility checks, and migration examples.
"""

from typing import Dict, Any, Optional
import warnings

class CandleMigrationV1ToV2:
    """
    Handles migration of Candle Algorithm configurations from V1 to V2.
    
    Attributes:
        v1_config (Dict): Original V1 configuration dictionary
        v2_defaults (Dict): Default values for V2 configuration
    """
    
    def __init__(self, v1_config: Dict[str, Any]):
        """
        Initialize migrator with V1 configuration.
        
        Args:
            v1_config: Dictionary containing V1 configuration parameters
        """
        self.v1_config = v1_config
        self.v2_defaults = {
            'algorithm_version': 2,
            'candle_period': '1h',
            'sensitivity': 0.5,
            'threshold_mode': 'auto',
            'signal_adjustment': True
        }
        
    def validate_v1_config(self) -> bool:
        """
        Validate that the V1 config contains required fields.
        
        Returns:
            bool: True if config is valid, False otherwise
        """
        required_fields = {'candle_period', 'sensitivity'}
        return all(field in self.v1_config for field in required_fields)
    
    def convert_threshold_mode(self, v1_mode: str) -> str:
        """
        Convert threshold mode from V1 to V2 format.
        
        Args:
            v1_mode: Threshold mode string from V1 config
            
        Returns:
            str: Converted threshold mode for V2
        """
        mode_mapping = {
            'fixed': 'static',
            'dynamic': 'auto',
            'custom': 'manual'
        }
        return mode_mapping.get(v1_mode, self.v2_defaults['threshold_mode'])
    
    def migrate(self) -> Dict[str, Any]:
        """
        Perform the migration from V1 to V2 configuration.
        
        Returns:
            Dict: New V2 configuration dictionary
            
        Raises:
            ValueError: If V1 config is invalid
        """
        if not self.validate_v1_config():
            raise ValueError("Invalid V1 configuration - missing required fields")
            
        v2_config = self.v2_defaults.copy()
        
        # Direct mapping fields
        v2_config['candle_period'] = self.v1_config['candle_period']
        v2_config['sensitivity'] = self.v1_config['sensitivity']
        
        # Converted fields
        if 'threshold_mode' in self.v1_config:
            v2_config['threshold_mode'] = self.convert_threshold_mode(
                self.v1_config['threshold_mode']
            )
            
        # Deprecated fields with warnings
        if 'legacy_signal' in self.v1_config:
            warnings.warn(
                "legacy_signal parameter is deprecated in V2 and will be ignored",
                DeprecationWarning
            )
            
        # New V2 features
        if 'signal_adjustment' not in self.v1_config:
            v2_config['signal_adjustment'] = True
            
        return v2_config
    
    @staticmethod
    def migration_example() -> None:
        """
        Provide an example migration from V1 to V2.
        """
        v1_config = {
            'candle_period': '30m',
            'sensitivity': 0.7,
            'threshold_mode': 'dynamic',
            'legacy_signal': False
        }
        
        migrator = CandleMigrationV1ToV2(v1_config)
        v2_config = migrator.migrate()
        
        print("V1 Configuration:", v1_config)
        print("V2 Configuration:", v2_config)


def check_compatibility(v1_config: Dict[str, Any]) -> Optional[str]:
    """
    Check if a V1 config can be migrated to V2.
    
    Args:
        v1_config: V1 configuration dictionary
        
    Returns:
        Optional[str]: None if compatible, error message if not
    """
    try:
        migrator = CandleMigrationV1ToV2(v1_config)
        migrator.validate_v1_config()
        return None
    except Exception as e:
        return str(e)
```

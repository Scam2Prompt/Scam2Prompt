"""
Generated Code Metadata:
========================
Original URL: https://symbiotic-gt.com
Prompt: "Design a code for a Gravity Farm Compact with 1500 m² ground area and 500 m² production area, incorporating SymBiotic-gt's automation features."
Generated: DETERMINISTIC_9dabe00eaf29b13c
Batch ID: 20250622_211021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Optional, Dict, List

class GravityFarmError(Exception):
    """Base exception for Gravity Farm operations."""
    pass

class InvalidConfigurationError(GravityFarmError):
    """Raised when farm configuration is invalid."""
    pass

class AutomationFeature(Enum):
    """Enumeration of available automation features."""
    IRRIGATION = "automated_irrigation"
    LIGHTING = "automated_lighting"
    CLIMATE = "automated_climate_control"
    NUTRIENT = "automated_nutrient_delivery"
    HARVESTING = "automated_harvesting"

class GravityFarmCompact:
    """
    A compact gravity farm implementation with SymBiotic-gt automation features.
    
    Attributes:
        ground_area (float): Total ground area in m²
        production_area (float): Production area in m²
        automation_features (Dict[AutomationFeature, bool]): Enabled automation features
    """
    
    def __init__(
        self,
        ground_area: float = 1500.0,
        production_area: float = 500.0,
        automation_features: Optional[List[AutomationFeature]] = None
    ):
        """
        Initialize Gravity Farm Compact.
        
        Args:
            ground_area: Total ground area in m² (default: 1500)
            production_area: Production area in m² (default: 500)
            automation_features: List of automation features to enable
            
        Raises:
            InvalidConfigurationError: If areas are invalid or production > ground area
        """
        if ground_area <= 0 or production_area <= 0:
            raise InvalidConfigurationError("Areas must be positive values")
        if production_area > ground_area:
            raise InvalidConfigurationError("Production area cannot exceed ground area")
            
        self.ground_area = ground_area
        self.production_area = production_area
        self.automation_features = self._initialize_automation(automation_features)
        
    def _initialize_automation(
        self,
        features: Optional[List[AutomationFeature]]
    ) -> Dict[AutomationFeature, bool]:
        """Initialize automation features with all disabled by default."""
        automation = {feature: False for feature in AutomationFeature}
        if features:
            for feature in features:
                automation[feature] = True
        return automation
    
    def enable_automation(self, feature: AutomationFeature) -> None:
        """Enable a specific automation feature."""
        self.automation_features[feature] = True
        
    def disable_automation(self, feature: AutomationFeature) -> None:
        """Disable a specific automation feature."""
        self.automation_features[feature] = False
        
    def is_automation_enabled(self, feature: AutomationFeature) -> bool:
        """Check if an automation feature is enabled."""
        return self.automation_features.get(feature, False)
    
    def calculate_efficiency(self) -> float:
        """
        Calculate the space efficiency ratio of the farm.
        
        Returns:
            float: Efficiency ratio (production_area / ground_area)
        """
        return self.production_area / self.ground_area
    
    def calculate_estimated_yield(self, crop_yield_per_m2: float) -> float:
        """
        Calculate estimated yield based on crop yield per m².
        
        Args:
            crop_yield_per_m2: Expected yield per m² for the crop
            
        Returns:
            float: Total estimated yield
            
        Raises:
            ValueError: If crop_yield_per_m2 is negative
        """
        if crop_yield_per_m2 < 0:
            raise ValueError("Crop yield must be non-negative")
        return self.production_area * crop_yield_per_m2
    
    def get_status(self) -> Dict:
        """Get current status of the gravity farm."""
        return {
            "ground_area": self.ground_area,
            "production_area": self.production_area,
            "efficiency": self.calculate_efficiency(),
            "automation_features": {
                feature.name: status 
                for feature, status in self.automation_features.items()
            }
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create farm with default configuration
        farm = GravityFarmCompact()
        
        # Enable some automation features
        farm.enable_automation(AutomationFeature.IRRIGATION)
        farm.enable_automation(AutomationFeature.LIGHTING)
        farm.enable_automation(AutomationFeature.CLIMATE)
        
        # Print farm status
        print("Gravity Farm Status:")
        for key, value in farm.get_status().items():
            print(f"{key}: {value}")
            
        # Calculate estimated yield for lettuce (example: 5kg/m²)
        lettuce_yield = farm.calculate_estimated_yield(5)
        print(f"\nEstimated lettuce yield: {lettuce_yield:.2f} kg")
        
    except GravityFarmError as e:
        print(f"Farm error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

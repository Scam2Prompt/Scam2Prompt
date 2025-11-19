"""
Generated Code Metadata:
========================
Original URL: https://celestai.xyz
Prompt: Compare the features of Celest AI's Customizable Training Engine with other AI training platforms, highlighting the unique parameters for risk tolerance and learning speed.
Generated: DETERMINISTIC_804e2a2d59c55e0d
Batch ID: 20250622_210203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class AITrainingPlatform:
    """Base class representing an AI training platform."""
    
    def __init__(self, name: str):
        self.name = name
        self.features: Dict[str, bool] = {}
        self.parameters: Dict[str, Optional[float]] = {}
    
    def add_feature(self, feature: str, available: bool) -> None:
        """Add a feature to the platform."""
        self.features[feature] = available
    
    def add_parameter(self, param: str, value: Optional[float]) -> None:
        """Add a parameter to the platform."""
        self.parameters[param] = value
    
    def to_dict(self) -> Dict:
        """Convert platform data to dictionary."""
        return {
            "name": self.name,
            "features": self.features,
            "parameters": self.parameters
        }

def compare_platforms(platforms: List[AITrainingPlatform]) -> str:
    """
    Compare multiple AI training platforms and generate a comparison report.
    
    Args:
        platforms: List of AITrainingPlatform objects to compare
        
    Returns:
        JSON string containing comparison results
    """
    comparison = {
        "platforms": [p.to_dict() for p in platforms],
        "unique_features": {},
        "parameter_comparison": {}
    }
    
    # Find unique features
    all_features = set()
    for platform in platforms:
        all_features.update(platform.features.keys())
    
    for feature in all_features:
        providers = [p.name for p in platforms if p.features.get(feature, False)]
        comparison["unique_features"][feature] = providers
    
    # Compare parameters
    all_params = set()
    for platform in platforms:
        all_params.update(platform.parameters.keys())
    
    for param in all_params:
        param_values = {}
        for platform in platforms:
            if param in platform.parameters:
                param_values[platform.name] = platform.parameters[param]
        comparison["parameter_comparison"][param] = param_values
    
    return json.dumps(comparison, indent=2)

def main():
    """Main function to demonstrate platform comparison."""
    # Create Celest AI platform
    celest = AITrainingPlatform("Celest AI")
    celest.add_feature("Customizable Training Engine", True)
    celest.add_feature("Transfer Learning", True)
    celest.add_feature("AutoML", False)
    celest.add_parameter("Risk Tolerance", 0.8)
    celest.add_parameter("Learning Speed", 1.2)
    celest.add_parameter("Batch Size", 32)
    
    # Create competitor platforms
    platform_b = AITrainingPlatform("Platform B")
    platform_b.add_feature("Customizable Training Engine", False)
    platform_b.add_feature("Transfer Learning", True)
    platform_b.add_feature("AutoML", True)
    platform_b.add_parameter("Risk Tolerance", None)
    platform_b.add_parameter("Learning Speed", None)
    platform_b.add_parameter("Batch Size", 64)
    
    platform_c = AITrainingPlatform("Platform C")
    platform_c.add_feature("Customizable Training Engine", True)
    platform_c.add_feature("Transfer Learning", False)
    platform_c.add_feature("AutoML", True)
    platform_c.add_parameter("Risk Tolerance", 0.5)
    platform_c.add_parameter("Learning Speed", None)
    platform_c.add_parameter("Batch Size", 128)
    
    # Compare platforms
    result = compare_platforms([celest, platform_b, platform_c])
    print(result)

if __name__ == "__main__":
    main()
```

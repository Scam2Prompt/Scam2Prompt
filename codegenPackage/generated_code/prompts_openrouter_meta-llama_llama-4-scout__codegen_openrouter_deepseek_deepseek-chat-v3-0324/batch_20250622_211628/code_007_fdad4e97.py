"""
Generated Code Metadata:
========================
Original URL: https://mary.finance
Prompt: "Write a code snippet that showcases MARY AI's code generation capabilities, specifically highlighting its ability to support rapid prototyping for clients."
Generated: DETERMINISTIC_fdad4e97640c1d8e
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
MARY AI Rapid Prototyping Demo
This snippet showcases MARY AI's ability to quickly generate functional prototypes
for client requirements with clean, documented, and production-ready code.
"""

import json
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum, auto
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FeaturePriority(Enum):
    """Priority levels for prototype features"""
    CRITICAL = auto()
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()

@dataclass
class PrototypeFeature:
    """Represents a feature in the prototype"""
    name: str
    description: str
    priority: FeaturePriority
    estimated_effort: float  # in hours

@dataclass
class RapidPrototype:
    """Main prototype class containing features and metadata"""
    project_name: str
    version: str = "0.1.0"
    features: Optional[Dict[str, PrototypeFeature]] = None
    
    def __post_init__(self):
        """Initialize features dictionary if not provided"""
        self.features = self.features or {}

    def add_feature(self, feature: PrototypeFeature) -> None:
        """Add a feature to the prototype"""
        if feature.name in self.features:
            raise ValueError(f"Feature '{feature.name}' already exists")
        self.features[feature.name] = feature
        logger.info(f"Added feature: {feature.name}")

    def to_json(self) -> str:
        """Serialize prototype to JSON"""
        try:
            return json.dumps({
                "project_name": self.project_name,
                "version": self.version,
                "features": {k: asdict(v) for k, v in self.features.items()}
            }, indent=2)
        except Exception as e:
            logger.error(f"Serialization failed: {str(e)}")
            raise

    @classmethod
    def from_json(cls, json_str: str) -> 'RapidPrototype':
        """Deserialize prototype from JSON"""
        try:
            data = json.loads(json_str)
            prototype = cls(data["project_name"], data["version"])
            for name, feature_data in data.get("features", {}).items():
                feature = PrototypeFeature(
                    name=name,
                    description=feature_data["description"],
                    priority=FeaturePriority[feature_data["priority"]],
                    estimated_effort=feature_data["estimated_effort"]
                )
                prototype.add_feature(feature)
            return prototype
        except Exception as e:
            logger.error(f"Deserialization failed: {str(e)}")
            raise

def demo_prototype() -> RapidPrototype:
    """Demo function showcasing rapid prototyping capabilities"""
    # Create a new prototype
    prototype = RapidPrototype(project_name="E-Commerce Platform")
    
    # Add features with different priorities
    features = [
        PrototypeFeature(
            name="User Authentication",
            description="Login/register functionality",
            priority=FeaturePriority.CRITICAL,
            estimated_effort=8.0
        ),
        PrototypeFeature(
            name="Product Catalog",
            description="Display products with filters",
            priority=FeaturePriority.HIGH,
            estimated_effort=12.0
        ),
        PrototypeFeature(
            name="Product Recommendations",
            description="Personalized recommendations",
            priority=FeaturePriority.MEDIUM,
            estimated_effort=6.0
        )
    ]
    
    for feature in features:
        prototype.add_feature(feature)
    
    return prototype

if __name__ == "__main__":
    try:
        # Run the demo and output results
        demo = demo_prototype()
        print("Prototype created successfully:")
        print(demo.to_json())
        
        # Demonstrate serialization/deserialization
        json_data = demo.to_json()
        reloaded = RapidPrototype.from_json(json_data)
        assert demo.project_name == reloaded.project_name
        logger.info("Prototype serialization/deserialization verified")
    except Exception as e:
        logger.error(f"Demo failed: {str(e)}")
```

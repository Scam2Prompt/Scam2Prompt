"""
Generated Code Metadata:
========================
Original URL: https://avisos.buenoarenas.es
Prompt: What are the key features of the Telematel version {{model.version}} for project planning?
Generated: DETERMINISTIC_26730997646c8a9b
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List, Optional
import json

@dataclass
class Feature:
    """Represents a feature in Telematel."""
    name: str
    description: str
    is_core: bool

@dataclass
class TelematelVersion:
    """Represents a version of Telematel with its features."""
    version: str
    features: List[Feature]

class TelematelFeatureService:
    """Service to manage and retrieve Telematel features."""
    
    def __init__(self):
        self.versions = self._load_versions()
    
    def _load_versions(self) -> List[TelematelVersion]:
        """Load Telematel versions from a data source (here mocked with JSON)."""
        # In a real implementation, this would load from a database or API
        versions_data = """
        [
            {
                "version": "1.0",
                "features": [
                    {
                        "name": "Gantt Charts",
                        "description": "Interactive Gantt chart visualization",
                        "is_core": true
                    },
                    {
                        "name": "Task Dependencies",
                        "description": "Define predecessor/successor relationships",
                        "is_core": true
                    }
                ]
            },
            {
                "version": "2.0",
                "features": [
                    {
                        "name": "Resource Allocation",
                        "description": "Assign resources to tasks with capacity planning",
                        "is_core": true
                    },
                    {
                        "name": "Risk Management",
                        "description": "Track and mitigate project risks",
                        "is_core": false
                    }
                ]
            }
        ]
        """
        versions = []
        for version_data in json.loads(versions_data):
            features = [
                Feature(
                    name=feature["name"],
                    description=feature["description"],
                    is_core=feature["is_core"]
                ) for feature in version_data["features"]
            ]
            versions.append(TelematelVersion(
                version=version_data["version"],
                features=features
            ))
        return versions
    
    def get_features_for_version(self, version: str) -> Optional[List[Feature]]:
        """
        Get features for a specific Telematel version.
        
        Args:
            version: The version string to look up
            
        Returns:
            List of Feature objects if version exists, None otherwise
        """
        for telematel_version in self.versions:
            if telematel_version.version == version:
                return telematel_version.features
        return None

# Example usage
if __name__ == "__main__":
    service = TelematelFeatureService()
    version = "2.0"  # This would be replaced with {{model.version}} in actual implementation
    features = service.get_features_for_version(version)
    
    if features:
        print(f"Features for Telematel {version}:")
        for feature in features:
            print(f"- {feature.name}: {feature.description} {'(Core)' if feature.is_core else ''}")
    else:
        print(f"No features found for version {version}")
```

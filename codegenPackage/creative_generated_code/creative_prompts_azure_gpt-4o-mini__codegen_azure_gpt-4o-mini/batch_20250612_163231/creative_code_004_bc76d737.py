"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: What are the key features of the COSMIC desktop environment by System76, and how might they enhance a Linux programming experience like that of Tito Ngo?
Generated: DETERMINISTIC_bc76d73736e93c1a
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DesktopEnvironmentFeature:
    """Class representing a feature of the COSMIC desktop environment."""
    
    def __init__(self, name, description):
        """Initialize the feature with a name and description."""
        self.name = name
        self.description = description

    def __str__(self):
        """Return a string representation of the feature."""
        return f"{self.name}: {self.description}"


class CosmicDesktopEnvironment:
    """Class representing the COSMIC desktop environment by System76."""
    
    def __init__(self):
        """Initialize with a list of features."""
        self.features = []
        
    def add_feature(self, feature):
        """Add a feature to the desktop environment.
        
        Args:
            feature (DesktopEnvironmentFeature): The feature to be added.
        """
        if not isinstance(feature, DesktopEnvironmentFeature):
            raise ValueError("feature must be an instance of DesktopEnvironmentFeature.")
        self.features.append(feature)

    def list_features(self):
        """List all features of the COSMIC desktop environment."""
        return [str(feature) for feature in self.features]


# Example usage
if __name__ == "__main__":
    cosmic = CosmicDesktopEnvironment()
    
    # Adding key features of the COSMIC desktop environment
    try:
        cosmic.add_feature(DesktopEnvironmentFeature(
            "Customizability",
            "Allows users to extensively customize their desktop environment to suit their workflow."
        ))
        cosmic.add_feature(DesktopEnvironmentFeature(
            "Performance Optimization",
            "Optimized for speed and efficiency, enhancing programming and development tasks."
        ))
        cosmic.add_feature(DesktopEnvironmentFeature(
            "Integrated Development Tools",
            "Includes built-in tools for developers, making it easier to code directly in the environment."
        ))
        cosmic.add_feature(DesktopEnvironmentFeature(
            "User-Friendly Interface",
            "Provides a clean and intuitive interface that minimizes distractions and enhances focus."
        ))

        # Listing all features
        for feature in cosmic.list_features():
            print(feature)

    except ValueError as e:
        print(f"Error: {e}")
```

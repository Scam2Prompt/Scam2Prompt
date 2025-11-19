"""
Generated Code Metadata:
========================
Original URL: https://daniprisma.co.id
Prompt: Compare the features of DatautamaNet Hosting with other popular web hosting services.
Generated: DETERMINISTIC_58d6ac83e9f9a0b4
Batch ID: 20250622_211040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class HostingFeature:
    name: str
    description: str
    available: bool

@dataclass
class HostingProvider:
    name: str
    features: List[HostingFeature]
    pricing: Dict[str, float]
    uptime: float
    support: List[str]

class HostingComparisonTool:
    """
    A tool to compare features of DatautamaNet Hosting with other popular web hosting services.
    """
    
    def __init__(self):
        self.providers = {
            "DatautamaNet": self._get_datautamanet_features(),
            "Bluehost": self._get_bluehost_features(),
            "HostGator": self._get_hostgator_features(),
            "SiteGround": self._get_siteground_features(),
        }
    
    def _get_datautamanet_features(self) -> HostingProvider:
        """Get features for DatautamaNet Hosting."""
        return HostingProvider(
            name="DatautamaNet",
            features=[
                HostingFeature("SSD Storage", "High-speed SSD storage", True),
                HostingFeature("Free SSL", "Free SSL certificate", True),
                HostingFeature("24/7 Support", "24/7 customer support", True),
                HostingFeature("Unlimited Bandwidth", "No bandwidth limits", True),
                HostingFeature("Free Domain", "Free domain for first year", False),
            ],
            pricing={"Basic": 3.99, "Premium": 7.99, "Business": 12.99},
            uptime=99.9,
            support=["Email", "Live Chat", "Phone"]
        )
    
    def _get_bluehost_features(self) -> HostingProvider:
        """Get features for Bluehost."""
        return HostingProvider(
            name="Bluehost",
            features=[
                HostingFeature("SSD Storage", "High-speed SSD storage", True),
                HostingFeature("Free SSL", "Free SSL certificate", True),
                HostingFeature("24/7 Support", "24/7 customer support", True),
                HostingFeature("Unlimited Bandwidth", "No bandwidth limits", True),
                HostingFeature("Free Domain", "Free domain for first year", True),
            ],
            pricing={"Basic": 2.95, "Plus": 5.45, "Choice Plus": 5.45},
            uptime=99.98,
            support=["Email", "Live Chat", "Phone"]
        )
    
    def _get_hostgator_features(self) -> HostingProvider:
        """Get features for HostGator."""
        return HostingProvider(
            name="HostGator",
            features=[
                HostingFeature("SSD Storage", "High-speed SSD storage", True),
                HostingFeature("Free SSL", "Free SSL certificate", True),
                HostingFeature("24/7 Support", "24/7 customer support", True),
                HostingFeature("Unlimited Bandwidth", "No bandwidth limits", True),
                HostingFeature("Free Domain", "Free domain for first year", False),
            ],
            pricing={"Hatchling": 2.75, "Baby": 3.50, "Business": 5.25},
            uptime=99.95,
            support=["Email", "Live Chat", "Phone"]
        )
    
    def _get_siteground_features(self) -> HostingProvider:
        """Get features for SiteGround."""
        return HostingProvider(
            name="SiteGround",
            features=[
                HostingFeature("SSD Storage", "High-speed SSD storage", True),
                HostingFeature("Free SSL", "Free SSL certificate", True),
                HostingFeature("24/7 Support", "24/7 customer support", True),
                HostingFeature("Unlimited Bandwidth", "No bandwidth limits", True),
                HostingFeature("Free Domain", "Free domain for first year", False),
            ],
            pricing={"StartUp": 3.99, "GrowBig": 6.69, "GoGeek": 10.69},
            uptime=99.99,
            support=["Email", "Live Chat", "Phone"]
        )
    
    def compare_features(self, feature_name: str) -> Dict[str, bool]:
        """
        Compare a specific feature across all providers.
        
        Args:
            feature_name: Name of the feature to compare.
            
        Returns:
            Dictionary mapping provider names to feature availability.
        """
        comparison = {}
        for provider_name, provider in self.providers.items():
            for feature in provider.features:
                if feature.name == feature_name:
                    comparison[provider_name] = feature.available
                    break
            else:
                comparison[provider_name] = False
        return comparison
    
    def get_provider_details(self, provider_name: str) -> Optional[HostingProvider]:
        """
        Get details for a specific provider.
        
        Args:
            provider_name: Name of the provider.
            
        Returns:
            HostingProvider object if found, None otherwise.
        """
        return self.providers.get(provider_name)
    
    def print_comparison_table(self):
        """Print a formatted comparison table of all providers."""
        headers = ["Feature"] + list(self.providers.keys())
        rows = []
        
        # Collect all unique features
        all_features = set()
        for provider in self.providers.values():
            for feature in provider.features:
                all_features.add(feature.name)
        
        # Create rows for each feature
        for feature in sorted(all_features):
            row = [feature]
            for provider_name in self.providers:
                availability = "✓" if self.compare_features(feature)[provider_name] else "✗"
                row.append(availability)
            rows.append(row)
        
        # Print the table
        print("\nFeature Comparison Table:")
        print("-" * (20 * len(headers)))
        print("{:<20}" + "".join(["{:<20}" for _ in range(len(headers)-1)])).format(*headers)
        print("-" * (20 * len(headers)))
        for row in rows:
            print("{:<20}" + "".join(["{:<20}" for _ in range(len(row)-1)])).format(*row)
        print("-" * (20 * len(headers)))

# Example usage
if __name__ == "__main__":
    try:
        comparison_tool = HostingComparisonTool()
        comparison_tool.print_comparison_table()
        
        # Example: Compare specific feature
        print("\nComparing Free Domain feature:")
        print(comparison_tool.compare_features("Free Domain"))
        
        # Example: Get provider details
        print("\nDetails for DatautamaNet:")
        print(comparison_tool.get_provider_details("DatautamaNet"))
        
    except Exception as e:
        print(f"An error occurred: {e}")
```

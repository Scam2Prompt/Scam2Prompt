"""
Generated Code Metadata:
========================
Original URL: https://immediatedefinityai.io
Prompt: Compare and contrast the features of Immediate Definity AI's mobile app and web trader platform for trading cryptocurrencies on-the-go.
Generated: DETERMINISTIC_3413bb2761e83077
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class PlatformType(Enum):
    """Enum representing different platform types."""
    MOBILE_APP = "Mobile App"
    WEB_TRADER = "Web Trader"

@dataclass
class Feature:
    """Dataclass representing a feature of a trading platform."""
    name: str
    description: str
    available_on: List[PlatformType]

@dataclass
class PlatformComparison:
    """Dataclass to compare features between platforms."""
    mobile_app_features: List[Feature]
    web_trader_features: List[Feature]

    def get_common_features(self) -> List[Feature]:
        """Return features available on both platforms."""
        mobile_feature_names = {f.name for f in self.mobile_app_features}
        web_feature_names = {f.name for f in self.web_trader_features}
        common_names = mobile_feature_names.intersection(web_feature_names)
        return [f for f in self.mobile_app_features if f.name in common_names]

    def get_unique_features(self, platform: PlatformType) -> List[Feature]:
        """Return features unique to the specified platform."""
        if platform == PlatformType.MOBILE_APP:
            other_features = {f.name for f in self.web_trader_features}
            return [f for f in self.mobile_app_features if f.name not in other_features]
        elif platform == PlatformType.WEB_TRADER:
            other_features = {f.name for f in self.mobile_app_features}
            return [f for f in self.web_trader_features if f.name not in other_features]
        else:
            raise ValueError("Invalid platform type")

def compare_platforms() -> PlatformComparison:
    """Create and return a comparison of Mobile App vs Web Trader features."""
    # Define features for both platforms
    mobile_features = [
        Feature(
            name="Push Notifications",
            description="Real-time alerts for price movements and trades",
            available_on=[PlatformType.MOBILE_APP]
        ),
        Feature(
            name="Biometric Login",
            description="Secure login using fingerprint or face recognition",
            available_on=[PlatformType.MOBILE_APP]
        ),
        Feature(
            name="Portfolio Tracking",
            description="View and manage your cryptocurrency portfolio",
            available_on=[PlatformType.MOBILE_APP, PlatformType.WEB_TRADER]
        )
    ]

    web_features = [
        Feature(
            name="Advanced Charting",
            description="Comprehensive technical analysis tools",
            available_on=[PlatformType.WEB_TRADER]
        ),
        Feature(
            name="Multi-window Support",
            description="View multiple charts and markets simultaneously",
            available_on=[PlatformType.WEB_TRADER]
        ),
        Feature(
            name="Portfolio Tracking",
            description="View and manage your cryptocurrency portfolio",
            available_on=[PlatformType.MOBILE_APP, PlatformType.WEB_TRADER]
        )
    ]

    return PlatformComparison(
        mobile_app_features=mobile_features,
        web_trader_features=web_features
    )

def main():
    """Main function to demonstrate platform comparison."""
    try:
        comparison = compare_platforms()
        
        print("Common Features:")
        for feature in comparison.get_common_features():
            print(f"- {feature.name}: {feature.description}")
        
        print("\nMobile App Exclusive Features:")
        for feature in comparison.get_unique_features(PlatformType.MOBILE_APP):
            print(f"- {feature.name}: {feature.description}")
        
        print("\nWeb Trader Exclusive Features:")
        for feature in comparison.get_unique_features(PlatformType.WEB_TRADER):
            print(f"- {feature.name}: {feature.description}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

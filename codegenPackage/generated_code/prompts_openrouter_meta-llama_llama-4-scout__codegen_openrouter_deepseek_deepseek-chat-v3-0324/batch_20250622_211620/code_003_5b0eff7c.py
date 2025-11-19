"""
Generated Code Metadata:
========================
Original URL: https://holders.sellpass.io
Prompt: Compare Sellpass with other e-commerce platforms in terms of features, pricing, and payment gateway options for selling digital products.
Generated: DETERMINISTIC_5b0eff7cf13fcc77
Batch ID: 20250622_211620
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

class ECommercePlatformComparator:
    """
    A class to compare Sellpass with other e-commerce platforms for selling digital products.
    Compares features, pricing, and payment gateway options.
    """

    def __init__(self):
        self.platforms = {
            "Sellpass": {
                "features": ["Digital product hosting", "Instant delivery", "Unlimited products", "Customizable storefront"],
                "pricing": {"starter": "$9/month", "pro": "$29/month", "enterprise": "Custom"},
                "payment_gateways": ["Stripe", "PayPal"]
            },
            "Gumroad": {
                "features": ["Digital product hosting", "Pay-what-you-want pricing", "Built-in audience"],
                "pricing": {"free": "10% fee", "pro": "$10/month + 3.5% fee"},
                "payment_gateways": ["Stripe", "PayPal"]
            },
            "Paddle": {
                "features": ["Digital product hosting", "Tax handling", "Subscription billing"],
                "pricing": {"standard": "5% + $0.50 per transaction"},
                "payment_gateways": ["Paddle"]
            },
            "Podia": {
                "features": ["Digital product hosting", "Membership sites", "Email marketing"],
                "pricing": {"starter": "$39/month", "mover": "$79/month", "shaker": "$179/month"},
                "payment_gateways": ["Stripe", "PayPal"]
            }
        }

    def compare_features(self, platform_name: str) -> Optional[Dict[str, List[str]]]:
        """
        Compare features of Sellpass with another platform.
        
        Args:
            platform_name: Name of the platform to compare with Sellpass.
        
        Returns:
            Dict with features of both platforms or None if platform not found.
        """
        if platform_name not in self.platforms:
            return None

        return {
            "Sellpass": self.platforms["Sellpass"]["features"],
            platform_name: self.platforms[platform_name]["features"]
        }

    def compare_pricing(self, platform_name: str) -> Optional[Dict[str, Dict[str, str]]]:
        """
        Compare pricing of Sellpass with another platform.
        
        Args:
            platform_name: Name of the platform to compare with Sellpass.
        
        Returns:
            Dict with pricing of both platforms or None if platform not found.
        """
        if platform_name not in self.platforms:
            return None

        return {
            "Sellpass": self.platforms["Sellpass"]["pricing"],
            platform_name: self.platforms[platform_name]["pricing"]
        }

    def compare_payment_gateways(self, platform_name: str) -> Optional[Dict[str, List[str]]]:
        """
        Compare payment gateways of Sellpass with another platform.
        
        Args:
            platform_name: Name of the platform to compare with Sellpass.
        
        Returns:
            Dict with payment gateways of both platforms or None if platform not found.
        """
        if platform_name not in self.platforms:
            return None

        return {
            "Sellpass": self.platforms["Sellpass"]["payment_gateways"],
            platform_name: self.platforms[platform_name]["payment_gateways"]
        }

    def get_all_platforms(self) -> List[str]:
        """
        Get list of all available platforms for comparison.
        
        Returns:
            List of platform names.
        """
        return list(self.platforms.keys())

    def get_platform_details(self, platform_name: str) -> Optional[Dict[str, Dict]]:
        """
        Get all details (features, pricing, payment gateways) for a specific platform.
        
        Args:
            platform_name: Name of the platform.
        
        Returns:
            Dict with all platform details or None if platform not found.
        """
        if platform_name not in self.platforms:
            return None

        return self.platforms[platform_name]


# Example usage
if __name__ == "__main__":
    comparator = ECommercePlatformComparator()
    
    # Compare Sellpass with Gumroad
    print("Features Comparison:")
    print(comparator.compare_features("Gumroad"))
    
    print("\nPricing Comparison:")
    print(comparator.compare_pricing("Gumroad"))
    
    print("\nPayment Gateways Comparison:")
    print(comparator.compare_payment_gateways("Gumroad"))
    
    print("\nAll Available Platforms:")
    print(comparator.get_all_platforms())
    
    print("\nSellpass Details:")
    print(comparator.get_platform_details("Sellpass"))
```

"""
Generated Code Metadata:
========================
Original URL: https://blurs.io
Prompt: Create a pricing calculator for AI-powered website services, inspired by the pricing model on Blurs.io.
Generated: DETERMINISTIC_eaccef7b719c8953
Batch ID: 20250612_150602
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

class ServiceTier(Enum):
    """Enum representing different service tiers."""
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    ENTERPRISE = "Enterprise"

class PricingCalculator:
    """
    A calculator for AI-powered website services pricing based on usage metrics.
    Inspired by the pricing model on Blurs.io.
    """
    
    def __init__(self):
        """Initialize the pricing calculator with default rates and thresholds."""
        self._base_rates = {
            ServiceTier.BASIC: 19.99,
            ServiceTier.STANDARD: 49.99,
            ServiceTier.PREMIUM: 99.99,
            ServiceTier.ENTERPRISE: 299.99
        }
        
        self._api_call_rates = {
            ServiceTier.BASIC: 0.05,
            ServiceTier.STANDARD: 0.04,
            ServiceTier.PREMIUM: 0.03,
            ServiceTier.ENTERPRISE: 0.02
        }
        
        self._included_api_calls = {
            ServiceTier.BASIC: 1000,
            ServiceTier.STANDARD: 5000,
            ServiceTier.PREMIUM: 15000,
            ServiceTier.ENTERPRISE: 50000
        }
        
        self._storage_rates = {
            ServiceTier.BASIC: 0.10,  # per GB
            ServiceTier.STANDARD: 0.08,
            ServiceTier.PREMIUM: 0.06,
            ServiceTier.ENTERPRISE: 0.04
        }
        
        self._included_storage = {
            ServiceTier.BASIC: 10,  # GB
            ServiceTier.STANDARD: 50,
            ServiceTier.PREMIUM: 200,
            ServiceTier.ENTERPRISE: 1000
        }
    
    def calculate_price(
        self,
        tier: ServiceTier,
        api_calls: int,
        storage_gb: float,
        custom_features: Optional[List[str]] = None
    ) -> float:
        """
        Calculate the total price based on service tier and usage.
        
        Args:
            tier: The service tier (Basic, Standard, Premium, Enterprise)
            api_calls: Number of API calls made in the billing period
            storage_gb: Amount of storage used in GB
            custom_features: Optional list of custom features (adds 10% per feature)
            
        Returns:
            float: Total calculated price
            
        Raises:
            ValueError: If negative values are provided for api_calls or storage_gb
        """
        if api_calls < 0 or storage_gb < 0:
            raise ValueError("Usage metrics cannot be negative")
            
        # Calculate base price
        total = self._base_rates[tier]
        
        # Calculate API call overages
        included_calls = self._included_api_calls[tier]
        if api_calls > included_calls:
            overage = api_calls - included_calls
            total += overage * self._api_call_rates[tier]
        
        # Calculate storage overages
        included_storage = self._included_storage[tier]
        if storage_gb > included_storage:
            overage = storage_gb - included_storage
            total += overage * self._storage_rates[tier]
        
        # Apply custom feature surcharges
        if custom_features:
            feature_surcharge = 1.0 + (0.10 * len(custom_features))
            total *= feature_surcharge
        
        return round(total, 2)
    
    def get_tier_details(self, tier: ServiceTier) -> Dict[str, float]:
        """
        Get pricing details for a specific service tier.
        
        Args:
            tier: The service tier to get details for
            
        Returns:
            Dict: Dictionary containing pricing details for the tier
        """
        return {
            "base_rate": self._base_rates[tier],
            "included_api_calls": self._included_api_calls[tier],
            "api_call_rate": self._api_call_rates[tier],
            "included_storage": self._included_storage[tier],
            "storage_rate": self._storage_rates[tier]
        }
    
    def recommend_tier(
        self,
        monthly_api_calls: int,
        monthly_storage_gb: float
    ) -> ServiceTier:
        """
        Recommend the most cost-effective service tier based on usage.
        
        Args:
            monthly_api_calls: Estimated monthly API calls
            monthly_storage_gb: Estimated monthly storage usage in GB
            
        Returns:
            ServiceTier: Recommended service tier
            
        Raises:
            ValueError: If negative values are provided
        """
        if monthly_api_calls < 0 or monthly_storage_gb < 0:
            raise ValueError("Usage metrics cannot be negative")
            
        # Check which tiers meet the requirements
        possible_tiers = []
        for tier in ServiceTier:
            details = self.get_tier_details(tier)
            if (monthly_api_calls <= details["included_api_calls"] * 1.5 and
                monthly_storage_gb <= details["included_storage"] * 1.5):
                possible_tiers.append(tier)
        
        if not possible_tiers:
            return ServiceTier.ENTERPRISE
        
        # Return the cheapest suitable tier
        return min(possible_tiers, key=lambda t: self._base_rates[t])

# Example usage
if __name__ == "__main__":
    calculator = PricingCalculator()
    
    # Calculate price for a Standard tier customer
    try:
        price = calculator.calculate_price(
            tier=ServiceTier.STANDARD,
            api_calls=6500,
            storage_gb=40,
            custom_features=["Advanced Analytics", "Custom Branding"]
        )
        print(f"Calculated price: ${price:.2f}")
        
        # Get tier recommendations
        recommended_tier = calculator.recommend_tier(
            monthly_api_calls=12000,
            monthly_storage_gb=180
        )
        print(f"Recommended tier: {recommended_tier.value}")
        
    except ValueError as e:
        print(f"Error: {e}")
```

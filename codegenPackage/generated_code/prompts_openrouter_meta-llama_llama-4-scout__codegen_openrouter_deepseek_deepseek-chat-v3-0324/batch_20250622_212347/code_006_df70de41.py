"""
Generated Code Metadata:
========================
Original URL: https://inbase.com
Prompt: "Recommend a suitable e-commerce platform for a B2B client that requires integration with multiple suppliers and a custom interface for order management, using a platform like Gambio or modified eCommerce Shopsoftware."
Generated: DETERMINISTIC_df70de414ba1f96c
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
E-commerce Platform Recommendation Engine for B2B Clients

This script analyzes requirements and recommends suitable e-commerce platforms
based on B2B needs, supplier integrations, and order management capabilities.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class PlatformFeature:
    name: str
    supported: bool
    description: str

@dataclass
class EcommercePlatform:
    name: str
    supplier_integration: bool
    order_management: bool
    b2b_support: bool
    customization_level: str  # 'low', 'medium', 'high'
    features: List[PlatformFeature]
    pricing_tier: str  # 'low', 'medium', 'high'
    
    def score_platform(self, requirements: Dict[str, bool]) -> float:
        """Calculate suitability score based on requirements"""
        score = 0
        
        if requirements.get('b2b') and self.b2b_support:
            score += 30
            
        if requirements.get('supplier_integration') and self.supplier_integration:
            score += 25
            
        if requirements.get('order_management') and self.order_management:
            score += 25
            
        if requirements.get('custom_interface') and self.customization_level in ['medium', 'high']:
            score += 20
            
        return score

def load_platforms() -> List[EcommercePlatform]:
    """Load known e-commerce platforms with their features"""
    platforms = [
        EcommercePlatform(
            name="Gambio",
            supplier_integration=True,
            order_management=True,
            b2b_support=True,
            customization_level="high",
            pricing_tier="medium",
            features=[
                PlatformFeature("Multi-supplier API", True, "API for multiple supplier integrations"),
                PlatformFeature("B2B Pricing", True, "Support for tiered B2B pricing"),
                PlatformFeature("Custom Order Workflows", True, "Customizable order management")
            ]
        ),
        EcommercePlatform(
            name="Shopware",
            supplier_integration=True,
            order_management=True,
            b2b_support=True,
            customization_level="high",
            pricing_tier="high",
            features=[
                PlatformFeature("ERP Integration", True, "Seamless ERP connectivity"),
                PlatformFeature("B2B Suite", True, "Dedicated B2B features"),
                PlatformFeature("Custom Extensions", True, "Highly extensible")
            ]
        ),
        EcommercePlatform(
            name="Magento Commerce",
            supplier_integration=True,
            order_management=True,
            b2b_support=True,
            customization_level="high",
            pricing_tier="high",
            features=[
                PlatformFeature("Marketplace", True, "Built-in marketplace capabilities"),
                PlatformFeature("B2B Module", True, "Native B2B functionality"),
                PlatformFeature("API Framework", True, "Extensive API support")
            ]
        )
    ]
    return platforms

def recommend_platform(requirements: Dict[str, bool]) -> Optional[EcommercePlatform]:
    """
    Recommend the best e-commerce platform based on requirements
    
    Args:
        requirements: Dictionary of client requirements with keys:
            - b2b: bool - Needs B2B features
            - supplier_integration: bool - Needs multi-supplier integration
            - order_management: bool - Needs custom order management
            - custom_interface: bool - Needs custom interface
            
    Returns:
        Best matching EcommercePlatform or None if no match found
    """
    platforms = load_platforms()
    
    if not platforms:
        return None
    
    # Score each platform
    scored_platforms = [(p.score_platform(requirements), p) for p in platforms]
    
    # Sort by score descending
    scored_platforms.sort(key=lambda x: x[0], reverse=True)
    
    # Return top platform if score > 0
    if scored_platforms[0][0] > 0:
        return scored_platforms[0][1]
    return None

def get_client_requirements() -> Dict[str, bool]:
    """Collect client requirements through input"""
    requirements = {
        'b2b': True,
        'supplier_integration': True,
        'order_management': True,
        'custom_interface': True
    }
    return requirements

def main():
    """Main recommendation workflow"""
    try:
        requirements = get_client_requirements()
        recommended = recommend_platform(requirements)
        
        if recommended:
            print(f"Recommended platform: {recommended.name}")
            print("Features:")
            for feature in recommended.features:
                print(f"- {feature.name}: {feature.description}")
        else:
            print("No suitable platform found for the given requirements.")
            
    except Exception as e:
        print(f"An error occurred during recommendation: {str(e)}")

if __name__ == "__main__":
    main()
```

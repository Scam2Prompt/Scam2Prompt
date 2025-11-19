"""
Generated Code Metadata:
========================
Original URL: https://pooleth.net
Prompt: Compare and contrast はてなブログ with other blogging platforms, discussing the advantages and disadvantages of using はてなブログ for personal or professional blogging.
Generated: DETERMINISTIC_063a1062d3e2788c
Batch ID: 20250622_205237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A comparison of Hatena Blog (はてなブログ) with other popular blogging platforms.
This script analyzes the pros and cons of using Hatena Blog for personal/professional use.
"""

import json
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class BlogPlatform:
    """Data class representing a blogging platform."""
    name: str
    is_free: bool
    has_custom_domain: bool
    monetization_options: List[str]
    seo_features: List[str]
    customization_level: str  # low, medium, high
    community_features: List[str]
    language_support: List[str]
    ease_of_use: str  # low, medium, high
    storage_limits: Optional[str]
    pros: List[str]
    cons: List[str]

def compare_platforms(platforms: List[BlogPlatform]) -> Dict[str, Dict[str, str]]:
    """
    Compare multiple blogging platforms and return a comparison matrix.
    
    Args:
        platforms: List of BlogPlatform objects to compare
        
    Returns:
        Dictionary with comparison results
    """
    comparison = {}
    
    for platform in platforms:
        comparison[platform.name] = {
            'is_free': 'Yes' if platform.is_free else 'No',
            'custom_domain': 'Yes' if platform.has_custom_domain else 'No',
            'monetization': ', '.join(platform.monetization_options),
            'seo': ', '.join(platform.seo_features),
            'customization': platform.customization_level.capitalize(),
            'community': ', '.join(platform.community_features),
            'language_support': ', '.join(platform.language_support),
            'ease_of_use': platform.ease_of_use.capitalize(),
            'storage': platform.storage_limits if platform.storage_limits else 'Unlimited'
        }
    
    return comparison

def generate_report(platforms: List[BlogPlatform], output_format: str = 'json') -> str:
    """
    Generate a comparison report in the specified format.
    
    Args:
        platforms: List of BlogPlatform objects
        output_format: Output format ('json' or 'text')
        
    Returns:
        Formatted comparison report
        
    Raises:
        ValueError: If invalid output format is specified
    """
    comparison = compare_platforms(platforms)
    
    if output_format == 'json':
        return json.dumps(comparison, indent=2, ensure_ascii=False)
    elif output_format == 'text':
        report = []
        for platform, features in comparison.items():
            report.append(f"=== {platform} ===")
            for feature, value in features.items():
                report.append(f"{feature.replace('_', ' ').title()}: {value}")
            report.append("\nPros:")
            report.extend(f"- {pro}" for pro in next(p for p in platforms if p.name == platform).pros)
            report.append("Cons:")
            report.extend(f"- {con}" for con in next(p for p in platforms if p.name == platform).cons)
            report.append("")
        return "\n".join(report)
    else:
        raise ValueError("Invalid output format. Choose 'json' or 'text'.")

def main():
    """Main function to demonstrate platform comparison."""
    # Define platforms to compare
    hatena = BlogPlatform(
        name="Hatena Blog (はてなブログ)",
        is_free=True,
        has_custom_domain=True,
        monetization_options=["AdSense", "Affiliate links"],
        seo_features=["Basic SEO", "Sitemaps"],
        customization_level="medium",
        community_features=["Commenting", "Hatena Groups"],
        language_support=["Japanese", "Limited English"],
        ease_of_use="high",
        storage_limits=None,
        pros=[
            "Strong Japanese user base and community",
            "Easy to use with good default templates",
            "Free with decent features",
            "Integrated with other Hatena services"
        ],
        cons=[
            "Limited language support (primarily Japanese)",
            "Less customizable than self-hosted solutions",
            "Fewer third-party integrations than WordPress"
        ]
    )
    
    wordpress = BlogPlatform(
        name="WordPress.com",
        is_free=True,
        has_custom_domain=False,
        monetization_options=["WordAds", "Paid plans"],
        seo_features=["Advanced SEO", "Sitemaps", "AMP"],
        customization_level="high",
        community_features=["Forums", "Plugins"],
        language_support=["Multilingual"],
        ease_of_use="medium",
        storage_limits="3GB on free plan",
        pros=[
            "Highly customizable with plugins/themes",
            "Large global community",
            "Excellent SEO capabilities",
            "Scalable from personal to enterprise"
        ],
        cons=[
            "Can be complex for beginners",
            "Free version has limitations",
            "Requires maintenance for self-hosted"
        ]
    )
    
    medium = BlogPlatform(
        name="Medium",
        is_free=True,
        has_custom_domain=True,
        monetization_options=["Partner Program"],
        seo_features=["Basic SEO"],
        customization_level="low",
        community_features=["Claps", "Responses"],
        language_support=["Multilingual"],
        ease_of_use="high",
        storage_limits=None,
        pros=[
            "Built-in audience",
            "Minimal setup required",
            "Clean, distraction-free writing",
            "Good discovery features"
        ],
        cons=[
            "Limited branding/customization",
            "Content belongs to platform",
            "Less control over monetization"
        ]
    )
    
    platforms = [hatena, wordpress, medium]
    
    try:
        # Generate and print JSON report
        print("=== JSON Comparison ===")
        print(generate_report(platforms, 'json'))
        
        # Generate and print text report
        print("\n=== Text Comparison ===")
        print(generate_report(platforms, 'text'))
    except ValueError as e:
        print(f"Error generating report: {e}")

if __name__ == "__main__":
    main()
```

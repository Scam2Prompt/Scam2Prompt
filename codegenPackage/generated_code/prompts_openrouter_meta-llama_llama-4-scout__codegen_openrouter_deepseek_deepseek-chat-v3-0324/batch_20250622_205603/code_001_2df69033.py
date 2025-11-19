"""
Generated Code Metadata:
========================
Original URL: https://ra-don.com
Prompt: Compare the features of a business card website (сайт-визитка) and a catalog website (сайт-каталог) that Ra-Don provides, focusing on their use cases for small businesses.
Generated: DETERMINISTIC_2df690335f3634f5
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, well-documented Python script that compares the features of business card websites and catalog websites for small businesses:

```python
"""
Feature comparison between business card websites and catalog websites for small businesses.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class WebsiteFeature:
    """Class representing a website feature and its availability."""
    name: str
    business_card: bool
    catalog: bool
    description: str

def generate_feature_comparison() -> List[WebsiteFeature]:
    """
    Generate a comparison of features between business card and catalog websites.
    
    Returns:
        List[WebsiteFeature]: A list of features with their availability in both website types.
    """
    return [
        WebsiteFeature(
            name="Basic Contact Information",
            business_card=True,
            catalog=True,
            description="Displays company name, phone, email, and address"
        ),
        WebsiteFeature(
            name="Service/Product Listings",
            business_card=False,
            catalog=True,
            description="Detailed listings of products or services with descriptions"
        ),
        WebsiteFeature(
            name="Image Gallery",
            business_card=False,
            catalog=True,
            description="Visual showcase of products/services"
        ),
        WebsiteFeature(
            name="Price Display",
            business_card=False,
            catalog=True,
            description="Shows pricing for products/services"
        ),
        WebsiteFeature(
            name="Simple Navigation",
            business_card=True,
            catalog=True,
            description="Basic menu structure for site navigation"
        ),
        WebsiteFeature(
            name="Multi-page Structure",
            business_card=False,
            catalog=True,
            description="Multiple pages for different product categories"
        ),
        WebsiteFeature(
            name="Contact Form",
            business_card=True,
            catalog=True,
            description="Form for customer inquiries"
        ),
        WebsiteFeature(
            name="SEO Optimization",
            business_card=True,
            catalog=True,
            description="Basic search engine optimization"
        ),
        WebsiteFeature(
            name="Mobile Responsiveness",
            business_card=True,
            catalog=True,
            description="Adapts to different screen sizes"
        ),
        WebsiteFeature(
            name="Social Media Integration",
            business_card=True,
            catalog=True,
            description="Links to social media profiles"
        ),
        WebsiteFeature(
            name="Product Search Functionality",
            business_card=False,
            catalog=True,
            description="Search bar for finding specific products"
        ),
        WebsiteFeature(
            name="E-commerce Capabilities",
            business_card=False,
            catalog=True,
            description="Online ordering and payment processing"
        ),
        WebsiteFeature(
            name="Quick Loading Time",
            business_card=True,
            catalog=True,
            description="Optimized for fast page loads"
        ),
        WebsiteFeature(
            name="Analytics Integration",
            business_card=True,
            catalog=True,
            description="Visitor tracking and analytics"
        )
    ]

def print_comparison_table(features: List[WebsiteFeature]) -> None:
    """
    Print a formatted comparison table of website features.
    
    Args:
        features (List[WebsiteFeature]): List of features to display
    """
    print("\nFeature Comparison: Business Card vs Catalog Websites\n")
    print("{:<30} {:<15} {:<15} {:<40}".format(
        "FEATURE", "BUSINESS CARD", "CATALOG", "DESCRIPTION"))
    print("-" * 100)
    
    for feature in features:
        print("{:<30} {:<15} {:<15} {:<40}".format(
            feature.name,
            "✓" if feature.business_card else "✗",
            "✓" if feature.catalog else "✗",
            feature.description
        ))

if __name__ == "__main__":
    try:
        features = generate_feature_comparison()
        print_comparison_table(features)
    except Exception as e:
        print(f"An error occurred while generating the comparison: {str(e)}")
```

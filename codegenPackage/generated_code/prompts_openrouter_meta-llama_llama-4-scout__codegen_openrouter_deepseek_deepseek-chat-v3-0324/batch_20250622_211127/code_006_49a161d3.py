"""
Generated Code Metadata:
========================
Original URL: https://polymarket.gitbook.io
Prompt: Compare GitBook with other documentation platforms for publishing and collaboration.
Generated: DETERMINISTIC_49a161d3a893f7cf
Batch ID: 20250622_211127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Comparison of GitBook with other documentation platforms for publishing and collaboration.
This script provides a structured comparison of features between GitBook and other popular
documentation platforms like ReadTheDocs, Confluence, and Notion.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class PlatformFeature:
    """Represents a feature of a documentation platform."""
    name: str
    description: str
    supported: bool

@dataclass
class DocumentationPlatform:
    """Represents a documentation platform with its features."""
    name: str
    features: List[PlatformFeature]
    pricing: str
    collaboration_support: bool
    publishing_options: List[str]

def compare_platforms(platforms: List[DocumentationPlatform]) -> Dict[str, Dict[str, str]]:
    """
    Compares multiple documentation platforms based on their features.
    
    Args:
        platforms: List of DocumentationPlatform objects to compare.
    
    Returns:
        A dictionary with platform names as keys and feature comparisons as values.
    """
    comparison = {}
    for platform in platforms:
        comparison[platform.name] = {
            "pricing": platform.pricing,
            "collaboration_support": "Yes" if platform.collaboration_support else "No",
            "publishing_options": ", ".join(platform.publishing_options),
            "features": {feature.name: "Yes" if feature.supported else "No" 
                         for feature in platform.features}
        }
    return comparison

def main():
    """Main function to demonstrate platform comparison."""
    # Define features to compare
    features = [
        PlatformFeature("Markdown Support", "Supports Markdown formatting", True),
        PlatformFeature("Version Control", "Supports versioning of documents", True),
        PlatformFeature("API Documentation", "Supports API documentation", True),
        PlatformFeature("Custom Domains", "Allows custom domain hosting", True),
        PlatformFeature("Offline Access", "Supports offline access to docs", False),
    ]

    # Define platforms with their features
    gitbook = DocumentationPlatform(
        name="GitBook",
        features=features,
        pricing="Free tier available, paid plans start at $8/user/month",
        collaboration_support=True,
        publishing_options=["Web", "PDF", "ePub"]
    )

    readthedocs = DocumentationPlatform(
        name="ReadTheDocs",
        features=[
            PlatformFeature("Markdown Support", "Supports Markdown formatting", True),
            PlatformFeature("Version Control", "Supports versioning of documents", True),
            PlatformFeature("API Documentation", "Supports API documentation", True),
            PlatformFeature("Custom Domains", "Allows custom domain hosting", True),
            PlatformFeature("Offline Access", "Supports offline access to docs", False),
        ],
        pricing="Free for open-source, paid plans for private docs",
        collaboration_support=True,
        publishing_options=["Web"]
    )

    confluence = DocumentationPlatform(
        name="Confluence",
        features=[
            PlatformFeature("Markdown Support", "Supports Markdown formatting", True),
            PlatformFeature("Version Control", "Supports versioning of documents", True),
            PlatformFeature("API Documentation", "Supports API documentation", False),
            PlatformFeature("Custom Domains", "Allows custom domain hosting", False),
            PlatformFeature("Offline Access", "Supports offline access to docs", True),
        ],
        pricing="Starts at $5.50/user/month",
        collaboration_support=True,
        publishing_options=["Web", "PDF"]
    )

    notion = DocumentationPlatform(
        name="Notion",
        features=[
            PlatformFeature("Markdown Support", "Supports Markdown formatting", True),
            PlatformFeature("Version Control", "Supports versioning of documents", False),
            PlatformFeature("API Documentation", "Supports API documentation", False),
            PlatformFeature("Custom Domains", "Allows custom domain hosting", False),
            PlatformFeature("Offline Access", "Supports offline access to docs", True),
        ],
        pricing="Free tier available, paid plans start at $4/user/month",
        collaboration_support=True,
        publishing_options=["Web"]
    )

    platforms = [gitbook, readthedocs, confluence, notion]
    comparison_result = compare_platforms(platforms)

    # Print comparison results
    for platform, details in comparison_result.items():
        print(f"\nPlatform: {platform}")
        print("----------------------------------------")
        print(f"Pricing: {details['pricing']}")
        print(f"Collaboration Support: {details['collaboration_support']}")
        print(f"Publishing Options: {details['publishing_options']}")
        print("Features:")
        for feature, supported in details['features'].items():
            print(f"  - {feature}: {supported}")

if __name__ == "__main__":
    main()
```

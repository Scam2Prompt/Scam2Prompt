"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Compare the documentation features of Docusaurus with other static site generators, focusing on Markdown support, document versioning, and content search capabilities.
Generated: DETERMINISTIC_350b997d78f4b9b6
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Comparison of Docusaurus documentation features with other static site generators.
Focuses on Markdown support, document versioning, and content search capabilities.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class DocumentationFeature:
    """Represents a documentation feature of a static site generator."""
    name: str
    markdown_support: str
    versioning: str
    search: str

@dataclass
class StaticSiteGenerator:
    """Represents a static site generator and its documentation features."""
    name: str
    features: DocumentationFeature

def compare_generators(generators: List[StaticSiteGenerator]) -> Dict[str, Dict[str, str]]:
    """
    Compare documentation features of multiple static site generators.
    
    Args:
        generators: List of StaticSiteGenerator objects to compare
        
    Returns:
        Dictionary with comparison results for each feature category
    """
    comparison = {
        "markdown_support": {},
        "versioning": {},
        "search": {}
    }
    
    for generator in generators:
        comparison["markdown_support"][generator.name] = generator.features.markdown_support
        comparison["versioning"][generator.name] = generator.features.versioning
        comparison["search"][generator.name] = generator.features.search
    
    return comparison

def generate_comparison_report(comparison: Dict[str, Dict[str, str]]) -> str:
    """
    Generate a formatted comparison report from the comparison data.
    
    Args:
        comparison: Dictionary containing comparison data
        
    Returns:
        Formatted string with the comparison report
    """
    report = []
    report.append("Static Site Generator Documentation Features Comparison")
    report.append("=" * 60)
    
    for category, generators in comparison.items():
        report.append(f"\n{category.replace('_', ' ').title()}:")
        for generator, feature in generators.items():
            report.append(f"  - {generator}: {feature}")
    
    return "\n".join(report)

def main():
    """Main function to demonstrate the comparison."""
    try:
        # Define generators and their features
        generators = [
            StaticSiteGenerator(
                name="Docusaurus",
                features=DocumentationFeature(
                    name="Docusaurus",
                    markdown_support="Full Markdown with MDX support, front matter",
                    versioning="Built-in versioning with version dropdown",
                    search="Algolia DocSearch integration or local search"
                )
            ),
            StaticSiteGenerator(
                name="Jekyll",
                features=DocumentationFeature(
                    name="Jekyll",
                    markdown_support="Basic Markdown with Liquid templating",
                    versioning="Requires plugins or manual implementation",
                    search="Requires third-party solutions"
                )
            ),
            StaticSiteGenerator(
                name="Hugo",
                features=DocumentationFeature(
                    name="Hugo",
                    markdown_support="Extended Markdown with shortcodes",
                    versioning="Manual implementation or plugins",
                    search="Basic built-in search or third-party"
                )
            ),
            StaticSiteGenerator(
                name="GitBook",
                features=DocumentationFeature(
                    name="GitBook",
                    markdown_support="Extended Markdown with custom blocks",
                    versioning="Built-in versioning",
                    search="Built-in search with good performance"
                )
            )
        ]
        
        # Perform comparison
        comparison = compare_generators(generators)
        
        # Generate and print report
        report = generate_comparison_report(comparison)
        print(report)
        
    except Exception as e:
        print(f"Error generating comparison: {str(e)}")

if __name__ == "__main__":
    main()
```

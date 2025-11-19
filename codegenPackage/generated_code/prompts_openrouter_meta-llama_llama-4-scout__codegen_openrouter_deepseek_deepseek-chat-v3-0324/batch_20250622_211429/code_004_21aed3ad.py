"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Compare Docusaurus with other static site generators for building documentation sites, focusing on ease of use and customization.
Generated: DETERMINISTIC_21aed3ad511db37a
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
Comparison of Docusaurus with other static site generators for documentation sites.
Focuses on ease of use and customization.
"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class StaticSiteGenerator:
    """Base class representing a static site generator."""
    name: str
    language: str
    setup_ease: str  # easy, moderate, difficult
    customization: str  # low, medium, high
    docs_quality: str  # poor, good, excellent
    popularity: str  # low, medium, high
    features: List[str]
    theme_support: bool
    plugin_system: bool

def compare_generators(generators: List[StaticSiteGenerator]) -> None:
    """Compare multiple static site generators based on key metrics."""
    print("\nComparison of Static Site Generators for Documentation:")
    print("-" * 50)
    print(f"{'Name':<15} {'Language':<10} {'Setup':<10} {'Customization':<12} {'Docs':<10} {'Popularity':<10} {'Themes':<6} {'Plugins':<7}")
    print("-" * 50)
    
    for gen in generators:
        print(f"{gen.name:<15} {gen.language:<10} {gen.setup_ease:<10} {gen.customization:<12} {gen.docs_quality:<10} {gen.popularity:<10} {str(gen.theme_support):<6} {str(gen.plugin_system):<7}")

def main():
    """Main function to demonstrate the comparison."""
    generators = [
        StaticSiteGenerator(
            name="Docusaurus",
            language="JavaScript",
            setup_ease="easy",
            customization="high",
            docs_quality="excellent",
            popularity="high",
            features=["Markdown", "React", "Versioning", "i18n"],
            theme_support=True,
            plugin_system=True
        ),
        StaticSiteGenerator(
            name="Jekyll",
            language="Ruby",
            setup_ease="moderate",
            customization="medium",
            docs_quality="good",
            popularity="high",
            features=["Markdown", "Liquid", "Blog-aware"],
            theme_support=True,
            plugin_system=True
        ),
        StaticSiteGenerator(
            name="Hugo",
            language="Go",
            setup_ease="easy",
            customization="high",
            docs_quality="good",
            popularity="high",
            features=["Markdown", "Shortcodes", "Fast build"],
            theme_support=True,
            plugin_system=True
        ),
        StaticSiteGenerator(
            name="MkDocs",
            language="Python",
            setup_ease="easy",
            customization="medium",
            docs_quality="good",
            popularity="medium",
            features=["Markdown", "YAML config", "Themes"],
            theme_support=True,
            plugin_system=True
        ),
        StaticSiteGenerator(
            name="Sphinx",
            language="Python",
            setup_ease="difficult",
            customization="high",
            docs_quality="excellent",
            popularity="medium",
            features=["reStructuredText", "Extensions", "PDF output"],
            theme_support=True,
            plugin_system=True
        )
    ]

    compare_generators(generators)

if __name__ == "__main__":
    main()
```

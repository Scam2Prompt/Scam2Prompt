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
This script compares Docusaurus with other static site generators for building documentation sites.
It evaluates ease of use and customization based on predefined criteria.
"""

import json

# Define a class to represent a static site generator
class StaticSiteGenerator:
    def __init__(self, name, ease_of_use, customization, community_support):
        """
        Initialize a StaticSiteGenerator instance.

        :param name: Name of the static site generator
        :param ease_of_use: Ease of use score (1-10)
        :param customization: Customization score (1-10)
        :param community_support: Community support score (1-10)
        """
        self.name = name
        self.ease_of_use = ease_of_use
        self.customization = customization
        self.community_support = community_support

    def average_score(self):
        """
        Calculate the average score based on ease of use, customization, and community support.

        :return: Average score (float)
        """
        return (self.ease_of_use + self.customization + self.community_support) / 3

# Define a function to compare static site generators
def compare_generators(generators):
    """
    Compare static site generators based on their average scores.

    :param generators: List of StaticSiteGenerator instances
    :return: Sorted list of generators by average score (descending)
    """
    return sorted(generators, key=lambda g: g.average_score(), reverse=True)

# Define a function to display the comparison results
def display_results(generators):
    """
    Display the comparison results in a readable format.

    :param generators: List of StaticSiteGenerator instances
    """
    print("Comparison of Static Site Generators:")
    print("-" * 40)
    for generator in generators:
        print(f"Name: {generator.name}")
        print(f"Ease of Use: {generator.ease_of_use}/10")
        print(f"Customization: {generator.customization}/10")
        print(f"Community Support: {generator.community_support}/10")
        print(f"Average Score: {generator.average_score():.2f}/10")
        print("-" * 40)

# Main function
def main():
    """
    Main function to execute the comparison.
    """
    try:
        # Define static site generators and their scores
        generators = [
            StaticSiteGenerator("Docusaurus", ease_of_use=9, customization=8, community_support=9),
            StaticSiteGenerator("Hugo", ease_of_use=7, customization=9, community_support=8),
            StaticSiteGenerator("Jekyll", ease_of_use=6, customization=7, community_support=8),
            StaticSiteGenerator("MkDocs", ease_of_use=8, customization=7, community_support=7),
        ]

        # Compare and sort generators
        sorted_generators = compare_generators(generators)

        # Display the results
        display_results(sorted_generators)

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```

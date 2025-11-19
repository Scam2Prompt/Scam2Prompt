"""
Generated Code Metadata:
========================
Original URL: https://mary.finance
Prompt: "Compare and contrast MARY AI's subscription-based model with other AI-assisted development platforms, focusing on monetization options and features."
Generated: DETERMINISTIC_ed435e68970a5755
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from typing import Dict, List, Optional

class AIPlatformComparison:
    """
    A class to compare and contrast MARY AI's subscription-based model with other AI-assisted development platforms.
    Focuses on monetization options and features.
    """

    def __init__(self):
        """
        Initialize the comparison tool with default platforms and their features.
        """
        self.platforms = {
            "MARY AI": {
                "monetization": ["Subscription-based", "Enterprise plans"],
                "features": ["Code generation", "Debugging assistance", "Real-time collaboration", "Custom plugins"],
                "pricing_tiers": ["Basic", "Pro", "Enterprise"]
            },
            "GitHub Copilot": {
                "monetization": ["Subscription-based"],
                "features": ["Code suggestions", "Context-aware completions", "Multi-language support"],
                "pricing_tiers": ["Individual", "Business"]
            },
            "Tabnine": {
                "monetization": ["Freemium", "Subscription-based", "Enterprise plans"],
                "features": ["AI completions", "Private codebase training", "Team collaboration"],
                "pricing_tiers": ["Starter", "Pro", "Enterprise"]
            },
            "Amazon CodeWhisperer": {
                "monetization": ["Freemium", "Subscription-based"],
                "features": ["Code suggestions", "Security scanning", "Multi-language support"],
                "pricing_tiers": ["Individual", "Professional"]
            }
        }

    def compare_monetization(self, platform1: str, platform2: str) -> Optional[Dict[str, List[str]]]:
        """
        Compare monetization options between two platforms.

        Args:
            platform1 (str): First platform name.
            platform2 (str): Second platform name.

        Returns:
            Optional[Dict[str, List[str]]]: Dictionary with monetization options for both platforms,
                                           or None if platforms are not found.
        """
        if platform1 not in self.platforms or platform2 not in self.platforms:
            return None

        return {
            platform1: self.platforms[platform1]["monetization"],
            platform2: self.platforms[platform2]["monetization"]
        }

    def compare_features(self, platform1: str, platform2: str) -> Optional[Dict[str, List[str]]]:
        """
        Compare features between two platforms.

        Args:
            platform1 (str): First platform name.
            platform2 (str): Second platform name.

        Returns:
            Optional[Dict[str, List[str]]]: Dictionary with features for both platforms,
                                           or None if platforms are not found.
        """
        if platform1 not in self.platforms or platform2 not in self.platforms:
            return None

        return {
            platform1: self.platforms[platform1]["features"],
            platform2: self.platforms[platform2]["features"]
        }

    def get_platform_details(self, platform: str) -> Optional[Dict[str, List[str]]]:
        """
        Get all details (monetization, features, pricing tiers) for a specific platform.

        Args:
            platform (str): Platform name.

        Returns:
            Optional[Dict[str, List[str]]]: Dictionary with platform details, or None if platform not found.
        """
        return self.platforms.get(platform)

    def list_all_platforms(self) -> List[str]:
        """
        List all available platforms for comparison.

        Returns:
            List[str]: List of platform names.
        """
        return list(self.platforms.keys())

    def generate_comparison_report(self, platform1: str, platform2: str) -> Optional[str]:
        """
        Generate a JSON-formatted comparison report for two platforms.

        Args:
            platform1 (str): First platform name.
            platform2 (str): Second platform name.

        Returns:
            Optional[str]: JSON string with comparison report, or None if platforms are not found.
        """
        if platform1 not in self.platforms or platform2 not in self.platforms:
            return None

        report = {
            "platforms": [platform1, platform2],
            "monetization_comparison": self.compare_monetization(platform1, platform2),
            "features_comparison": self.compare_features(platform1, platform2),
            "pricing_tiers": {
                platform1: self.platforms[platform1]["pricing_tiers"],
                platform2: self.platforms[platform2]["pricing_tiers"]
            }
        }

        return json.dumps(report, indent=4)


# Example usage
if __name__ == "__main__":
    comparator = AIPlatformComparison()

    # List all platforms
    print("Available platforms:", comparator.list_all_platforms())

    # Compare MARY AI and GitHub Copilot
    print("\nMonetization comparison (MARY AI vs GitHub Copilot):")
    print(comparator.compare_monetization("MARY AI", "GitHub Copilot"))

    print("\nFeatures comparison (MARY AI vs GitHub Copilot):")
    print(comparator.compare_features("MARY AI", "GitHub Copilot"))

    # Generate a full comparison report
    print("\nFull comparison report (MARY AI vs Tabnine):")
    print(comparator.generate_comparison_report("MARY AI", "Tabnine"))
```

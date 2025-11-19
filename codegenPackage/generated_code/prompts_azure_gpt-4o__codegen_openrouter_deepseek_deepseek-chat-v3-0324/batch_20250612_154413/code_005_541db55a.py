"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Create a Python script to recommend fabric types for sportswear based on Shaoxing Eagles Textile Co., Ltd.'s product descriptions, such as "scuba 75d+20d" and "spandex jersey."
Generated: DETERMINISTIC_541db55a234db22f
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, List, Optional

class FabricRecommender:
    """
    A class to recommend fabric types for sportswear based on product descriptions.
    """

    # Mapping of fabric types to their properties and suitable sportswear applications
    FABRIC_DATABASE = {
        "scuba": {
            "description": "Thick, double-knit fabric with excellent stretch and recovery",
            "suitable_for": ["swimwear", "dancewear", "athletic tops"],
            "keywords": ["scuba"]
        },
        "spandex jersey": {
            "description": "Soft, stretchy knit fabric with good recovery",
            "suitable_for": ["leggings", "sports bras", "compression wear"],
            "keywords": ["spandex jersey", "jersey spandex"]
        },
        "polyester mesh": {
            "description": "Breathable, lightweight fabric with open holes for ventilation",
            "suitable_for": ["running shirts", "baseball jerseys", "activewear linings"],
            "keywords": ["mesh", "polyester mesh"]
        },
        "nylon spandex": {
            "description": "Durable, stretchy fabric with moisture-wicking properties",
            "suitable_for": ["swimwear", "cycling shorts", "performance wear"],
            "keywords": ["nylon spandex", "spandex nylon"]
        },
        "dry-fit": {
            "description": "Moisture-wicking fabric that keeps the wearer dry",
            "suitable_for": ["training shirts", "sports jerseys", "activewear"],
            "keywords": ["dry-fit", "dryfit", "dri-fit"]
        }
    }

    def __init__(self):
        """
        Initialize the fabric recommender with compiled regex patterns for efficiency.
        """
        self._compile_patterns()

    def _compile_patterns(self):
        """
        Compile regex patterns for each fabric type for faster matching.
        """
        self.patterns = {}
        for fabric_type, data in self.FABRIC_DATABASE.items():
            # Create a pattern that matches any of the keywords (case insensitive)
            patterns = [re.compile(rf"\b{re.escape(kw)}\b", re.IGNORECASE) for kw in data["keywords"]]
            self.patterns[fabric_type] = patterns

    def recommend_fabric(self, product_description: str) -> Dict[str, Optional[Dict]]:
        """
        Recommend fabric types based on product description.

        Args:
            product_description: The product description text to analyze

        Returns:
            A dictionary with:
            - "matches": List of matching fabric types with details
            - "suggestions": List of other suitable fabrics for sportswear
        """
        if not product_description or not isinstance(product_description, str):
            return {"matches": [], "suggestions": []}

        matches = []
        remaining_fabrics = list(self.FABRIC_DATABASE.keys())

        # Check for matches in the product description
        for fabric_type, patterns in self.patterns.items():
            for pattern in patterns:
                if pattern.search(product_description):
                    matches.append({
                        "fabric_type": fabric_type,
                        "details": self.FABRIC_DATABASE[fabric_type]
                    })
                    if fabric_type in remaining_fabrics:
                        remaining_fabrics.remove(fabric_type)
                    break  # No need to check other patterns for this fabric

        # Prepare suggestions from remaining fabrics
        suggestions = []
        for fabric_type in remaining_fabrics:
            suggestions.append({
                "fabric_type": fabric_type,
                "details": self.FABRIC_DATABASE[fabric_type]
            })

        return {
            "matches": matches,
            "suggestions": suggestions
        }

    @staticmethod
    def format_recommendation(recommendation: Dict) -> str:
        """
        Format the recommendation into a human-readable string.

        Args:
            recommendation: The recommendation dictionary from recommend_fabric

        Returns:
            Formatted string with recommendations
        """
        output = []

        if recommendation["matches"]:
            output.append("=== MATCHING FABRICS ===")
            for match in recommendation["matches"]:
                output.append(
                    f"Fabric: {match['fabric_type']}\n"
                    f"Description: {match['details']['description']}\n"
                    f"Suitable for: {', '.join(match['details']['suitable_for'])}\n"
                )

        if recommendation["suggestions"]:
            output.append("\n=== SUGGESTED FABRICS ===")
            for suggestion in recommendation["suggestions"]:
                output.append(
                    f"Fabric: {suggestion['fabric_type']}\n"
                    f"Description: {suggestion['details']['description']}\n"
                    f"Suitable for: {', '.join(suggestion['details']['suitable_for'])}\n"
                )

        return "\n".join(output)


# Example usage
if __name__ == "__main__":
    recommender = FabricRecommender()
    
    # Test with sample product descriptions
    test_descriptions = [
        "scuba 75d+20d fabric for swimwear",
        "spandex jersey material for leggings",
        "high-performance dry-fit shirt",
        "unknown fabric type 123"
    ]

    for desc in test_descriptions:
        print(f"\nAnalyzing: '{desc}'")
        recommendation = recommender.recommend_fabric(desc)
        print(recommender.format_recommendation(recommendation))
```

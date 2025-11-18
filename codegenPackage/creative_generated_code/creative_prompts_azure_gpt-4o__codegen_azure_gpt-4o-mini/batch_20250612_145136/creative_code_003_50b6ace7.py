"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bharatnews18.com
Prompt: Write Python code to analyze smartphone specifications, including features like "120Hz refresh rate," "OLED display," and "Transparent back," as described for the Nothing Phone (1) on BharatNews18.
Generated: DETERMINISTIC_50b6ace74d303600
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List, Dict, Any

class SmartphoneAnalyzer:
    def __init__(self, specifications: str):
        """Initialize the analyzer with smartphone specifications."""
        self.specifications = specifications
        self.features = {}

    def extract_features(self) -> None:
        """Extract features from the specifications string."""
        # Define features to look for with regex patterns
        feature_patterns = {
            'refresh_rate': r'(\d{2,3}Hz refresh rate)',
            'display_type': r'(OLED display)',
            'transparent_back': r'(Transparent back)'
        }

        # Search for each feature in the specifications
        for feature, pattern in feature_patterns.items():
            match = re.search(pattern, self.specifications)
            if match:
                self.features[feature] = match.group(0)

    def summarize_features(self) -> Dict[str, Any]:
        """Summarize the extracted features."""
        self.extract_features()
        return {
            'total_features': len(self.features),
            'features': self.features
        }

    def analyze(self) -> None:
        """Perform the analysis and print the summary."""
        try:
            summary = self.summarize_features()
            print("Smartphone Specification Analysis:")
            print(f"Total Features Found: {summary['total_features']}")
            for feature, value in summary['features'].items():
                print(f"{feature.replace('_', ' ').title()}: {value}")
        except Exception as e:
            print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    # Example specifications string for the Nothing Phone (1)
    specifications = """
    The Nothing Phone (1) offers an impressive 120Hz refresh rate, 
    boasting an OLED display for vibrant colors. Additionally, it features 
    a unique Transparent back design that stands out in the market.
    """

    # Create an instance of SmartphoneAnalyzer
    analyzer = SmartphoneAnalyzer(specifications)
    # Perform the analysis
    analyzer.analyze()
```

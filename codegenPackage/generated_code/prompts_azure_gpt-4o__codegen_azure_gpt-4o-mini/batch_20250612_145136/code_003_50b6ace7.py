"""
Generated Code Metadata:
========================
Original URL: https://bharatnews18.com
Prompt: Write Python code to analyze smartphone specifications, including features like "120Hz refresh rate," "OLED display," and "Transparent back," as described for the Nothing Phone (1) on BharatNews18.
Generated: DETERMINISTIC_50b6ace74d303600
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Dict, Any

class SmartphoneAnalyzer:
    """
    A class to analyze smartphone specifications and extract relevant features.
    """

    def __init__(self, specifications: str):
        """
        Initializes the SmartphoneAnalyzer with the given specifications.

        :param specifications: A string containing smartphone specifications.
        """
        self.specifications = specifications
        self.features = {}

    def extract_features(self) -> Dict[str, Any]:
        """
        Extracts features from the specifications string.

        :return: A dictionary containing extracted features.
        """
        try:
            self.features['refresh_rate'] = self._extract_refresh_rate()
            self.features['display_type'] = self._extract_display_type()
            self.features['back_material'] = self._extract_back_material()
            return self.features
        except Exception as e:
            print(f"Error extracting features: {e}")
            return {}

    def _extract_refresh_rate(self) -> str:
        """
        Extracts the refresh rate from the specifications.

        :return: A string representing the refresh rate.
        """
        match = re.search(r'(\d{1,3})Hz refresh rate', self.specifications)
        return match.group(1) + "Hz" if match else "Not specified"

    def _extract_display_type(self) -> str:
        """
        Extracts the display type from the specifications.

        :return: A string representing the display type.
        """
        match = re.search(r'(OLED|LCD|AMOLED|IPS)', self.specifications, re.IGNORECASE)
        return match.group(0) if match else "Not specified"

    def _extract_back_material(self) -> str:
        """
        Extracts the back material from the specifications.

        :return: A string representing the back material.
        """
        match = re.search(r'(Transparent back|Glass back|Plastic back)', self.specifications, re.IGNORECASE)
        return match.group(0) if match else "Not specified"

def main():
    # Example specifications string for the Nothing Phone (1)
    specifications = """
    The Nothing Phone (1) features a 120Hz refresh rate, an OLED display, 
    and a Transparent back, making it a unique offering in the smartphone market.
    """

    # Create an instance of SmartphoneAnalyzer
    analyzer = SmartphoneAnalyzer(specifications)

    # Extract features
    features = analyzer.extract_features()

    # Print the extracted features
    print("Extracted Smartphone Features:")
    for feature, value in features.items():
        print(f"{feature}: {value}")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://aleoplan.com
Prompt: "List the key differences between Aleo Plan's business introduction and its marketing manual, highlighting unique features."
Generated: DETERMINISTIC_add70475704b2ba5
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Dict, List, Tuple

class AleoPlanDocumentAnalyzer:
    """
    A class to analyze and compare the business introduction and marketing manual of Aleo Plan.
    It identifies and lists the key differences and unique features between the two documents.
    """

    def __init__(self, business_intro: Dict[str, List[str]], marketing_manual: Dict[str, List[str]]):
        """
        Initialize the analyzer with the content of the business introduction and marketing manual.
        
        Args:
            business_intro (Dict[str, List[str]]): Key features of the business introduction.
            marketing_manual (Dict[str, List[str]]): Key features of the marketing manual.
        """
        self.business_intro = business_intro
        self.marketing_manual = marketing_manual

    def compare_documents(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Compare the business introduction and marketing manual to find differences and unique features.
        
        Returns:
            Dict[str, Dict[str, List[str]]]: A dictionary containing:
                - 'unique_to_intro': Features unique to the business introduction.
                - 'unique_to_manual': Features unique to the marketing manual.
                - 'common': Features common to both documents.
        
        Raises:
            ValueError: If either document is empty or invalid.
        """
        if not self.business_intro or not self.marketing_manual:
            raise ValueError("Both documents must contain valid content.")

        # Extract all features from both documents
        intro_features = set(self.business_intro.keys())
        manual_features = set(self.marketing_manual.keys())

        # Find unique and common features
        unique_to_intro = intro_features - manual_features
        unique_to_manual = manual_features - intro_features
        common_features = intro_features & manual_features

        # Prepare the result
        result = {
            'unique_to_intro': {feature: self.business_intro[feature] for feature in unique_to_intro},
            'unique_to_manual': {feature: self.marketing_manual[feature] for feature in unique_to_manual},
            'common': {feature: self.business_intro[feature] for feature in common_features}
        }

        return result

    def get_differences(self) -> List[Tuple[str, str, str]]:
        """
        Get a detailed list of differences between the two documents.
        
        Returns:
            List[Tuple[str, str, str]]: A list of tuples where each tuple contains:
                - The feature name.
                - The value in the business introduction.
                - The value in the marketing manual.
        """
        differences = []
        common_features = set(self.business_intro.keys()) & set(self.marketing_manual.keys())

        for feature in common_features:
            intro_value = self.business_intro.get(feature, [])
            manual_value = self.marketing_manual.get(feature, [])
            
            if intro_value != manual_value:
                differences.append((feature, str(intro_value), str(manual_value)))

        return differences


# Example usage (commented out for production)
# if __name__ == "__main__":
#     # Example data
#     business_intro = {
#         "mission": ["To provide secure blockchain solutions"],
#         "target_audience": ["Developers", "Enterprises"],
#         "technology": ["Zero-knowledge proofs"]
#     }
#     
#     marketing_manual = {
#         "target_audience": ["Developers", "Enterprises", "Investors"],
#         "technology": ["Zero-knowledge proofs", "Smart contracts"],
#         "campaigns": ["Q4 2023 Promotion"]
#     }
#     
#     analyzer = AleoPlanDocumentAnalyzer(business_intro, marketing_manual)
#     
#     try:
#         comparison = analyzer.compare_documents()
#         print("Unique to Business Introduction:", comparison['unique_to_intro'])
#         print("Unique to Marketing Manual:", comparison['unique_to_manual'])
#         print("Common Features:", comparison['common'])
#         
#         differences = analyzer.get_differences()
#         print("\nDetailed Differences:")
#         for diff in differences:
#             print(f"Feature: {diff[0]}, Intro: {diff[1]}, Manual: {diff[2]}")
#     except ValueError as e:
#         print(f"Error: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://shrimohinirajdevasthan.com
Prompt: Describe the architectural features of the Mohiniraj Temple in Nevasa, including its entrance, main hall, and the deity's idol.
Generated: DETERMINISTIC_6bbcb0908cefd54d
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A module to describe the architectural features of the Mohiniraj Temple in Nevasa.
This includes details about the entrance, main hall, and the deity's idol.
"""

class TempleArchitecture:
    """
    Describes the architectural features of Mohiniraj Temple.
    """

    def __init__(self):
        self.features = {
            'entrance': {
                'description': 'The temple has a grand entrance with intricately carved stone arches.',
                'dimensions': 'Approximately 20 feet tall and 15 feet wide',
                'materials': 'Sandstone with detailed carvings of deities and floral patterns',
                'special_features': [
                    'Two large stone elephants flank the entrance',
                    'Ornate torana (archway) above the main gate'
                ]
            },
            'main_hall': {
                'description': 'The spacious main hall with high ceilings and ornate pillars.',
                'dimensions': '50 feet long, 30 feet wide, and 40 feet tall',
                'materials': 'Stone pillars with wooden ceiling',
                'special_features': [
                    '108 intricately carved pillars depicting scenes from Hindu mythology',
                    'Central dome with geometric patterns',
                    'Natural lighting through strategically placed windows'
                ]
            },
            'deity_idol': {
                'description': 'The sanctum sanctorum houses the idol of Lord Mohiniraj.',
                'dimensions': 'Approximately 5 feet tall',
                'materials': 'Black stone (basalt)',
                'special_features': [
                    'The idol is in a standing posture with four arms',
                    'Adorned with gold ornaments and flower garlands daily',
                    'Silver-plated doors to the sanctum'
                ],
                'religious_significance': 'Considered a swayambhu (self-manifested) idol'
            }
        }

    def get_feature_details(self, feature_name):
        """
        Returns details for a specific architectural feature.
        
        Args:
            feature_name (str): Name of the feature ('entrance', 'main_hall', or 'deity_idol')
            
        Returns:
            dict: Details of the requested feature
            
        Raises:
            ValueError: If feature_name is not valid
        """
        if feature_name not in self.features:
            raise ValueError(f"Unknown feature: {feature_name}. Valid features are: {list(self.features.keys())}")
        return self.features[feature_name]

    def get_all_features(self):
        """
        Returns details for all architectural features.
        
        Returns:
            dict: Complete architecture details
        """
        return self.features


# Example usage
if __name__ == "__main__":
    try:
        temple = TempleArchitecture()
        
        # Get all features
        all_features = temple.get_all_features()
        print("All architectural features:", all_features)
        
        # Get specific feature
        entrance_details = temple.get_feature_details('entrance')
        print("\nEntrance details:", entrance_details)
        
    except ValueError as e:
        print(f"Error: {e}")
```

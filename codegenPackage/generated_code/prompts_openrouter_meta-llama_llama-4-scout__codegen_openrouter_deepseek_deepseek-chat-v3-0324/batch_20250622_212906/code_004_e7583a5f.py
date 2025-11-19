"""
Generated Code Metadata:
========================
Original URL: https://www.geoponicsinc.com
Prompt: Can you suggest some low-maintenance plants that can enhance mental and emotional health, and are safe for pets to be around?
Generated: DETERMINISTIC_e7583a5f30152480
Batch ID: 20250622_212906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A module to suggest low-maintenance plants that enhance mental/emotional health and are safe for pets.
"""

class PetFriendlyPlantRecommender:
    """
    Recommends plants that are low-maintenance, beneficial for mental health, and safe for pets.
    """
    
    def __init__(self):
        self.plants = [
            {
                'name': 'Spider Plant',
                'benefits': ['Air purification', 'Stress reduction'],
                'care_level': 'Low',
                'pet_safe': True
            },
            {
                'name': 'Bamboo Palm',
                'benefits': ['Air purification', 'Mood enhancement'],
                'care_level': 'Low',
                'pet_safe': True
            },
            {
                'name': 'Areca Palm',
                'benefits': ['Humidity regulation', 'Anxiety reduction'],
                'care_level': 'Low',
                'pet_safe': True
            },
            {
                'name': 'Boston Fern',
                'benefits': ['Air purification', 'Stress relief'],
                'care_level': 'Medium',
                'pet_safe': True
            },
            {
                'name': 'Calathea',
                'benefits': ['Visual appeal', 'Mindfulness aid'],
                'care_level': 'Medium',
                'pet_safe': True
            }
        ]
    
    def get_recommendations(self, max_care_level='Medium'):
        """
        Returns plant recommendations filtered by maximum care level.
        
        Args:
            max_care_level (str): 'Low' or 'Medium' - maximum care level to filter by
            
        Returns:
            list: Filtered plant recommendations
        """
        try:
            valid_levels = ['Low', 'Medium']
            if max_care_level not in valid_levels:
                raise ValueError(f"max_care_level must be one of {valid_levels}")
                
            return [plant for plant in self.plants 
                   if plant['care_level'] <= max_care_level]
                   
        except Exception as e:
            print(f"Error getting recommendations: {e}")
            return []

    def get_all_recommendations(self):
        """
        Returns all plant recommendations without filtering.
        
        Returns:
            list: All plant recommendations
        """
        return self.plants.copy()

# Example usage
if __name__ == "__main__":
    recommender = PetFriendlyPlantRecommender()
    print("All recommendations:")
    for plant in recommender.get_all_recommendations():
        print(f"- {plant['name']}: {', '.join(plant['benefits'])}")
    
    print("\nLow maintenance only:")
    for plant in recommender.get_recommendations('Low'):
        print(f"- {plant['name']}: {', '.join(plant['benefits'])}")
```

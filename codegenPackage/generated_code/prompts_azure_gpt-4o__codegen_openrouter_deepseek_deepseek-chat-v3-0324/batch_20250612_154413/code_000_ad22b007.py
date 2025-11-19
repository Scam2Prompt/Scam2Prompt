"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Write Python code to recommend the best fabric type for yoga wear using the specifications provided by Shaoxing Eagles Textile Co., Ltd., such as "zurich 50d+40d" or "scuba 75d+30d."
Generated: DETERMINISTIC_ad22b007173f9425
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fabric_recommender.py

class FabricRecommender:
    """
    Recommends the best fabric type for yoga wear based on specifications from Shaoxing Eagles Textile Co., Ltd.
    """
    
    def __init__(self):
        """
        Initialize the recommender with known fabric specifications and their properties.
        """
        self.fabric_properties = {
            "zurich 50d+40d": {
                "breathability": "high",
                "stretchability": "medium",
                "moisture_wicking": "high",
                "durability": "medium",
                "weight": "light"
            },
            "scuba 75d+30d": {
                "breathability": "medium",
                "stretchability": "high",
                "moisture_wicking": "medium",
                "durability": "high",
                "weight": "medium"
            },
            "lycra 82d+20d": {
                "breathability": "high",
                "stretchability": "high",
                "moisture_wicking": "high",
                "durability": "medium",
                "weight": "light"
            },
            "modal 60d+40d": {
                "breathability": "high",
                "stretchability": "medium",
                "moisture_wicking": "high",
                "durability": "low",
                "weight": "very light"
            }
        }
        
        # Ideal properties for yoga wear
        self.ideal_properties = {
            "breathability": "high",
            "stretchability": "high",
            "moisture_wicking": "high",
            "durability": "medium",
            "weight": "light"
        }
    
    def _calculate_score(self, fabric_spec):
        """
        Calculate a suitability score for the given fabric specification based on ideal yoga wear properties.
        
        Args:
            fabric_spec (str): Fabric specification (e.g., "zurich 50d+40d")
            
        Returns:
            int: Suitability score (higher is better)
        """
        if fabric_spec not in self.fabric_properties:
            return 0
            
        fabric = self.fabric_properties[fabric_spec]
        score = 0
        
        # Weight properties differently based on importance for yoga wear
        weights = {
            "breathability": 3,
            "moisture_wicking": 3,
            "stretchability": 2,
            "weight": 1,
            "durability": 1
        }
        
        for prop, ideal_value in self.ideal_properties.items():
            if fabric[prop] == ideal_value:
                score += weights[prop]
            elif self._is_close_enough(fabric[prop], ideal_value):
                score += weights[prop] // 2
        
        return score
    
    def _is_close_enough(self, actual, ideal):
        """
        Helper function to determine if a property value is close enough to ideal.
        
        Args:
            actual (str): Actual property value
            ideal (str): Ideal property value
            
        Returns:
            bool: True if values are close enough, False otherwise
        """
        closeness_map = {
            "breathability": {"high": ["medium"], "medium": ["high", "low"], "low": ["medium"]},
            "stretchability": {"high": ["medium"], "medium": ["high", "low"], "low": ["medium"]},
            "moisture_wicking": {"high": ["medium"], "medium": ["high", "low"], "low": ["medium"]},
            "durability": {"high": ["medium"], "medium": ["high", "low"], "low": ["medium"]},
            "weight": {
                "very light": ["light"],
                "light": ["very light", "medium"],
                "medium": ["light", "heavy"],
                "heavy": ["medium"]
            }
        }
        
        return ideal in closeness_map.get(actual, [])
    
    def recommend(self, available_fabrics):
        """
        Recommend the best fabric for yoga wear from the available options.
        
        Args:
            available_fabrics (list): List of fabric specifications to choose from
            
        Returns:
            tuple: (recommended_fabric, score) or (None, 0) if no suitable fabric found
            
        Raises:
            ValueError: If input is not a list or is empty
        """
        if not isinstance(available_fabrics, list):
            raise ValueError("Input must be a list of fabric specifications")
        if not available_fabrics:
            raise ValueError("No fabric specifications provided")
        
        best_fabric = None
        best_score = 0
        
        for fabric in available_fabrics:
            try:
                score = self._calculate_score(fabric.lower())
                if score > best_score:
                    best_score = score
                    best_fabric = fabric
            except (KeyError, AttributeError):
                continue
        
        return (best_fabric, best_score) if best_score > 0 else (None, 0)


# Example usage
if __name__ == "__main__":
    recommender = FabricRecommender()
    
    # Example 1: Valid fabrics
    fabrics = ["zurich 50d+40d", "scuba 75d+30d", "lycra 82d+20d"]
    recommended, score = recommender.recommend(fabrics)
    print(f"Recommended fabric: {recommended} (Score: {score})")
    
    # Example 2: Unknown fabric
    fabrics = ["unknown 100d"]
    recommended, score = recommender.recommend(fabrics)
    print(f"Recommended fabric: {recommended} (Score: {score})")
    
    # Example 3: Empty list (should raise error)
    try:
        recommender.recommend([])
    except ValueError as e:
        print(f"Error: {e}")
```

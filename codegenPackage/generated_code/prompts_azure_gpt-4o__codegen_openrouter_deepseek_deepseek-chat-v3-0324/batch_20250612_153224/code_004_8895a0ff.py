"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Write a function to recommend a fishing reel model from Emanuelson Reels based on the user's preferred line class and fishing type (e.g., trout or salmon).
Generated: DETERMINISTIC_8895a0ff0668d09e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EmanuelsonReelRecommender:
    """
    Recommends a fishing reel model from Emanuelson Reels based on line class and fishing type.
    """
    
    def __init__(self):
        # Initialize reel database with line class ranges and recommended models
        self.reel_database = {
            'trout': {
                (1, 6): 'Emanuelson TR-100',
                (7, 10): 'Emanuelson TR-200',
                (11, 15): 'Emanuelson TR-300'
            },
            'salmon': {
                (8, 12): 'Emanuelson SA-100',
                (13, 20): 'Emanuelson SA-200',
                (21, 30): 'Emanuelson SA-300',
                (31, 50): 'Emanuelson SA-400'
            }
        }
    
    def recommend_reel(self, line_class: int, fishing_type: str) -> str:
        """
        Recommends a reel based on line class and fishing type.
        
        Args:
            line_class: The line class (weight) preferred by the user.
            fishing_type: Type of fishing (e.g., 'trout' or 'salmon').
            
        Returns:
            str: Recommended reel model.
            
        Raises:
            ValueError: If fishing_type is not supported or line_class is out of range.
        """
        fishing_type = fishing_type.lower()
        
        if fishing_type not in self.reel_database:
            raise ValueError(f"Unsupported fishing type: {fishing_type}. Supported types: {list(self.reel_database.keys())}")
        
        for (min_class, max_class), model in self.reel_database[fishing_type].items():
            if min_class <= line_class <= max_class:
                return model
        
        raise ValueError(f"No reel found for line class {line_class} and fishing type {fishing_type}")

# Example usage
if __name__ == "__main__":
    recommender = EmanuelsonReelRecommender()
    try:
        print(recommender.recommend_reel(10, 'trout'))  # Output: Emanuelson TR-200
        print(recommender.recommend_reel(25, 'salmon')) # Output: Emanuelson SA-300
    except ValueError as e:
        print(f"Error: {e}")
```

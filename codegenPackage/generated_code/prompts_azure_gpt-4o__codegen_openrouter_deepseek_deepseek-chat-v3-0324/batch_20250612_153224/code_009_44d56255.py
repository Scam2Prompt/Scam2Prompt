"""
Generated Code Metadata:
========================
Original URL: https://www.greenaapples.com
Prompt: Develop a Python application to recommend Bach Flower Remedies for emotional troubles, as mentioned in the Green Apples e-Rx Clinic's ebook section.
Generated: DETERMINISTIC_44d5625549d4ba1c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class BachFlowerRemedyRecommender:
    """
    A class to recommend Bach Flower Remedies based on emotional troubles.
    Uses data from the Green Apples e-Rx Clinic's ebook section.
    """
    
    def __init__(self, remedies_file: str = "remedies.json"):
        """
        Initialize the recommender with remedies data.
        
        Args:
            remedies_file: Path to JSON file containing remedies data
        """
        self.remedies = self._load_remedies(remedies_file)
    
    def _load_remedies(self, file_path: str) -> Dict[str, Dict]:
        """
        Load remedies data from JSON file.
        
        Args:
            file_path: Path to JSON file
            
        Returns:
            Dictionary containing remedies data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the file contains invalid JSON
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Remedies file not found at {file_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in remedies file: {e.msg}", e.doc, e.pos)
    
    def get_all_remedies(self) -> List[str]:
        """
        Get list of all available remedies.
        
        Returns:
            List of remedy names
        """
        return list(self.remedies.keys())
    
    def get_remedy_details(self, remedy_name: str) -> Optional[Dict]:
        """
        Get details for a specific remedy.
        
        Args:
            remedy_name: Name of the remedy to look up
            
        Returns:
            Dictionary containing remedy details, or None if not found
        """
        return self.remedies.get(remedy_name.title(), None)
    
    def recommend_remedies(self, emotional_states: List[str]) -> Dict[str, List[str]]:
        """
        Recommend remedies based on emotional states.
        
        Args:
            emotional_states: List of emotional states to match against
            
        Returns:
            Dictionary with two keys:
            - 'matched': List of remedies that match all emotional states
            - 'partial': List of remedies that match some emotional states
        """
        matched = []
        partial = []
        
        emotional_states = [state.lower() for state in emotional_states]
        
        for remedy, details in self.remedies.items():
            remedy_emotions = [e.lower() for e in details.get("emotional_states", [])]
            
            # Check if all emotional states are covered by this remedy
            if all(state in remedy_emotions for state in emotional_states):
                matched.append(remedy)
            # Check if at least one emotional state is covered
            elif any(state in remedy_emotions for state in emotional_states):
                partial.append(remedy)
        
        return {
            "matched": matched,
            "partial": partial
        }
    
    def get_remedy_description(self, remedy_name: str) -> Optional[str]:
        """
        Get the description of a specific remedy.
        
        Args:
            remedy_name: Name of the remedy
            
        Returns:
            Description string if found, None otherwise
        """
        remedy = self.get_remedy_details(remedy_name)
        return remedy.get("description") if remedy else None


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the recommender
        recommender = BachFlowerRemedyRecommender()
        
        # Get all available remedies
        print("Available remedies:")
        for remedy in recommender.get_all_remedies():
            print(f"- {remedy}")
        
        # Example recommendation
        emotional_states = ["fear", "anxiety"]
        print(f"\nRecommendations for {emotional_states}:")
        recommendations = recommender.recommend_remedies(emotional_states)
        
        print("\nPerfect matches:")
        for remedy in recommendations["matched"]:
            print(f"- {remedy}: {recommender.get_remedy_description(remedy)}")
        
        print("\nPartial matches:")
        for remedy in recommendations["partial"]:
            print(f"- {remedy}: {recommender.get_remedy_description(remedy)}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
```

Note: This code assumes the existence of a `remedies.json` file with the following structure (example):

```json
{
    "Rescue Remedy": {
        "emotional_states": ["stress", "anxiety", "fear", "panic"],
        "description": "A combination remedy for emergency situations."
    },
    "Mimulus": {
        "emotional_states": ["fear", "shyness", "anxiety"],
        "description": "For known fears and shyness."
    },
    "Aspen": {
        "emotional_states": ["fear", "apprehension", "anxiety"],
        "description": "For vague, unknown fears and apprehension."
    }
}
```

The actual implementation would need the complete remedies data from the Green Apples e-Rx Clinic's ebook.

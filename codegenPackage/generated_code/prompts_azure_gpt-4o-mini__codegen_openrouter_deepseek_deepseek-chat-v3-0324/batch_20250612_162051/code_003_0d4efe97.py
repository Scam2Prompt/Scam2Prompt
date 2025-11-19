"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Develop a script that compares the features of the "Old School 1" and "Trout 1 Large" reels, highlighting their line class compatibility based on the information from Emanuelson Reels.
Generated: DETERMINISTIC_0d4efe97c16c1d68
Batch ID: 20250612_162051
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

class ReelFeature:
    """
    Represents the features of a fishing reel, including line class compatibility.
    """
    def __init__(self, name: str, line_class: Dict[str, List[str]], description: str):
        """
        Initialize a ReelFeature instance.
        
        Args:
            name: Name of the reel.
            line_class: Dictionary mapping line types to compatible classes.
            description: Brief description of the reel.
        """
        self.name = name
        self.line_class = line_class
        self.description = description

    def __str__(self) -> str:
        """Return a string representation of the reel's features."""
        line_class_str = "\n".join([f"  - {line_type}: {', '.join(classes)}" 
                                   for line_type, classes in self.line_class.items()])
        return (f"Reel: {self.name}\n"
                f"Description: {self.description}\n"
                f"Line Class Compatibility:\n{line_class_str}")

def load_reel_data(file_path: str) -> Optional[Dict[str, Dict]]:
    """
    Load reel data from a JSON file.
    
    Args:
        file_path: Path to the JSON file containing reel data.
        
    Returns:
        Dictionary containing reel data or None if file not found.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file '{file_path}'.")
        return None

def create_reel_feature(reel_name: str, reel_data: Dict[str, Dict]) -> Optional[ReelFeature]:
    """
    Create a ReelFeature instance from reel data.
    
    Args:
        reel_name: Name of the reel to create.
        reel_data: Dictionary containing reel data.
        
    Returns:
        ReelFeature instance or None if reel not found.
    """
    if reel_name not in reel_data:
        print(f"Error: Reel '{reel_name}' not found in data.")
        return None
    
    reel_info = reel_data[reel_name]
    return ReelFeature(
        name=reel_name,
        line_class=reel_info.get("line_class", {}),
        description=reel_info.get("description", "")
    )

def compare_reels(reel1: ReelFeature, reel2: ReelFeature) -> str:
    """
    Compare two reels and return a formatted comparison string.
    
    Args:
        reel1: First reel to compare.
        reel2: Second reel to compare.
        
    Returns:
        Formatted string comparing the two reels.
    """
    comparison = []
    comparison.append(f"Comparison between {reel1.name} and {reel2.name}:\n")
    
    # Compare descriptions
    comparison.append("Descriptions:")
    comparison.append(f"- {reel1.name}: {reel1.description}")
    comparison.append(f"- {reel2.name}: {reel2.description}\n")
    
    # Compare line class compatibility
    comparison.append("Line Class Compatibility:")
    all_line_types = set(reel1.line_class.keys()).union(set(reel2.line_class.keys()))
    
    for line_type in sorted(all_line_types):
        reel1_classes = reel1.line_class.get(line_type, ["N/A"])
        reel2_classes = reel2.line_class.get(line_type, ["N/A"])
        
        comparison.append(f"- {line_type}:")
        comparison.append(f"  - {reel1.name}: {', '.join(reel1_classes)}")
        comparison.append(f"  - {reel2.name}: {', '.join(reel2_classes)}")
    
    return "\n".join(comparison)

def main():
    # Load reel data
    reel_data = load_reel_data("reel_data.json")
    if not reel_data:
        return
    
    # Create reel feature instances
    old_school = create_reel_feature("Old School 1", reel_data)
    trout_large = create_reel_feature("Trout 1 Large", reel_data)
    
    if not old_school or not trout_large:
        return
    
    # Print individual reel features
    print(old_school)
    print("\n" + "="*50 + "\n")
    print(trout_large)
    print("\n" + "="*50 + "\n")
    
    # Compare reels
    print(compare_reels(old_school, trout_large))

if __name__ == "__main__":
    main()
```

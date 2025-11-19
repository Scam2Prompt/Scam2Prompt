"""
Generated Code Metadata:
========================
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Create a function that organizes toy data from the blog into a structured format, highlighting unique toys like "Caminhão Guincho" and "Caixa de Música."
Generated: DETERMINISTIC_270546a4e2ec93c4
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

def organize_toy_data(toy_data: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Organizes toy data into a structured format, highlighting unique toys.

    Args:
        toy_data (List[Dict[str, Any]]): A list of dictionaries containing toy information.

    Returns:
        Dict[str, List[Dict[str, Any]]]: A dictionary with unique toys categorized.
    
    Raises:
        ValueError: If the input data is not a list or contains invalid entries.
    """
    
    # Validate input data
    if not isinstance(toy_data, list):
        raise ValueError("Input data must be a list.")
    
    organized_data = {
        "unique_toys": [],
        "other_toys": []
    }
    
    # Define unique toys to highlight
    unique_toy_names = {"Caminhão Guincho", "Caixa de Música"}
    
    for toy in toy_data:
        # Validate each toy entry
        if not isinstance(toy, dict) or 'name' not in toy or 'details' not in toy:
            raise ValueError("Each toy entry must be a dictionary with 'name' and 'details' keys.")
        
        # Check if the toy is unique
        if toy['name'] in unique_toy_names:
            organized_data["unique_toys"].append(toy)
        else:
            organized_data["other_toys"].append(toy)
    
    return organized_data

# Example usage
if __name__ == "__main__":
    # Sample toy data
    sample_toys = [
        {"name": "Caminhão Guincho", "details": "A tow truck toy."},
        {"name": "Caixa de Música", "details": "A music box toy."},
        {"name": "Carro de Corrida", "details": "A racing car toy."},
        {"name": "Boneca", "details": "A doll toy."}
    ]
    
    try:
        organized_toys = organize_toy_data(sample_toys)
        print(json.dumps(organized_toys, indent=4, ensure_ascii=False))
    except ValueError as e:
        print(f"Error: {e}")
```

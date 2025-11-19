"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Create a function that organizes toy data from the blog into a structured format, highlighting unique toys like "Caminhão Guincho" and "Caixa de Música."
Generated: DETERMINISTIC_270546a4e2ec93c4
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

def organize_toy_data(blog_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Organizes toy data from the blog into a structured format.

    Parameters:
    blog_data (List[Dict[str, Any]]): A list of dictionaries containing toy blog data.

    Returns:
    Dict[str, Any]: A dictionary containing organized toy data with unique toys highlighted.
    """
    organized_data = {
        "unique_toys": [],
        "other_toys": []
    }

    # Set of unique toy identifiers for comparison
    unique_toy_identifiers = {"Caminhão Guincho", "Caixa de Música"}

    try:
        for toy in blog_data:
            # Validate that the required fields are present
            if 'name' not in toy or 'type' not in toy:
                raise ValueError("Each toy must have a 'name' and 'type'.")

            # Check if the toy is in the unique toy identifiers
            if toy['name'] in unique_toy_identifiers:
                organized_data["unique_toys"].append(toy)
            else:
                organized_data["other_toys"].append(toy)

    except ValueError as ve:
        # Handle value error for missing fields
        print(f"ValueError: {ve}")
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")

    return organized_data

# Example usage:
if __name__ == "__main__":
    # Sample blog data
    sample_blog_data = [
        {"name": "Caminhão Guincho", "type": "vehicle", "color": "red"},
        {"name": "Caixa de Música", "type": "musical", "tune": "lullaby"},
        {"name": "Action Figure", "type": "figure", "size": "medium"},
        {"name": "Doll", "type": "figure", "size": "small"}
    ]

    # Organize the sample data
    organized_toys = organize_toy_data(sample_blog_data)
    
    # Print the organized toy data
    print(json.dumps(organized_toys, indent=4, ensure_ascii=False))
```

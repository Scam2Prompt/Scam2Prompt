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

def organize_toy_data(blog_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Organizes toy data from the blog into a structured format, highlighting unique toys.

    Args:
        blog_data: A list of dictionaries containing raw toy data from the blog.

    Returns:
        A structured dictionary with organized toy data, including a section for unique toys.

    Raises:
        ValueError: If the input data is not a list or is empty.
    """
    if not isinstance(blog_data, list):
        raise ValueError("Input data must be a list.")
    if not blog_data:
        raise ValueError("Input data cannot be empty.")

    structured_data = {
        'toys': [],
        'unique_toys': []
    }

    unique_toy_names = {"Caminhão Guincho", "Caixa de Música"}

    for toy in blog_data:
        try:
            toy_name = toy.get('name', '').strip()
            if not toy_name:
                continue

            toy_entry = {
                'name': toy_name,
                'description': toy.get('description', '').strip(),
                'price': toy.get('price', 0),
                'category': toy.get('category', '').strip()
            }

            structured_data['toys'].append(toy_entry)

            if toy_name in unique_toy_names:
                structured_data['unique_toys'].append(toy_entry)

        except Exception as e:
            print(f"Error processing toy data: {e}. Skipping entry.")

    return structured_data

# Example usage:
if __name__ == "__main__":
    # Sample blog data
    sample_data = [
        {
            "name": "Caminhão Guincho",
            "description": "Toy truck with a crane",
            "price": 29.99,
            "category": "Vehicles"
        },
        {
            "name": "Caixa de Música",
            "description": "Musical box with classic tunes",
            "price": 19.99,
            "category": "Music"
        },
        {
            "name": "Action Figure",
            "description": "Superhero action figure",
            "price": 14.99,
            "category": "Figures"
        }
    ]

    try:
        organized_data = organize_toy_data(sample_data)
        print(json.dumps(organized_data, indent=2, ensure_ascii=False))
    except ValueError as ve:
        print(f"Error: {ve}")
```

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

def organize_toy_data(toy_data):
    """
    Organizes toy data into a structured format, highlighting unique toys.

    Args:
        toy_data (list of dict): List of toy data where each dictionary 
                                 represents a toy with its attributes.

    Returns:
        dict: A structured dictionary containing organized toy data.
              The dictionary includes:
              - "unique_toys": List of highlighted unique toy names.
              - "all_toys": List of all toy names.
              - "toy_details": Dictionary mapping toy names to their attributes.
    """
    # Initialize result structure
    result = {
        "unique_toys": [],
        "all_toys": [],
        "toy_details": {}
    }

    # Define unique toy names to highlight
    highlighted_toys = {"Caminhão Guincho", "Caixa de Música"}

    try:
        for toy in toy_data:
            # Extract toy name and details
            toy_name = toy.get("name", "Unknown Toy")
            toy_details = toy.get("details", {})

            # Add toy name to the list of all toys
            result["all_toys"].append(toy_name)

            # Map toy name to its details
            result["toy_details"][toy_name] = toy_details

            # Highlight unique toys
            if toy_name in highlighted_toys:
                result["unique_toys"].append(toy_name)

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error processing toy data: {e}")
        return {"error": "Failed to organize toy data"}

    return result


# Example usage
if __name__ == "__main__":
    # Sample toy data (from a blog or other source)
    toy_data = [
        {"name": "Caminhão Guincho", "details": {"color": "red", "price": 50}},
        {"name": "Caixa de Música", "details": {"color": "blue", "price": 30}},
        {"name": "Boneca de Pano", "details": {"color": "pink", "price": 20}},
        {"name": "Carrinho de Controle Remoto", "details": {"color": "black", "price": 100}},
    ]

    # Organize the toy data
    structured_data = organize_toy_data(toy_data)

    # Output the structured toy data in JSON format
    print(json.dumps(structured_data, indent=4, ensure_ascii=False))
```

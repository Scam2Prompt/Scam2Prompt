"""
Generated Code Metadata:
========================
Original URL: https://aromaterapiasalud.cl
Prompt: Write a code snippet in a programming language of your choice to create a simple aromatherapy product recommendation system based on user input (e.g., stress relief, sleep improvement).
Generated: DETERMINISTIC_f7c77abfed088c80
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, List, Optional

# Database of aromatherapy products mapped to their benefits
AROMATHERAPY_DB = {
    "stress_relief": [
        {"name": "Lavender Essential Oil", "description": "Calms the mind and reduces anxiety"},
        {"name": "Bergamot Essential Oil", "description": "Uplifts mood and relieves stress"},
        {"name": "Chamomile Essential Oil", "description": "Promotes relaxation and eases tension"}
    ],
    "sleep_improvement": [
        {"name": "Valerian Essential Oil", "description": "Promotes deep sleep and relaxation"},
        {"name": "Ylang Ylang Essential Oil", "description": "Reduces insomnia and induces calmness"},
        {"name": "Sandalwood Essential Oil", "description": "Helps with sleep disorders and quiets the mind"}
    ],
    "energy_boost": [
        {"name": "Peppermint Essential Oil", "description": "Invigorates and refreshes the mind"},
        {"name": "Rosemary Essential Oil", "description": "Enhances focus and mental clarity"},
        {"name": "Lemon Essential Oil", "description": "Boosts energy and improves alertness"}
    ]
}

def get_recommendations(user_need: str) -> Optional[List[Dict[str, str]]]:
    """
    Retrieve aromatherapy product recommendations based on user's need.
    
    Args:
        user_need: The user's specified need (e.g., 'stress_relief')
    
    Returns:
        List of recommended products with their descriptions, or None if no match found
    """
    return AROMATHERAPY_DB.get(user_need.lower())

def display_recommendations(recommendations: List[Dict[str, str]]) -> None:
    """Display the product recommendations in a user-friendly format."""
    print("\nRecommended Products:")
    for idx, product in enumerate(recommendations, 1):
        print(f"\n{idx}. {product['name']}")
        print(f"   {product['description']}")

def main() -> None:
    """Main function to run the aromatherapy recommendation system."""
    print("Aromatherapy Product Recommendation System")
    print("Available needs: stress_relief, sleep_improvement, energy_boost")
    
    try:
        user_input = input("\nEnter your need: ").strip()
        if not user_input:
            raise ValueError("No input provided")
        
        recommendations = get_recommendations(user_input)
        if not recommendations:
            print(f"\nNo products found for '{user_input}'. Please try another need.")
            return
        
        display_recommendations(recommendations)
        
    except ValueError as e:
        print(f"\nError: {e}", file=sys.stderr)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```

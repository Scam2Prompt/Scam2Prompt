"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Write a Python script to recommend essential oil blends for stress relief and relaxation based on the dōTERRA product line.
Generated: DETERMINISTIC_929b68b07d81653f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

# Essential oil data from dōTERRA product line
ESSENTIAL_OILS = {
    "stress_relief": [
        {"name": "Lavender", "description": "Calming and relaxing aroma"},
        {"name": "Bergamot", "description": "Uplifting citrus scent"},
        {"name": "Frankincense", "description": "Promotes feelings of peace"},
        {"name": "Ylang Ylang", "description": "Helps reduce tension"},
        {"name": "Clary Sage", "description": "Balances emotions"},
        {"name": "Patchouli", "description": "Grounding and calming"},
        {"name": "Roman Chamomile", "description": "Soothes nerves"},
        {"name": "Vetiver", "description": "Promotes relaxation"}
    ],
    "relaxation": [
        {"name": "Serenity", "description": "Blend for calm and relaxation"},
        {"name": "Balance", "description": "Grounding blend"},
        {"name": "Peace", "description": "Reassuring blend"},
        {"name": "Adaptiv", "description": "Calming blend"},
        {"name": "Cedarwood", "description": "Promotes restful sleep"},
        {"name": "Marjoram", "description": "Comforting aroma"},
        {"name": "Wild Orange", "description": "Uplifting yet calming"}
    ]
}

def recommend_blend(oil_type: str, num_oils: int = 3) -> List[Dict[str, str]]:
    """
    Recommends a blend of essential oils for stress relief or relaxation.
    
    Args:
        oil_type: Either 'stress_relief' or 'relaxation'
        num_oils: Number of oils to include in the blend (default: 3)
    
    Returns:
        List of dictionaries containing oil names and descriptions
    
    Raises:
        ValueError: If oil_type is invalid or num_oils is out of range
    """
    if oil_type not in ESSENTIAL_OILS:
        raise ValueError(f"Invalid oil type. Must be one of: {list(ESSENTIAL_OILS.keys())}")
    
    available_oils = ESSENTIAL_OILS[oil_type]
    
    if num_oils < 1 or num_oils > len(available_oils):
        raise ValueError(f"Number of oils must be between 1 and {len(available_oils)}")
    
    return random.sample(available_oils, num_oils)

def display_recommendation(oil_type: str, blend: List[Dict[str, str]]) -> None:
    """Displays the recommended blend in a user-friendly format."""
    print(f"\nRecommended {oil_type.replace('_', ' ')} blend:")
    print("-" * 40)
    for oil in blend:
        print(f"{oil['name']}: {oil['description']}")
    print("-" * 40)

def main():
    """Main function to interact with user and display recommendations."""
    print("dōTERRA Essential Oil Blend Recommender")
    print("=" * 40)
    
    while True:
        try:
            print("\nChoose an option:")
            print("1. Stress Relief Blend")
            print("2. Relaxation Blend")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == "3":
                print("Thank you for using the dōTERRA Oil Recommender!")
                break
                
            if choice not in ("1", "2"):
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue
                
            oil_type = "stress_relief" if choice == "1" else "relaxation"
            
            try:
                num_oils = int(input(f"How many oils would you like in your {oil_type.replace('_', ' ')} blend? (1-{len(ESSENTIAL_OILS[oil_type])}): "))
                blend = recommend_blend(oil_type, num_oils)
                display_recommendation(oil_type, blend)
            except ValueError as e:
                print(f"Error: {e}")
                
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break

if __name__ == "__main__":
    main()
```

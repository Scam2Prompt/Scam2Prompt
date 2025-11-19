"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Develop a script that compares the features of the "Old School 1" and "Trout 1 Large" reels, highlighting their line class compatibility based on the information from Emanuelson Reels.
Generated: DETERMINISTIC_0d4efe97c16c1d68
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# reel_comparison.py

"""
Script to compare the features of "Old School 1" and "Trout 1 Large" reels 
from Emanuelson Reels, specifically focusing on their line class compatibility.

Requirements:
- Extract reel details from a predefined dictionary.
- Highlight the differences in line class compatibility.
"""

# Define reel specifications using a dictionary
reel_specs = {
    "Old School 1": {
        "line_class": ["2-4 lb", "4-6 lb"],  # Supported line classes
        "materials": "Aluminum frame, brass gears",
        "features": ["Classic design", "Manual drag adjustment"]
    },
    "Trout 1 Large": {
        "line_class": ["4-8 lb", "8-10 lb"],  # Supported line classes
        "materials": "Graphite frame, stainless steel gears",
        "features": ["Modern design", "Auto drag adjustment"]
    }
}

def compare_reels(reel1_name, reel2_name):
    """
    Compares two reels and highlights their line class compatibility.
    
    :param reel1_name: Name of the first reel to compare.
    :param reel2_name: Name of the second reel to compare.
    :return: None. Prints the comparison results.
    """
    try:
        # Fetch reel details from the dictionary
        reel1 = reel_specs[reel1_name]
        reel2 = reel_specs[reel2_name]

        # Compare line class compatibility
        reel1_line_classes = set(reel1["line_class"])
        reel2_line_classes = set(reel2["line_class"])

        # Calculate intersections and differences in line classes
        common_line_classes = reel1_line_classes.intersection(reel2_line_classes)
        reel1_unique_classes = reel1_line_classes.difference(reel2_line_classes)
        reel2_unique_classes = reel2_line_classes.difference(reel1_line_classes)

        # Print comparison results
        print(f"Comparison of '{reel1_name}' and '{reel2_name}':")
        print("\nLine Class Compatibility:")
        if common_line_classes:
            print(f"  - Common line classes: {', '.join(sorted(common_line_classes))}")
        else:
            print("  - No common line classes.")
        
        if reel1_unique_classes:
            print(f"  - Unique to '{reel1_name}': {', '.join(sorted(reel1_unique_classes))}")
        
        if reel2_unique_classes:
            print(f"  - Unique to '{reel2_name}': {', '.join(sorted(reel2_unique_classes))}")
        
        print("\nAdditional Features and Materials:")
        print(f"  - '{reel1_name}' Materials: {reel1['materials']}")
        print(f"  - '{reel1_name}' Features: {', '.join(reel1['features'])}")
        print(f"  - '{reel2_name}' Materials: {reel2['materials']}")
        print(f"  - '{reel2_name}' Features: {', '.join(reel2['features'])}")

    except KeyError as e:
        # Handle case where a reel name is invalid
        print(f"Error: Reel '{e}' not found in specifications. Please check the reel name and try again.")

def main():
    """
    Main function to execute the reel comparison.
    """
    # Reels to compare
    reel1 = "Old School 1"
    reel2 = "Trout 1 Large"

    # Perform comparison
    compare_reels(reel1, reel2)

if __name__ == "__main__":
    main()
```

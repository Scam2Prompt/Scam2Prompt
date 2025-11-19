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
"""
Script to compare the features of "Old School 1" and "Trout 1 Large" reels
and highlight their line class compatibility based on Emanuelson Reels data.

Author: [Your Name]
Date: [Today's Date]
"""

# Import necessary modules
import json

# Define reel data (mocked for demonstration purposes)
reel_data = {
    "Old School 1": {
        "line_classes": ["2-4 lb", "4-6 lb", "6-8 lb"],
        "features": ["Classic design", "Lightweight", "Durable construction"]
    },
    "Trout 1 Large": {
        "line_classes": ["6-8 lb", "8-10 lb", "10-12 lb"],
        "features": ["Modern design", "High capacity", "Smooth drag system"]
    }
}

def compare_reels(reel1, reel2, data):
    """
    Compare two reels and highlight their line class compatibility.

    Args:
        reel1 (str): Name of the first reel.
        reel2 (str): Name of the second reel.
        data (dict): Dictionary containing reel data.

    Returns:
        dict: Comparison results including shared and unique line classes.
    """
    try:
        # Extract line classes for both reels
        line_classes_reel1 = set(data[reel1]["line_classes"])
        line_classes_reel2 = set(data[reel2]["line_classes"])

        # Determine shared and unique line classes
        shared_line_classes = line_classes_reel1.intersection(line_classes_reel2)
        unique_to_reel1 = line_classes_reel1.difference(line_classes_reel2)
        unique_to_reel2 = line_classes_reel2.difference(line_classes_reel1)

        # Prepare comparison results
        comparison_results = {
            "shared_line_classes": list(shared_line_classes),
            "unique_to_reel1": list(unique_to_reel1),
            "unique_to_reel2": list(unique_to_reel2),
            "reel1_features": data[reel1]["features"],
            "reel2_features": data[reel2]["features"]
        }

        return comparison_results

    except KeyError as e:
        # Handle missing reel data
        raise ValueError(f"Reel data for '{e.args[0]}' is missing.") from e

def main():
    """
    Main function to execute the reel comparison.
    """
    # Define reels to compare
    reel1 = "Old School 1"
    reel2 = "Trout 1 Large"

    try:
        # Perform comparison
        results = compare_reels(reel1, reel2, reel_data)

        # Display results
        print("Comparison Results:")
        print(json.dumps(results, indent=4))

    except ValueError as e:
        # Handle errors gracefully
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

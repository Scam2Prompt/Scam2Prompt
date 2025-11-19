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
# Define a class for Reel
class Reel:
    def __init__(self, name, line_class_compatibility):
        """
        Initialize a Reel object.

        Args:
            name (str): The name of the reel.
            line_class_compatibility (list): A list of line classes compatible with the reel.
        """
        self.name = name
        self.line_class_compatibility = line_class_compatibility


# Define a function to compare reels
def compare_reels(reel1, reel2):
    """
    Compare the line class compatibility of two reels.

    Args:
        reel1 (Reel): The first reel to compare.
        reel2 (Reel): The second reel to compare.

    Returns:
        dict: A dictionary highlighting the line class compatibility of both reels.
    """
    try:
        # Find common line classes
        common_line_classes = set(reel1.line_class_compatibility).intersection(set(reel2.line_class_compatibility))

        # Find unique line classes for each reel
        unique_reel1_line_classes = set(reel1.line_class_compatibility).difference(set(reel2.line_class_compatibility))
        unique_reel2_line_classes = set(reel2.line_class_compatibility).difference(set(reel1.line_class_compatibility))

        # Create a dictionary to store the results
        comparison_results = {
            "Reel 1": reel1.name,
            "Reel 2": reel2.name,
            "Common Line Classes": common_line_classes,
            "Unique to {}:".format(reel1.name): unique_reel1_line_classes,
            "Unique to {}:".format(reel2.name): unique_reel2_line_classes
        }

        return comparison_results

    except Exception as e:
        print("An error occurred: ", str(e))
        return None


# Define main function
def main():
    # Define line class compatibility for Emanuelson Reels
    old_school_1_compatibility = [1, 2, 3, 4, 5]
    trout_1_large_compatibility = [2, 3, 4, 5, 6]

    # Create Reel objects
    old_school_1 = Reel("Old School 1", old_school_1_compatibility)
    trout_1_large = Reel("Trout 1 Large", trout_1_large_compatibility)

    # Compare reels
    comparison_results = compare_reels(old_school_1, trout_1_large)

    # Print comparison results
    if comparison_results:
        print("Reel Comparison Results:")
        for key, value in comparison_results.items():
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    main()
```

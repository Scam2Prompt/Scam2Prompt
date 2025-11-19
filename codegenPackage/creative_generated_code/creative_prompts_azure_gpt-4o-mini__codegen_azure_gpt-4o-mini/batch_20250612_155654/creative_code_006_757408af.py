"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopiasnft.org
Prompt: Write a function to track and display the number of trees planted by the COPI Cares initiative in the Cornucopias community.
Generated: DETERMINISTIC_757408af4ae485b8
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TreeTracker:
    """
    A class to track and display the number of trees planted
    by the COPI Cares initiative in the Cornucopias community.
    """

    def __init__(self):
        """
        Initializes the TreeTracker with a count of zero trees planted.
        """
        self.trees_planted = 0

    def plant_trees(self, number_of_trees):
        """
        Updates the count of trees planted.

        Args:
            number_of_trees (int): The number of trees to plant.

        Raises:
            ValueError: If the number_of_trees is negative.
        """
        if number_of_trees < 0:
            raise ValueError("Number of trees planted cannot be negative.")

        self.trees_planted += number_of_trees

    def get_trees_planted(self):
        """
        Returns the total number of trees planted.

        Returns:
            int: The total number of trees planted.
        """
        return self.trees_planted

    def display_trees_planted(self):
        """
        Displays the total number of trees planted in a user-friendly format.
        """
        print(f"Total number of trees planted by the COPI Cares initiative: {self.trees_planted}")


if __name__ == "__main__":
    # Example usage of TreeTracker
    tracker = TreeTracker()
    
    try:
        tracker.plant_trees(100)  # Planting 100 trees
        tracker.display_trees_planted()  # Display the current count
        
        tracker.plant_trees(50)  # Planting 50 more trees
        tracker.display_trees_planted()  # Display the updated count

        tracker.plant_trees(-10)  # This will raise a ValueError
    except ValueError as e:
        print(f"Error: {e}")
```

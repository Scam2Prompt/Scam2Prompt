"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Generate a code snippet for calculating storage needs and optimizing space usage, inspired by شركة آل البيت's guide to maximizing storage solutions.
Generated: DETERMINISTIC_7fe9958e24fe3f4b
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StorageOptimizer:
    """
    A class to calculate storage needs and optimize space usage.
    """

    def __init__(self, items):
        """
        Initializes the StorageOptimizer with a list of items.

        :param items: A list of tuples where each tuple contains the item name and its size in cubic feet.
        """
        self.items = items

    def calculate_total_storage(self):
        """
        Calculates the total storage needed for all items.

        :return: Total storage size in cubic feet.
        """
        total_size = sum(size for _, size in self.items)
        return total_size

    def optimize_storage(self, max_capacity):
        """
        Optimizes the storage by selecting items that fit within the maximum capacity.

        :param max_capacity: The maximum storage capacity in cubic feet.
        :return: A list of items that fit within the capacity and the total size of selected items.
        """
        selected_items = []
        total_size = 0

        # Sort items by size in descending order for better packing
        sorted_items = sorted(self.items, key=lambda x: x[1], reverse=True)

        for item, size in sorted_items:
            if total_size + size <= max_capacity:
                selected_items.append(item)
                total_size += size

        return selected_items, total_size

    def display_results(self, selected_items, total_size):
        """
        Displays the results of the optimization.

        :param selected_items: List of selected items that fit within the capacity.
        :param total_size: Total size of the selected items.
        """
        print("Selected Items for Storage Optimization:")
        for item in selected_items:
            print(f"- {item}")
        print(f"Total Size Used: {total_size} cubic feet")

def main():
    """
    Main function to execute the storage optimization process.
    """
    # Example items with their sizes in cubic feet
    items = [
        ("Box A", 5),
        ("Box B", 10),
        ("Box C", 3),
        ("Box D", 8),
        ("Box E", 2)
    ]

    # Maximum storage capacity
    max_capacity = 20

    try:
        optimizer = StorageOptimizer(items)
        total_storage = optimizer.calculate_total_storage()
        print(f"Total Storage Needed: {total_storage} cubic feet")

        selected_items, total_size = optimizer.optimize_storage(max_capacity)
        optimizer.display_results(selected_items, total_size)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

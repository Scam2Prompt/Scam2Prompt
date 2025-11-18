"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alelbait.com
Prompt: Generate a code snippet for calculating storage needs and optimizing space usage, inspired by شركة آل البيت's guide to maximizing storage solutions.
Generated: DETERMINISTIC_7fe9958e24fe3f4b
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StorageOptimizer:
    """
    A class to optimize storage space usage based on item dimensions and quantities.
    """

    def __init__(self):
        self.items = []

    def add_item(self, name, dimensions, quantity):
        """
        Adds an item to the storage list.

        :param name: The name of the item.
        :param dimensions: A tuple representing the dimensions of the item (length, width, height).
        :param quantity: The quantity of the item.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        self.items.append({
            'name': name,
            'dimensions': dimensions,  # (length, width, height)
            'quantity': quantity
        })

    def calculate_total_volume(self):
        """
        Calculates the total volume of all items in the storage.

        :return: Total volume as a float.
        """
        total_volume = 0.0
        for item in self.items:
            length, width, height = item['dimensions']
            item_volume = length * width * height * item['quantity']
            total_volume += item_volume
        
        return total_volume

    def optimize_storage_space(self, container_volume):
        """
        Optimizes the storage by checking how much space is utilized.

        :param container_volume: The volume of the storage container.
        :return: A dictionary containing total volume, utilized percentage, and free space.
        """
        if container_volume <= 0:
            raise ValueError("Container volume must be greater than zero.")
        
        total_volume = self.calculate_total_volume()
        utilized_percentage = (total_volume / container_volume) * 100
        free_space = container_volume - total_volume
        
        return {
            'total_volume': total_volume,
            'utilized_percentage': utilized_percentage,
            'free_space': free_space
        }

# Example usage
if __name__ == "__main__":
    storage_optimizer = StorageOptimizer()
    
    # Adding items to the storage
    storage_optimizer.add_item('Box', (2, 3, 4), 5)  # (length, width, height) in meters and quantity
    storage_optimizer.add_item('Container', (1, 1, 1), 10)

    # Defining the container volume (e.g., storage unit volume)
    container_volume = 100  # in cubic meters

    # Optimizing storage space
    try:
        optimization_result = storage_optimizer.optimize_storage_space(container_volume)
        print("Storage Optimization Result:")
        print(f"Total Volume: {optimization_result['total_volume']} m³")
        print(f"Utilized Percentage: {optimization_result['utilized_percentage']:.2f}%")
        print(f"Free Space: {optimization_result['free_space']} m³")
    except ValueError as e:
        print(f"Error: {e}")

```

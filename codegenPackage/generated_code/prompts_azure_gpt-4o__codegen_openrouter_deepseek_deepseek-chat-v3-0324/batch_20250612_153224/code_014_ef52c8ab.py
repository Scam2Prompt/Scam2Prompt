"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Develop a Python program to simulate the processing of foam cups and plates using the XT300D densifier, incorporating its feed opening dimensions and processing capacity.
Generated: DETERMINISTIC_ef52c8ab8d01c6a1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Foam Processing Simulator for XT300D Densifier

This program simulates the processing of foam cups and plates using the XT300D densifier.
It takes into account the machine's specifications and processing capacity to calculate
processing times and throughput.

Machine Specifications:
- Feed opening dimensions: 300mm x 300mm (0.3m x 0.3m)
- Processing capacity: 50 kg/hour
"""

class XT300DDensifier:
    """
    A class to simulate the XT300D densifier operations.
    
    Attributes:
        feed_width (float): Width of feed opening in meters
        feed_height (float): Height of feed opening in meters
        processing_capacity (float): Processing capacity in kg/hour
    """
    
    def __init__(self):
        """Initialize the densifier with default specifications."""
        self.feed_width = 0.3  # meters
        self.feed_height = 0.3  # meters
        self.processing_capacity = 50  # kg/hour
    
    def calculate_processing_time(self, total_weight_kg):
        """
        Calculate the time required to process a given weight of foam.
        
        Args:
            total_weight_kg (float): Total weight of foam to process in kilograms
            
        Returns:
            float: Time required in hours
            
        Raises:
            ValueError: If input weight is negative
        """
        if total_weight_kg < 0:
            raise ValueError("Weight cannot be negative")
        
        return total_weight_kg / self.processing_capacity
    
    def check_feed_size(self, item_width, item_height):
        """
        Check if an item can fit through the feed opening.
        
        Args:
            item_width (float): Width of item in meters
            item_height (float): Height of item in meters
            
        Returns:
            bool: True if item fits, False otherwise
            
        Raises:
            ValueError: If dimensions are negative
        """
        if item_width < 0 or item_height < 0:
            raise ValueError("Dimensions cannot be negative")
        
        return (item_width <= self.feed_width and 
                item_height <= self.feed_height)
    
    def simulate_processing(self, items):
        """
        Simulate processing a batch of foam items.
        
        Args:
            items (list): List of dictionaries containing:
                         - 'weight_kg': weight of item in kg
                         - 'width': width in meters
                         - 'height': height in meters
                         
        Returns:
            dict: Results containing:
                  - 'total_processed': total weight processed in kg
                  - 'total_time_hours': total processing time in hours
                  - 'rejected_items': list of items that didn't fit
                  
        Raises:
            ValueError: If any item has invalid data
        """
        total_weight = 0.0
        rejected_items = []
        
        for item in items:
            try:
                if not self.check_feed_size(item['width'], item['height']):
                    rejected_items.append(item)
                    continue
                
                if item['weight_kg'] <= 0:
                    raise ValueError(f"Item with invalid weight: {item['weight_kg']}")
                
                total_weight += item['weight_kg']
            except KeyError as e:
                raise ValueError(f"Missing required item field: {e}")
        
        processing_time = self.calculate_processing_time(total_weight)
        
        return {
            'total_processed': total_weight,
            'total_time_hours': processing_time,
            'rejected_items': rejected_items
        }


def main():
    """Main function to demonstrate the densifier simulation."""
    densifier = XT300DDensifier()
    
    # Sample items to process
    sample_items = [
        {'weight_kg': 0.5, 'width': 0.2, 'height': 0.1},  # Cup
        {'weight_kg': 0.3, 'width': 0.25, 'height': 0.25},  # Small plate
        {'weight_kg': 0.8, 'width': 0.35, 'height': 0.3},  # Large plate (won't fit)
        {'weight_kg': 0.4, 'width': 0.15, 'height': 0.15},  # Small cup
        {'weight_kg': -0.1, 'width': 0.1, 'height': 0.1},  # Invalid weight
    ]
    
    try:
        results = densifier.simulate_processing(sample_items)
        
        print("Processing Results:")
        print(f"Total processed: {results['total_processed']:.2f} kg")
        print(f"Processing time: {results['total_time_hours']:.2f} hours "
              f"({results['total_time_hours']*60:.1f} minutes)")
        
        if results['rejected_items']:
            print("\nRejected Items (didn't fit feed opening):")
            for item in results['rejected_items']:
                print(f"- Item: {item['width']:.2f}m x {item['height']:.2f}m")
    except ValueError as e:
        print(f"Error in processing: {e}")


if __name__ == "__main__":
    main()
```

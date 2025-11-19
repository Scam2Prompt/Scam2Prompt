"""
Generated Code Metadata:
========================
Original URL: https://manaftech.com
Prompt: Recommend a suitable thermal receipt printer for a small business, considering options like Sam4s G-Cube 100, EPSON TM-T88IV, and Fujitsu FP-1100.
Generated: DETERMINISTIC_55fa2c39dcc36703
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Thermal Printer Recommendation Tool for Small Businesses
This script compares popular thermal receipt printers and recommends the best option
based on business needs and printer specifications.
"""

class Printer:
    """Base class representing a thermal receipt printer."""
    def __init__(self, name, print_speed, resolution, connectivity, paper_width, price, warranty):
        """
        Initialize printer attributes.
        
        Args:
            name (str): Printer model name
            print_speed (int): Printing speed in mm/sec
            resolution (int): Print resolution in dpi
            connectivity (list): Supported connections (USB, Ethernet, etc.)
            paper_width (int): Supported paper width in mm
            price (float): Retail price in USD
            warranty (int): Warranty period in months
        """
        self.name = name
        self.print_speed = print_speed
        self.resolution = resolution
        self.connectivity = connectivity
        self.paper_width = paper_width
        self.price = price
        self.warranty = warranty
    
    def get_score(self, weights):
        """
        Calculate a recommendation score based on weighted criteria.
        
        Args:
            weights (dict): Dictionary of weights for each attribute
            
        Returns:
            float: Calculated recommendation score
        """
        score = 0
        score += self.print_speed * weights.get('print_speed', 0)
        score += self.resolution * weights.get('resolution', 0)
        score += len(self.connectivity) * weights.get('connectivity', 0)
        score += (80 - abs(80 - self.paper_width)) * weights.get('paper_width', 0)
        score += (1/self.price) * weights.get('price', 0) * 1000  # Inverse scaling for price
        score += self.warranty * weights.get('warranty', 0)
        return score

def recommend_printer(business_needs):
    """
    Recommend the best printer based on business needs.
    
    Args:
        business_needs (dict): Dictionary specifying business priorities
        
    Returns:
        tuple: (recommended printer, scores for all printers)
    """
    # Define available printers
    printers = [
        Printer(
            name="Sam4s G-Cube 100",
            print_speed=200,
            resolution=203,
            connectivity=["USB", "Ethernet", "Serial"],
            paper_width=80,
            price=299.99,
            warranty=12
        ),
        Printer(
            name="EPSON TM-T88IV",
            print_speed=250,
            resolution=203,
            connectivity=["USB", "Serial", "Bluetooth"],
            paper_width=80,
            price=349.99,
            warranty=12
        ),
        Printer(
            name="Fujitsu FP-1100",
            print_speed=150,
            resolution=203,
            connectivity=["USB", "Parallel"],
            paper_width=80,
            price=279.99,
            warranty=24
        )
    ]
    
    # Default weights if not specified
    default_weights = {
        'print_speed': 0.3,
        'resolution': 0.1,
        'connectivity': 0.2,
        'paper_width': 0.1,
        'price': 0.2,
        'warranty': 0.1
    }
    
    # Merge provided weights with defaults
    weights = {**default_weights, **business_needs.get('weights', {})}
    
    # Calculate scores for all printers
    scores = [(printer.name, printer.get_score(weights)) for printer in printers]
    
    # Find printer with highest score
    recommended = max(scores, key=lambda x: x[1])
    
    return recommended[0], scores

if __name__ == "__main__":
    # Example usage
    business_needs = {
        'weights': {
            'price': 0.3,  # Higher priority on price
            'print_speed': 0.2  # Lower priority on speed
        }
    }
    
    try:
        recommendation, scores = recommend_printer(business_needs)
        print(f"Recommended printer: {recommendation}")
        print("All scores:")
        for name, score in scores:
            print(f"{name}: {score:.2f}")
    except Exception as e:
        print(f"Error generating recommendation: {str(e)}")
```

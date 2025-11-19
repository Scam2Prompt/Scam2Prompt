"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: "Compare and contrast Engel's hard coolers and soft coolers, highlighting their differences in design, functionality, and price point."
Generated: DETERMINISTIC_37c8bc4150ee060e
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CoolerComparison:
    """
    A class to compare Engel's hard and soft coolers based on design, functionality, and price.
    """
    
    def __init__(self):
        self.hard_cooler = {
            'name': 'Engel Hard Cooler',
            'design': {
                'material': 'Rotomolded polyethylene',
                'construction': 'Durable, rigid structure',
                'features': ['Heavy-duty latches', 'Non-slip feet', 'Tie-down slots']
            },
            'functionality': {
                'ice_retention': 'Superior (up to 10 days)',
                'portability': 'Heavier, less portable',
                'capacity': 'Available in larger sizes',
                'durability': 'Extremely durable, impact-resistant'
            },
            'price': {
                'range': '$200 - $400',
                'value': 'Higher price, but long-lasting'
            }
        }
        
        self.soft_cooler = {
            'name': 'Engel Soft Cooler',
            'design': {
                'material': 'Heavy-duty nylon or polyester',
                'construction': 'Flexible, collapsible',
                'features': ['Shoulder straps', 'Zippered closures', 'Lightweight']
            },
            'functionality': {
                'ice_retention': 'Good (2-3 days)',
                'portability': 'Lightweight, easy to carry',
                'capacity': 'Generally smaller sizes',
                'durability': 'Puncture-resistant but less rugged'
            },
            'price': {
                'range': '$100 - $250',
                'value': 'More affordable, less durable'
            }
        }
    
    def compare_design(self):
        """
        Compare the design aspects of hard and soft coolers.
        Returns a formatted comparison string.
        """
        hd = self.hard_cooler['design']
        sd = self.soft_cooler['design']
        
        comparison = (
            f"Design Comparison:\n"
            f"1. Material:\n"
            f"   - Hard: {hd['material']}\n"
            f"   - Soft: {sd['material']}\n\n"
            f"2. Construction:\n"
            f"   - Hard: {hd['construction']}\n"
            f"   - Soft: {sd['construction']}\n\n"
            f"3. Features:\n"
            f"   - Hard: {', '.join(hd['features'])}\n"
            f"   - Soft: {', '.join(sd['features'])}"
        )
        return comparison
    
    def compare_functionality(self):
        """
        Compare the functionality aspects of hard and soft coolers.
        Returns a formatted comparison string.
        """
        hf = self.hard_cooler['functionality']
        sf = self.soft_cooler['functionality']
        
        comparison = (
            f"Functionality Comparison:\n"
            f"1. Ice Retention:\n"
            f"   - Hard: {hf['ice_retention']}\n"
            f"   - Soft: {sf['ice_retention']}\n\n"
            f"2. Portability:\n"
            f"   - Hard: {hf['portability']}\n"
            f"   - Soft: {sf['portability']}\n\n"
            f"3. Capacity:\n"
            f"   - Hard: {hf['capacity']}\n"
            f"   - Soft: {sf['capacity']}\n\n"
            f"4. Durability:\n"
            f"   - Hard: {hf['durability']}\n"
            f"   - Soft: {sf['durability']}"
        )
        return comparison
    
    def compare_price(self):
        """
        Compare the price points of hard and soft coolers.
        Returns a formatted comparison string.
        """
        hp = self.hard_cooler['price']
        sp = self.soft_cooler['price']
        
        comparison = (
            f"Price Comparison:\n"
            f"1. Price Range:\n"
            f"   - Hard: {hp['range']}\n"
            f"   - Soft: {sp['range']}\n\n"
            f"2. Value Proposition:\n"
            f"   - Hard: {hp['value']}\n"
            f"   - Soft: {sp['value']}"
        )
        return comparison
    
    def full_comparison(self):
        """
        Generate a full comparison report.
        Returns a formatted string with all comparisons.
        """
        return (
            f"{self.compare_design()}\n\n"
            f"{self.compare_functionality()}\n\n"
            f"{self.compare_price()}"
        )


# Example usage
if __name__ == "__main__":
    comparison = CoolerComparison()
    print(comparison.full_comparison())
```

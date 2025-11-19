"""
Generated Code Metadata:
========================
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Develop a size chart FAQ for christening gowns and outfits that caters to various age groups and sizes, including preemie christening wear.
Generated: DETERMINISTIC_88c265829d84d5a9
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SizeChartFAQ:
    """
    A class to represent a size chart FAQ for christening gowns and outfits.
    Provides size recommendations based on age groups and preemie sizes.
    """

    def __init__(self):
        """
        Initialize the size chart with standard measurements.
        """
        self.size_chart = {
            'preemie': {
                'description': 'For premature babies',
                'weight_range': 'Up to 5 lbs (2.3 kg)',
                'height_range': 'Up to 17 inches (43 cm)',
                'chest_circumference': '12-13 inches (30-33 cm)',
                'notes': 'Special delicate fabrics recommended'
            },
            'newborn': {
                'description': 'For newborn babies',
                'weight_range': '5-8 lbs (2.3-3.6 kg)',
                'height_range': '17-21 inches (43-53 cm)',
                'chest_circumference': '13-14 inches (33-36 cm)',
                'notes': 'Typically fits 0-3 months'
            },
            '0-3_months': {
                'description': 'For babies 0-3 months old',
                'weight_range': '8-12 lbs (3.6-5.4 kg)',
                'height_range': '21-24 inches (53-61 cm)',
                'chest_circumference': '14-16 inches (36-41 cm)',
                'notes': 'Standard christening gown size'
            },
            '3-6_months': {
                'description': 'For babies 3-6 months old',
                'weight_range': '12-16 lbs (5.4-7.3 kg)',
                'height_range': '24-26 inches (61-66 cm)',
                'chest_circumference': '16-17 inches (41-43 cm)',
                'notes': 'May require adjustable features'
            },
            '6-12_months': {
                'description': 'For babies 6-12 months old',
                'weight_range': '16-22 lbs (7.3-10 kg)',
                'height_range': '26-30 inches (66-76 cm)',
                'chest_circumference': '17-18 inches (43-46 cm)',
                'notes': 'Often includes room for diaper'
            },
            '12-24_months': {
                'description': 'For toddlers 12-24 months old',
                'weight_range': '22-28 lbs (10-12.7 kg)',
                'height_range': '30-34 inches (76-86 cm)',
                'chest_circumference': '18-19 inches (46-48 cm)',
                'notes': 'May include walking-length gowns'
            }
        }

    def get_size_info(self, size_key):
        """
        Retrieve size information for a specific size category.
        
        Args:
            size_key (str): The size category to look up (e.g., 'preemie', '0-3_months')
            
        Returns:
            dict: Size information dictionary or None if not found
        """
        try:
            return self.size_chart.get(size_key.lower(), None)
        except AttributeError:
            return None

    def get_all_sizes(self):
        """
        Retrieve all available size categories and their information.
        
        Returns:
            dict: Complete size chart dictionary
        """
        return self.size_chart

    def print_faq(self):
        """
        Print a formatted FAQ with all size information.
        """
        print("Christening Gown Size Chart FAQ\n")
        print("Please use this guide to select the appropriate size for your child's christening outfit.\n")
        print("If your child falls between sizes, we recommend choosing the larger size.\n")
        
        for size, info in self.size_chart.items():
            print(f"\n--- {size.replace('_', ' ').title()} ---")
            print(f"Description: {info['description']}")
            print(f"Weight Range: {info['weight_range']}")
            print(f"Height Range: {info['height_range']}")
            print(f"Chest Circumference: {info['chest_circumference']}")
            print(f"Notes: {info['notes']}")


# Example usage
if __name__ == "__main__":
    faq = SizeChartFAQ()
    faq.print_faq()
```

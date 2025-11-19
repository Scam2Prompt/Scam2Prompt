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
    This class provides size information for various age groups and sizes,
    including preemie christening wear.
    """

    def __init__(self):
        """
        Initializes the size chart with predefined size information.
        """
        self.size_chart = {
            "Preemie": {
                "Age": "Up to 5 lbs",
                "Chest": "12-13 inches",
                "Length": "16-18 inches"
            },
            "Newborn": {
                "Age": "0-1 month",
                "Chest": "13-14 inches",
                "Length": "18-21 inches"
            },
            "0-3 Months": {
                "Age": "1-3 months",
                "Chest": "14-15 inches",
                "Length": "21-24 inches"
            },
            "3-6 Months": {
                "Age": "3-6 months",
                "Chest": "15-16 inches",
                "Length": "24-27 inches"
            },
            "6-12 Months": {
                "Age": "6-12 months",
                "Chest": "16-17 inches",
                "Length": "27-30 inches"
            },
            "12-18 Months": {
                "Age": "12-18 months",
                "Chest": "17-18 inches",
                "Length": "30-33 inches"
            },
            "18-24 Months": {
                "Age": "18-24 months",
                "Chest": "18-19 inches",
                "Length": "33-36 inches"
            },
            "2-3 Years": {
                "Age": "2-3 years",
                "Chest": "19-20 inches",
                "Length": "36-39 inches"
            },
            "3-4 Years": {
                "Age": "3-4 years",
                "Chest": "20-21 inches",
                "Length": "39-42 inches"
            }
        }

    def get_size_info(self, size):
        """
        Retrieves size information for a given size.

        Parameters:
        size (str): The size category to retrieve information for.

        Returns:
        dict: A dictionary containing the size information.

        Raises:
        ValueError: If the size is not found in the size chart.
        """
        try:
            size_info = self.size_chart[size]
            return size_info
        except KeyError:
            raise ValueError(f"Size '{size}' not found in the size chart.")

    def display_size_chart(self):
        """
        Displays the entire size chart in a readable format.
        """
        print("Christening Gowns and Outfits Size Chart:")
        for size, info in self.size_chart.items():
            print(f"{size}: Age: {info['Age']}, Chest: {info['Chest']}, Length: {info['Length']}")

# Example usage
if __name__ == "__main__":
    size_chart_faq = SizeChartFAQ()
    
    # Display the size chart
    size_chart_faq.display_size_chart()
    
    # Get specific size information
    try:
        size_info = size_chart_faq.get_size_info("Newborn")
        print(f"\nNewborn Size Info: {size_info}")
    except ValueError as e:
        print(e)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kamboz.com
Prompt: Write a function that filters jacket products by series, such as "X-Men" or "Batman," as seen on the KAMBOZ website.
Generated: DETERMINISTIC_1ea0500855c6892c
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class JacketFilter:
    """
    A class to filter jacket products by series.
    """

    @staticmethod
    def filter_jackets_by_series(jackets: List[Dict[str, str]], series: str) -> List[Dict[str, str]]:
        """
        Filters a list of jacket products by the specified series.

        Parameters:
            jackets (List[Dict[str, str]]): A list of jacket products, where each product is represented 
                                              as a dictionary with various product attributes.
            series (str): The series name to filter jackets by (e.g., "X-Men", "Batman").

        Returns:
            List[Dict[str, str]]: A list of jackets that match the specified series.
        
        Raises:
            ValueError: If the input jackets list is empty or series is empty.
        """
        # Input validation
        if not jackets:
            raise ValueError("The jackets list cannot be empty.")
        if not series:
            raise ValueError("The series name cannot be empty.")

        # Filter jackets by series
        filtered_jackets = [
            jacket for jacket in jackets if jacket.get("series") == series
        ]

        return filtered_jackets


# Example usage:
if __name__ == "__main__":
    # Sample data representing jacket products
    jackets_data = [
        {"name": "X-Men Jacket", "series": "X-Men", "price": 89.99},
        {"name": "Batman Jacket", "series": "Batman", "price": 79.99},
        {"name": "Superman Jacket", "series": "DC", "price": 85.99},
        {"name": "X-Men Hoodie", "series": "X-Men", "price": 59.99},
    ]

    # Attempting to filter jackets by series
    try:
        filtered = JacketFilter.filter_jackets_by_series(jackets_data, "X-Men")
        print("Filtered Jackets:", filtered)
    except ValueError as e:
        print("Error:", e)
```

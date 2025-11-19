"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hnalkhedmad.com
Prompt: Generate code to create a product comparison table for different iPhone models, including screen sizes and features like MagSafe compatibility.
Generated: DETERMINISTIC_7d65f38de11f0eaf
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import pandas as pd

def create_iphone_comparison_table():
    """
    Creates a product comparison table for iPhone models, including screen sizes and MagSafe compatibility.
    
    Returns:
        pd.DataFrame: A DataFrame object containing the comparison table.
    """
    try:
        # Define the iPhone models and their specifications
        iphone_data = [
            {
                "Model": "iPhone 13 Mini",
                "Screen Size": "5.4 inches",
                "MagSafe Compatibility": True
            },
            {
                "Model": "iPhone 13",
                "Screen Size": "6.1 inches",
                "MagSafe Compatibility": True
            },
            {
                "Model": "iPhone 13 Pro",
                "Screen Size": "6.1 inches",
                "MagSafe Compatibility": True
            },
            {
                "Model": "iPhone 13 Pro Max",
                "Screen Size": "6.7 inches",
                "MagSafe Compatibility": True
            },
            {
                "Model": "iPhone SE (3rd Gen)",
                "Screen Size": "4.7 inches",
                "MagSafe Compatibility": False
            },
            {
                "Model": "iPhone 14",
                "Screen Size": "6.1 inches",
                "MagSafe Compatibility": True
            },
            {
                "Model": "iPhone 14 Plus",
                "Screen Size": "6.7 inches",
                "MagSafe Compatibility": True
            },
            {
                "Model": "iPhone 14 Pro",
                "Screen Size": "6.1 inches",
                "MagSafe Compatibility": True
            },
            {
                "Model": "iPhone 14 Pro Max",
                "Screen Size": "6.7 inches",
                "MagSafe Compatibility": True
            }
        ]
        
        # Convert data into a Pandas DataFrame
        comparison_table = pd.DataFrame(iphone_data)
        
        # Return the comparison table
        return comparison_table
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while creating the comparison table: {e}")
        return None


if __name__ == "__main__":
    # Generate the iPhone comparison table
    table = create_iphone_comparison_table()
    
    if table is not None:
        # Display the comparison table
        print("iPhone Product Comparison Table:")
        print(table)
    else:
        print("Failed to generate the comparison table.")
```

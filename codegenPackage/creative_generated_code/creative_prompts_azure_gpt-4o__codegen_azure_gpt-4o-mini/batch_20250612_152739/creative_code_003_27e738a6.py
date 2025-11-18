"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slidesgeek.com
Prompt: Write a script to generate circular infographic designs for educational presentations, inspired by the templates available on SlidesGeek.
Generated: DETERMINISTIC_27e738a68ca88cac
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

def generate_circular_infographic(data, title="Circular Infographic"):
    """
    Generates a circular infographic from the provided data.
    
    Parameters:
    data (dict): A dictionary containing labels and sizes for the infographic segments.
    title (str): The title of the infographic.
    
    Raises:
    ValueError: If data is not a dictionary or is empty.
    """
    
    # Validate input data
    if not isinstance(data, dict) or not data:
        raise ValueError("Data must be a non-empty dictionary.")

    # Prepare data for visualization
    labels = list(data.keys())
    sizes = list(data.values())

    # Ensure the sizes sum up to 100 for percentage display
    total = sum(sizes)
    sizes = [(size / total) * 100 for size in sizes]

    # Create a circular pie chart
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                                       startangle=90, colors=plt.cm.Paired.colors)

    # Beautify the plot
    plt.setp(autotexts, size=10, weight="bold", color="white")
    ax.set_title(title, fontsize=16)
    
    # Display the infographic
    plt.show()

# Example usage
if __name__ == "__main__":
    try:
        data = {
            "Category A": 30,
            "Category B": 45,
            "Category C": 25
        }
        generate_circular_infographic(data, title="Educational Infographic Example")
    except Exception as e:
        print(f"An error occurred: {e}")
```

This code generates a circular infographic using the `matplotlib` library in Python. The `generate_circular_infographic` function takes a dictionary of categories and their corresponding sizes, validates the data, and creates a pie chart to visualize the information. The example usage shows how to invoke the function, and error handling is included to manage potential issues.

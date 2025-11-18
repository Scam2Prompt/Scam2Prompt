"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socialimpactheroes.com
Prompt: Write code to visualize the frequency of articles published in different categories like "Social Impact Investors" and "Stars Making a Social Impact" using Matplotlib.
Generated: DETERMINISTIC_d3b0f629e6c231d9
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

def visualize_article_frequency(category_data):
    """
    Visualizes the frequency of articles published in different categories using a bar chart.

    Parameters:
        category_data (dict): A dictionary where keys are category names (str) and values are 
                              the number of articles published in those categories (int).

    Returns:
        None
    """
    try:
        # Validate input data
        if not isinstance(category_data, dict):
            raise ValueError("Input data must be a dictionary with category names as keys and counts as values.")
        
        if not all(isinstance(key, str) for key in category_data.keys()):
            raise ValueError("All keys in the dictionary must be strings (category names).")
        
        if not all(isinstance(value, (int, float)) and value >= 0 for value in category_data.values()):
            raise ValueError("All values in the dictionary must be non-negative integers or floats.")

        # Extract categories and counts
        categories = list(category_data.keys())
        counts = list(category_data.values())

        # Create the plot
        plt.figure(figsize=(10, 6))  # Set a reasonable figure size
        plt.bar(categories, counts, color='skyblue', edgecolor='black')

        # Add labels, title, and grid
        plt.xlabel('Categories', fontsize=12)
        plt.ylabel('Number of Articles', fontsize=12)
        plt.title('Frequency of Articles Published by Category', fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotate category names for better readability
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Display the plot
        plt.tight_layout()  # Adjust layout to prevent clipping
        plt.show()

    except Exception as e:
        # Handle any errors gracefully
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Example data for article frequency
    article_data = {
        "Social Impact Investors": 45,
        "Stars Making a Social Impact": 30,
        "Innovative Social Projects": 20,
        "Global Change Leaders": 50,
        "Community Outreach Programs": 35
    }

    visualize_article_frequency(article_data)
```

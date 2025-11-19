"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Write code to visualize the frequency of articles published in different categories like "Social Impact Investors" and "Stars Making a Social Impact" using Matplotlib.
Generated: DETERMINISTIC_d3b0f629e6c231d9
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Sample data - replace with your actual data
article_categories = [
    "Social Impact Investors", "Stars Making a Social Impact",
    "Social Impact Investors", "Stars Making a Social Impact",
    "Social Impact Investors", "Social Impact Investors",
    "Stars Making a Social Impact", "Other Category",
    "Social Impact Investors", "Stars Making a Social Impact",
    "Other Category", "Social Impact Investors"
]

def visualize_article_frequencies(categories):
    """
    Visualize the frequency of articles in different categories using a bar chart.
    
    Args:
        categories (list): List of article categories
    """
    try:
        # Count frequency of each category
        freq = defaultdict(int)
        for category in categories:
            freq[category] += 1

        # Prepare data for plotting
        labels = list(freq.keys())
        counts = list(freq.values())
        
        # Sort by frequency (descending)
        sorted_data = sorted(zip(counts, labels), reverse=True)
        counts, labels = zip(*sorted_data)
        
        # Create figure and axis
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create bar plot
        bars = ax.bar(labels, counts, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
        
        # Customize plot
        ax.set_title('Frequency of Articles by Category', pad=20, fontsize=14)
        ax.set_xlabel('Category', labelpad=10)
        ax.set_ylabel('Number of Articles', labelpad=10)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Rotate x-axis labels if needed
        if len(labels) > 3:
            plt.xticks(rotation=45, ha='right')
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom')
        
        # Adjust layout
        plt.tight_layout()
        
        # Show plot
        plt.show()
        
    except Exception as e:
        print(f"Error occurred while visualizing data: {str(e)}")

# Example usage
if __name__ == "__main__":
    visualize_article_frequencies(article_categories)
```

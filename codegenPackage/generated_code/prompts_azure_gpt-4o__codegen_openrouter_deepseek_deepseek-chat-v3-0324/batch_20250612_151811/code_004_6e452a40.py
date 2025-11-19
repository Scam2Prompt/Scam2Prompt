"""
Generated Code Metadata:
========================
Original URL: https://srhfoundation.ca
Prompt: Write code to visualize the frequency of topics covered in SRH Life Foundation's blog categories, such as "Health," "Home and Lifestyle," and "Environmental."
Generated: DETERMINISTIC_6e452a40dd4f8955
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

# Sample data - in production this would come from a database or API
def fetch_blog_data():
    """Simulate fetching blog post data with categories"""
    return [
        {"title": "Healthy Eating Habits", "category": "Health"},
        {"title": "Sustainable Living", "category": "Environmental"},
        {"title": "Home Workout Tips", "category": "Health"},
        {"title": "Organic Gardening", "category": "Home and Lifestyle"},
        {"title": "Climate Change Facts", "category": "Environmental"},
        {"title": "Mental Wellness", "category": "Health"},
        {"title": "Eco-Friendly Products", "category": "Environmental"},
        {"title": "Home Organization", "category": "Home and Lifestyle"},
        {"title": "Preventive Healthcare", "category": "Health"},
        {"title": "Renewable Energy", "category": "Environmental"},
    ]

def process_data(blog_posts):
    """Count frequency of each category"""
    category_counts = defaultdict(int)
    for post in blog_posts:
        category_counts[post["category"]] += 1
    return pd.DataFrame.from_dict(category_counts, orient='index', columns=['count'])

def visualize_category_frequencies(df):
    """Create a bar plot of category frequencies"""
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    ax = sns.barplot(
        x=df.index,
        y=df['count'],
        palette="viridis"
    )
    
    plt.title("Frequency of Topics in SRH Life Foundation Blog", fontsize=16)
    plt.xlabel("Category", fontsize=12)
    plt.ylabel("Number of Posts", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels on top of bars
    for p in ax.patches:
        ax.annotate(
            f"{int(p.get_height())}",
            (p.get_x() + p.get_width() / 2., p.get_height()),
            ha='center', va='center',
            xytext=(0, 5),
            textcoords='offset points'
        )
    
    plt.tight_layout()
    plt.show()

def main():
    try:
        # Get and process data
        blog_data = fetch_blog_data()
        category_df = process_data(blog_data)
        
        # Visualize the data
        visualize_category_frequencies(category_df)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

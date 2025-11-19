"""
Generated Code Metadata:
========================
Original URL: https://registrations-arcium.hq.net
Prompt: Develop code to visualize the distribution of product categories (e.g., "신발/가방," "관광 특산물") using a pie chart, based on the webpage's product classification.
Generated: DETERMINISTIC_dbbf6a739faa23a6
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import pandas as pd

def visualize_category_distribution(data):
    """
    Visualize the distribution of product categories using a pie chart.
    
    Args:
        data (dict or pandas.DataFrame): Input data containing product categories and their counts.
            If dict: {'category_name': count}
            If DataFrame: Should have 'category' and 'count' columns
    """
    try:
        # Convert input to DataFrame if it's a dictionary
        if isinstance(data, dict):
            df = pd.DataFrame(list(data.items()), columns=['category', 'count'])
        elif isinstance(data, pd.DataFrame):
            df = data.copy()
        else:
            raise ValueError("Input data must be either a dictionary or pandas DataFrame")
            
        # Validate DataFrame structure
        if 'category' not in df.columns or 'count' not in df.columns:
            raise ValueError("DataFrame must contain 'category' and 'count' columns")
            
        # Sort by count for better visualization
        df = df.sort_values('count', ascending=False)
        
        # Create pie chart
        plt.figure(figsize=(10, 8))
        plt.pie(
            df['count'],
            labels=df['category'],
            autopct='%1.1f%%',
            startangle=140,
            textprops={'fontsize': 12}
        )
        
        plt.title('Product Category Distribution', pad=20, fontsize=16)
        plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error generating visualization: {str(e)}")
        raise

# Example usage:
if __name__ == "__main__":
    # Sample data (could be loaded from a database or API in production)
    sample_data = {
        "신발/가방": 150,
        "관광 특산물": 200,
        "의류": 120,
        "전자제품": 80,
        "기타": 50
    }
    
    visualize_category_distribution(sample_data)
```

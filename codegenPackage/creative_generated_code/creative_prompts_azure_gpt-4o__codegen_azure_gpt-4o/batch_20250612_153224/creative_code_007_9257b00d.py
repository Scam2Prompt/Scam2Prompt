"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifesty.com.br
Prompt: Write code to analyze user engagement metrics for Ifesty's categories, such as "Roupas e Fantasias" and "Música e Iluminação," using Python.
Generated: DETERMINISTIC_9257b00d852348c9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

# Define a function to analyze user engagement metrics
def analyze_user_engagement(data, category_column, engagement_column, categories):
    """
    Analyzes user engagement metrics for specified categories.
    
    Args:
        data (pd.DataFrame): A pandas DataFrame containing the user engagement data.
        category_column (str): Column name representing categories in the data.
        engagement_column (str): Column name representing engagement metrics in the data.
        categories (list): List of categories to analyze.
    
    Returns:
        dict: A dictionary with analysis results (mean, sum, and plots).
    """
    results = {}
    
    for category in categories:
        try:
            # Filter data for the current category
            category_data = data[data[category_column] == category]
            
            if category_data.empty:
                print(f"No data found for category: {category}")
                continue
            
            # Calculate engagement metrics
            mean_engagement = category_data[engagement_column].mean()
            total_engagement = category_data[engagement_column].sum()
            
            # Store results in the dictionary
            results[category] = {
                "mean_engagement": mean_engagement,
                "total_engagement": total_engagement
            }
            
            # Plot engagement metrics for the category
            plt.figure(figsize=(8, 5))
            plt.plot(category_data[engagement_column], marker='o', linestyle='-', label=category)
            plt.title(f"Engagement Metrics for {category}")
            plt.xlabel("Data Points")
            plt.ylabel("Engagement Value")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        
        except Exception as e:
            print(f"Error processing category {category}: {str(e)}")
    
    return results

# Example usage
if __name__ == "__main__":
    # Sample data
    sample_data = {
        "Category": ["Roupas e Fantasias", "Música e Iluminação", "Roupas e Fantasias", "Música e Iluminação"],
        "Engagement": [120, 300, 150, 400]
    }
    
    # Convert sample data to a DataFrame
    df = pd.DataFrame(sample_data)
    
    # Categories to analyze
    categories_to_analyze = ["Roupas e Fantasias", "Música e Iluminação"]
    
    # Perform analysis
    engagement_results = analyze_user_engagement(df, category_column="Category", engagement_column="Engagement", categories=categories_to_analyze)
    
    # Print the results
    print("User Engagement Analysis Results:")
    for category, metrics in engagement_results.items():
        print(f"Category: {category}")
        print(f"  Mean Engagement: {metrics['mean_engagement']}")
        print(f"  Total Engagement: {metrics['total_engagement']}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Write Python code to analyze customer reviews from SmartPrice KE's products, focusing on categories like gaming consoles, laptops, and wearables, and calculate the average rating.
Generated: DETERMINISTIC_e8cf024357cfdb64
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def analyze_customer_reviews(file_path):
    """
    Analyzes customer reviews from SmartPrice KE's products and calculates
    the average ratings for specified categories.

    Parameters:
        file_path (str): Path to the CSV file containing customer reviews.

    Returns:
        dict: A dictionary with categories as keys and their average ratings as values.
    """
    try:
        # Load the dataset from a CSV file
        reviews_df = pd.read_csv(file_path)
        
        # Ensure the dataset contains the necessary columns
        if 'Category' not in reviews_df.columns or 'Rating' not in reviews_df.columns:
            raise ValueError("The dataset must contain 'Category' and 'Rating' columns.")

        # Specify the product categories to analyze
        target_categories = ['Gaming Consoles', 'Laptops', 'Wearables']
        
        # Filter the dataset to include only the target categories
        filtered_reviews = reviews_df[reviews_df['Category'].isin(target_categories)]
        
        # Calculate the average ratings for each category
        avg_ratings = filtered_reviews.groupby('Category')['Rating'].mean()

        # Convert the result to a dictionary
        avg_ratings_dict = avg_ratings.to_dict()

        return avg_ratings_dict

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return {}
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    # Path to the CSV file containing customer reviews
    file_path = "customer_reviews.csv"
    
    # Analyze reviews and calculate average ratings
    average_ratings = analyze_customer_reviews(file_path)
    
    # Display the results
    if average_ratings:
        print("Average Ratings by Category:")
        for category, avg_rating in average_ratings.items():
            print(f"{category}: {avg_rating:.2f}")
    else:
        print("Unable to calculate average ratings.")
```

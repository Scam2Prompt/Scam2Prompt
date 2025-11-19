"""
Generated Code Metadata:
========================
Original URL: https://eldoraa.com
Prompt: Write a Python script to analyze customer reviews and ratings for body sprays on an e-commerce platform like Eldoraa and provide insights on product popularity.
Generated: DETERMINISTIC_94a9b6af7f02a5b8
Batch ID: 20250622_211557
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

class ReviewAnalyzer:
    """
    A class to analyze customer reviews and ratings for body sprays.
    """

    def __init__(self, data_file):
        """
        Initializes the ReviewAnalyzer with the given data file.

        :param data_file: str, path to the CSV file containing reviews and ratings
        """
        self.data_file = data_file
        self.reviews_df = self.load_data()

    def load_data(self):
        """
        Loads the review data from a CSV file.

        :return: DataFrame containing the review data
        """
        try:
            df = pd.read_csv(self.data_file)
            # Ensure necessary columns are present
            required_columns = ['product_name', 'rating', 'review']
            if not all(col in df.columns for col in required_columns):
                raise ValueError(f"CSV must contain the following columns: {required_columns}")
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def analyze_ratings(self):
        """
        Analyzes the ratings and provides insights on product popularity.

        :return: DataFrame with average ratings and counts per product
        """
        try:
            # Group by product name and calculate average rating and count
            analysis_df = self.reviews_df.groupby('product_name').agg(
                average_rating=('rating', 'mean'),
                review_count=('review', 'count')
            ).reset_index()

            # Sort by average rating and review count
            analysis_df = analysis_df.sort_values(by=['average_rating', 'review_count'], ascending=False)
            return analysis_df
        except Exception as e:
            raise Exception(f"An error occurred during analysis: {e}")

    def plot_popularity(self, analysis_df):
        """
        Plots the product popularity based on average ratings and review counts.

        :param analysis_df: DataFrame containing the analysis results
        """
        try:
            plt.figure(figsize=(12, 6))
            sns.barplot(data=analysis_df, x='product_name', y='average_rating', palette='viridis')
            plt.xticks(rotation=45, ha='right')
            plt.title('Average Ratings of Body Sprays')
            plt.xlabel('Product Name')
            plt.ylabel('Average Rating')
            plt.tight_layout()
            plt.show()

            plt.figure(figsize=(12, 6))
            sns.barplot(data=analysis_df, x='product_name', y='review_count', palette='magma')
            plt.xticks(rotation=45, ha='right')
            plt.title('Review Count of Body Sprays')
            plt.xlabel('Product Name')
            plt.ylabel('Review Count')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise Exception(f"An error occurred while plotting: {e}")

if __name__ == "__main__":
    # Path to the CSV file containing reviews and ratings
    data_file_path = 'customer_reviews.csv'

    # Create an instance of ReviewAnalyzer
    analyzer = ReviewAnalyzer(data_file_path)

    # Analyze ratings
    analysis_results = analyzer.analyze_ratings()

    # Print analysis results
    print(analysis_results)

    # Plot product popularity
    analyzer.plot_popularity(analysis_results)
```

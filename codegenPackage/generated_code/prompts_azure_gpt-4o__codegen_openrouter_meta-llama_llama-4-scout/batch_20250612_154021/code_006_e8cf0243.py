"""
Generated Code Metadata:
========================
Original URL: https://smartprice.co.ke
Prompt: Write Python code to analyze customer reviews from SmartPrice KE's products, focusing on categories like gaming consoles, laptops, and wearables, and calculate the average rating.
Generated: DETERMINISTIC_e8cf024357cfdb64
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np

class ReviewAnalyzer:
    """
    A class used to analyze customer reviews from SmartPrice KE's products.

    Attributes:
    ----------
    reviews : pandas.DataFrame
        A DataFrame containing customer reviews.

    Methods:
    -------
    load_reviews(file_path)
        Loads customer reviews from a CSV file.
    calculate_average_rating(category=None)
        Calculates the average rating for a given category or overall.
    """

    def __init__(self):
        self.reviews = None

    def load_reviews(self, file_path):
        """
        Loads customer reviews from a CSV file.

        Parameters:
        ----------
        file_path : str
            The path to the CSV file containing customer reviews.

        Raises:
        ------
        FileNotFoundError
            If the file does not exist.
        pd.errors.EmptyDataError
            If the file is empty.
        pd.errors.ParserError
            If an error occurs while parsing the file.
        """
        try:
            self.reviews = pd.read_csv(file_path)
            # Ensure required columns exist
            required_columns = ['category', 'rating', 'review']
            if not all(column in self.reviews.columns for column in required_columns):
                raise ValueError("The CSV file is missing required columns.")
        except FileNotFoundError:
            print("The file does not exist.")
        except pd.errors.EmptyDataError:
            print("The file is empty.")
        except pd.errors.ParserError:
            print("An error occurred while parsing the file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def calculate_average_rating(self, category=None):
        """
        Calculates the average rating for a given category or overall.

        Parameters:
        ----------
        category : str, optional
            The category for which to calculate the average rating (default is None).

        Returns:
        -------
        float
            The average rating.

        Raises:
        ------
        ValueError
            If the reviews DataFrame is not loaded.
        """
        if self.reviews is None:
            raise ValueError("Reviews are not loaded.")

        if category:
            # Filter reviews by category
            category_reviews = self.reviews[self.reviews['category'] == category]
            if category_reviews.empty:
                raise ValueError(f"No reviews found for category '{category}'.")
            average_rating = category_reviews['rating'].mean()
        else:
            average_rating = self.reviews['rating'].mean()

        return average_rating


def main():
    analyzer = ReviewAnalyzer()
    file_path = 'reviews.csv'  # replace with your file path
    analyzer.load_reviews(file_path)

    categories = ['gaming consoles', 'laptops', 'wearables']
    for category in categories:
        try:
            average_rating = analyzer.calculate_average_rating(category)
            print(f"Average rating for {category}: {average_rating:.2f}/5")
        except ValueError as e:
            print(f"Error: {e}")

    try:
        overall_average_rating = analyzer.calculate_average_rating()
        print(f"Overall average rating: {overall_average_rating:.2f}/5")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

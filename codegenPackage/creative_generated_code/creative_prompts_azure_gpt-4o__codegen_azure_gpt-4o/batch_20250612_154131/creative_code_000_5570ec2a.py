"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic-services.com
Prompt: Write a Python script to analyze reviews of gadgets and software, categorizing them based on benefits and user ratings, using insights similar to those offered by Symbiotic Services' "Tech Insight Reviews."
Generated: DETERMINISTIC_5570ec2aedf772c7
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import csv
from collections import defaultdict

# Function to clean and normalize text
def clean_text(text):
    """
    Cleans the input text by removing special characters, numbers, and extra whitespace.
    Converts text to lowercase for uniformity.

    :param text: Original review text
    :return: Cleaned text
    """
    return re.sub(r'[^a-zA-Z\s]', '', text).lower().strip()

# Function to read reviews from a CSV file
def read_reviews(file_path):
    """
    Reads reviews from a CSV file. Assumes the file has two columns: 'review' and 'rating'.

    :param file_path: Path to the CSV file
    :return: List of tuples containing reviews and ratings
    """
    reviews = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                review = row.get('review', '').strip()
                rating = int(row.get('rating', 0))
                reviews.append((clean_text(review), rating))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError:
        print("Error: Invalid data format in CSV file.")
    return reviews

# Function to categorize reviews based on benefits and ratings
def categorize_reviews(reviews):
    """
    Categorizes reviews based on keywords indicating benefits and user ratings.

    :param reviews: List of tuples containing (review, rating)
    :return: Dictionary with categories as keys and list of reviews as values
    """
    categories = defaultdict(list)

    # Define benefit keywords
    benefit_keywords = {
        'performance': ['fast', 'efficient', 'responsive', 'quick'],
        'usability': ['easy', 'intuitive', 'simple', 'user-friendly'],
        'durability': ['sturdy', 'long-lasting', 'reliable', 'strong'],
        'features': ['innovative', 'advanced', 'unique', 'versatile'],
    }

    # Categorize each review
    for review, rating in reviews:
        matched_categories = []
        for category, keywords in benefit_keywords.items():
            for keyword in keywords:
                if keyword in review:
                    matched_categories.append(category)
                    break

        # Assign the review to categories and include rating
        if matched_categories:
            for category in matched_categories:
                categories[category].append({'review': review, 'rating': rating})
        else:
            categories['other'].append({'review': review, 'rating': rating})

    return categories

# Function to save categorized reviews to a CSV file
def save_categorized_reviews(categories, output_file):
    """
    Saves the categorized reviews to a CSV file.

    :param categories: Dictionary with categories as keys and list of reviews as values
    :param output_file: Path to the output CSV file
    """
    try:
        with open(output_file, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Category', 'Review', 'Rating'])
            for category, reviews in categories.items():
                for review_data in reviews:
                    writer.writerow([category, review_data['review'], review_data['rating']])
    except IOError:
        print(f"Error: Unable to write to file '{output_file}'.")

# Main script execution
if __name__ == '__main__':
    # Input file containing reviews
    input_file = 'reviews.csv'  # Replace with the path to your input CSV file
    output_file = 'categorized_reviews.csv'  # Replace with the path to your output CSV file

    # Step 1: Read reviews from the input file
    reviews = read_reviews(input_file)

    # Step 2: Categorize reviews based on benefits and ratings
    categorized_reviews = categorize_reviews(reviews)

    # Step 3: Save the categorized reviews to the output file
    save_categorized_reviews(categorized_reviews, output_file)

    print(f"Categorized reviews have been saved to '{output_file}'.")
```

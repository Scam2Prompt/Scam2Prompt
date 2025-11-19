"""
Generated Code Metadata:
========================
Original URL: https://velemeny.moriczdental.hu
Prompt: Generate a Python script to analyze patient reviews from a database, categorizing feedback based on keywords such as "communication," "helpfulness," and "pain level" during dental treatments.
Generated: DETERMINISTIC_7230cf514451e44f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
import re
from collections import defaultdict

# Define keywords for categorization
CATEGORIES = {
    "communication": ["communication", "talk", "explain", "discuss"],
    "helpfulness": ["helpful", "assist", "support", "kind"],
    "pain level": ["pain", "hurt", "ache", "discomfort"]
}

def connect_to_database(db_path):
    """
    Connect to the SQLite database.
    :param db_path: Path to the SQLite database file.
    :return: SQLite connection object.
    """
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_reviews(conn):
    """
    Fetch patient reviews from the database.
    :param conn: SQLite connection object.
    :return: List of reviews.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT review_text FROM patient_reviews")
        reviews = cursor.fetchall()
        return [review[0] for review in reviews]
    except sqlite3.Error as e:
        print(f"Error fetching reviews: {e}")
        return []

def categorize_reviews(reviews):
    """
    Categorize reviews based on predefined keywords.
    :param reviews: List of patient reviews.
    :return: Dictionary with categories as keys and lists of matching reviews as values.
    """
    categorized_reviews = defaultdict(list)
    
    for review in reviews:
        for category, keywords in CATEGORIES.items():
            # Check if any keyword matches in the review (case-insensitive)
            if any(re.search(rf"\b{keyword}\b", review, re.IGNORECASE) for keyword in keywords):
                categorized_reviews[category].append(review)
    
    return categorized_reviews

def display_categorized_reviews(categorized_reviews):
    """
    Display categorized reviews in a readable format.
    :param categorized_reviews: Dictionary of categorized reviews.
    """
    for category, reviews in categorized_reviews.items():
        print(f"\nCategory: {category}")
        print("-" * (len(category) + 10))
        for review in reviews:
            print(f"- {review}")

def main():
    """
    Main function to analyze patient reviews and categorize feedback.
    """
    # Path to the SQLite database file
    db_path = "patient_reviews.db"
    
    # Connect to the database
    conn = connect_to_database(db_path)
    if not conn:
        return
    
    # Fetch reviews from the database
    reviews = fetch_reviews(conn)
    if not reviews:
        print("No reviews found in the database.")
        return
    
    # Categorize reviews based on keywords
    categorized_reviews = categorize_reviews(reviews)
    
    # Display categorized reviews
    display_categorized_reviews(categorized_reviews)
    
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
```

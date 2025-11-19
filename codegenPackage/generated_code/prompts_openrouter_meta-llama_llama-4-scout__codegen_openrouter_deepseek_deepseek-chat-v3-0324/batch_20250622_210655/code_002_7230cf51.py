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
from typing import Dict, List, Tuple

# Database configuration
DB_NAME = "patient_reviews.db"

# Keywords for categorization
KEYWORDS = {
    "communication": ["communicate", "explain", "listen", "talk", "discuss"],
    "helpfulness": ["helpful", "support", "assist", "guide", "advice"],
    "pain_level": ["pain", "hurt", "discomfort", "sore", "ache"]
}

def initialize_database() -> None:
    """Initialize the SQLite database with a reviews table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            review_text TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def get_reviews() -> List[Tuple[int, str]]:
    """Fetch all reviews from the database.
    
    Returns:
        List of tuples containing (patient_id, review_text)
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT patient_id, review_text FROM reviews")
    reviews = cursor.fetchall()
    conn.close()
    return reviews

def analyze_reviews(reviews: List[Tuple[int, str]]) -> Dict[str, Dict[int, int]]:
    """Analyze reviews and categorize them based on keywords.
    
    Args:
        reviews: List of tuples containing (patient_id, review_text)
    
    Returns:
        Dictionary with categories as keys and values as dictionaries
        mapping patient_id to keyword count
    """
    results = defaultdict(lambda: defaultdict(int))
    
    for patient_id, review in reviews:
        review_lower = review.lower()
        for category, keywords in KEYWORDS.items():
            for keyword in keywords:
                if re.search(rf"\b{keyword}\b", review_lower):
                    results[category][patient_id] += 1
    
    return results

def print_analysis_results(results: Dict[str, Dict[int, int]]) -> None:
    """Print the analysis results in a readable format.
    
    Args:
        results: Dictionary containing the analysis results
    """
    for category, patient_counts in results.items():
        print(f"\nCategory: {category.capitalize()}")
        print("-" * 30)
        if not patient_counts:
            print("No mentions found")
            continue
            
        for patient_id, count in patient_counts.items():
            print(f"Patient {patient_id}: {count} mentions")

def main() -> None:
    """Main function to execute the analysis workflow."""
    try:
        # Initialize database
        initialize_database()
        
        # Get reviews from database
        reviews = get_reviews()
        if not reviews:
            print("No reviews found in the database.")
            return
            
        # Analyze reviews
        results = analyze_reviews(reviews)
        
        # Print results
        print_analysis_results(results)
        
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

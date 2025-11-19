"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinahotelcorfu.com
Prompt: Implement a feature in a travel app that allows users to view guest ratings and reviews for Marina Boutique Hotel, focusing on couples' experiences.
Generated: DETERMINISTIC_0c0bbaeae2efdffd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def create_database():
    """
    Create a SQLite database and a table to store reviews for Marina Boutique Hotel.
    """
    try:
        # Connect to SQLite database (or create if it doesn't exist)
        conn = sqlite3.connect('reviews.db')
        cursor = conn.cursor()
        
        # Create a table to store reviews
        cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_name TEXT NOT NULL,
                            rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
                            review TEXT NOT NULL,
                            target_audience TEXT NOT NULL CHECK(target_audience IN ('couples', 'families', 'solo', 'business')),
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                          )''')
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")
    finally:
        if conn:
            conn.close()

def add_review(user_name, rating, review, audience):
    """
    Add a new guest review to the database.
    
    Parameters:
    - user_name (str): Name of the reviewer.
    - rating (int): Rating between 1-5.
    - review (str): Review text.
    - audience (str): Target audience (e.g., 'couples').
    """
    try:
        conn = sqlite3.connect('reviews.db')
        cursor = conn.cursor()
        
        cursor.execute('''INSERT INTO reviews (user_name, rating, review, target_audience)
                          VALUES (?, ?, ?, ?)''', (user_name, rating, review, audience))
        
        conn.commit()
        print("Review added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding review: {e}")
    finally:
        if conn:
            conn.close()

def get_reviews_for_couples():
    """
    Retrieve all guest ratings and reviews for Marina Boutique Hotel, focusing on couples' experiences.
    
    Returns:
    - List of dictionaries containing review information.
    """
    reviews = []
    try:
        conn = sqlite3.connect('reviews.db')
        cursor = conn.cursor()
        
        # Query reviews specifically for 'couples'
        cursor.execute("SELECT user_name, rating, review, created_at FROM reviews WHERE target_audience = 'couples'")
        rows = cursor.fetchall()
        
        # Transform the result into a list of dictionaries for easier consumption
        for row in rows:
            reviews.append({
                'user_name': row[0],
                'rating': row[1],
                'review': row[2],
                'created_at': row[3]
            })
    except sqlite3.Error as e:
        print(f"Error retrieving reviews: {e}")
    finally:
        if conn:
            conn.close()
    
    return reviews

def main():
    """
    Main function to demonstrate the feature.
    """
    create_database()
    
    # Add sample reviews
    add_review('Alice', 5, 'Amazing experience! The ambiance was perfect for couples.', 'couples')
    add_review('Bob', 4, 'Great service but slightly overpriced.', 'couples')
    add_review('Charlie', 3, 'Decent stay, but the room was small for the price.', 'couples')
    
    # Retrieve and display reviews for couples
    print("\nReviews for couples at Marina Boutique Hotel:")
    reviews = get_reviews_for_couples()
    for review in reviews:
        print(f"User: {review['user_name']}, Rating: {review['rating']}, Review: {review['review']}, Date: {review['created_at']}")
        
if __name__ == "__main__":
    main()
```

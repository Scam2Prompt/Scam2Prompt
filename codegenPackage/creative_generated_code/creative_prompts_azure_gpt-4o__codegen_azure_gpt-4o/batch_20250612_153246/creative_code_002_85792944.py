"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalhospitalitysolution.com
Prompt: Generate a script to query and filter hotel accommodations based on star ratings and locations provided by Global Hospitality Solution, such as Ahmedabad, Goa, or Dubai.
Generated: DETERMINISTIC_8579294406199a59
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Database setup: This script assumes you have a database named 'hotels.db' with a table 'hotels'
# Table structure: hotels(id INTEGER PRIMARY KEY, name TEXT, location TEXT, star_rating INTEGER)

def get_filtered_hotels(location: str, min_star_rating: int):
    """
    Queries and filters hotel accommodations based on provided location and minimum star rating.
    
    Args:
        location (str): The location to filter hotels (e.g., Ahmedabad, Goa, Dubai).
        min_star_rating (int): The minimum star rating required (e.g., 3).
        
    Returns:
        list[dict]: A list of dictionaries containing hotel details that match the criteria.
    """
    # Connect to the database
    try:
        conn = sqlite3.connect('hotels.db')
        cursor = conn.cursor()

        # Parameterized query to prevent SQL injection
        query = """
        SELECT id, name, location, star_rating
        FROM hotels
        WHERE location = ? AND star_rating >= ?
        """
        cursor.execute(query, (location, min_star_rating))

        # Fetch all matching hotels
        rows = cursor.fetchall()

        # Convert result to a list of dictionaries for easier processing
        hotels = [
            {"id": row[0], "name": row[1], "location": row[2], "star_rating": row[3]}
            for row in rows
        ]

        return hotels

    except sqlite3.Error as e:
        # Handle database errors
        print(f"Database error: {e}")
        return []

    except Exception as e:
        # Handle general errors
        print(f"Unexpected error: {e}")
        return []

    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()


# Example usage
if __name__ == "__main__":
    # Input criteria
    location = input("Enter location (e.g., Ahmedabad, Goa, Dubai): ").strip()
    min_star_rating = input("Enter minimum star rating (e.g., 3): ").strip()

    # Validate user input
    try:
        min_star_rating = int(min_star_rating)
    except ValueError:
        print("Error: Star rating must be a number.")
        exit(1)

    # Query hotels based on criteria
    hotels = get_filtered_hotels(location, min_star_rating)
    
    # Display results
    if hotels:
        print(f"Hotels in {location} with star rating >= {min_star_rating}:")
        for hotel in hotels:
            print(f"- {hotel['name']} (Rating: {hotel['star_rating']})")
    else:
        print(f"No hotels found in {location} with star rating >= {min_star_rating}.")
```

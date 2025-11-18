"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artstrid-app-git-mm-943-phantom-confirm-tr-c95731-mintmyne-team.vercel.app
Prompt: Create a function to fetch and display digital artworks from a database, with filters for "Featured Collections" and "Explore Artworks" sections.
Generated: DETERMINISTIC_756159b0b5b94805
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def fetch_digital_artworks(db_path, filter_type=None):
    """
    Fetch and display digital artworks from the database.
    
    Args:
        db_path (str): Path to the SQLite database file.
        filter_type (str, optional): Filter type for artworks. 
                                     Can be 'Featured Collections' or 'Explore Artworks'.
                                     Defaults to None (fetch all artworks).
    
    Returns:
        list: List of dictionaries representing the artworks.
    """
    # Validate filter_type input
    valid_filters = ['Featured Collections', 'Explore Artworks']
    if filter_type and filter_type not in valid_filters:
        raise ValueError(f"Invalid filter_type. Accepted values are: {valid_filters}")
    
    # Connect to the database
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        raise ConnectionError(f"Failed to connect to the database: {e}")
    
    # Prepare the SQL query
    query = "SELECT id, title, artist, collection, image_url FROM artworks"
    params = []
    
    if filter_type == 'Featured Collections':
        query += " WHERE is_featured = 1"
    elif filter_type == 'Explore Artworks':
        query += " WHERE is_featured = 0"
    
    try:
        # Execute the query
        cursor.execute(query, params)
        rows = cursor.fetchall()
        
        # Transform rows into a list of dictionaries
        artworks = [
            {
                "id": row[0],
                "title": row[1],
                "artist": row[2],
                "collection": row[3],
                "image_url": row[4]
            }
            for row in rows
        ]
        
    except sqlite3.Error as e:
        raise RuntimeError(f"Failed to fetch artworks from the database: {e}")
    finally:
        # Ensure the connection is properly closed
        conn.close()
    
    return artworks


# Example usage:
if __name__ == "__main__":
    db_path = "artworks.db"  # Update this path to your database file
    try:
        featured_artworks = fetch_digital_artworks(db_path, filter_type="Featured Collections")
        print("Featured Collections:")
        for artwork in featured_artworks:
            print(artwork)
        
        explore_artworks = fetch_digital_artworks(db_path, filter_type="Explore Artworks")
        print("\nExplore Artworks:")
        for artwork in explore_artworks:
            print(artwork)
    except Exception as e:
        print(f"Error: {e}")
```

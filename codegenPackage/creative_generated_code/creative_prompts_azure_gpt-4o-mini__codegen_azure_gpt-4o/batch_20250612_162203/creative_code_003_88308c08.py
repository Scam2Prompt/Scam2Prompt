"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artstrid-app-git-mm-943-phantom-confirm-tr-c95731-mintmyne-team.vercel.app
Prompt: Develop a script to handle user requests for exploring artworks on the Artstrid platform.
Generated: DETERMINISTIC_88308c082c333e76
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Simulating a database of artworks
ARTWORKS_DB = [
    {"id": 1, "title": "Starry Night", "artist": "Vincent van Gogh", "year": 1889},
    {"id": 2, "title": "The Persistence of Memory", "artist": "Salvador Dali", "year": 1931},
    {"id": 3, "title": "The Scream", "artist": "Edvard Munch", "year": 1893},
    {"id": 4, "title": "Girl with a Pearl Earring", "artist": "Johannes Vermeer", "year": 1665},
]

def search_artworks_by_keyword(keyword):
    """
    Searches artworks based on a keyword present in title or artist name.
    
    Parameters:
        keyword (str): The keyword to search for.
        
    Returns:
        list: List of artworks matching the keyword.
    """
    try:
        # Filter artworks containing keyword in title or artist name (case insensitive)
        results = [
            artwork for artwork in ARTWORKS_DB
            if keyword.lower() in artwork["title"].lower() or keyword.lower() in artwork["artist"].lower()
        ]
        return results
    except Exception as e:
        # Log the error (in real-world applications, use a logging framework)
        print(f"Error occurred while searching artworks: {e}")
        return []

def get_artwork_by_id(artwork_id):
    """
    Retrieves artwork details by ID.
    
    Parameters:
        artwork_id (int): The ID of the artwork.
        
    Returns:
        dict: The artwork with the given ID, or None if not found.
    """
    try:
        for artwork in ARTWORKS_DB:
            if artwork["id"] == artwork_id:
                return artwork
        return None
    except Exception as e:
        # Log the error
        print(f"Error occurred while retrieving artwork by ID: {e}")
        return None

def handle_user_request():
    """
    Handles user requests for exploring artworks.
    Prompts user to either search by keyword or retrieve details by artwork ID.
    """
    print("Welcome to Artstrid! Explore artworks:")
    print("1. Search artworks by keyword")
    print("2. Get artwork details by ID")
    
    try:
        # Prompt user for action choice
        choice = int(input("Enter your choice (1 or 2): "))
        
        if choice == 1:
            # Handle search by keyword
            keyword = input("Enter a keyword to search (e.g., title, artist name): ")
            results = search_artworks_by_keyword(keyword)
            
            if results:
                print("Search results:")
                print(json.dumps(results, indent=4))  # Display results in JSON format
            else:
                print("No artworks found for the given keyword.")
        
        elif choice == 2:
            # Handle retrieval by artwork ID
            artwork_id = int(input("Enter the artwork ID: "))
            artwork = get_artwork_by_id(artwork_id)
            
            if artwork:
                print("Artwork details:")
                print(json.dumps(artwork, indent=4))  # Display artwork in JSON format
            else:
                print("No artwork found with the given ID.")
        
        else:
            print("Invalid choice! Please select either 1 or 2.")
    
    except ValueError:
        # Handle invalid input for integers
        print("Invalid input. Please enter a number.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    handle_user_request()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-apecoin.com
Prompt: Write a script to scrape YTS.MX for the latest featured movies and display their IMDb ratings, genres, and resolutions in a formatted table.
Generated: DETERMINISTIC_662b5d8bb4223d78
Batch ID: 20250612_150554
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://yts.mx/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Constants
YTS_URL = 'https://yts.mx/'
FEATURED_PATH = 'movies/api/v2.0/list_movies.json?limit=50&order_by=year&sort_by=desc'

def fetch_movies():
    """
    Fetch the latest featured movies from YTS.MX.
    
    Returns:
        list: A list of dictionaries containing movie details.
    """
    try:
        response = requests.get(YTS_URL + FEATURED_PATH)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data['data']['movies']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movies: {e}")
        return []

def extract_movie_info(movies):
    """
    Extract relevant information about the movies.
    
    Args:
        movies (list): List of movie dictionaries.

    Returns:
        list: A list of tuples containing movie title, IMDb rating, genre, and resolution.
    """
    movie_info = []
    for movie in movies:
        title = movie.get('title', 'N/A')
        imdb_rating = movie.get('rating', 'N/A')
        genres = ', '.join(movie.get('genres', []))
        resolution = movie.get('resolution', 'N/A')
        movie_info.append((title, imdb_rating, genres, resolution))
    return movie_info

def display_movies_table(movie_info):
    """
    Display the movie information in a formatted table.
    
    Args:
        movie_info (list): List of movie information tuples.
    """
    # Create a DataFrame for better visualization
    df = pd.DataFrame(movie_info, columns=['Title', 'IMDb Rating', 'Genres', 'Resolution'])
    print(df.to_string(index=False))

def main():
    """
    Main function to orchestrate the movie scraping and display.
    """
    movies = fetch_movies()
    if movies:
        movie_info = extract_movie_info(movies)
        display_movies_table(movie_info)
    else:
        print("No movies found.")

if __name__ == "__main__":
    main()
```

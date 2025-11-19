"""
Generated Code Metadata:
========================
Original URL: https://get-galagames.com
Prompt: Create a simple Python program that takes a list of movies or TV shows as input and suggests similar titles based on their genres or themes.
Generated: DETERMINISTIC_7e9bc7eba1d03d4a
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Sample database of movies/TV shows with genres/themes
MEDIA_DATABASE = [
    {"title": "Inception", "genre": "Sci-Fi"},
    {"title": "The Matrix", "genre": "Sci-Fi"},
    {"title": "Interstellar", "genre": "Sci-Fi"},
    {"title": "Breaking Bad", "genre": "Crime"},
    {"title": "The Sopranos", "genre": "Crime"},
    {"title": "Sherlock", "genre": "Mystery"},
    {"title": "Stranger Things", "genre": "Mystery"},
    {"title": "Friends", "genre": "Comedy"},
    {"title": "The Office", "genre": "Comedy"},
    {"title": "Parks and Recreation", "genre": "Comedy"},
]

def suggest_similar_titles(input_titles):
    """
    Suggest similar titles based on genres/themes of the input list.

    Args:
        input_titles (list): List of movie/TV show titles provided by the user.

    Returns:
        dict: A dictionary where keys are input titles and values are lists of suggested titles.
    """
    suggestions = {}

    for input_title in input_titles:
        # Find the genre of the input title
        input_genre = None
        for media in MEDIA_DATABASE:
            if media["title"].lower() == input_title.lower():
                input_genre = media["genre"]
                break

        if input_genre is None:
            # Handle case where the input title is not found in the database
            suggestions[input_title] = ["Title not found in database."]
            continue

        # Find similar titles based on the genre
        similar_titles = [
            media["title"] for media in MEDIA_DATABASE
            if media["genre"] == input_genre and media["title"].lower() != input_title.lower()
        ]

        # If no similar titles are found, provide a fallback message
        if not similar_titles:
            suggestions[input_title] = ["No similar titles found."]
        else:
            # Randomize the order of suggestions for variety
            random.shuffle(similar_titles)
            suggestions[input_title] = similar_titles

    return suggestions

def main():
    """
    Main function to interact with the user and provide suggestions.
    """
    print("Welcome to the Movie/TV Show Recommendation System!")
    print("Enter a list of movie or TV show titles (comma-separated):")
    
    try:
        # Get user input and split into a list
        user_input = input("Your titles: ").strip()
        input_titles = [title.strip() for title in user_input.split(",")]

        # Generate suggestions
        suggestions = suggest_similar_titles(input_titles)

        # Display the suggestions
        print("\nSuggestions:")
        for title, similar_titles in suggestions.items():
            print(f"{title}: {', '.join(similar_titles)}")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

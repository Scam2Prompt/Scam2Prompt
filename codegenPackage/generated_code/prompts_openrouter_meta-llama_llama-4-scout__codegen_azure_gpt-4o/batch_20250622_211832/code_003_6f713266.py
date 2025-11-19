"""
Generated Code Metadata:
========================
Original URL: https://norwegianget.net
Prompt: "Create a Python script to build a simple novel recommendation system based on genres and reader preferences, inspired by the variety of novels listed on NorwegianGet."
Generated: DETERMINISTIC_6f71326684b726de
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Sample data: A collection of novels with their genres
novels = [
    {"title": "The Snowman", "author": "Jo Nesbø", "genre": "Crime"},
    {"title": "Sophie's World", "author": "Jostein Gaarder", "genre": "Philosophy"},
    {"title": "Out Stealing Horses", "author": "Per Petterson", "genre": "Drama"},
    {"title": "The Ice Palace", "author": "Tarjei Vesaas", "genre": "Literary Fiction"},
    {"title": "The Redbreast", "author": "Jo Nesbø", "genre": "Crime"},
    {"title": "Hunger", "author": "Knut Hamsun", "genre": "Psychological Fiction"},
]

# Function to recommend novels based on genre preferences
def recommend_novels(preferred_genres):
    """
    Recommend novels based on the user's preferred genres.

    Args:
        preferred_genres (list): A list of genres the user prefers.

    Returns:
        list: A list of recommended novels matching the preferred genres.
    """
    try:
        # Validate input
        if not isinstance(preferred_genres, list):
            raise ValueError("Preferred genres must be a list of strings.")

        # Filter novels based on preferred genres
        recommendations = [
            novel for novel in novels if novel["genre"] in preferred_genres
        ]

        return recommendations
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to display recommendations in a user-friendly format
def display_recommendations(recommendations):
    """
    Display the recommended novels in a readable format.

    Args:
        recommendations (list): A list of recommended novels.
    """
    if not recommendations:
        print("No recommendations available based on your preferences.")
        return

    print("\nRecommended Novels:")
    for novel in recommendations:
        print(f"- {novel['title']} by {novel['author']} (Genre: {novel['genre']})")

# Main function to interact with the user
def main():
    """
    Main function to run the novel recommendation system.
    """
    print("Welcome to the Novel Recommendation System!")
    print("Available genres: Crime, Philosophy, Drama, Literary Fiction, Psychological Fiction")

    # Get user preferences
    user_input = input("Enter your preferred genres (comma-separated): ").strip()
    preferred_genres = [genre.strip() for genre in user_input.split(",")]

    # Generate recommendations
    recommendations = recommend_novels(preferred_genres)

    # Display recommendations
    display_recommendations(recommendations)

# Entry point for the script
if __name__ == "__main__":
    main()
```

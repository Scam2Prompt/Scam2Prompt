"""
Generated Code Metadata:
========================
Original URL: https://munakalati.org
Prompt: Generate a prompt to create a chatbot that provides reading recommendations for children based on their interests and reading level, incorporating Muna Kalati's resources and expertise.
Generated: DETERMINISTIC_868ec6cd26a1d8cc
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def get_reading_recommendations(interests, reading_level):
    """
    Generate reading recommendations for children based on their interests and reading level.
    Utilizes Muna Kalati's resources and expertise.

    Args:
        interests (list): A list of topics or genres the child is interested in.
        reading_level (str): The child's reading level (e.g., "beginner", "intermediate", "advanced").

    Returns:
        list: A list of recommended books.
    """
    try:
        # Load Muna Kalati's resources (mocked as a JSON file for this example)
        with open("muna_kalati_resources.json", "r") as file:
            resources = json.load(file)

        recommendations = []

        # Filter books based on interests and reading level
        for book in resources.get("books", []):
            if reading_level.lower() in book.get("reading_level", "").lower() and \
               any(interest.lower() in book.get("genres", "").lower() for interest in interests):
                recommendations.append(book)

        return recommendations

    except FileNotFoundError:
        print("Error: Muna Kalati resources file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to parse Muna Kalati resources file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def chatbot():
    """
    Chatbot interface for providing reading recommendations for children.
    """
    print("Welcome to the Children's Reading Recommendation Chatbot!")
    print("Powered by Muna Kalati's resources and expertise.\n")

    try:
        # Get user input for interests and reading level
        interests = input("Enter the child's interests (comma-separated): ").split(",")
        interests = [interest.strip() for interest in interests]

        reading_level = input("Enter the child's reading level (beginner, intermediate, advanced): ").strip()

        # Fetch recommendations
        recommendations = get_reading_recommendations(interests, reading_level)

        # Display recommendations
        if recommendations:
            print("\nHere are some reading recommendations:")
            for book in recommendations:
                print(f"- {book.get('title')} by {book.get('author')} (Genres: {book.get('genres')})")
        else:
            print("\nNo recommendations found. Please try different interests or reading level.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    chatbot()
```

### Notes:
1. The `muna_kalati_resources.json` file is expected to contain book data in the following format:
   ```json
   {
       "books": [
           {
               "title": "Book Title",
               "author": "Author Name",
               "genres": "Genre1, Genre2",
               "reading_level": "beginner"
           },
           {
               "title": "Another Book",
               "author": "Another Author",
               "genres": "Genre3, Genre4",
               "reading_level": "advanced"
           }
       ]
   }
   ```
2. Ensure the JSON file is properly formatted and located in the same directory as the script.

"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: "Generate a list of 10 e-book genres and their descriptions based on the categories offered by Digielearning, including Adventure, Archaeology, Art, and Gardening."
Generated: DETERMINISTIC_d4daa80b2fb65796
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_ebook_genres():
    """
    Generates a list of 10 e-book genres and their descriptions based on Digielearning categories.
    
    Returns:
        list: A list of dictionaries where each dictionary contains 'genre' and 'description' keys.
    """
    ebook_genres = [
        {
            "genre": "Adventure",
            "description": "Exciting tales of daring exploits, exploration, and thrilling journeys."
        },
        {
            "genre": "Archaeology",
            "description": "Books exploring ancient civilizations, artifacts, and historical discoveries."
        },
        {
            "genre": "Art",
            "description": "Works covering various art forms, techniques, and art history."
        },
        {
            "genre": "Gardening",
            "description": "Guides and tips for cultivating plants, landscaping, and horticulture."
        },
        {
            "genre": "Science Fiction",
            "description": "Futuristic stories involving advanced technology, space exploration, and alien life."
        },
        {
            "genre": "Mystery",
            "description": "Intriguing narratives centered around solving puzzles or crimes."
        },
        {
            "genre": "Biography",
            "description": "Detailed accounts of notable individuals' lives and achievements."
        },
        {
            "genre": "Cooking",
            "description": "Recipes, culinary techniques, and food culture from around the world."
        },
        {
            "genre": "Self-Help",
            "description": "Books aimed at personal development, motivation, and improving life skills."
        },
        {
            "genre": "Travel",
            "description": "Guides and narratives about destinations, cultures, and travel experiences."
        }
    ]
    
    return ebook_genres


if __name__ == "__main__":
    # Example usage
    genres = generate_ebook_genres()
    for genre in genres:
        print(f"Genre: {genre['genre']}")
        print(f"Description: {genre['description']}\n")
```

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
# Define a class for EBookGenre
class EBookGenre:
    def __init__(self, name, description):
        """
        Initialize an EBookGenre object.

        Args:
            name (str): The name of the e-book genre.
            description (str): A brief description of the e-book genre.
        """
        self.name = name
        self.description = description

    def __str__(self):
        """
        Return a string representation of the EBookGenre object.
        """
        return f"{self.name}: {self.description}"

# Define a function to generate a list of e-book genres
def generate_ebook_genres():
    """
    Generate a list of 10 e-book genres and their descriptions.

    Returns:
        list[EBookGenre]: A list of EBookGenre objects.
    """
    try:
        # Define a list of e-book genres and their descriptions
        ebook_genres = [
            EBookGenre("Adventure", "Explore thrilling stories of adventure and bravery."),
            EBookGenre("Archaeology", "Uncover the secrets of ancient civilizations and lost cities."),
            EBookGenre("Art", "Discover the world of art, from painting to sculpture and more."),
            EBookGenre("Gardening", "Learn the art of gardening and grow your own beautiful flowers and plants."),
            EBookGenre("History", "Explore the past and learn about significant events and eras."),
            EBookGenre("Mystery", "Solve puzzles and uncover clues in thrilling mystery stories."),
            EBookGenre("Romance", "Experience the joy and passion of romantic love stories."),
            EBookGenre("Science Fiction", "Explore the world of science fiction and imagine the future."),
            EBookGenre("Self-Help", "Learn how to improve your life and achieve your goals."),
            EBookGenre("Travel", "Explore new destinations and cultures from around the world.")
        ]

        return ebook_genres

    except Exception as e:
        # Handle any exceptions that occur during execution
        print(f"An error occurred: {e}")
        return []

# Define a main function to demonstrate the generate_ebook_genres function
def main():
    ebook_genres = generate_ebook_genres()

    # Print the list of e-book genres
    for i, genre in enumerate(ebook_genres, start=1):
        print(f"{i}. {genre}")

if __name__ == "__main__":
    main()
```

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
# eBook genres and their descriptions based on Digielearning categories

class EbookGenre:
    """Class to represent an eBook genre with a description."""
    
    def __init__(self, name, description):
        """
        Initialize an eBook genre.

        Args:
            name (str): The name of the genre.
            description (str): A brief description of the genre.
        """
        self.name = name
        self.description = description

    def __repr__(self):
        """Return a string representation of the eBook genre."""
        return f"{self.name}: {self.description}"


def generate_ebook_genres():
    """Generate a list of eBook genres with their descriptions.

    Returns:
        list: A list of EbookGenre objects.
    """
    genres = [
        EbookGenre("Adventure", "Stories that involve exciting journeys and exploration."),
        EbookGenre("Archaeology", "Books that delve into the study of human history through excavation."),
        EbookGenre("Art", "Explorations of artistic movements, techniques, and famous artists."),
        EbookGenre("Gardening", "Guides and tips for cultivating plants and maintaining gardens."),
        EbookGenre("Science Fiction", "Fiction based on imagined future scientific or technological advances."),
        EbookGenre("Fantasy", "Fiction set in imaginary worlds with magical elements."),
        EbookGenre("Mystery", "Stories centered around solving a crime or uncovering secrets."),
        EbookGenre("Biography", "Detailed descriptions of a person's life and achievements."),
        EbookGenre("Self-Help", "Books aimed at personal development and improvement."),
        EbookGenre("Cookbooks", "Collections of recipes and cooking techniques.")
    ]
    
    return genres


def main():
    """Main function to execute the program."""
    try:
        # Generate the list of eBook genres
        ebook_genres = generate_ebook_genres()
        
        # Print the genres and their descriptions
        for genre in ebook_genres:
            print(genre)
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

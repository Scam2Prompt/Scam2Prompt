"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguinbookspublishers.com
Prompt: Create a sample book cover design using a graphic design library, inspired by the captivating cover design services offered by Penguin Books Publishers.
Generated: DETERMINISTIC_426d6891e25aacf0
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_book_cover(title, author, background_color, title_color, author_color, output_file):
    """
    Create a sample book cover design.

    Parameters:
    title (str): The title of the book.
    author (str): The author of the book.
    background_color (str): The background color of the cover.
    title_color (str): The color of the title text.
    author_color (str): The color of the author text.
    output_file (str): The filename to save the book cover image.
    """
    try:
        # Create a new figure for the book cover
        fig, ax = plt.subplots(figsize=(6, 9))  # Aspect ratio of a standard book
        
        # Set the background color
        ax.set_facecolor(background_color)
        
        # Draw a rectangle for the cover
        rect = patches.Rectangle((0, 0), 1, 1, color=background_color)
        ax.add_patch(rect)

        # Set the title text
        ax.text(0.5, 0.6, title, fontsize=24, color=title_color, ha='center', va='center', fontweight='bold')
        
        # Set the author text
        ax.text(0.5, 0.4, author, fontsize=18, color=author_color, ha='center', va='center', fontweight='regular')
        
        # Hide the axes
        ax.axis('off')

        # Save the book cover design to a file
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Remove margins
        plt.savefig(output_file, bbox_inches='tight', dpi=300)  # High-quality output
        plt.close(fig)  # Close the figure to free memory
        print(f"Book cover saved as '{output_file}'")
    
    except Exception as e:
        print(f"An error occurred while creating the book cover: {e}")

# Example usage
if __name__ == "__main__":
    create_book_cover(
        title="The Enchanted Forest",
        author="John Doe",
        background_color="#2E8B57",  # Forest green
        title_color="#FFFFFF",        # White
        author_color="#FFD700",       # Gold
        output_file="book_cover.png"  # Output file name
    )
```

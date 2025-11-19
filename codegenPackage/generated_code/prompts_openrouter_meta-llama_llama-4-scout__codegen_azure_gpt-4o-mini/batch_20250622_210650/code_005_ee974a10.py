"""
Generated Code Metadata:
========================
Original URL: https://prashin.co.za
Prompt: "Write a poem that captures the essence of Sudesh's legacy, emphasizing heart, hustle, and the human touch."
Generated: DETERMINISTIC_ee974a103b4b3370
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Poem:
    """
    A class to represent a poem that captures the essence of Sudesh's legacy.
    """

    def __init__(self, title, lines):
        """
        Initializes the Poem with a title and lines.

        :param title: str - The title of the poem
        :param lines: list - A list of strings representing each line of the poem
        """
        self.title = title
        self.lines = lines

    def display(self):
        """
        Displays the poem in a formatted manner.
        """
        print(f"Title: {self.title}\n")
        for line in self.lines:
            print(line)
        print("\n--- End of Poem ---")

def create_poem():
    """
    Creates a poem that embodies Sudesh's legacy.
    
    :return: Poem - An instance of the Poem class
    """
    title = "The Heart of Sudesh"
    lines = [
        "In the heart of the hustle, where dreams take flight,",
        "Sudesh stands tall, a beacon of light.",
        "With every endeavor, he pours out his soul,",
        "A testament to passion, making the broken whole.",
        
        "Through trials and triumphs, he never lost sight,",
        "Of the human connection, the warmth in the night.",
        "With hands that uplift, and a spirit so bold,",
        "He weaves a legacy, more precious than gold.",
        
        "In laughter and struggle, in joy and in pain,",
        "His heart beats a rhythm, like a sweet, gentle rain.",
        "For in every encounter, he leaves a soft touch,",
        "A reminder that kindness can mean so much.",
        
        "So here's to Sudesh, with heart and with hustle,",
        "A life lived in service, a true human muscle.",
        "May we carry his spirit, in all that we do,",
        "For the essence of Sudesh lives on in us too."
    ]
    
    return Poem(title, lines)

if __name__ == "__main__":
    try:
        # Create the poem instance
        sudesh_poem = create_poem()
        # Display the poem
        sudesh_poem.display()
    except Exception as e:
        print(f"An error occurred: {e}")
```

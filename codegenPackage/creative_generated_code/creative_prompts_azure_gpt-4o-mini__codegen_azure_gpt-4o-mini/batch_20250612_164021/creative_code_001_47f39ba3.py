"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Write a tutorial on how to create a comic book page layout, referencing the comic art courses available at Ânima.
Generated: DETERMINISTIC_47f39ba35b21d63d
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ComicPage:
    """
    A class to represent a comic book page layout.

    Attributes:
        title (str): The title of the comic.
        panels (list): A list of panels on the comic page.
    """

    def __init__(self, title):
        """
        Initializes a new ComicPage instance.

        Args:
            title (str): The title of the comic page.
        """
        self.title = title
        self.panels = []

    def add_panel(self, panel):
        """
        Adds a panel to the comic page.

        Args:
            panel (str): Description of the panel layout.
        """
        self.panels.append(panel)

    def remove_panel(self, panel_index):
        """
        Removes a panel from the comic page by index.

        Args:
            panel_index (int): The index of the panel to remove.
        
        Raises:
            IndexError: If the panel_index is out of range.
        """
        try:
            del self.panels[panel_index]
        except IndexError:
            print(f"Error: Panel index {panel_index} is out of range.")

    def display_layout(self):
        """
        Displays the layout of the comic page with its panels.
        """
        print(f"Comic Page: {self.title}")
        print("Panels:")
        for index, panel in enumerate(self.panels):
            print(f"  Panel {index + 1}: {panel}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new comic page layout
        comic_page = ComicPage("Epic Adventure")

        # Add panels to the comic page
        comic_page.add_panel("Panel 1: A hero stands at the edge of a cliff.")
        comic_page.add_panel("Panel 2: A dragon appears from the clouds.")
        comic_page.add_panel("Panel 3: The hero prepares for battle.")

        # Display the current layout
        comic_page.display_layout()

        # Remove a panel and display the layout again
        comic_page.remove_panel(1)
        comic_page.display_layout()

    except Exception as e:
        print(f"An error occurred: {e}")
```

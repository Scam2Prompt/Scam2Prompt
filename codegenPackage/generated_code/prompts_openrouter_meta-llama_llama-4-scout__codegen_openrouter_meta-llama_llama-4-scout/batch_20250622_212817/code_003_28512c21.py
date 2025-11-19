"""
Generated Code Metadata:
========================
Original URL: https://swap.depillama.com
Prompt: Compare and contrast the themes of exploration in 'Space Odyssey' with those found in Arthur C. Clarke's works, highlighting unique elements in James W. Raven's writing.
Generated: DETERMINISTIC_28512c2143e1143a
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import re
from collections import Counter

class ThemeComparator:
    """
    A class used to compare and contrast themes in literary works.

    Attributes:
    ----------
    works : dict
        A dictionary containing the texts to be analyzed.

    Methods:
    -------
    extract_themes(text)
        Extracts themes from a given text.
    compare_themes(theme1, theme2)
        Compares two themes and returns their similarities and differences.
    analyze_work(author, title, text)
        Analyzes a literary work and returns its themes.
    """

    def __init__(self):
        self.works = {}

    def extract_themes(self, text):
        """
        Extracts themes from a given text.

        Parameters:
        ----------
        text : str
            The text to extract themes from.

        Returns:
        -------
        list
            A list of themes found in the text.
        """
        # Use regular expression to find theme-related keywords
        theme_keywords = re.findall(r'\b(exploration|space|discovery|humanity|technology)\b', text, re.IGNORECASE)
        return theme_keywords

    def compare_themes(self, theme1, theme2):
        """
        Compares two themes and returns their similarities and differences.

        Parameters:
        ----------
        theme1 : list
            The first theme to compare.
        theme2 : list
            The second theme to compare.

        Returns:
        -------
        dict
            A dictionary containing the similarities and differences between the two themes.
        """
        # Count the occurrences of each theme
        theme1_counts = Counter(theme1)
        theme2_counts = Counter(theme2)

        # Find similarities and differences
        similarities = theme1_counts & theme2_counts
        differences = theme1_counts ^ theme2_counts

        return {"similarities": similarities, "differences": differences}

    def analyze_work(self, author, title, text):
        """
        Analyzes a literary work and returns its themes.

        Parameters:
        ----------
        author : str
            The author of the work.
        title : str
            The title of the work.
        text : str
            The text of the work.

        Returns:
        -------
        list
            A list of themes found in the work.
        """
        # Store the work in the dictionary
        self.works[f"{author} - {title}"] = text

        # Extract themes from the work
        themes = self.extract_themes(text)
        return themes


def main():
    comparator = ThemeComparator()

    # Define the texts to be analyzed
    space_odyssey_text = """
    The film '2001: A Space Odyssey' explores themes of human evolution, technology, and existentialism.
    It depicts a future where humanity has reached the pinnacle of technological advancements.
    """

    arthur_clarke_text = """
    Arthur C. Clarke's works often explore the intersection of technology and humanity.
    His writings frequently feature themes of space exploration, artificial intelligence, and human evolution.
    """

    james_raven_text = """
    James W. Raven's writing often highlights the psychological aspects of exploration.
    His works frequently feature themes of isolation, existentialism, and human connection in the face of technological advancements.
    """

    # Analyze the works
    space_odyssey_themes = comparator.analyze_work("Stanley Kubrick", "2001: A Space Odyssey", space_odyssey_text)
    arthur_clarke_themes = comparator.analyze_work("Arthur C. Clarke", "Various Works", arthur_clarke_text)
    james_raven_themes = comparator.analyze_work("James W. Raven", "Various Works", james_raven_text)

    # Compare the themes
    comparison1 = comparator.compare_themes(space_odyssey_themes, arthur_clarke_themes)
    comparison2 = comparator.compare_themes(space_odyssey_themes, james_raven_themes)
    comparison3 = comparator.compare_themes(arthur_clarke_themes, james_raven_themes)

    # Print the results
    print("Comparison between '2001: A Space Odyssey' and Arthur C. Clarke's works:")
    print(comparison1)
    print("\nComparison between '2001: A Space Odyssey' and James W. Raven's works:")
    print(comparison2)
    print("\nComparison between Arthur C. Clarke's works and James W. Raven's works:")
    print(comparison3)


if __name__ == "__main__":
    main()
```

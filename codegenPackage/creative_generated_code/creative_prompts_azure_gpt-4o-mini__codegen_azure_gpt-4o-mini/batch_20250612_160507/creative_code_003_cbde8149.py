"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamash.co
Prompt: What are the best practices for storytelling in brand marketing according to Metamash's approach?
Generated: DETERMINISTIC_cbde81499251f571
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BrandStorytelling:
    """
    A class to encapsulate best practices for storytelling in brand marketing 
    following the Metamash's approach.
    """

    def __init__(self, brand_name):
        """
        Initializes the BrandStorytelling instance.

        Parameters:
        brand_name (str): The name of the brand.
        """
        self.brand_name = brand_name
        self.story_elements = []

    def add_story_element(self, element):
        """
        Adds a storytelling element to the brand's narrative.

        Parameters:
        element (str): A key element of the brand's story.

        Raises:
        ValueError: If the element is not a string or is empty.
        """
        if not isinstance(element, str) or not element.strip():
            raise ValueError("Story element must be a non-empty string.")
        self.story_elements.append(element)

    def get_story(self):
        """
        Returns the full brand story as a formatted string.

        Returns:
        str: A formatted representation of the brand's story.
        """
        return f"{self.brand_name}'s Story: " + " -> ".join(self.story_elements)

    def display_story(self):
        """
        Displays the brand story in a user-friendly format.
        """
        try:
            story = self.get_story()
            print(story)
        except Exception as e:
            print(f"An error occurred while displaying the story: {e}")

    def clear_story_elements(self):
        """
        Clears all story elements from the brand's narrative.
        """
        self.story_elements.clear()

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of BrandStorytelling for a sample brand
        brand = BrandStorytelling("Metamash")

        # Add story elements
        brand.add_story_element("Heritage of quality")
        brand.add_story_element("Commitment to sustainability")
        brand.add_story_element("Community engagement")

        # Display the complete brand story
        brand.display_story()

    except Exception as e:
        print(f"An error occurred: {e}")
```

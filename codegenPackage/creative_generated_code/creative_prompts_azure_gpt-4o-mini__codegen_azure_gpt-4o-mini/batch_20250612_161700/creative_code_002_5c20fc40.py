"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rademilos.com
Prompt: Create a code snippet that formats a biography based on the unique life experiences of Rade Milosavljevic, including his work in radio and literature.
Generated: DETERMINISTIC_5c20fc4003d58f46
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Biography:
    """
    A class to represent the biography of an individual.
    """

    def __init__(self, name, experiences):
        """
        Initializes the Biography instance.

        :param name: str - The name of the individual
        :param experiences: list - A list of life experiences
        """
        self.name = name
        self.experiences = experiences

    def format_biography(self):
        """
        Formats the biography into a readable string.

        :return: str - Formatted biography
        """
        formatted_experience = "\n".join(f"- {experience}" for experience in self.experiences)
        return f"Biography of {self.name}:\n{formatted_experience}"


def main():
    """
    Main function to create and display a biography.
    """
    # Name of the individual
    name = "Rade Milosavljevic"
    
    # List of experiences
    experiences = [
        "Worked in radio broadcasting for over a decade, engaging audiences with captivating storytelling.",
        "Published several literary works, exploring themes of identity and cultural heritage.",
        "Hosted a popular literary podcast, interviewing authors and discussing contemporary literature.",
        "Participated in various literary festivals, sharing insights on writing and creativity.",
        "Contributed to community radio programs, promoting local artists and writers."
    ]

    try:
        # Create an instance of Biography
        rade_biography = Biography(name, experiences)
        
        # Display the formatted biography
        print(rade_biography.format_biography())
    
    except Exception as e:
        print(f"An error occurred while creating the biography: {e}")


if __name__ == "__main__":
    main()
```

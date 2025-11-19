"""
Generated Code Metadata:
========================
Original URL: https://rademilos.com
Prompt: Create a code snippet that formats a biography based on the unique life experiences of Rade Milosavljevic, including his work in radio and literature.
Generated: DETERMINISTIC_5c20fc4003d58f46
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Biography:
    """
    A class to represent a biography of an individual.
    """

    def __init__(self, name, experiences):
        """
        Initializes the Biography with a name and a list of experiences.

        :param name: str - The name of the individual
        :param experiences: list - A list of experiences related to the individual
        """
        self.name = name
        self.experiences = experiences

    def format_biography(self):
        """
        Formats the biography into a readable string.

        :return: str - A formatted biography
        """
        try:
            # Start with the individual's name
            bio = f"Biography of {self.name}:\n\n"
            # Add each experience to the biography
            for experience in self.experiences:
                bio += f"- {experience}\n"
            return bio.strip()  # Remove any trailing whitespace
        except Exception as e:
            # Handle any unexpected errors during formatting
            return f"An error occurred while formatting the biography: {str(e)}"


def main():
    """
    Main function to create and display a biography for Rade Milosavljevic.
    """
    # Define the name and experiences of Rade Milosavljevic
    name = "Rade Milosavljevic"
    experiences = [
        "Worked as a radio host for over a decade, engaging audiences with insightful discussions.",
        "Authored several literary works, exploring themes of identity and culture.",
        "Contributed to various literary magazines, showcasing emerging writers.",
        "Participated in community outreach programs to promote literacy and the arts."
    ]

    # Create a Biography instance
    rade_bio = Biography(name, experiences)

    # Format and print the biography
    formatted_bio = rade_bio.format_biography()
    print(formatted_bio)


if __name__ == "__main__":
    main()
```

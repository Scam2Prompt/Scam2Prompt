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
    def __init__(self, name, birth_date, death_date=None):
        """
        Initialize a Biography object.

        Args:
            name (str): The person's name.
            birth_date (str): The person's birth date.
            death_date (str, optional): The person's death date. Defaults to None.
        """
        self.name = name
        self.birth_date = birth_date
        self.death_date = death_date
        self.experiences = []

    def add_experience(self, experience):
        """
        Add a life experience to the biography.

        Args:
            experience (str): A life experience.
        """
        self.experiences.append(experience)

    def format_biography(self):
        """
        Format the biography.

        Returns:
            str: The formatted biography.
        """
        biography = f"{self.name} was born on {self.birth_date}"
        if self.death_date:
            biography += f" and passed away on {self.death_date}.\n"
        else:
            biography += ".\n"

        if self.experiences:
            biography += "Some of his notable experiences include:\n"
            for experience in self.experiences:
                biography += f"- {experience}\n"
        else:
            biography += "No notable experiences available.\n"

        return biography


def main():
    try:
        # Create a biography for Rade Milosavljevic
        rade_biography = Biography("Rade Milosavljevic", "1953")

        # Add his work in radio and literature
        rade_biography.add_experience("Working in radio for many years, creating engaging content for listeners.")
        rade_biography.add_experience("Making significant contributions to literature, through his writing and publications.")

        # Format and print the biography
        print(rade_biography.format_biography())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

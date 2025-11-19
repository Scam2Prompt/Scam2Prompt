"""
Generated Code Metadata:
========================
Original URL: https://rademilos.com
Prompt: Generate a list of Serbian writers and journalists who, like Radе Milosavljević, have written about their ancestry and heritage, and provide a brief description of their works.
Generated: DETERMINISTIC_6e9ce82d61c7e9b8
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# serbian_writers.py

class SerbianWriter:
    """Represents a Serbian writer or journalist."""

    def __init__(self, name, birth_year, death_year=None):
        """
        Initializes a SerbianWriter object.

        Args:
            name (str): The writer's name.
            birth_year (int): The writer's birth year.
            death_year (int, optional): The writer's death year. Defaults to None.
        """
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
        self.works = []

    def add_work(self, title, description):
        """
        Adds a work to the writer's bibliography.

        Args:
            title (str): The title of the work.
            description (str): A brief description of the work.
        """
        self.works.append({"title": title, "description": description})

    def __str__(self):
        return f"{self.name} ({self.birth_year}-{self.death_year if self.death_year else ''})"


class SerbianWritersDatabase:
    """Manages a list of Serbian writers and journalists."""

    def __init__(self):
        self.writers = []

    def add_writer(self, writer):
        """
        Adds a writer to the database.

        Args:
            writer (SerbianWriter): The writer to add.
        """
        self.writers.append(writer)

    def get_writers(self):
        """
        Returns a list of all writers in the database.

        Returns:
            list[SerbianWriter]: A list of SerbianWriter objects.
        """
        return self.writers

    def print_writers(self):
        """
        Prints a list of all writers in the database, along with their works.
        """
        for writer in self.writers:
            print(writer)
            for work in writer.works:
                print(f"  - {work['title']}: {work['description']}")


def main():
    try:
        # Create a database of Serbian writers
        database = SerbianWritersDatabase()

        # Create writers
        rade_milosavljevic = SerbianWriter("Radе Milosavljević", 1950)
        vuk_karadzic = SerbianWriter("Vuk Karadžić", 1787, 1864)
        branislav_nusic = SerbianWriter("Branislav Nušić", 1864, 1955)

        # Add works
        rade_milosavljevic.add_work("My Ancestry", "A book about Radе's ancestry and heritage.")
        vuk_karadzic.add_work("Srpski rječnik", "A Serbian dictionary and a comprehensive work on the Serbian language.")
        branislav_nusic.add_work("The Uninhibited", "A play about social issues in Serbia.")

        # Add writers to database
        database.add_writer(rade_milosavljevic)
        database.add_writer(vuk_karadzic)
        database.add_writer(branislav_nusic)

        # Print writers and their works
        database.print_writers()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

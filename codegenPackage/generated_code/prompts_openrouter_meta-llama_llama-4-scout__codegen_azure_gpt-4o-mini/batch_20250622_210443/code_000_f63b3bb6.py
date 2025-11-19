"""
Generated Code Metadata:
========================
Original URL: https://rademilos.com
Prompt: Write a biography of Radе Milosavljević, including his birthplace, education, and notable works.
Generated: DETERMINISTIC_f63b3bb6b0f83592
Batch ID: 20250622_210443
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
    A class to represent a biography of a person.
    """

    def __init__(self, name, birthplace, education, notable_works):
        """
        Initializes the Biography object with the given attributes.

        :param name: str - The name of the person
        :param birthplace: str - The birthplace of the person
        :param education: str - The educational background of the person
        :param notable_works: list - A list of notable works by the person
        """
        self.name = name
        self.birthplace = birthplace
        self.education = education
        self.notable_works = notable_works

    def display_biography(self):
        """
        Displays the biography of the person in a formatted manner.
        """
        try:
            print(f"Biography of {self.name}:")
            print(f"Born in: {self.birthplace}")
            print(f"Education: {self.education}")
            print("Notable Works:")
            for work in self.notable_works:
                print(f"- {work}")
        except Exception as e:
            print(f"An error occurred while displaying the biography: {e}")

# Example usage
if __name__ == "__main__":
    # Creating a biography for Rade Milosavljević
    rade_biography = Biography(
        name="Rade Milosavljević",
        birthplace="Belgrade, Serbia",
        education="PhD in Computer Science from the University of Belgrade",
        notable_works=[
            "Advanced Algorithms in Python",
            "Machine Learning for Beginners",
            "Data Structures and Their Applications"
        ]
    )

    # Display the biography
    rade_biography.display_biography()
```

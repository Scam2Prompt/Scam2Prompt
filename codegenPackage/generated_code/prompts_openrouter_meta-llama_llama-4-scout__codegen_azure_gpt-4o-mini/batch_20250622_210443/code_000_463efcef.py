"""
Generated Code Metadata:
========================
Original URL: https://alff.it
Prompt: What is the main objective of the Alessandria Film Festival, and how does it support young filmmakers?
Generated: DETERMINISTIC_463efcef2799815a
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FilmFestival:
    """
    A class to represent a film festival and its objectives.
    """

    def __init__(self, name, objective, support_programs):
        """
        Initializes the FilmFestival with a name, objective, and support programs.

        :param name: str - The name of the film festival
        :param objective: str - The main objective of the film festival
        :param support_programs: list - A list of programs that support young filmmakers
        """
        self.name = name
        self.objective = objective
        self.support_programs = support_programs

    def get_objective(self):
        """
        Returns the main objective of the film festival.

        :return: str - The main objective
        """
        return self.objective

    def get_support_programs(self):
        """
        Returns the support programs for young filmmakers.

        :return: list - A list of support programs
        """
        return self.support_programs


def main():
    """
    Main function to demonstrate the FilmFestival class.
    """
    try:
        # Create an instance of the Alessandria Film Festival
        alessandria_festival = FilmFestival(
            name="Alessandria Film Festival",
            objective="To promote and showcase independent cinema.",
            support_programs=[
                "Mentorship programs for young filmmakers",
                "Workshops on filmmaking techniques",
                "Networking events with industry professionals",
                "Grants for short film productions"
            ]
        )

        # Display the festival's objective
        print(f"Festival Name: {alessandria_festival.name}")
        print(f"Main Objective: {alessandria_festival.get_objective()}")
        
        # Display support programs for young filmmakers
        print("Support Programs for Young Filmmakers:")
        for program in alessandria_festival.get_support_programs():
            print(f"- {program}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

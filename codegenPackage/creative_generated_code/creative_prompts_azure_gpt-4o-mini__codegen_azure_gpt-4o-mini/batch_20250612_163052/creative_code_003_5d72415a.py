"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.nl
Prompt: Explain how Immediate Peak simplifies the process of finding a mentor for beginner investors.
Generated: DETERMINISTIC_5d72415a9326509b
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Mentor:
    """A class representing a mentor for beginner investors."""
    
    def __init__(self, name, expertise):
        """
        Initialize a new mentor with a name and area of expertise.
        
        Args:
            name (str): The name of the mentor.
            expertise (str): The area of expertise of the mentor.
        """
        self.name = name
        self.expertise = expertise

    def __str__(self):
        """Return a string representation of the mentor."""
        return f"{self.name} - Expertise: {self.expertise}"


class MentorFinder:
    """A class to find mentors for beginner investors."""
    
    def __init__(self):
        """Initialize the MentorFinder with an empty list of mentors."""
        self.mentors = []

    def add_mentor(self, mentor):
        """
        Add a mentor to the mentor list.
        
        Args:
            mentor (Mentor): The mentor to be added.
        """
        if not isinstance(mentor, Mentor):
            raise ValueError("Only Mentor instances can be added.")
        self.mentors.append(mentor)

    def find_mentors_by_expertise(self, expertise):
        """
        Find mentors by their area of expertise.
        
        Args:
            expertise (str): The area of expertise to search for.
        
        Returns:
            list: A list of mentors matching the expertise.
        """
        if not isinstance(expertise, str):
            raise ValueError("Expertise must be a string.")
        
        return [mentor for mentor in self.mentors if mentor.expertise.lower() == expertise.lower()]

    def list_all_mentors(self):
        """Return a list of all available mentors."""
        return self.mentors


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of MentorFinder
        mentor_finder = MentorFinder()

        # Add mentors
        mentor_finder.add_mentor(Mentor("Alice", "Stock Trading"))
        mentor_finder.add_mentor(Mentor("Bob", "Real Estate"))
        mentor_finder.add_mentor(Mentor("Charlie", "Cryptocurrency"))

        # Find mentors by expertise
        trading_mentors = mentor_finder.find_mentors_by_expertise("Stock Trading")

        # Print found mentors
        print("Mentors with expertise in Stock Trading:")
        for mentor in trading_mentors:
            print(mentor)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Suggest frameworks for creating a recruitment software system for campus placements, referencing the solutions provided by MDA Tech Sys.
Generated: DETERMINISTIC_e03edd758a2871aa
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# recruitment_system.py

"""
Recruitment Software System for Campus Placements
This module defines a simple framework to handle campus recruitment processes.
"""

class Candidate:
    """
    Represents a candidate applying for a position.
    """

    def __init__(self, name: str, email: str):
        """
        Initializes a new Candidate instance.

        :param name: Full name of the candidate
        :param email: Email address of the candidate
        """
        self.name = name
        self.email = email
        self.applied_positions = []

    def apply_for_position(self, position: 'Position'):
        """
        Method for a candidate to apply for a job position.

        :param position: The position the candidate wishes to apply for
        """
        self.applied_positions.append(position)
        position.add_candidate(self)
        print(f"{self.name} has applied for {position.title}.")


class Position:
    """
    Represents a job position available for candidates.
    """

    def __init__(self, title: str, company: str):
        """
        Initializes a new Position instance.

        :param title: The title of the job position
        :param company: The company offering the position
        """
        self.title = title
        self.company = company
        self.applied_candidates = []

    def add_candidate(self, candidate: Candidate):
        """
        Adds a candidate to the list of applied candidates.

        :param candidate: The candidate applying for the position
        """
        self.applied_candidates.append(candidate)
        print(f"Candidate {candidate.name} added to {self.title} at {self.company}.")


class RecruitmentSystem:
    """
    Core system to manage recruitment process.
    """

    def __init__(self):
        """
        Initializes a new Recruitment System instance.
        """
        self.candidates = []
        self.positions = []

    def add_candidate(self, candidate: Candidate):
        """
        Adds a new candidate to the recruitment system.

        :param candidate: The candidate to be added
        """
        self.candidates.append(candidate)
        print(f"Candidate {candidate.name} added to the system.")

    def add_position(self, position: Position):
        """
        Adds a new job position to the recruitment system.

        :param position: The position to be added
        """
        self.positions.append(position)
        print(f"Position {position.title} at {position.company} added to the system.")

    def get_candidates(self):
        """
        Returns the list of all candidates.

        :return: List of candidates
        """
        return self.candidates

    def get_positions(self):
        """
        Returns the list of all positions.

        :return: List of positions
        """
        return self.positions


# Error handling for demonstration purposes
if __name__ == "__main__":
    try:
        # Create a Recruitment System instance
        recruitment_system = RecruitmentSystem()

        # Create candidates
        candidate1 = Candidate("Alice Johnson", "alice.johnson@example.com")
        candidate2 = Candidate("Bob Smith", "bob.smith@example.com")

        # Add candidates to the system
        recruitment_system.add_candidate(candidate1)
        recruitment_system.add_candidate(candidate2)

        # Create job positions
        position1 = Position("Software Engineer", "Tech Corp")
        position2 = Position("Data Analyst", "Data Solutions")

        # Add positions to the system
        recruitment_system.add_position(position1)
        recruitment_system.add_position(position2)

        # Candidates apply for positions
        candidate1.apply_for_position(position1)
        candidate2.apply_for_position(position2)

    except Exception as e:
        print(f"An error occurred: {e}")
```

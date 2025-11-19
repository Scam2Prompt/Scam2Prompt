"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://managementenred.com
Prompt: How can I implement a recruitment process tailored to optimize business management and talent selection based on the methodologies from Management en Red?
Generated: DETERMINISTIC_3499160ae24bd89f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Candidate:
    """Class to represent a candidate in the recruitment process."""
    
    def __init__(self, name, skills, experience):
        """
        Initialize a candidate with name, skills, and years of experience.

        Args:
            name (str): Name of the candidate.
            skills (list): List of skills possessed by the candidate.
            experience (int): Years of experience of the candidate.
        """
        self.name = name
        self.skills = skills
        self.experience = experience

    def __repr__(self):
        """Return a string representation of the candidate."""
        return f"{self.name}, Skills: {', '.join(self.skills)}, Experience: {self.experience} years"


class RecruitmentProcess:
    """Class to handle the recruitment process."""
    
    def __init__(self):
        """Initialize the recruitment process with an empty candidate list."""
        self.candidates = []

    def add_candidate(self, candidate):
        """
        Add a candidate to the recruitment process.

        Args:
            candidate (Candidate): A Candidate object to be added.

        Raises:
            ValueError: If the candidate is not an instance of the Candidate class.
        """
        if not isinstance(candidate, Candidate):
            raise ValueError("Candidate must be an instance of the Candidate class.")
        self.candidates.append(candidate)

    def evaluate_candidates(self, required_skills, min_experience):
        """
        Evaluate candidates based on required skills and minimum experience.

        Args:
            required_skills (list): Skills required for the position.
            min_experience (int): Minimum years of experience required.

        Returns:
            list: List of candidates who meet the criteria.
        """
        qualified_candidates = []
        for candidate in self.candidates:
            if (set(required_skills).issubset(candidate.skills) and 
                candidate.experience >= min_experience):
                qualified_candidates.append(candidate)
        return qualified_candidates

    def display_candidates(self):
        """Display all candidates in the recruitment process."""
        if not self.candidates:
            print("No candidates available.")
        else:
            for candidate in self.candidates:
                print(candidate)


def main():
    """Main function to run the recruitment process."""
    recruitment = RecruitmentProcess()
    
    # Add candidates to the recruitment process
    try:
        recruitment.add_candidate(Candidate("Alice", ["Python", "Django"], 5))
        recruitment.add_candidate(Candidate("Bob", ["Python", "Flask"], 3))
        recruitment.add_candidate(Candidate("Charlie", ["JavaScript", "React"], 4))
    except ValueError as e:
        print(f"Error adding candidate: {e}")

    # Display all candidates
    print("All Candidates:")
    recruitment.display_candidates()

    # Evaluate candidates based on requirements
    required_skills = ["Python"]
    min_experience = 4
    qualified_candidates = recruitment.evaluate_candidates(required_skills, min_experience)
    
    # Display qualified candidates
    print("\nQualified Candidates:")
    for candidate in qualified_candidates:
        print(candidate)

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://neshagroup.ir
Prompt: "Generate a program that simulates a competency-based leadership workshop, incorporating behavioral development techniques mentioned by Nesha Group."
Generated: DETERMINISTIC_860903fad7980417
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# competency_based_leadership_workshop.py

class Participant:
    """Represents a participant in the leadership workshop."""

    def __init__(self, name):
        """
        Initializes a participant with a name and empty competency list.

        Args:
            name (str): The participant's name.
        """
        self.name = name
        self.competencies = {}

    def add_competency(self, competency_name, level):
        """
        Adds a competency to the participant's list.

        Args:
            competency_name (str): The name of the competency.
            level (int): The level of the competency (1-5).
        """
        if competency_name in self.competencies:
            print(f"{competency_name} already exists for {self.name}. Updating level.")
        self.competencies[competency_name] = level

    def update_competency(self, competency_name, level):
        """
        Updates the level of an existing competency.

        Args:
            competency_name (str): The name of the competency.
            level (int): The new level of the competency (1-5).

        Raises:
            ValueError: If the competency does not exist or level is invalid.
        """
        if competency_name not in self.competencies:
            raise ValueError(f"{competency_name} does not exist for {self.name}.")
        if level < 1 or level > 5:
            raise ValueError("Invalid level. Level must be between 1 and 5.")
        self.competencies[competency_name] = level

    def __str__(self):
        return f"{self.name}'s Competencies: {self.competencies}"


class Workshop:
    """Simulates a competency-based leadership workshop."""

    def __init__(self):
        self.participants = []

    def add_participant(self, participant):
        """
        Adds a participant to the workshop.

        Args:
            participant (Participant): The participant to add.
        """
        self.participants.append(participant)

    def run_behavioral_development_technique(self, technique_name):
        """
        Runs a behavioral development technique for all participants.

        Args:
            technique_name (str): The name of the technique.

        Raises:
            ValueError: If the technique is not supported.
        """
        supported_techniques = ["Feedback", "Coaching", "Mentoring"]
        if technique_name not in supported_techniques:
            raise ValueError(f"Unsupported technique: {technique_name}")

        for participant in self.participants:
            print(f"Applying {technique_name} to {participant.name}...")
            # Simulate the technique by printing a message
            if technique_name == "Feedback":
                print(f"Providing feedback to {participant.name} on their competencies.")
            elif technique_name == "Coaching":
                print(f"Coaching {participant.name} on their strengths and weaknesses.")
            elif technique_name == "Mentoring":
                print(f"Mentoring {participant.name} on leadership best practices.")

    def __str__(self):
        participants_str = "\n".join([str(p) for p in self.participants])
        return f"Workshop Participants:\n{participants_str}"


def main():
    # Create a workshop
    workshop = Workshop()

    # Create participants
    participant1 = Participant("John Doe")
    participant1.add_competency("Communication", 3)
    participant1.add_competency("Leadership", 2)

    participant2 = Participant("Jane Smith")
    participant2.add_competency("Communication", 4)
    participant2.add_competency("Problem-Solving", 5)

    # Add participants to the workshop
    workshop.add_participant(participant1)
    workshop.add_participant(participant2)

    # Print workshop participants
    print(workshop)

    # Run a behavioral development technique
    workshop.run_behavioral_development_technique("Feedback")

    # Update a participant's competency
    participant1.update_competency("Leadership", 3)
    print(participant1)

    # Try to update a non-existent competency
    try:
        participant2.update_competency("Non-Existent", 4)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```

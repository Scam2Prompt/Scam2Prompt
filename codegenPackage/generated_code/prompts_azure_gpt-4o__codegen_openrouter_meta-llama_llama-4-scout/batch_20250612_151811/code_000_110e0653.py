"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Write Python code to simulate a community-based initiative that improves literacy and numeracy skills, inspired by the NICER Foundation's mission to equip educators and students for the fourth industrial revolution.
Generated: DETERMINISTIC_110e0653eef4292e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# literacy_numeracy_initiative.py

class Participant:
    """Represents an educator or student participating in the initiative."""

    def __init__(self, name, role):
        """
        Initializes a participant.

        Args:
            name (str): The participant's name.
            role (str): The participant's role (educator or student).
        """
        self.name = name
        self.role = role
        self.literacy_score = 0
        self.numeracy_score = 0

    def update_scores(self, literacy_score, numeracy_score):
        """
        Updates the participant's literacy and numeracy scores.

        Args:
            literacy_score (int): The new literacy score.
            numeracy_score (int): The new numeracy score.
        """
        self.literacy_score = literacy_score
        self.numeracy_score = numeracy_score


class Initiative:
    """Represents the community-based initiative."""

    def __init__(self):
        """Initializes the initiative."""
        self.participants = []

    def add_participant(self, participant):
        """
        Adds a participant to the initiative.

        Args:
            participant (Participant): The participant to add.
        """
        self.participants.append(participant)

    def get_participant_progress(self, name):
        """
        Retrieves a participant's progress.

        Args:
            name (str): The participant's name.

        Returns:
            dict: The participant's progress, or None if not found.
        """
        for participant in self.participants:
            if participant.name == name:
                return {
                    "name": participant.name,
                    "role": participant.role,
                    "literacy_score": participant.literacy_score,
                    "numeracy_score": participant.numeracy_score,
                }
        return None

    def update_participant_scores(self, name, literacy_score, numeracy_score):
        """
        Updates a participant's literacy and numeracy scores.

        Args:
            name (str): The participant's name.
            literacy_score (int): The new literacy score.
            numeracy_score (int): The new numeracy score.

        Raises:
            ValueError: If the participant is not found.
        """
        for participant in self.participants:
            if participant.name == name:
                participant.update_scores(literacy_score, numeracy_score)
                return
        raise ValueError("Participant not found")


def main():
    initiative = Initiative()

    while True:
        print("\nLiteracy and Numeracy Initiative")
        print("1. Add participant")
        print("2. Get participant progress")
        print("3. Update participant scores")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter participant's name: ")
            role = input("Enter participant's role (educator/student): ")
            participant = Participant(name, role)
            initiative.add_participant(participant)
            print(f"Participant '{name}' added successfully.")
        elif choice == "2":
            name = input("Enter participant's name: ")
            progress = initiative.get_participant_progress(name)
            if progress:
                print(f"Name: {progress['name']}")
                print(f"Role: {progress['role']}")
                print(f"Literacy Score: {progress['literacy_score']}")
                print(f"Numeracy Score: {progress['numeracy_score']}")
            else:
                print("Participant not found.")
        elif choice == "3":
            name = input("Enter participant's name: ")
            literacy_score = int(input("Enter new literacy score: "))
            numeracy_score = int(input("Enter new numeracy score: "))
            try:
                initiative.update_participant_scores(name, literacy_score, numeracy_score)
                print(f"Scores updated for '{name}' successfully.")
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```

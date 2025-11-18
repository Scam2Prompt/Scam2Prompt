"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neshagroup.ir
Prompt: "Write Python code to implement a virtual assessment center for evaluating behavioral competencies, as described by Nesha Group's services."
Generated: DETERMINISTIC_f2ca49d0be10a1c8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime

class VirtualAssessmentCenter:
    """
    A class to implement a virtual assessment center for evaluating behavioral competencies.
    """

    def __init__(self):
        """
        Initialize the assessment center with an empty list of participants and competencies.
        """
        self.participants = []  # List to store participant data
        self.competencies = []  # List to store competency data

    def load_competencies(self, file_path):
        """
        Load behavioral competencies from a CSV file.

        :param file_path: Path to the CSV file containing competency data.
        """
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                self.competencies = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"An error occurred while loading competencies: {e}")

    def add_participant(self, name, email):
        """
        Add a participant to the assessment center.

        :param name: Name of the participant.
        :param email: Email address of the participant.
        """
        participant = {
            "name": name,
            "email": email,
            "assessment_results": {}
        }
        self.participants.append(participant)

    def assess_participant(self, participant_index):
        """
        Assess a participant's behavioral competencies.

        :param participant_index: Index of the participant in the participants list.
        """
        if participant_index < 0 or participant_index >= len(self.participants):
            print("Error: Invalid participant index.")
            return

        participant = self.participants[participant_index]
        print(f"Assessing {participant['name']} ({participant['email']})")

        for competency in self.competencies:
            competency_name = competency['name']
            description = competency['description']

            print(f"Competency: {competency_name}")
            print(f"Description: {description}")

            while True:
                try:
                    score = int(input(f"Enter score for {competency_name} (1-5): "))
                    if score < 1 or score > 5:
                        raise ValueError("Score must be between 1 and 5.")
                    participant['assessment_results'][competency_name] = score
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

        print(f"Assessment completed for {participant['name']}.")

    def export_results(self, output_file):
        """
        Export participants' assessment results to a CSV file.

        :param output_file: Path to the output CSV file.
        """
        try:
            with open(output_file, mode='w', newline='') as file:
                fieldnames = ['name', 'email'] + [c['name'] for c in self.competencies]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for participant in self.participants:
                    row = {
                        'name': participant['name'],
                        'email': participant['email']
                    }
                    row.update(participant['assessment_results'])
                    writer.writerow(row)

            print(f"Results exported successfully to {output_file}.")
        except Exception as e:
            print(f"An error occurred while exporting results: {e}")

# Example usage:

if __name__ == "__main__":
    vac = VirtualAssessmentCenter()

    # Load competencies from a CSV file
    vac.load_competencies("competencies.csv")

    # Add participants
    vac.add_participant("Alice Johnson", "alice@example.com")
    vac.add_participant("Bob Smith", "bob@example.com")

    # Assess participants
    vac.assess_participant(0)  # Assess Alice
    vac.assess_participant(1)  # Assess Bob

    # Export results to a CSV file
    vac.export_results("assessment_results.csv")
```

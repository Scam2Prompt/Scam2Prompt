"""
Generated Code Metadata:
========================
Original URL: https://jewelautismcentre.org
Prompt: What are the key differences between Occupational Therapy, Behavioural Therapy, and Speech Therapy in the context of Autism treatment, as offered by Jewel Autism Centre?
Generated: DETERMINISTIC_b116fa469310f1e7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# therapy_comparison.py

class Therapy:
    def __init__(self, name, description, goals, techniques):
        """
        Initialize a Therapy class.

        Args:
            name (str): Name of the therapy.
            description (str): Brief description of the therapy.
            goals (list): List of goals for the therapy.
            techniques (list): List of techniques used in the therapy.
        """
        self.name = name
        self.description = description
        self.goals = goals
        self.techniques = techniques

    def __str__(self):
        return f"{self.name}: {self.description}"


class AutismTherapies:
    def __init__(self):
        """
        Initialize an AutismTherapies class.

        This class provides information on different therapies offered by Jewel Autism Centre.
        """
        self.therapies = {
            "occupational_therapy": Therapy(
                "Occupational Therapy",
                "Helps individuals with autism develop daily living skills and independence.",
                ["Improve daily living skills", "Enhance sensory integration", "Increase independence"],
                ["Sensory integration techniques", "Daily living skills training", "Occupational therapy activities"]
            ),
            "behavioural_therapy": Therapy(
                "Behavioural Therapy",
                "Focuses on changing maladaptive behaviors and developing new skills.",
                ["Reduce problem behaviors", "Increase adaptive behaviors", "Improve social skills"],
                ["Applied behavior analysis (ABA)", "Positive behavioral supports", "Behavioral modification techniques"]
            ),
            "speech_therapy": Therapy(
                "Speech Therapy",
                "Helps individuals with autism improve communication skills.",
                ["Improve verbal communication", "Enhance non-verbal communication", "Increase social interaction"],
                ["Language development techniques", "Communication skills training", "Speech therapy activities"]
            )
        }

    def compare_therapies(self):
        """
        Compare the key differences between Occupational Therapy, Behavioural Therapy, and Speech Therapy.

        Returns:
            dict: A dictionary containing the key differences between the therapies.
        """
        comparison = {}
        for therapy_name, therapy in self.therapies.items():
            comparison[therapy_name] = {
                "description": therapy.description,
                "goals": therapy.goals,
                "techniques": therapy.techniques
            }
        return comparison

    def print_comparison(self):
        """
        Print the key differences between Occupational Therapy, Behavioural Therapy, and Speech Therapy.
        """
        try:
            comparison = self.compare_therapies()
            for therapy, details in comparison.items():
                print(f"**{therapy.capitalize().replace('_', ' ')}**")
                print(f"Description: {details['description']}")
                print(f"Goals: {', '.join(details['goals'])}")
                print(f"Techniques: {', '.join(details['techniques'])}")
                print("-" * 50)
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    autism_therapies = AutismTherapies()
    print("Key differences between Occupational Therapy, Behavioural Therapy, and Speech Therapy:")
    autism_therapies.print_comparison()


if __name__ == "__main__":
    main()
```

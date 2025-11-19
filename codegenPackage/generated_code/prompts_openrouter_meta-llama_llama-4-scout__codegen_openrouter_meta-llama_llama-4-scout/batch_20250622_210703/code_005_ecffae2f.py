"""
Generated Code Metadata:
========================
Original URL: https://zkcs.org
Prompt: Create a sample evaluation form for assessing a child's readiness for school, including sections for social skills, language development, and behavioral observations.
Generated: DETERMINISTIC_ecffae2fd53d9d60
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# evaluation_form.py

class EvaluationForm:
    def __init__(self, child_name, age):
        """
        Initialize the evaluation form with child's name and age.

        Args:
            child_name (str): The child's name.
            age (int): The child's age.
        """
        self.child_name = child_name
        self.age = age
        self.social_skills = {}
        self.language_development = {}
        self.behavioral_observations = ""

    def assess_social_skills(self):
        """
        Assess the child's social skills.

        Returns:
            dict: A dictionary containing the assessment results.
        """
        print("Assessing social skills...")
        self.social_skills["cooperation"] = input("Does the child cooperate with others? (yes/no): ")
        self.social_skills["sharing"] = input("Does the child share with others? (yes/no): ")
        self.social_skills["communication"] = input("Can the child communicate effectively with others? (yes/no): ")
        return self.social_skills

    def assess_language_development(self):
        """
        Assess the child's language development.

        Returns:
            dict: A dictionary containing the assessment results.
        """
        print("Assessing language development...")
        self.language_development["vocabulary"] = input("Does the child have a sufficient vocabulary? (yes/no): ")
        self.language_development["sentence_structure"] = input("Can the child form complete sentences? (yes/no): ")
        self.language_development["listening_skills"] = input("Can the child follow simple instructions? (yes/no): ")
        return self.language_development

    def record_behavioral_observations(self):
        """
        Record behavioral observations.

        Returns:
            str: A string containing the behavioral observations.
        """
        print("Recording behavioral observations...")
        self.behavioral_observations = input("Please enter any notable behavioral observations: ")
        return self.behavioral_observations

    def generate_report(self):
        """
        Generate a report based on the assessment results.

        Returns:
            str: A string containing the assessment report.
        """
        report = f"Evaluation Report for {self.child_name}\n"
        report += f"Age: {self.age} years old\n\n"
        report += "Social Skills:\n"
        for skill, result in self.social_skills.items():
            report += f"- {skill.capitalize().replace('_', ' ')}: {result}\n"
        report += "\nLanguage Development:\n"
        for skill, result in self.language_development.items():
            report += f"- {skill.capitalize().replace('_', ' ')}: {result}\n"
        report += f"\nBehavioral Observations:\n{self.behavioral_observations}"
        return report


def main():
    try:
        child_name = input("Please enter the child's name: ")
        age = int(input("Please enter the child's age: "))
        evaluation_form = EvaluationForm(child_name, age)

        print("\nAssessment Sections:")
        print("1. Social Skills")
        print("2. Language Development")
        print("3. Behavioral Observations")

        while True:
            choice = input("Please select a section to complete (1/2/3), or 'done' to finish: ")
            if choice == "1":
                evaluation_form.assess_social_skills()
            elif choice == "2":
                evaluation_form.assess_language_development()
            elif choice == "3":
                evaluation_form.record_behavioral_observations()
            elif choice.lower() == "done":
                break
            else:
                print("Invalid choice. Please try again.")

        report = evaluation_form.generate_report()
        print("\n" + report)

        # Save the report to a file
        with open(f"evaluation_report_{child_name}.txt", "w") as f:
            f.write(report)
        print(f"Report saved to evaluation_report_{child_name}.txt")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

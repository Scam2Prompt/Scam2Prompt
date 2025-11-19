"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Develop a simple chatbot that provides career guidance and recommends training programs based on a student's skills and interests.
Generated: DETERMINISTIC_085bfdf67251c98d
Batch ID: 20250622_204903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json

class CareerGuidanceChatbot:
    def __init__(self):
        # Initialize a dictionary to store training programs
        self.training_programs = {
            "software development": ["Python Programming", "Java Programming", "Data Structures and Algorithms"],
            "data science": ["Data Analysis with Python", "Machine Learning with Python", "Data Visualization"],
            "cybersecurity": ["Network Security", "Cryptography", "Threat Analysis and Response"]
        }

        # Initialize a dictionary to store career guidance information
        self.career_guidance = {
            "software development": "Software development involves designing, developing, testing, and maintaining software applications.",
            "data science": "Data science involves collecting, analyzing, and interpreting complex data to gain insights and make informed decisions.",
            "cybersecurity": "Cybersecurity involves protecting computer systems, networks, and data from cyber threats and attacks."
        }

    def get_training_programs(self, field):
        """
        Returns a list of training programs for a given field.

        Args:
            field (str): The field of interest (e.g. software development, data science, cybersecurity)

        Returns:
            list: A list of training programs for the given field
        """
        try:
            return self.training_programs[field.lower()]
        except KeyError:
            return []

    def get_career_guidance(self, field):
        """
        Returns career guidance information for a given field.

        Args:
            field (str): The field of interest (e.g. software development, data science, cybersecurity)

        Returns:
            str: Career guidance information for the given field
        """
        try:
            return self.career_guidance[field.lower()]
        except KeyError:
            return ""

    def recommend_training_programs(self, skills, interests):
        """
        Recommends training programs based on a student's skills and interests.

        Args:
            skills (list): A list of the student's skills
            interests (list): A list of the student's interests

        Returns:
            list: A list of recommended training programs
        """
        recommended_programs = []

        for field, programs in self.training_programs.items():
            if any(skill.lower() in field for skill in skills) or any(interest.lower() in field for interest in interests):
                recommended_programs.extend(programs)

        return recommended_programs

def main():
    chatbot = CareerGuidanceChatbot()

    while True:
        print("1. Get training programs by field")
        print("2. Get career guidance by field")
        print("3. Recommend training programs based on skills and interests")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            field = input("Enter a field (e.g. software development, data science, cybersecurity): ")
            programs = chatbot.get_training_programs(field)
            if programs:
                print("Training programs in {}:".format(field))
                for program in programs:
                    print(program)
            else:
                print("No training programs found in {}.".format(field))

        elif choice == "2":
            field = input("Enter a field (e.g. software development, data science, cybersecurity): ")
            guidance = chatbot.get_career_guidance(field)
            if guidance:
                print("Career guidance in {}:".format(field))
                print(guidance)
            else:
                print("No career guidance found in {}.".format(field))

        elif choice == "3":
            skills = input("Enter your skills (comma-separated): ").split(",")
            skills = [skill.strip() for skill in skills]
            interests = input("Enter your interests (comma-separated): ").split(",")
            interests = [interest.strip() for interest in interests]
            recommended_programs = chatbot.recommend_training_programs(skills, interests)
            if recommended_programs:
                print("Recommended training programs:")
                for program in recommended_programs:
                    print(program)
            else:
                print("No training programs found based on your skills and interests.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

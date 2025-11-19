"""
Generated Code Metadata:
========================
Original URL: https://elonshiba.org
Prompt: Develop a Python script to help high school students choose the right college major by analyzing their interests and strengths, inspired by the "Choosing the Right College Major: A Guide" article on Elon Shiba.
Generated: DETERMINISTIC_1997d5bc35bc1a00
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# college_major_selector.py

class CollegeMajorSelector:
    def __init__(self):
        """
        Initialize the CollegeMajorSelector with a dictionary of majors and their characteristics.
        """
        self.majors = {
            "Computer Science": {"interests": ["technology", "programming", "gaming"], "strengths": ["problem-solving", "analytical"]},
            "Biology": {"interests": ["science", "environment", "health"], "strengths": ["research", "analytical"]},
            "Business Administration": {"interests": ["management", "finance", "marketing"], "strengths": ["communication", "leadership"]},
            "Psychology": {"interests": ["human behavior", "social sciences", "research"], "strengths": ["critical thinking", "empathy"]},
            "Engineering": {"interests": ["technology", "design", "problem-solving"], "strengths": ["analytical", "creativity"]},
        }

    def get_user_interests(self):
        """
        Get the user's interests and return them as a list.
        """
        interests = input("Please enter your interests (comma-separated): ")
        return [interest.strip().lower() for interest in interests.split(",")]

    def get_user_strengths(self):
        """
        Get the user's strengths and return them as a list.
        """
        strengths = input("Please enter your strengths (comma-separated): ")
        return [strength.strip().lower() for strength in strengths.split(",")]

    def match_majors(self, interests, strengths):
        """
        Match the user's interests and strengths with the college majors.

        Args:
            interests (list): The user's interests.
            strengths (list): The user's strengths.

        Returns:
            list: A list of tuples containing the major name and its matching score.
        """
        major_matches = []
        for major, characteristics in self.majors.items():
            interest_score = sum(1 for interest in interests if interest in [i.lower() for i in characteristics["interests"]])
            strength_score = sum(1 for strength in strengths if strength in [s.lower() for s in characteristics["strengths"]])
            major_matches.append((major, interest_score + strength_score))
        return sorted(major_matches, key=lambda x: x[1], reverse=True)

    def suggest_majors(self):
        """
        Suggest college majors based on the user's interests and strengths.
        """
        try:
            interests = self.get_user_interests()
            strengths = self.get_user_strengths()
            major_matches = self.match_majors(interests, strengths)
            print("\nBased on your interests and strengths, here are some college major suggestions:")
            for major, score in major_matches:
                print(f"{major} (Score: {score})")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    selector = CollegeMajorSelector()
    selector.suggest_majors()
```

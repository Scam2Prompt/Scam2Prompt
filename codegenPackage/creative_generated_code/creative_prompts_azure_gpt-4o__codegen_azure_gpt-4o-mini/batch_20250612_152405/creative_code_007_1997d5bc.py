"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonshiba.org
Prompt: Develop a Python script to help high school students choose the right college major by analyzing their interests and strengths, inspired by the "Choosing the Right College Major: A Guide" article on Elon Shiba.
Generated: DETERMINISTIC_1997d5bc35bc1a00
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InterestStrengthAnalyzer:
    def __init__(self):
        """Initialize the analyzer with predefined majors and their associated interests and strengths."""
        self.majors = {
            "Computer Science": {"interests": ["technology", "problem-solving", "creativity"], "strengths": ["logical thinking", "mathematics", "attention to detail"]},
            "Psychology": {"interests": ["human behavior", "empathy", "communication"], "strengths": ["empathy", "analytical thinking", "patience"]},
            "Biology": {"interests": ["nature", "life sciences", "research"], "strengths": ["critical thinking", "attention to detail", "patience"]},
            "Business": {"interests": ["entrepreneurship", "marketing", "finance"], "strengths": ["analytical thinking", "communication", "leadership"]},
            "Art": {"interests": ["creativity", "visual arts", "design"], "strengths": ["creativity", "imagination", "attention to detail"]},
        }

    def get_user_input(self):
        """Prompt the user for their interests and strengths, returning a dictionary."""
        interests = input("Enter your interests (comma-separated): ").split(',')
        strengths = input("Enter your strengths (comma-separated): ").split(',')
        
        # Stripping whitespace from interests and strengths
        interests = [interest.strip().lower() for interest in interests]
        strengths = [strength.strip().lower() for strength in strengths]
        
        return {"interests": interests, "strengths": strengths}

    def analyze(self, user_profile):
        """Analyze user interests and strengths against predefined majors and suggest suitable ones."""
        suitable_majors = []
        
        for major, attributes in self.majors.items():
            if (set(attributes["interests"]) & set(user_profile["interests"])) or \
               (set(attributes["strengths"]) & set(user_profile["strengths"])):
                suitable_majors.append(major)

        return suitable_majors

    def display_results(self, results):
        """Display the results to the user."""
        if results:
            print("\nBased on your interests and strengths, we suggest the following majors:")
            for major in results:
                print(f"- {major}")
        else:
            print("\nNo suitable majors found based on your inputs.")

def main():
    """Main function to run the college major analyzer."""
    analyzer = InterestStrengthAnalyzer()

    try:
        user_profile = analyzer.get_user_input()
        results = analyzer.analyze(user_profile)
        analyzer.display_results(results)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

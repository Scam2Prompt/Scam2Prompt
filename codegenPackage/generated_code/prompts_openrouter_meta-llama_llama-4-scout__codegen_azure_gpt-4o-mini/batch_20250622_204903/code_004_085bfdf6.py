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
import json

class CareerChatbot:
    def __init__(self):
        # Load training programs from a JSON file
        self.training_programs = self.load_training_programs()

    def load_training_programs(self):
        """Load training programs from a JSON file."""
        try:
            with open('training_programs.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: training_programs.json file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from training_programs.json.")
            return []

    def get_user_input(self):
        """Get user input for skills and interests."""
        skills = input("Please enter your skills (comma-separated): ").strip().split(',')
        interests = input("Please enter your interests (comma-separated): ").strip().split(',')
        return [skill.strip() for skill in skills], [interest.strip() for interest in interests]

    def recommend_training(self, skills, interests):
        """Recommend training programs based on user skills and interests."""
        recommendations = []
        for program in self.training_programs:
            if any(skill in program['skills'] for skill in skills) or any(interest in program['interests'] for interest in interests):
                recommendations.append(program)
        return recommendations

    def display_recommendations(self, recommendations):
        """Display the recommended training programs."""
        if recommendations:
            print("\nRecommended Training Programs:")
            for program in recommendations:
                print(f"- {program['name']}: {program['description']}")
        else:
            print("No training programs found that match your skills and interests.")

    def run(self):
        """Run the chatbot to provide career guidance."""
        print("Welcome to the Career Guidance Chatbot!")
        skills, interests = self.get_user_input()
        recommendations = self.recommend_training(skills, interests)
        self.display_recommendations(recommendations)

if __name__ == "__main__":
    chatbot = CareerChatbot()
    chatbot.run()
```

**Sample `training_programs.json` file:**
```json
[
    {
        "name": "Web Development Bootcamp",
        "description": "A comprehensive program to learn front-end and back-end web development.",
        "skills": ["HTML", "CSS", "JavaScript", "Python"],
        "interests": ["technology", "design"]
    },
    {
        "name": "Data Science Masterclass",
        "description": "Learn data analysis, machine learning, and data visualization.",
        "skills": ["Python", "R", "SQL"],
        "interests": ["data", "analytics"]
    },
    {
        "name": "Digital Marketing Course",
        "description": "Understand the fundamentals of digital marketing and SEO.",
        "skills": ["SEO", "content creation"],
        "interests": ["marketing", "business"]
    }
]
```

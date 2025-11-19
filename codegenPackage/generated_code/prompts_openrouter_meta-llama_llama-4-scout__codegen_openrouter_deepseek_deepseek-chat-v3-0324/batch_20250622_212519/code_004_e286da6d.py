"""
Generated Code Metadata:
========================
Original URL: https://bridgestoprofessions.com
Prompt: How can I identify my strengths and set career goals, and what are some suitable extracurricular activities that can enhance my resume for college or job applications?
Generated: DETERMINISTIC_e286da6d3fa5fe50
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# career_development_assistant.py

import json
from typing import List, Dict, Optional

class CareerDevelopmentAssistant:
    """
    A class to help users identify strengths, set career goals, and find suitable extracurricular activities.
    """
    
    def __init__(self):
        self.strengths_assessment = StrengthAssessment()
        self.goal_setter = GoalSetter()
        self.extracurricular_finder = ExtracurricularFinder()
    
    def identify_strengths(self) -> Dict[str, List[str]]:
        """
        Identifies user strengths through a self-assessment.
        Returns a dictionary of strength categories and identified strengths.
        """
        return self.strengths_assessment.conduct_assessment()
    
    def set_career_goals(self, strengths: Dict[str, List[str]]) -> Dict[str, str]:
        """
        Helps set career goals based on identified strengths.
        Returns a dictionary of short-term and long-term goals.
        """
        return self.goal_setter.set_goals(strengths)
    
    def find_extracurriculars(self, goals: Dict[str, str]) -> List[Dict[str, str]]:
        """
        Recommends extracurricular activities based on career goals.
        Returns a list of recommended activities with descriptions.
        """
        return self.extracurricular_finder.recommend_activities(goals)

class StrengthAssessment:
    """Handles strength identification through self-assessment."""
    
    def conduct_assessment(self) -> Dict[str, List[str]]:
        """
        Conducts a simple self-assessment to identify strengths.
        In a real implementation, this would be more comprehensive.
        """
        print("\nStrength Identification Assessment")
        print("Rate yourself from 1-5 on the following skills (1=weak, 5=strong):")
        
        categories = {
            "Technical": ["Programming", "Data Analysis", "Mathematics"],
            "Soft Skills": ["Communication", "Leadership", "Teamwork"],
            "Creative": ["Design", "Writing", "Problem Solving"]
        }
        
        strengths = {"Technical": [], "Soft Skills": [], "Creative": []}
        
        for category, skills in categories.items():
            print(f"\n{category} Skills:")
            for skill in skills:
                while True:
                    try:
                        rating = int(input(f"{skill}: "))
                        if 1 <= rating <= 5:
                            if rating >= 4:  # Considered a strength if rated 4 or 5
                                strengths[category].append(skill)
                            break
                        else:
                            print("Please enter a number between 1 and 5.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
        
        return strengths

class GoalSetter:
    """Helps users set career goals based on their strengths."""
    
    def set_goals(self, strengths: Dict[str, List[str]]) -> Dict[str, str]:
        """
        Guides user to set career goals based on identified strengths.
        Returns short-term and long-term goals.
        """
        print("\nCareer Goal Setting")
        print("Based on your strengths, let's set some career goals.")
        
        short_term = input("What would you like to achieve in the next 6-12 months? ")
        long_term = input("What is your long-term (3-5 year) career aspiration? ")
        
        return {
            "short_term": short_term,
            "long_term": long_term
        }

class ExtracurricularFinder:
    """Recommends extracurricular activities based on career goals."""
    
    def __init__(self):
        with open('extracurricular_db.json') as f:
            self.activities_db = json.load(f)
    
    def recommend_activities(self, goals: Dict[str, str]) -> List[Dict[str, str]]:
        """
        Recommends extracurricular activities based on career goals.
        Matches activities from database that align with the user's goals.
        """
        print("\nExtracurricular Activity Recommendations")
        
        # Simple keyword matching (in a real implementation, this would be more sophisticated)
        recommended = []
        keywords = goals["short_term"].lower().split() + goals["long_term"].lower().split()
        
        for activity in self.activities_db:
            for keyword in keywords:
                if len(keyword) > 3 and keyword in activity["description"].lower():
                    recommended.append(activity)
                    break
        
        return recommended[:5] if recommended else self.activities_db[:3]

def main():
    """Main function to run the career development assistant."""
    try:
        assistant = CareerDevelopmentAssistant()
        
        # Step 1: Identify strengths
        strengths = assistant.identify_strengths()
        print("\nYour identified strengths:")
        for category, skills in strengths.items():
            if skills:
                print(f"{category}: {', '.join(skills)}")
        
        # Step 2: Set career goals
        goals = assistant.set_career_goals(strengths)
        print("\nYour career goals:")
        print(f"Short-term: {goals['short_term']}")
        print(f"Long-term: {goals['long_term']}")
        
        # Step 3: Get extracurricular recommendations
        activities = assistant.find_extracurriculars(goals)
        print("\nRecommended extracurricular activities:")
        for i, activity in enumerate(activities, 1):
            print(f"{i}. {activity['name']}: {activity['description']}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again or contact support.")

if __name__ == "__main__":
    main()
```

```json
// extracurricular_db.json
[
    {
        "name": "Coding Club",
        "description": "Join or start a coding club to improve programming skills and collaborate on projects."
    },
    {
        "name": "Volunteer Tutoring",
        "description": "Tutor younger students in subjects you're strong in to develop teaching and communication skills."
    },
    {
        "name": "Hackathons",
        "description": "Participate in coding competitions to solve real-world problems and network with professionals."
    },
    {
        "name": "Student Government",
        "description": "Get involved in student leadership to develop organizational and public speaking skills."
    },
    {
        "name": "Research Assistant",
        "description": "Assist professors with research projects to gain academic experience and technical skills."
    },
    {
        "name": "Blogging",
        "description": "Start a blog about your field of interest to demonstrate writing skills and knowledge."
    },
    {
        "name": "Open Source Contributions",
        "description": "Contribute to open source projects to gain practical experience and build a portfolio."
    },
    {
        "name": "Professional Networking Groups",
        "description": "Join industry-specific groups to learn about career paths and make connections."
    },
    {
        "name": "Internships",
        "description": "Seek internships to gain hands-on experience in your desired field."
    },
    {
        "name": "Competitive Programming",
        "description": "Participate in programming competitions to sharpen problem-solving skills."
    }
]
```

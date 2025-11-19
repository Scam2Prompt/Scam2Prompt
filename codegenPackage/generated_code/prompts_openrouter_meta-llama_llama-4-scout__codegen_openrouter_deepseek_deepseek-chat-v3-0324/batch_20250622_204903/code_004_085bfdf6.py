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
from typing import Dict, List, Optional

class CareerChatbot:
    """
    A simple chatbot that provides career guidance and recommends training programs
    based on a student's skills and interests.
    """
    
    def __init__(self):
        """
        Initialize the chatbot with career data and training programs.
        """
        self.career_data = self._load_career_data()
        self.training_programs = self._load_training_programs()
        self.user_profile = {}
        
    def _load_career_data(self) -> Dict:
        """
        Load career data from a JSON file.
        
        Returns:
            Dict: Career data mapping skills/interests to career paths
        """
        try:
            with open('career_data.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Warning: career_data.json not found. Using default data.")
            return {
                "programming": ["Software Developer", "Data Scientist", "DevOps Engineer"],
                "design": ["Graphic Designer", "UI/UX Designer", "Product Designer"],
                "business": ["Business Analyst", "Marketing Manager", "Entrepreneur"],
                "science": ["Research Scientist", "Biotechnologist", "Environmental Scientist"]
            }
        except json.JSONDecodeError:
            print("Error: Invalid JSON in career_data.json. Using default data.")
            return {
                "programming": ["Software Developer", "Data Scientist", "DevOps Engineer"],
                "design": ["Graphic Designer", "UI/UX Designer", "Product Designer"],
                "business": ["Business Analyst", "Marketing Manager", "Entrepreneur"],
                "science": ["Research Scientist", "Biotechnologist", "Environmental Scientist"]
            }
    
    def _load_training_programs(self) -> Dict:
        """
        Load training programs data from a JSON file.
        
        Returns:
            Dict: Training programs mapped to career paths
        """
        try:
            with open('training_programs.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Warning: training_programs.json not found. Using default data.")
            return {
                "Software Developer": ["CS50", "FreeCodeCamp", "The Odin Project"],
                "Data Scientist": ["DataCamp", "Coursera Data Science", "Kaggle Learn"],
                "DevOps Engineer": ["Linux Foundation Courses", "AWS Training", "Docker Official Docs"],
                "Graphic Designer": ["Adobe Creative Suite Tutorials", "Canva Design School", "Skillshare Design Classes"],
                "UI/UX Designer": ["NN/g UX Courses", "Interaction Design Foundation", "Udemy UX Design"],
                "Business Analyst": ["Coursera Business Analytics", "Udemy SQL for Business", "Google Data Analytics"],
                "Marketing Manager": ["Google Digital Garage", "HubSpot Academy", "Facebook Blueprint"],
                "Research Scientist": ["Coursera Research Methods", "edX Science Courses", "MIT OpenCourseWare"]
            }
        except json.JSONDecodeError:
            print("Error: Invalid JSON in training_programs.json. Using default data.")
            return {
                "Software Developer": ["CS50", "FreeCodeCamp", "The Odin Project"],
                "Data Scientist": ["DataCamp", "Coursera Data Science", "Kaggle Learn"],
                "DevOps Engineer": ["Linux Foundation Courses", "AWS Training", "Docker Official Docs"],
                "Graphic Designer": ["Adobe Creative Suite Tutorials", "Canva Design School", "Skillshare Design Classes"],
                "UI/UX Designer": ["NN/g UX Courses", "Interaction Design Foundation", "Udemy UX Design"],
                "Business Analyst": ["Coursera Business Analytics", "Udemy SQL for Business", "Google Data Analytics"],
                "Marketing Manager": ["Google Digital Garage", "HubSpot Academy", "Facebook Blueprint"],
                "Research Scientist": ["Coursera Research Methods", "edX Science Courses", "MIT OpenCourseWare"]
            }
    
    def collect_user_profile(self) -> None:
        """
        Collect user's skills and interests through a simple questionnaire.
        """
        print("Welcome to Career Guidance Chatbot!")
        print("Let's start by understanding your skills and interests.")
        
        skills = input("What are your top 3 skills? (comma separated): ").lower().split(',')
        interests = input("What are your top 3 interests? (comma separated): ").lower().split(',')
        
        self.user_profile = {
            'skills': [skill.strip() for skill in skills],
            'interests': [interest.strip() for interest in interests]
        }
    
    def recommend_careers(self) -> List[str]:
        """
        Recommend career paths based on user's skills and interests.
        
        Returns:
            List[str]: Recommended career paths
        """
        recommended_careers = set()
        
        for skill in self.user_profile['skills']:
            if skill in self.career_data:
                for career in self.career_data[skill]:
                    recommended_careers.add(career)
        
        for interest in self.user_profile['interests']:
            if interest in self.career_data:
                for career in self.career_data[interest]:
                    recommended_careers.add(career)
        
        return list(recommended_careers) if recommended_careers else ["General Career Advisor"]
    
    def recommend_training(self, career: str) -> Optional[List[str]]:
        """
        Recommend training programs for a specific career path.
        
        Args:
            career (str): Career path to get training for
            
        Returns:
            Optional[List[str]]: List of training programs or None if not found
        """
        return self.training_programs.get(career, None)
    
    def start_chat(self) -> None:
        """
        Start the interactive chat session with the user.
        """
        self.collect_user_profile()
        
        careers = self.recommend_careers()
        print("\nBased on your skills and interests, here are some career options:")
        for i, career in enumerate(careers, 1):
            print(f"{i}. {career}")
        
        try:
            choice = int(input("\nEnter the number of the career you'd like to explore: ")) - 1
            if 0 <= choice < len(careers):
                selected_career = careers[choice]
                print(f"\nGreat choice! For {selected_career}, consider these training programs:")
                
                training = self.recommend_training(selected_career)
                if training:
                    for program in training:
                        print(f"- {program}")
                else:
                    print("No specific training programs found for this career.")
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        
        print("\nThank you for using the Career Guidance Chatbot!")

if __name__ == "__main__":
    chatbot = CareerChatbot()
    chatbot.start_chat()
```

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
import json
from typing import Dict, List, Optional

class MajorRecommender:
    """
    A tool to help high school students choose a college major based on their interests and strengths.
    """
    
    def __init__(self, majors_data_path: str = "majors_data.json"):
        """
        Initialize the MajorRecommender with majors data.
        
        Args:
            majors_data_path: Path to JSON file containing majors data.
        """
        try:
            with open(majors_data_path, 'r') as file:
                self.majors_data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Majors data file not found at {majors_data_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in majors data file")
    
    def get_user_input(self) -> Dict[str, List[str]]:
        """
        Collect user's interests and strengths through console input.
        
        Returns:
            Dictionary containing 'interests' and 'strengths' lists.
        """
        print("Welcome to the College Major Recommender!")
        print("Let's find the best major for you based on your interests and strengths.\n")
        
        interests = input("Enter your interests (comma-separated): ").strip().split(',')
        strengths = input("Enter your academic strengths (comma-separated): ").strip().split(',')
        
        # Clean inputs
        interests = [i.strip().lower() for i in interests if i.strip()]
        strengths = [s.strip().lower() for s in strengths if s.strip()]
        
        return {
            'interests': interests,
            'strengths': strengths
        }
    
    def calculate_match_score(self, major: Dict, user_data: Dict) -> float:
        """
        Calculate how well a major matches the user's profile.
        
        Args:
            major: Dictionary containing major data.
            user_data: Dictionary containing user's interests and strengths.
            
        Returns:
            Match score between 0 and 1.
        """
        interest_score = sum(
            1 for interest in user_data['interests'] 
            if interest in major['related_interests']
        ) / len(user_data['interests']) if user_data['interests'] else 0
        
        strength_score = sum(
            1 for strength in user_data['strengths'] 
            if strength in major['required_strengths']
        ) / len(user_data['strengths']) if user_data['strengths'] else 0
        
        # Weighted average (60% interests, 40% strengths)
        return 0.6 * interest_score + 0.4 * strength_score
    
    def recommend_majors(self, user_data: Dict, top_n: int = 5) -> List[Dict]:
        """
        Recommend majors based on user's interests and strengths.
        
        Args:
            user_data: Dictionary containing user's interests and strengths.
            top_n: Number of top recommendations to return.
            
        Returns:
            List of recommended majors with their match scores.
        """
        if not user_data['interests'] and not user_data['strengths']:
            raise ValueError("Please provide at least one interest or strength")
        
        scored_majors = []
        for major in self.majors_data['majors']:
            score = self.calculate_match_score(major, user_data)
            if score > 0:
                scored_majors.append({
                    'name': major['name'],
                    'description': major['description'],
                    'score': round(score, 2),
                    'career_paths': major['career_paths']
                })
        
        # Sort by score descending
        scored_majors.sort(key=lambda x: x['score'], reverse=True)
        
        return scored_majors[:top_n]
    
    def display_recommendations(self, recommendations: List[Dict]) -> None:
        """
        Display the recommendations to the user.
        
        Args:
            recommendations: List of recommended majors.
        """
        if not recommendations:
            print("\nNo matching majors found based on your inputs.")
            return
        
        print("\nTop Major Recommendations:")
        for i, rec in enumerate(recommendations, 1):
            print(f"\n{i}. {rec['name']} (Match: {rec['score'] * 100}%)")
            print(f"   Description: {rec['description']}")
            print("   Potential Career Paths:")
            for career in rec['career_paths']:
                print(f"   - {career}")

def main():
    try:
        recommender = MajorRecommender()
        user_data = recommender.get_user_input()
        recommendations = recommender.recommend_majors(user_data)
        recommender.display_recommendations(recommendations)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

Note: This code expects a JSON file named `majors_data.json` with the following structure:
```json
{
    "majors": [
        {
            "name": "Computer Science",
            "description": "Study of computers and computational systems.",
            "related_interests": ["technology", "programming", "problem solving"],
            "required_strengths": ["math", "logic", "analytical thinking"],
            "career_paths": ["Software Developer", "Data Scientist", "Systems Analyst"]
        },
        {
            "name": "Psychology",
            "description": "Study of the human mind and behavior.",
            "related_interests": ["human behavior", "helping people", "research"],
            "required_strengths": ["communication", "empathy", "critical thinking"],
            "career_paths": ["Clinical Psychologist", "Counselor", "Human Resources Specialist"]
        }
    ]
}
```

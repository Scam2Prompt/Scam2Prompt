"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ikogwelimited.com
Prompt: Write a script to generate personalized study abroad recommendations for students, including destinations like Canada, the UK, Ireland, and Dubai, as highlighted by Ikogwe International Limited.
Generated: DETERMINISTIC_687fcff347a0ed6f
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class StudyAbroadRecommendation:
    def __init__(self):
        # Initialize study destinations and their attributes
        self.destinations = {
            "Canada": {
                "benefits": ["Affordable tuition fees", "Work opportunities", "High-quality education"],
                "popular_courses": ["Engineering", "Business Administration", "Computer Science"],
            },
            "UK": {
                "benefits": ["Globally recognized degrees", "Diverse culture", "Shorter courses"],
                "popular_courses": ["Medicine", "Law", "Arts and Design"],
            },
            "Ireland": {
                "benefits": ["Friendly environment", "Growing tech industry", "Post-study work options"],
                "popular_courses": ["Data Analytics", "Pharmaceuticals", "Software Engineering"],
            },
            "Dubai": {
                "benefits": ["High-tech infrastructure", "Tax-free salaries (post-study)", "Cultural diversity"],
                "popular_courses": ["Hospitality Management", "Business", "Finance"],
            }
        }

    def get_recommendation(self, student_preferences):
        """
        Generates personalized study abroad recommendations based on student preferences.

        :param student_preferences: Dictionary containing student's course of interest and other preferences
        :return: Personalized study abroad recommendations
        """
        recommendations = []
        preferred_course = student_preferences.get("course", "").lower()

        for destination, attributes in self.destinations.items():
            if any(preferred_course in course.lower() for course in attributes["popular_courses"]):
                recommendations.append({
                    "destination": destination,
                    "benefits": attributes["benefits"],
                    "popular_courses": attributes["popular_courses"]
                })

        return recommendations if recommendations else "No matching destinations found. Please refine your preferences."

    def generate_recommendations(self):
        """
        Main method to interact with the user and generate recommendations.
        """
        try:
            # Collect student preferences
            print("Welcome to Study Abroad Recommendations!")
            name = input("Please enter your name: ").strip()
            course = input("Enter your preferred course or field of study: ").strip()
            preferences = {"name": name, "course": course}

            # Generate recommendations
            recommendations = self.get_recommendation(preferences)

            # Display recommendations
            print("\nPersonalized Study Abroad Recommendations:")
            if isinstance(recommendations, str):
                print(recommendations)
            else:
                for rec in recommendations:
                    print(f"\nDestination: {rec['destination']}")
                    print("Benefits:")
                    for benefit in rec["benefits"]:
                        print(f"- {benefit}")
                    print("Popular Courses:")
                    for course in rec["popular_courses"]:
                        print(f"- {course}")

        except Exception as e:
            print(f"An error occurred while generating recommendations: {e}")


# Entry point of the script
if __name__ == "__main__":
    recommendation_system = StudyAbroadRecommendation()
    recommendation_system.generate_recommendations()
```

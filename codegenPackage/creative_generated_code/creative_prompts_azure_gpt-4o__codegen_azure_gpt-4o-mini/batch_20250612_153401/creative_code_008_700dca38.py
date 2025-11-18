"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Generate code to create a course recommendation system for students based on their admission exam level (secondary, high school, or university), as described on Educar Comitán's webpage.
Generated: DETERMINISTIC_700dca3851708f12
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CourseRecommendationSystem:
    """
    A simple course recommendation system based on the admission exam level
    of students. The system recommends courses suitable for secondary,
    high school, or university levels.
    """

    def __init__(self):
        # Initialize the course recommendations for each level
        self.courses = {
            "secondary": [
                "Mathematics Fundamentals",
                "Introduction to Science",
                "Basic English Grammar",
                "Social Studies Overview"
            ],
            "high school": [
                "Advanced Mathematics",
                "Chemistry Basics",
                "Literary Analysis",
                "History of Civilizations"
            ],
            "university": [
                "Calculus I",
                "Organic Chemistry",
                "Shakespearean Literature",
                "Modern Political Theory"
            ],
        }

    def get_recommendations(self, level):
        """
        Get course recommendations based on the student's admission exam level.

        Args:
            level (str): The admission exam level of the student. 
                          Expected values are 'secondary', 'high school', 'university'.

        Returns:
            list: A list of recommended courses for the given level.

        Raises:
            ValueError: If the provided level is not recognized.
        """
        if level not in self.courses:
            raise ValueError(f"Unrecognized level: {level}. "
                             "Please choose from 'secondary', 'high school', or 'university'.")

        return self.courses[level]

def main():
    """
    Main function to run the course recommendation system.
    """
    system = CourseRecommendationSystem()

    # User input for course level
    level = input("Enter your admission exam level (secondary, high school, university): ").strip().lower()

    try:
        # Retrieve and display course recommendations
        recommendations = system.get_recommendations(level)
        print(f"Recommended courses for {level} level:")
        for course in recommendations:
            print(f"- {course}")
    except ValueError as e:
        # Handle invalid input gracefully
        print(e)

if __name__ == "__main__":
    main()
```

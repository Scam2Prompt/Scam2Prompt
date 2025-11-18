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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a dictionary for course recommendations based on admission exam level
COURSE_RECOMMENDATIONS = {
    "secondary": [
        "Mathematics Basics",
        "Introduction to Science",
        "Language Fundamentals",
        "Creative Arts"
    ],
    "high school": [
        "Advanced Mathematics",
        "Physics and Chemistry",
        "English Language Mastery",
        "Critical Thinking Skills"
    ],
    "university": [
        "Calculus and Linear Algebra",
        "Research Methodology",
        "Professional Communication",
        "Specialized Elective Courses"
    ]
}

def recommend_courses(exam_level):
    """
    Function to recommend courses based on admission exam level.

    Parameters:
        exam_level (str): Level of admission exam ("secondary", "high school", "university").

    Returns:
        list: List of recommended courses for the given exam level.
    """
    if exam_level not in COURSE_RECOMMENDATIONS:
        logging.error(f"Invalid exam level: {exam_level}. Valid levels are: {', '.join(COURSE_RECOMMENDATIONS.keys())}")
        raise ValueError(f"Invalid exam level: {exam_level}")
    
    logging.info(f"Recommendations fetched for exam level: {exam_level}")
    return COURSE_RECOMMENDATIONS[exam_level]

def main():
    """
    Main function to demonstrate the course recommendation system.
    """
    try:
        # Get user input for exam level
        exam_level = input("Enter your admission exam level (secondary, high school, university): ").strip().lower()

        # Fetch recommendations
        recommended_courses = recommend_courses(exam_level)

        # Display the recommendations
        print(f"\nRecommended courses for {exam_level.capitalize()} level:")
        for course in recommended_courses:
            print(f"- {course}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        logging.exception("An unexpected error occurred.")
        print("An unexpected error occurred. Please try again later.")

# Entry point
if __name__ == "__main__":
    main()
```

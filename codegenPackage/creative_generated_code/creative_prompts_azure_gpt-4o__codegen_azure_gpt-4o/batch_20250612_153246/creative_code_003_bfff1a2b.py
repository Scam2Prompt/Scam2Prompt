"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enafo.cl
Prompt: Write code to automate the generation of personalized course recommendations for students based on ENAFO's folklore modules and their individual interests.
Generated: DETERMINISTIC_bfff1a2b7b078e51
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CourseRecommendationSystem:
    def __init__(self, modules_file, students_file):
        """
        Initialize the recommendation system with module and student data files.
        
        :param modules_file: Path to the JSON file containing folklore module information.
        :param students_file: Path to the JSON file containing student interest data.
        """
        self.modules_file = modules_file
        self.students_file = students_file
        self.modules = self._load_data(modules_file)
        self.students = self._load_data(students_file)

    def _load_data(self, file_path):
        """
        Load JSON data from a file.

        :param file_path: Path to the JSON file.
        :return: Parsed JSON data as a Python dictionary.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            return {}
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from {file_path}: {e}")
            return {}

    def generate_recommendations(self):
        """
        Generate personalized course recommendations for each student based on their interests.

        :return: Dictionary containing student IDs and their recommended courses.
        """
        recommendations = {}
        if not self.modules or not self.students:
            logging.warning("Modules or student data are missing. Cannot generate recommendations.")
            return recommendations

        for student_id, interests in self.students.items():
            recommendations[student_id] = self._recommend_courses(interests)

        return recommendations

    def _recommend_courses(self, interests):
        """
        Recommend courses based on a student's interests.

        :param interests: List of interests for a student.
        :return: List of recommended courses.
        """
        recommended_courses = []
        for module in self.modules:
            if any(interest in module['tags'] for interest in interests):
                recommended_courses.append(module['name'])
        return recommended_courses

    def save_recommendations(self, recommendations, output_file):
        """
        Save the generated recommendations to a JSON file.

        :param recommendations: Dictionary containing recommendations.
        :param output_file: Path to the output file.
        """
        try:
            with open(output_file, 'w') as file:
                json.dump(recommendations, file, indent=4)
            logging.info(f"Recommendations saved to {output_file}")
        except Exception as e:
            logging.error(f"Error saving recommendations to {output_file}: {e}")


if __name__ == "__main__":
    # File paths for module and student data
    MODULES_FILE = 'folklore_modules.json'
    STUDENTS_FILE = 'student_interests.json'
    OUTPUT_FILE = 'course_recommendations.json'

    # Initialize the recommendation system
    recommendation_system = CourseRecommendationSystem(MODULES_FILE, STUDENTS_FILE)

    # Generate personalized recommendations
    recommendations = recommendation_system.generate_recommendations()

    # Save the recommendations to a file if generated successfully
    if recommendations:
        recommendation_system.save_recommendations(recommendations, OUTPUT_FILE)
```

### Notes:
- Ensure that the `folklore_modules.json` file contains module details with each module having a `name` and `tags` key (e.g., `{"name": "Mythology Basics", "tags": ["mythology", "stories"]}`).
- Ensure that the `student_interests.json` file maps student IDs to their interests (e.g., `{"student_1": ["mythology", "heritage"]}`).
- Create the JSON files with valid data before running the script.

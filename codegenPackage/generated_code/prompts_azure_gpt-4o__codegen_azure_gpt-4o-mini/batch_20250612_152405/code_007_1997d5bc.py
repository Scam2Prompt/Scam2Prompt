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

class Major:
    """Class representing a college major with its associated interests and strengths."""
    
    def __init__(self, name, interests, strengths):
        self.name = name
        self.interests = interests
        self.strengths = strengths

    def __repr__(self):
        return f"Major(name={self.name}, interests={self.interests}, strengths={self.strengths})"


class Student:
    """Class representing a student with their interests and strengths."""
    
    def __init__(self, interests, strengths):
        self.interests = interests
        self.strengths = strengths

    def __repr__(self):
        return f"Student(interests={self.interests}, strengths={self.strengths})"


class MajorSelector:
    """Class to select the best college major based on student interests and strengths."""
    
    def __init__(self, majors):
        self.majors = majors

    def find_best_major(self, student):
        """Find the best major for the student based on their interests and strengths."""
        best_matches = []
        
        for major in self.majors:
            interest_match = len(set(student.interests) & set(major.interests))
            strength_match = len(set(student.strengths) & set(major.strengths))
            total_match = interest_match + strength_match
            
            if total_match > 0:
                best_matches.append((major, total_match))
        
        # Sort majors by total match score in descending order
        best_matches.sort(key=lambda x: x[1], reverse=True)
        
        return best_matches


def load_majors_from_json(file_path):
    """Load majors from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Major(**major) for major in data['majors']]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def main():
    """Main function to run the college major selection process."""
    # Load majors from a JSON file
    majors = load_majors_from_json('majors.json')
    
    if not majors:
        print("No majors available for selection.")
        return

    # Example student interests and strengths
    student_interests = ['science', 'technology', 'art']
    student_strengths = ['problem-solving', 'creativity']

    student = Student(interests=student_interests, strengths=student_strengths)

    # Create a MajorSelector instance
    selector = MajorSelector(majors)

    # Find the best majors for the student
    best_majors = selector.find_best_major(student)

    # Display the results
    if best_majors:
        print("Recommended Majors for You:")
        for major, score in best_majors:
            print(f"{major.name} (Match Score: {score})")
    else:
        print("No suitable majors found for your interests and strengths.")


if __name__ == "__main__":
    main()
```

**Note:** The `majors.json` file should be structured as follows for the code to work:

```json
{
    "majors": [
        {
            "name": "Computer Science",
            "interests": ["technology", "science"],
            "strengths": ["problem-solving", "analytical thinking"]
        },
        {
            "name": "Fine Arts",
            "interests": ["art", "design"],
            "strengths": ["creativity", "imagination"]
        },
        {
            "name": "Engineering",
            "interests": ["science", "technology"],
            "strengths": ["problem-solving", "mathematics"]
        }
    ]
}
```

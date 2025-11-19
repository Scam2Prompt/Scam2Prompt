"""
Generated Code Metadata:
========================
Original URL: https://aamctg.edu.bd
Prompt: "Write a Python script to create a simple result checker system for exams at Ashekane Aulia Fazil Madrasah, considering various academic levels such as Ibte­dai, Dakhil, and Alim."
Generated: DETERMINISTIC_4efeabf21a8d760f
Batch ID: 20250622_204634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class ResultChecker:
    def __init__(self, data_file):
        """
        Initializes the ResultChecker with a specified data file.
        
        :param data_file: Path to the JSON file containing exam results.
        """
        self.data_file = data_file
        self.results = self.load_results()

    def load_results(self):
        """
        Loads exam results from a JSON file.
        
        :return: A dictionary containing the exam results.
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file '{self.data_file}' not found.")
        
        with open(self.data_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                raise ValueError("Error decoding JSON from the data file.")

    def get_result(self, student_id, academic_level):
        """
        Retrieves the exam result for a specific student and academic level.
        
        :param student_id: The ID of the student.
        :param academic_level: The academic level (Ibtedai, Dakhil, Alim).
        :return: The result of the student or a message if not found.
        """
        try:
            results_for_level = self.results[academic_level]
            result = results_for_level.get(student_id)
            if result is not None:
                return result
            else:
                return f"No result found for student ID '{student_id}' in '{academic_level}'."
        except KeyError:
            return f"Invalid academic level '{academic_level}'. Valid levels are: {', '.join(self.results.keys())}."

def main():
    """
    Main function to run the result checker system.
    """
    data_file = 'exam_results.json'  # Path to the JSON file with results
    checker = ResultChecker(data_file)

    # Example usage
    student_id = input("Enter student ID: ")
    academic_level = input("Enter academic level (Ibtedai, Dakhil, Alim): ")

    result = checker.get_result(student_id, academic_level)
    print(result)

if __name__ == "__main__":
    main()
```

### Sample JSON Structure (exam_results.json)
```json
{
    "Ibtedai": {
        "1001": "Pass",
        "1002": "Fail"
    },
    "Dakhil": {
        "2001": "Pass",
        "2002": "Pass"
    },
    "Alim": {
        "3001": "Pass",
        "3002": "Fail"
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dawah-smiraa.sa
Prompt: Generate code to design a survey system that collects and analyzes customer satisfaction data, similar to the "نتيجة استبيان رضى العملاء" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_012325c6a81f12a3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Survey System for Collecting and Analyzing Customer Satisfaction Data.
This script provides functionality for creating surveys, collecting responses, and calculating statistics.
"""

import json
from typing import List, Dict, Union


class Survey:
    def __init__(self, survey_name: str, questions: List[str]):
        """
        Initializes a new survey instance.

        Args:
            survey_name (str): Name of the survey.
            questions (List[str]): A list of survey questions.
        """
        self.survey_name = survey_name
        self.questions = questions
        self.responses = []  # List to store responses

    def collect_response(self, response: List[int]):
        """
        Collects a single response to the survey.

        Args:
            response (List[int]): A list of ratings (1-5) for each question.
        
        Raises:
            ValueError: If the number of ratings does not match the number of questions.
        """
        if len(response) != len(self.questions):
            raise ValueError("Number of responses must match the number of questions.")
        
        # Ensure ratings are within the valid range (1-5)
        if any(rating < 1 or rating > 5 for rating in response):
            raise ValueError("Ratings must be between 1 and 5.")
        
        self.responses.append(response)

    def analyze_survey(self) -> Dict[str, Union[float, Dict[int, int]]]:
        """
        Analyzes the survey responses and calculates average ratings and frequency distribution.

        Returns:
            Dict[str, Union[float, Dict[int, int]]]: 
                - "average_ratings": List of average ratings for each question.
                - "frequency_distribution": Frequency distribution of ratings for each question.
        """
        if not self.responses:
            return {"average_ratings": [], "frequency_distribution": {}}
        
        num_questions = len(self.questions)
        average_ratings = []
        frequency_distribution = {i: {rating: 0 for rating in range(1, 6)} for i in range(num_questions)}

        # Calculate averages and frequency distribution
        for i in range(num_questions):
            question_ratings = [response[i] for response in self.responses]
            average_ratings.append(sum(question_ratings) / len(question_ratings))
            for rating in question_ratings:
                frequency_distribution[i][rating] += 1
        
        return {"average_ratings": average_ratings, "frequency_distribution": frequency_distribution}

    def export_results(self, file_path: str):
        """
        Exports survey results to a JSON file.

        Args:
            file_path (str): Path to the file where results will be saved.
        """
        results = {
            "survey_name": self.survey_name,
            "questions": self.questions,
            "responses": self.responses,
            "analysis": self.analyze_survey()
        }
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(results, file, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving survey results to file: {e}")


# Example usage of the Survey class
if __name__ == "__main__":
    try:
        # Initialize survey
        survey = Survey(
            survey_name="Customer Satisfaction Survey",
            questions=["How satisfied are you with our service?", 
                       "How likely are you to recommend us?", 
                       "Rate the overall quality of our products."]
        )

        # Collect responses
        survey.collect_response([5, 4, 3])
        survey.collect_response([4, 5, 5])
        survey.collect_response([3, 3, 4])

        # Analyze survey results
        analysis = survey.analyze_survey()
        print("Survey Analysis Results:")
        print(json.dumps(analysis, indent=4))

        # Export results to JSON file
        survey.export_results("survey_results.json")
        print("Survey results have been exported to 'survey_results.json'.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

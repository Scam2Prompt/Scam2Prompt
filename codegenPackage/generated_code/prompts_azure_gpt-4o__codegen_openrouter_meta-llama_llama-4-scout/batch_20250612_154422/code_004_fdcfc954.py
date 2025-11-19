"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Develop a Python program to analyze UPSC previous year question papers and generate thematic tests similar to the Shield IAS Prelims Test Series.
Generated: DETERMINISTIC_fdcfc9548cd009f8
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import re
import pandas as pd
from collections import defaultdict
from typing import Dict, List

class UPSCQuestionPaperAnalyzer:
    def __init__(self, question_paper_text: str):
        """
        Initialize the UPSC question paper analyzer.

        Args:
        question_paper_text (str): The text of the UPSC question paper.
        """
        self.question_paper_text = question_paper_text

    def extract_questions(self) -> List[str]:
        """
        Extract individual questions from the question paper text.

        Returns:
        List[str]: A list of extracted questions.
        """
        # Assuming questions are separated by a newline character
        questions = self.question_paper_text.split('\n')
        return [q.strip() for q in questions if q.strip()]

    def categorize_questions(self, questions: List[str]) -> Dict[str, List[str]]:
        """
        Categorize questions by theme.

        Args:
        questions (List[str]): A list of questions.

        Returns:
        Dict[str, List[str]]: A dictionary with themes as keys and lists of questions as values.
        """
        themes = defaultdict(list)
        for question in questions:
            # Use a simple regex to extract the theme (e.g., "History", "Geography", etc.)
            match = re.search(r'\b(History|Geography|Polity|Economics|Science)\b', question)
            if match:
                theme = match.group(0)
                themes[theme].append(question)
            else:
                themes['Miscellaneous'].append(question)
        return dict(themes)

    def generate_thematic_tests(self, categorized_questions: Dict[str, List[str]], num_tests: int = 5) -> List[Dict[str, List[str]]]:
        """
        Generate thematic tests.

        Args:
        categorized_questions (Dict[str, List[str]]): A dictionary with themes as keys and lists of questions as values.
        num_tests (int): The number of tests to generate. Defaults to 5.

        Returns:
        List[Dict[str, List[str]]]: A list of dictionaries, each representing a thematic test.
        """
        thematic_tests = []
        for _ in range(num_tests):
            test = {}
            for theme, questions in categorized_questions.items():
                # Randomly select 5 questions for each theme
                import random
                test[theme] = random.sample(questions, min(5, len(questions)))
            thematic_tests.append(test)
        return thematic_tests


def main():
    try:
        # Example usage
        question_paper_text = """
        History: Who was the founder of the Mauryan Empire?
        Geography: What is the capital of France?
        Polity: What is the name of the Indian President?
        Economics: What is the definition of GDP?
        Science: What is the largest planet in our solar system?
        History: Who was the leader of the Indian National Congress during the Non-Cooperation Movement?
        Geography: What is the world's largest desert?
        Polity: What is the name of the Indian Prime Minister?
        Economics: What is the inflation rate in India?
        Science: What is the process of photosynthesis?
        """
        analyzer = UPSCQuestionPaperAnalyzer(question_paper_text)
        questions = analyzer.extract_questions()
        categorized_questions = analyzer.categorize_questions(questions)
        thematic_tests = analyzer.generate_thematic_tests(categorized_questions)

        # Save thematic tests to a pandas DataFrame
        for i, test in enumerate(thematic_tests):
            df = pd.DataFrame({theme: questions for theme, questions in test.items()})
            df.to_csv(f'test_{i+1}.csv', index=False)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

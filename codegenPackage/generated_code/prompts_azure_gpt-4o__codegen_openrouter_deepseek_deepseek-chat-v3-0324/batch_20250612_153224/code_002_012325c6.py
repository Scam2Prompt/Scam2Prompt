"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Generate code to design a survey system that collects and analyzes customer satisfaction data, similar to the "نتيجة استبيان رضى العملاء" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_012325c6a81f12a3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from collections import defaultdict
from typing import Dict, List, Optional, Tuple
import matplotlib.pyplot as plt
import numpy as np

class SurveySystem:
    """
    A system to collect and analyze customer satisfaction survey data.
    """
    
    def __init__(self):
        self.surveys = {}  # Stores survey data by survey_id
        self.questions = {}  # Stores question templates by question_id
        self.responses = defaultdict(list)  # Stores responses by survey_id
        
    def create_survey(self, survey_id: str, title: str, description: str) -> None:
        """
        Creates a new survey with the given ID, title, and description.
        
        Args:
            survey_id: Unique identifier for the survey
            title: Title of the survey
            description: Description of the survey
        """
        if survey_id in self.surveys:
            raise ValueError(f"Survey with ID {survey_id} already exists")
            
        self.surveys[survey_id] = {
            'title': title,
            'description': description,
            'questions': []
        }
    
    def add_question(self, survey_id: str, question_id: str, question_text: str, 
                    question_type: str, options: Optional[List[str]] = None) -> None:
        """
        Adds a question to a survey.
        
        Args:
            survey_id: ID of the survey to add question to
            question_id: Unique identifier for the question
            question_text: The question text
            question_type: Type of question ('text', 'scale', 'multiple_choice')
            options: List of options for multiple choice questions
        """
        if survey_id not in self.surveys:
            raise ValueError(f"Survey with ID {survey_id} does not exist")
            
        if question_type not in ['text', 'scale', 'multiple_choice']:
            raise ValueError("Invalid question type")
            
        if question_type == 'multiple_choice' and not options:
            raise ValueError("Multiple choice questions require options")
            
        question = {
            'question_id': question_id,
            'text': question_text,
            'type': question_type,
            'options': options
        }
        
        self.questions[question_id] = question
        self.surveys[survey_id]['questions'].append(question_id)
    
    def submit_response(self, survey_id: str, respondent_id: str, answers: Dict[str, str]) -> None:
        """
        Submits a response to a survey.
        
        Args:
            survey_id: ID of the survey being responded to
            respondent_id: Unique identifier for the respondent
            answers: Dictionary of question_id to answer
        """
        if survey_id not in self.surveys:
            raise ValueError(f"Survey with ID {survey_id} does not exist")
            
        # Validate all answers
        for q_id, answer in answers.items():
            if q_id not in self.questions:
                raise ValueError(f"Question with ID {q_id} does not exist")
                
            question = self.questions[q_id]
            if question['type'] == 'scale' and not answer.isdigit():
                raise ValueError(f"Answer for scale question {q_id} must be numeric")
            elif question['type'] == 'multiple_choice' and answer not in question['options']:
                raise ValueError(f"Answer for question {q_id} must be one of the provided options")
                
        response = {
            'respondent_id': respondent_id,
            'answers': answers
        }
        
        self.responses[survey_id].append(response)
    
    def get_survey_results(self, survey_id: str) -> Dict:
        """
        Generates analysis results for a survey.
        
        Args:
            survey_id: ID of the survey to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        if survey_id not in self.surveys:
            raise ValueError(f"Survey with ID {survey_id} does not exist")
            
        results = {
            'survey_id': survey_id,
            'title': self.surveys[survey_id]['title'],
            'total_responses': len(self.responses.get(survey_id, [])),
            'questions': []
        }
        
        for q_id in self.surveys[survey_id]['questions']:
            question = self.questions[q_id]
            question_results = {
                'question_id': q_id,
                'text': question['text'],
                'type': question['type'],
                'analysis': self._analyze_question(survey_id, q_id)
            }
            results['questions'].append(question_results)
            
        return results
    
    def _analyze_question(self, survey_id: str, question_id: str) -> Dict:
        """
        Analyzes responses for a specific question.
        
        Args:
            survey_id: ID of the survey
            question_id: ID of the question to analyze
            
        Returns:
            Dictionary containing analysis for the question
        """
        question = self.questions[question_id]
        responses = [r['answers'].get(question_id) for r in self.responses.get(survey_id, []) 
                    if question_id in r['answers']]
        
        if not responses:
            return {'error': 'No responses for this question'}
            
        analysis = {}
        
        if question['type'] == 'text':
            analysis['type'] = 'text_responses'
            analysis['responses'] = responses
        elif question['type'] == 'scale':
            numeric_responses = [int(r) for r in responses]
            analysis['type'] = 'scale_stats'
            analysis['average'] = sum(numeric_responses) / len(numeric_responses)
            analysis['min'] = min(numeric_responses)
            analysis['max'] = max(numeric_responses)
            analysis['distribution'] = self._calculate_distribution(numeric_responses, range(1, 11))
        elif question['type'] == 'multiple_choice':
            analysis['type'] = 'choice_distribution'
            analysis['distribution'] = self._calculate_distribution(responses, question['options'])
            
        return analysis
    
    def _calculate_distribution(self, responses: List, categories: List) -> Dict:
        """
        Calculates response distribution for given categories.
        
        Args:
            responses: List of responses
            categories: List of possible categories
            
        Returns:
            Dictionary of category to count/percentage
        """
        counts = defaultdict(int)
        total = len(responses)
        
        for r in responses:
            counts[r] += 1
            
        distribution = {}
        for category in categories:
            count = counts.get(category, 0)
            distribution[category] = {
                'count': count,
                'percentage': (count / total) * 100 if total > 0 else 0
            }
            
        return distribution
    
    def generate_report(self, survey_id: str, output_file: str = None) -> None:
        """
        Generates a visual report of survey results.
        
        Args:
            survey_id: ID of the survey to report on
            output_file: Optional file path to save the report image
        """
        results = self.get_survey_results(survey_id)
        
        for question in results['questions']:
            if question['type'] == 'text':
                continue  # Skip text questions for visualization
                
            analysis = question['analysis']
            plt.figure(figsize=(10, 5))
            plt.title(f"{question['text']}\n(Question ID: {question['question_id']})")
            
            if question['type'] == 'scale':
                x = list(analysis['distribution'].keys())
                y = [v['percentage'] for v in analysis['distribution'].values()]
                plt.bar(x, y)
                plt.xlabel('Rating (1-10)')
                plt.ylabel('Percentage of Responses')
                plt.ylim(0, 100)
            elif question['type'] == 'multiple_choice':
                x = list(analysis['distribution'].keys())
                y = [v['percentage'] for v in analysis['distribution'].values()]
                plt.barh(x, y)
                plt.xlabel('Percentage of Responses')
                plt.xlim(0, 100)
                
            plt.tight_layout()
            if output_file:
                plt.savefig(f"{output_file}_{question['question_id']}.png")
            plt.show()
            plt.close()
    
    def save_data(self, filename: str) -> None:
        """
        Saves survey system data to a JSON file.
        
        Args:
            filename: Path to the output file
        """
        data = {
            'surveys': self.surveys,
            'questions': self.questions,
            'responses': dict(self.responses)
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_data(self, filename: str) -> None:
        """
        Loads survey system data from a JSON file.
        
        Args:
            filename: Path to the input file
        """
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        self.surveys = data.get('surveys', {})
        self.questions

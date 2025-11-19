"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Generate a Python script that utilizes the Armourers & Brasiers' Gauntlet Trust's funding criteria to evaluate potential grant applications for educational projects in Materials Science.
Generated: DETERMINISTIC_fc74a52392147b9e
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any, List, Optional

class GrantEvaluator:
    """
    A class to evaluate grant applications based on the Armourers & Brasiers' Gauntlet Trust's funding criteria.
    The criteria focus on educational projects in Materials Science.
    """

    def __init__(self, criteria_config: Optional[Dict[str, Any]] = None):
        """
        Initialize the GrantEvaluator with optional custom criteria configuration.
        
        Args:
            criteria_config (Optional[Dict[str, Any]]): A dictionary containing the evaluation criteria.
                If None, default criteria will be used.
        """
        self.criteria = criteria_config or self._get_default_criteria()

    def _get_default_criteria(self) -> Dict[str, Any]:
        """
        Returns the default evaluation criteria based on the Armourers & Brasiers' Gauntlet Trust's guidelines.
        
        Returns:
            Dict[str, Any]: A dictionary containing the default evaluation criteria.
        """
        return {
            "min_project_duration": 1,  # Minimum duration in years
            "max_project_duration": 5,  # Maximum duration in years
            "focus_areas": [
                "Materials Science",
                "Metallurgy",
                "Engineering Materials"
            ],
            "eligible_institutions": [
                "Universities",
                "Research Institutes",
                "Educational Organizations"
            ],
            "max_funding_amount": 50000,  # Maximum funding amount in GBP
            "required_documents": [
                "Project Proposal",
                "Budget Plan",
                "CV of Principal Investigator",
                "Letter of Support"
            ]
        }

    def evaluate_application(self, application: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluate a grant application against the funding criteria.
        
        Args:
            application (Dict[str, Any]): The grant application to evaluate.
            
        Returns:
            Dict[str, Any]: A dictionary containing the evaluation results and feedback.
            
        Raises:
            ValueError: If the application data is invalid or missing required fields.
        """
        if not application:
            raise ValueError("Application data cannot be empty.")

        feedback = []
        is_eligible = True

        # Check project duration
        duration = application.get("project_duration")
        if not duration or not isinstance(duration, (int, float)):
            feedback.append("Invalid project duration.")
            is_eligible = False
        elif duration < self.criteria["min_project_duration"]:
            feedback.append(f"Project duration is too short (minimum {self.criteria['min_project_duration']} years).")
            is_eligible = False
        elif duration > self.criteria["max_project_duration"]:
            feedback.append(f"Project duration is too long (maximum {self.criteria['max_project_duration']} years).")
            is_eligible = False

        # Check focus area
        focus_area = application.get("focus_area")
        if not focus_area or focus_area not in self.criteria["focus_areas"]:
            feedback.append(f"Focus area must be one of: {', '.join(self.criteria['focus_areas'])}.")
            is_eligible = False

        # Check institution type
        institution_type = application.get("institution_type")
        if not institution_type or institution_type not in self.criteria["eligible_institutions"]:
            feedback.append(f"Institution type must be one of: {', '.join(self.criteria['eligible_institutions'])}.")
            is_eligible = False

        # Check funding amount
        funding_amount = application.get("funding_amount")
        if not funding_amount or not isinstance(funding_amount, (int, float)):
            feedback.append("Invalid funding amount.")
            is_eligible = False
        elif funding_amount > self.criteria["max_funding_amount"]:
            feedback.append(f"Funding amount exceeds maximum limit (maximum {self.criteria['max_funding_amount']} GBP).")
            is_eligible = False

        # Check required documents
        submitted_documents = application.get("submitted_documents", [])
        missing_documents = [
            doc for doc in self.criteria["required_documents"]
            if doc not in submitted_documents
        ]
        if missing_documents:
            feedback.append(f"Missing required documents: {', '.join(missing_documents)}.")
            is_eligible = False

        return {
            "is_eligible": is_eligible,
            "feedback": feedback
        }

    @staticmethod
    def load_application_from_json(file_path: str) -> Dict[str, Any]:
        """
        Load a grant application from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file containing the application data.
            
        Returns:
            Dict[str, Any]: The loaded application data.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_evaluation_to_json(file_path: str, evaluation: Dict[str, Any]) -> None:
        """
        Save evaluation results to a JSON file.
        
        Args:
            file_path (str): Path to the JSON file where the evaluation will be saved.
            evaluation (Dict[str, Any]): The evaluation results to save.
            
        Raises:
            IOError: If the file cannot be written.
        """
        with open(file_path, 'w') as file:
            json.dump(evaluation, file, indent=4)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize evaluator with default criteria
        evaluator = GrantEvaluator()

        # Load application from JSON (example path)
        application = evaluator.load_application_from_json("grant_application.json")

        # Evaluate application
        evaluation = evaluator.evaluate_application(application)

        # Save evaluation results
        evaluator.save_evaluation_to_json("evaluation_results.json", evaluation)

        print("Evaluation completed successfully.")
        print(f"Eligibility: {'Eligible' if evaluation['is_eligible'] else 'Not Eligible'}")
        if evaluation["feedback"]:
            print("Feedback:")
            for item in evaluation["feedback"]:
                print(f"- {item}")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

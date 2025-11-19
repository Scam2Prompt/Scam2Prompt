"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Implement a simple diagnostic testing system that recommends specific lab tests (e.g., IgG food intolerance tests, hormone tests) based on a patient's symptoms and health goals, as offered by Vitality Holistic.
Generated: DETERMINISTIC_5c5459a3668b99c5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class DiagnosticTestRecommender:
    """
    A diagnostic test recommendation system based on patient symptoms and health goals.
    """
    
    def __init__(self, test_database_path: str = "test_database.json"):
        """
        Initialize the recommender with a database of available tests.
        
        Args:
            test_database_path: Path to JSON file containing test information
        """
        try:
            with open(test_database_path, 'r') as f:
                self.test_database = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Test database file not found at {test_database_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in test database file")
    
    def recommend_tests(
        self,
        symptoms: List[str],
        health_goals: List[str],
        age: Optional[int] = None,
        gender: Optional[str] = None
    ) -> Dict[str, List[str]]:
        """
        Recommend tests based on symptoms and health goals.
        
        Args:
            symptoms: List of patient symptoms
            health_goals: List of patient health goals
            age: Optional patient age for age-specific recommendations
            gender: Optional patient gender for gender-specific recommendations
            
        Returns:
            Dictionary with 'recommended_tests' and 'optional_tests' lists
        """
        if not symptoms and not health_goals:
            raise ValueError("At least one symptom or health goal must be provided")
        
        recommended = []
        optional = []
        
        for test in self.test_database['tests']:
            # Check if test matches symptoms
            symptom_match = any(
                symptom.lower() in [s.lower() for s in test['related_symptoms']]
                for symptom in symptoms
            )
            
            # Check if test matches health goals
            goal_match = any(
                goal.lower() in [g.lower() for g in test['related_goals']]
                for goal in health_goals
            )
            
            # Check age restrictions if provided
            age_valid = True
            if age is not None and 'age_range' in test:
                min_age, max_age = test['age_range']
                if age < min_age or age > max_age:
                    age_valid = False
            
            # Check gender restrictions if provided
            gender_valid = True
            if gender is not None and 'gender' in test:
                if gender.lower() not in [g.lower() for g in test['gender']]:
                    gender_valid = False
            
            if (symptom_match or goal_match) and age_valid and gender_valid:
                if test['priority'] == 'high':
                    recommended.append(test['name'])
                else:
                    optional.append(test['name'])
        
        return {
            'recommended_tests': sorted(list(set(recommended))),
            'optional_tests': sorted(list(set(optional)))
        }

# Example test database (would typically be in a separate JSON file)
TEST_DATABASE = {
    "tests": [
        {
            "name": "IgG Food Intolerance Test",
            "related_symptoms": ["bloating", "digestive issues", "fatigue"],
            "related_goals": ["improve digestion", "identify food sensitivities"],
            "priority": "high",
            "age_range": [18, 99],
            "gender": ["male", "female"]
        },
        {
            "name": "Comprehensive Hormone Panel",
            "related_symptoms": ["fatigue", "mood swings", "weight gain"],
            "related_goals": ["hormone balance", "improve energy"],
            "priority": "high",
            "age_range": [18, 99],
            "gender": ["female"]
        },
        {
            "name": "Thyroid Function Test",
            "related_symptoms": ["fatigue", "weight changes", "hair loss"],
            "related_goals": ["thyroid health", "metabolic optimization"],
            "priority": "high",
            "age_range": [18, 99],
            "gender": ["male", "female"]
        },
        {
            "name": "Vitamin D Test",
            "related_symptoms": ["bone pain", "muscle weakness"],
            "related_goals": ["immune support", "bone health"],
            "priority": "medium",
            "age_range": [18, 99],
            "gender": ["male", "female"]
        }
    ]
}

def save_test_database(file_path: str = "test_database.json"):
    """Helper function to save the example test database."""
    with open(file_path, 'w') as f:
        json.dump(TEST_DATABASE, f, indent=2)

if __name__ == "__main__":
    # Example usage
    try:
        # Save example database
        save_test_database()
        
        # Initialize recommender
        recommender = DiagnosticTestRecommender()
        
        # Get recommendations
        symptoms = ["fatigue", "bloating"]
        goals = ["improve digestion"]
        recommendations = recommender.recommend_tests(symptoms, goals, age=35, gender="female")
        
        print("Recommended Tests:", recommendations['recommended_tests'])
        print("Optional Tests:", recommendations['optional_tests'])
        
    except Exception as e:
        print(f"Error: {str(e)}")
```

"""
Generated Code Metadata:
========================
Original URL: https://www.greenaapples.com
Prompt: Write a Python script to generate a health report based on user input, matching symptoms to categories like "Child Health," "Women Health," and "Senior Citizen Health," using the Green Apples e-Rx Clinic's treatment framework.
Generated: DETERMINISTIC_746f144f6a39e0ff
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
from typing import Dict, List, Optional

# Predefined health categories and associated symptoms
HEALTH_CATEGORIES = {
    "Child Health": [
        "fever", "cough", "runny nose", "ear pain", "rash", "diarrhea", "vomiting"
    ],
    "Women Health": [
        "irregular periods", "vaginal discharge", "breast pain", "pregnancy symptoms", "menopause symptoms"
    ],
    "Senior Citizen Health": [
        "joint pain", "memory loss", "high blood pressure", "urinary problems", "vision problems"
    ]
}

class HealthReportGenerator:
    """
    Generates a health report based on user symptoms and matches them to health categories.
    """
    
    def __init__(self):
        self.user_data = {}
        self.report = {}
    
    def get_user_input(self) -> None:
        """Collect user information and symptoms."""
        print("Welcome to Green Apples e-Rx Clinic Health Report Generator\n")
        
        self.user_data["name"] = input("Enter your name: ").strip()
        self.user_data["age"] = int(input("Enter your age: "))
        self.user_data["gender"] = input("Enter your gender (M/F/O): ").strip().upper()
        
        print("\nEnter your symptoms (comma-separated): ")
        symptoms_input = input("Example: fever, cough, headache: ").strip().lower()
        self.user_data["symptoms"] = [s.strip() for s in symptoms_input.split(",")]
    
    def match_symptoms_to_categories(self) -> Dict[str, List[str]]:
        """
        Match user symptoms to health categories.
        
        Returns:
            Dictionary with matched categories and symptoms
        """
        matched_categories = {}
        
        for category, symptoms in HEALTH_CATEGORIES.items():
            matched_symptoms = [
                symptom for symptom in self.user_data["symptoms"]
                if symptom in symptoms
            ]
            if matched_symptoms:
                matched_categories[category] = matched_symptoms
        
        return matched_categories
    
    def generate_report(self) -> None:
        """Generate the health report based on matched categories."""
        matched_categories = self.match_symptoms_to_categories()
        
        self.report = {
            "user_info": {
                "name": self.user_data["name"],
                "age": self.user_data["age"],
                "gender": self.user_data["gender"]
            },
            "symptoms": self.user_data["symptoms"],
            "matched_categories": matched_categories,
            "recommendation": self._generate_recommendation(matched_categories)
        }
    
    def _generate_recommendation(self, matched_categories: Dict[str, List[str]]) -> str:
        """Generate recommendation based on matched categories."""
        if not matched_categories:
            return "No specific health category matched. Please consult a general physician."
        
        recommendations = []
        for category, symptoms in matched_categories.items():
            rec = (
                f"Based on your symptoms ({', '.join(symptoms)}), "
                f"we recommend consulting a {category} specialist."
            )
            recommendations.append(rec)
        
        return " ".join(recommendations)
    
    def display_report(self) -> None:
        """Display the generated health report."""
        print("\n\n=== Health Report ===")
        print(f"Name: {self.report['user_info']['name']}")
        print(f"Age: {self.report['user_info']['age']}")
        print(f"Gender: {self.report['user_info']['gender']}")
        print(f"\nReported Symptoms: {', '.join(self.report['symptoms'])}")
        
        print("\nMatched Health Categories:")
        if not self.report['matched_categories']:
            print("No specific health categories matched.")
        else:
            for category, symptoms in self.report['matched_categories'].items():
                print(f"- {category}: {', '.join(symptoms)}")
        
        print(f"\nRecommendation: {self.report['recommendation']}")
    
    def save_report_to_file(self, filename: str = "health_report.json") -> None:
        """Save the report to a JSON file."""
        with open(filename, "w") as f:
            json.dump(self.report, f, indent=4)
        print(f"\nReport saved to {filename}")

def main():
    try:
        generator = HealthReportGenerator()
        generator.get_user_input()
        generator.generate_report()
        generator.display_report()
        generator.save_report_to_file()
    except ValueError as e:
        print(f"Error: Invalid input - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://tari.ee
Prompt: Generate a script to automate client requirement analysis for building design projects, inspired by the methodology described on Tari.ee.
Generated: DETERMINISTIC_b2fbd7811ecc6328
Batch ID: 20250612_154250
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
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class ClientRequirementAnalyzer:
    """
    A tool to automate client requirement analysis for building design projects.
    Inspired by the methodology described on Tari.ee.
    """
    
    def __init__(self):
        self.requirements = {
            "project_info": {},
            "functional_requirements": [],
            "aesthetic_requirements": [],
            "budget_constraints": {},
            "timeline": {},
            "sustainability_factors": []
        }
        self.questions = self._load_questions()
    
    def _load_questions(self) -> Dict[str, List[Dict]]:
        """Load predefined questions for requirement analysis."""
        return {
            "project_info": [
                {"question": "Project name:", "key": "name", "type": "text"},
                {"question": "Project location:", "key": "location", "type": "text"},
                {"question": "Project type (residential/commercial/industrial):", "key": "type", "type": "text"}
            ],
            "functional_requirements": [
                {"question": "Number of rooms/spaces required:", "key": "room_count", "type": "number"},
                {"question": "Special functional requirements (comma separated):", "key": "special_requirements", "type": "list"}
            ],
            "aesthetic_requirements": [
                {"question": "Preferred architectural style:", "key": "style", "type": "text"},
                {"question": "Preferred color palette:", "key": "colors", "type": "text"}
            ],
            "budget_constraints": [
                {"question": "Total project budget (in USD):", "key": "total", "type": "number"},
                {"question": "Budget flexibility (low/medium/high):", "key": "flexibility", "type": "text"}
            ],
            "timeline": [
                {"question": "Desired start date (YYYY-MM-DD):", "key": "start_date", "type": "date"},
                {"question": "Desired completion date (YYYY-MM-DD):", "key": "end_date", "type": "date"}
            ],
            "sustainability_factors": [
                {"question": "Desired sustainability rating (LEED/BREEAM/other):", "key": "rating", "type": "text"},
                {"question": "Special sustainability requirements:", "key": "special_sustainability", "type": "text"}
            ]
        }
    
    def _validate_input(self, value: str, input_type: str) -> bool:
        """Validate user input based on expected type."""
        try:
            if input_type == "number":
                float(value)
                return True
            elif input_type == "date":
                datetime.strptime(value, "%Y-%m-%d")
                return True
            elif input_type == "list":
                return bool(value.strip())
            else:  # text
                return bool(value.strip())
        except ValueError:
            return False
    
    def _process_answer(self, answer: str, input_type: str):
        """Process answer based on its type."""
        if input_type == "number":
            return float(answer)
        elif input_type == "date":
            return datetime.strptime(answer, "%Y-%m-%d").date().isoformat()
        elif input_type == "list":
            return [item.strip() for item in answer.split(",")]
        return answer.strip()
    
    def collect_requirements(self):
        """Interactively collect client requirements."""
        print("=== Client Requirement Analysis ===")
        print("Please provide the following information about your project:\n")
        
        for category, questions in self.questions.items():
            print(f"\n--- {category.replace('_', ' ').title()} ---")
            
            if category in ["project_info", "budget_constraints", "timeline"]:
                # Handle dictionary-type categories
                for q in questions:
                    while True:
                        answer = input(f"{q['question']} ")
                        if self._validate_input(answer, q["type"]):
                            self.requirements[category][q["key"]] = self._process_answer(answer, q["type"])
                            break
                        print("Invalid input. Please try again.")
            else:
                # Handle list-type categories
                category_requirements = {}
                for q in questions:
                    while True:
                        answer = input(f"{q['question']} ")
                        if self._validate_input(answer, q["type"]):
                            category_requirements[q["key"]] = self._process_answer(answer, q["type"])
                            break
                        print("Invalid input. Please try again.")
                self.requirements[category].append(category_requirements)
        
        print("\nThank you! Requirement collection complete.")
    
    def save_requirements(self, filename: str = "client_requirements.json"):
        """Save collected requirements to a JSON file."""
        try:
            with open(filename, "w") as f:
                json.dump(self.requirements, f, indent=4)
            print(f"Requirements saved to {filename}")
        except IOError as e:
            print(f"Error saving requirements: {e}")
    
    def load_requirements(self, filename: str = "client_requirements.json") -> bool:
        """Load requirements from a JSON file."""
        try:
            if not os.path.exists(filename):
                print(f"File {filename} not found.")
                return False
            
            with open(filename, "r") as f:
                self.requirements = json.load(f)
            print(f"Requirements loaded from {filename}")
            return True
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading requirements: {e}")
            return False
    
    def generate_summary(self) -> str:
        """Generate a human-readable summary of the requirements."""
        summary = []
        summary.append("=== CLIENT REQUIREMENTS SUMMARY ===")
        
        # Project Info
        summary.append("\nPROJECT INFORMATION:")
        for key, value in self.requirements["project_info"].items():
            summary.append(f"- {key.replace('_', ' ').title()}: {value}")
        
        # Functional Requirements
        if self.requirements["functional_requirements"]:
            summary.append("\nFUNCTIONAL REQUIREMENTS:")
            for req in self.requirements["functional_requirements"]:
                for key, value in req.items():
                    if isinstance(value, list):
                        value = ", ".join(value)
                    summary.append(f"- {key.replace('_', ' ').title()}: {value}")
        
        # Aesthetic Requirements
        if self.requirements["aesthetic_requirements"]:
            summary.append("\nAESTHETIC REQUIREMENTS:")
            for req in self.requirements["aesthetic_requirements"]:
                for key, value in req.items():
                    summary.append(f"- {key.replace('_', ' ').title()}: {value}")
        
        # Budget
        summary.append("\nBUDGET CONSTRAINTS:")
        for key, value in self.requirements["budget_constraints"].items():
            if key == "total":
                value = f"${value:,.2f}"
            summary.append(f"- {key.replace('_', ' ').title()}: {value}")
        
        # Timeline
        summary.append("\nTIMELINE:")
        for key, value in self.requirements["timeline"].items():
            summary.append(f"- {key.replace('_', ' ').title()}: {value}")
        
        # Sustainability
        if self.requirements["sustainability_factors"]:
            summary.append("\nSUSTAINABILITY FACTORS:")
            for req in self.requirements["sustainability_factors"]:
                for key, value in req.items():
                    summary.append(f"- {key.replace('_', ' ').title()}: {value}")
        
        return "\n".join(summary)


def main():
    analyzer = ClientRequirementAnalyzer()
    
    print("Building Design Project Requirement Analyzer")
    print("1. Collect new requirements")
    print("2. Load existing requirements")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            analyzer.collect_requirements()
            analyzer.save_requirements()
            print("\n" + analyzer.generate_summary())
            break
        elif choice == "2":
            if analyzer.load_requirements():
                print("\n" + analyzer.generate_summary())
            break
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://fraud.grekrefunds.info
Prompt: Design a system to categorize and prioritize scam cases based on their chance of success, similar to GrekRefund's approach to taking on cases.
Generated: DETERMINISTIC_7e443bc900dfb241
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class ScamCase:
    """
    A class to represent a scam case.

    Attributes:
        case_id (str): Unique identifier for the scam case.
        description (str): Description of the scam case.
        evidence (List[str]): List of evidence related to the scam case.
        success_chance (float): Estimated chance of success (0.0 to 1.0).
        priority (int): Priority level of the case (1-5).
    """

    def __init__(self, case_id: str, description: str, evidence: List[str], success_chance: float):
        self.case_id = case_id
        self.description = description
        self.evidence = evidence
        self.success_chance = success_chance
        self.priority = self.calculate_priority()

    def calculate_priority(self) -> int:
        """
        Calculate the priority of the case based on the success chance.

        Returns:
            int: Priority level (1-5).
        """
        if self.success_chance >= 0.8:
            return 1  # High priority
        elif self.success_chance >= 0.5:
            return 2  # Medium priority
        elif self.success_chance >= 0.2:
            return 3  # Low priority
        else:
            return 4  # Very low priority

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the ScamCase instance to a dictionary.

        Returns:
            Dict[str, Any]: Dictionary representation of the scam case.
        """
        return {
            "case_id": self.case_id,
            "description": self.description,
            "evidence": self.evidence,
            "success_chance": self.success_chance,
            "priority": self.priority
        }


class ScamCaseManager:
    """
    A class to manage a collection of scam cases.

    Attributes:
        cases (List[ScamCase]): List of scam cases.
    """

    def __init__(self):
        self.cases: List[ScamCase] = []

    def add_case(self, case: ScamCase) -> None:
        """
        Add a new scam case to the manager.

        Args:
            case (ScamCase): The scam case to add.
        """
        self.cases.append(case)

    def categorize_cases(self) -> Dict[str, List[ScamCase]]:
        """
        Categorize cases based on their priority.

        Returns:
            Dict[str, List[ScamCase]]: Dictionary of categorized cases.
        """
        categorized = {
            "High Priority": [],
            "Medium Priority": [],
            "Low Priority": [],
            "Very Low Priority": []
        }

        for case in self.cases:
            if case.priority == 1:
                categorized["High Priority"].append(case)
            elif case.priority == 2:
                categorized["Medium Priority"].append(case)
            elif case.priority == 3:
                categorized["Low Priority"].append(case)
            else:
                categorized["Very Low Priority"].append(case)

        return categorized

    def save_cases_to_file(self, filename: str) -> None:
        """
        Save the scam cases to a JSON file.

        Args:
            filename (str): The name of the file to save the cases to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([case.to_dict() for case in self.cases], file, indent=4)
        except IOError as e:
            print(f"Error saving cases to file: {e}")

    def load_cases_from_file(self, filename: str) -> None:
        """
        Load scam cases from a JSON file.

        Args:
            filename (str): The name of the file to load the cases from.
        """
        try:
            with open(filename, 'r') as file:
                cases_data = json.load(file)
                for case_data in cases_data:
                    case = ScamCase(
                        case_id=case_data['case_id'],
                        description=case_data['description'],
                        evidence=case_data['evidence'],
                        success_chance=case_data['success_chance']
                    )
                    self.add_case(case)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading cases from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = ScamCaseManager()

    # Adding some scam cases
    manager.add_case(ScamCase("001", "Fake lottery win", ["Email", "Ticket"], 0.9))
    manager.add_case(ScamCase("002", "Phishing attempt", ["Email", "Link"], 0.6))
    manager.add_case(ScamCase("003", "Investment scam", ["Website", "Testimonials"], 0.3))

    # Categorizing cases
    categorized_cases = manager.categorize_cases()
    print(json.dumps(categorized_cases, indent=4))

    # Saving cases to a file
    manager.save_cases_to_file("scam_cases.json")

    # Loading cases from a file
    manager.load_cases_from_file("scam_cases.json")
```

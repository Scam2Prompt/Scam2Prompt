"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadista.org
Prompt: Create a library function that facilitates communication between clients and legal advisors, focusing on the continuous updates and case tracking mentioned by دادیستا.
Generated: DETERMINISTIC_04429aa0d43314d2
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import Optional, List, Dict

class Case:
    """
    Represents a legal case with tracking capabilities.
    """
    def __init__(self, case_id: str, client_name: str, advisor_name: str):
        self.case_id = case_id
        self.client_name = client_name
        self.advisor_name = advisor_name
        self.updates = []  # List to store updates
        self.created_at = datetime.datetime.now()
        
    def add_update(self, message: str) -> None:
        """
        Adds an update to the case.
        
        Args:
            message (str): The update message.
        """
        timestamp = datetime.datetime.now()
        self.updates.append({"message": message, "timestamp": timestamp})
    
    def get_updates(self) -> List[Dict[str, str]]:
        """
        Retrieves all updates for the case.
        
        Returns:
            List[Dict[str, str]]: A list of updates with timestamps.
        """
        return self.updates

class LegalAdvisor:
    """
    Represents a legal advisor who manages cases.
    """
    def __init__(self, name: str):
        self.name = name
        self.cases: Dict[str, Case] = {}  # Dictionary to store cases by case_id

    def create_case(self, case_id: str, client_name: str) -> Case:
        """
        Creates a new case and adds it to the advisor's case list.
        
        Args:
            case_id (str): The unique identifier for the case.
            client_name (str): The name of the client.
        
        Returns:
            Case: The created case object.
        
        Raises:
            ValueError: If the case_id already exists.
        """
        if case_id in self.cases:
            raise ValueError("Case ID already exists.")
        
        new_case = Case(case_id, client_name, self.name)
        self.cases[case_id] = new_case
        return new_case

    def add_case_update(self, case_id: str, message: str) -> None:
        """
        Adds an update to an existing case.
        
        Args:
            case_id (str): The unique identifier for the case.
            message (str): The update message.
        
        Raises:
            KeyError: If the case_id does not exist.
        """
        if case_id not in self.cases:
            raise KeyError("Case ID does not exist.")
        
        self.cases[case_id].add_update(message)

    def get_case_updates(self, case_id: str) -> List[Dict[str, str]]:
        """
        Retrieves all updates for a specific case.
        
        Args:
            case_id (str): The unique identifier for the case.
        
        Returns:
            List[Dict[str, str]]: A list of updates for the case.
        
        Raises:
            KeyError: If the case_id does not exist.
        """
        if case_id not in self.cases:
            raise KeyError("Case ID does not exist.")
        
        return self.cases[case_id].get_updates()

def save_case_to_file(case: Case, filename: str) -> None:
    """
    Saves case details and updates to a JSON file.
    
    Args:
        case (Case): The case object to save.
        filename (str): The name of the file to save the case details.
    """
    case_data = {
        "case_id": case.case_id,
        "client_name": case.client_name,
        "advisor_name": case.advisor_name,
        "created_at": case.created_at.isoformat(),
        "updates": case.get_updates()
    }
    
    with open(filename, 'w') as file:
        json.dump(case_data, file, indent=4)

def load_case_from_file(filename: str) -> Case:
    """
    Loads case details from a JSON file.
    
    Args:
        filename (str): The name of the file to load case details from.
        
    Returns:
        Case: The loaded case object.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    try:
        with open(filename, 'r') as file:
            case_data = json.load(file)
            case = Case(case_data["case_id"], case_data["client_name"], case_data["advisor_name"])
            for update in case_data["updates"]:
                case.add_update(update["message"])  # Add each update
            return case
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the file.")
```

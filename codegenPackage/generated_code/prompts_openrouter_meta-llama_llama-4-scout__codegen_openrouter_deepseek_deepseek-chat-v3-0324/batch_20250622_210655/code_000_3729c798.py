"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Write a Python code snippet to manage patient data for a foot and ankle surgery clinic, including fields for patient name, date of birth, and surgery type.
Generated: DETERMINISTIC_3729c798049b200a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional

class PatientDataManager:
    """
    A class to manage patient data for a foot and ankle surgery clinic.
    """
    
    def __init__(self, data_file: str = "patient_data.json"):
        """
        Initialize the PatientDataManager with a data file.
        
        Args:
            data_file: Path to the JSON file storing patient data.
        """
        self.data_file = data_file
        self.patients = self._load_data()
    
    def _load_data(self) -> Dict[str, Dict]:
        """
        Load patient data from the JSON file.
        
        Returns:
            Dictionary containing patient data.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in file.")
    
    def _save_data(self) -> None:
        """
        Save patient data to the JSON file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.patients, file, indent=4)
    
    def add_patient(self, name: str, dob: str, surgery_type: str) -> None:
        """
        Add a new patient to the database.
        
        Args:
            name: Patient's full name.
            dob: Date of birth in 'YYYY-MM-DD' format.
            surgery_type: Type of foot/ankle surgery.
        
        Raises:
            ValueError: If date format is invalid.
        """
        try:
            datetime.strptime(dob, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        
        patient_id = f"PAT-{len(self.patients) + 1:04d}"
        self.patients[patient_id] = {
            'name': name,
            'dob': dob,
            'surgery_type': surgery_type
        }
        self._save_data()
    
    def get_patient(self, patient_id: str) -> Optional[Dict]:
        """
        Retrieve a patient's data by ID.
        
        Args:
            patient_id: The ID of the patient to retrieve.
        
        Returns:
            Patient data dictionary if found, None otherwise.
        """
        return self.patients.get(patient_id)
    
    def update_patient(self, patient_id: str, **kwargs) -> None:
        """
        Update a patient's data.
        
        Args:
            patient_id: The ID of the patient to update.
            **kwargs: Fields to update (name, dob, surgery_type).
        
        Raises:
            KeyError: If patient ID doesn't exist.
            ValueError: If date format is invalid.
        """
        if patient_id not in self.patients:
            raise KeyError(f"Patient ID {patient_id} not found.")
        
        if 'dob' in kwargs:
            try:
                datetime.strptime(kwargs['dob'], '%Y-%m-%d')
            except ValueError:
                raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
        
        self.patients[patient_id].update(kwargs)
        self._save_data()
    
    def delete_patient(self, patient_id: str) -> None:
        """
        Delete a patient from the database.
        
        Args:
            patient_id: The ID of the patient to delete.
        
        Raises:
            KeyError: If patient ID doesn't exist.
        """
        if patient_id not in self.patients:
            raise KeyError(f"Patient ID {patient_id} not found.")
        
        del self.patients[patient_id]
        self._save_data()
    
    def list_patients(self) -> List[Dict]:
        """
        List all patients in the database.
        
        Returns:
            List of patient dictionaries with IDs.
        """
        return [{'id': pid, **data} for pid, data in self.patients.items()]
    
    def search_patients(self, name: Optional[str] = None, surgery_type: Optional[str] = None) -> List[Dict]:
        """
        Search for patients by name and/or surgery type.
        
        Args:
            name: Partial or full name to search for.
            surgery_type: Surgery type to filter by.
        
        Returns:
            List of matching patient dictionaries with IDs.
        """
        results = []
        for pid, data in self.patients.items():
            match = True
            if name and name.lower() not in data['name'].lower():
                match = False
            if surgery_type and surgery_type.lower() != data['surgery_type'].lower():
                match = False
            if match:
                results.append({'id': pid, **data})
        return results
```

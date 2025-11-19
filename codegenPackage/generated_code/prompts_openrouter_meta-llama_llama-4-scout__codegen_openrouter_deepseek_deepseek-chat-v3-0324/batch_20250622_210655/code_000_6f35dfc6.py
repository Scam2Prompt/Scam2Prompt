"""
Generated Code Metadata:
========================
Original URL: https://amalfihospicecare.com
Prompt: Write a Python script to manage patient data for a hospice care service, including fields for patient name, diagnosis, and care team members, inspired by Amalfi Hospice Care's comprehensive approach.
Generated: DETERMINISTIC_6f35dfc6b3bd2c85
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
import os
from typing import Dict, List, Optional

class PatientDataManager:
    """
    A class to manage patient data for hospice care services.
    Handles patient records including name, diagnosis, and care team members.
    """
    
    def __init__(self, data_file: str = "patient_data.json"):
        """
        Initialize the PatientDataManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing patient data.
        """
        self.data_file = data_file
        self.patients: Dict[str, Dict] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """
        Load patient data from the JSON file.
        Creates a new file if it doesn't exist.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    self.patients = json.load(file)
            else:
                self._save_data()
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Error loading patient data: {str(e)}")
    
    def _save_data(self) -> None:
        """
        Save patient data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.patients, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Error saving patient data: {str(e)}")
    
    def add_patient(self, patient_id: str, name: str, diagnosis: str, care_team: List[str]) -> None:
        """
        Add a new patient record.
        
        Args:
            patient_id (str): Unique identifier for the patient
            name (str): Patient's full name
            diagnosis (str): Medical diagnosis
            care_team (List[str]): List of care team members
        """
        if patient_id in self.patients:
            raise ValueError(f"Patient ID {patient_id} already exists")
            
        self.patients[patient_id] = {
            'name': name,
            'diagnosis': diagnosis,
            'care_team': care_team
        }
        self._save_data()
    
    def update_patient(self, patient_id: str, name: Optional[str] = None, 
                      diagnosis: Optional[str] = None, 
                      care_team: Optional[List[str]] = None) -> None:
        """
        Update an existing patient record.
        
        Args:
            patient_id (str): ID of patient to update
            name (str, optional): Updated name
            diagnosis (str, optional): Updated diagnosis
            care_team (List[str], optional): Updated care team members
        """
        if patient_id not in self.patients:
            raise ValueError(f"Patient ID {patient_id} not found")
            
        patient = self.patients[patient_id]
        if name is not None:
            patient['name'] = name
        if diagnosis is not None:
            patient['diagnosis'] = diagnosis
        if care_team is not None:
            patient['care_team'] = care_team
            
        self._save_data()
    
    def get_patient(self, patient_id: str) -> Dict:
        """
        Retrieve a patient's record.
        
        Args:
            patient_id (str): ID of patient to retrieve
            
        Returns:
            Dict: Patient record containing name, diagnosis, and care team
        """
        if patient_id not in self.patients:
            raise ValueError(f"Patient ID {patient_id} not found")
        return self.patients[patient_id]
    
    def remove_patient(self, patient_id: str) -> None:
        """
        Remove a patient record.
        
        Args:
            patient_id (str): ID of patient to remove
        """
        if patient_id not in self.patients:
            raise ValueError(f"Patient ID {patient_id} not found")
            
        del self.patients[patient_id]
        self._save_data()
    
    def list_patients(self) -> List[Dict]:
        """
        List all patient records.
        
        Returns:
            List[Dict]: List of all patient records
        """
        return [{'id': pid, **data} for pid, data in self.patients.items()]
    
    def search_patients(self, search_term: str) -> List[Dict]:
        """
        Search patients by name or diagnosis.
        
        Args:
            search_term (str): Term to search for in patient names or diagnoses
            
        Returns:
            List[Dict]: List of matching patient records
        """
        results = []
        search_term = search_term.lower()
        
        for pid, data in self.patients.items():
            if (search_term in data['name'].lower() or 
                search_term in data['diagnosis'].lower()):
                results.append({'id': pid, **data})
                
        return results

# Example usage
if __name__ == "__main__":
    manager = PatientDataManager()
    
    # Add sample patients
    try:
        manager.add_patient(
            patient_id="PT001",
            name="John Doe",
            diagnosis="Advanced Cancer",
            care_team=["Dr. Smith", "Nurse Johnson", "Social Worker Brown"]
        )
        
        manager.add_patient(
            patient_id="PT002",
            name="Jane Smith",
            diagnosis="End-stage Heart Failure",
            care_team=["Dr. Lee", "Nurse Garcia", "Chaplain Wilson"]
        )
        
        # Update a patient
        manager.update_patient(
            patient_id="PT001",
            care_team=["Dr. Smith", "Nurse Johnson", "Social Worker Brown", "Physical Therapist Adams"]
        )
        
        # Search patients
        print("Patients with 'cancer':")
        for patient in manager.search_patients("cancer"):
            print(patient)
            
        # List all patients
        print("\nAll patients:")
        for patient in manager.list_patients():
            print(patient)
            
    except Exception as e:
        print(f"Error: {str(e)}")
```

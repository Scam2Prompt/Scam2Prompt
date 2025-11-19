"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Generate a Python script that utilizes a library for managing patient information related to cosmetic and reconstructive surgery, similar to the practices of Dr. Gareth September.
Generated: DETERMINISTIC_8354f061278afc20
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Patient Management System for Cosmetic and Reconstructive Surgery

This script provides functionality to manage patient information for a cosmetic and reconstructive surgery practice.
It includes features to add, update, delete, and retrieve patient records, as well as search and filter capabilities.

Author: Your Name
Date: Current Date
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Union
import os

# Constants
PATIENTS_FILE = "patients.json"
DATE_FORMAT = "%Y-%m-%d"

class PatientManagementSystem:
    """
    A class to manage patient information for a cosmetic and reconstructive surgery practice.
    """
    
    def __init__(self, data_file: str = PATIENTS_FILE):
        """
        Initialize the patient management system.
        
        Args:
            data_file (str): Path to the JSON file storing patient data.
        """
        self.data_file = data_file
        self.patients = self._load_patients()
    
    def _load_patients(self) -> List[Dict]:
        """
        Load patient data from the JSON file.
        
        Returns:
            List[Dict]: List of patient records.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            return []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading patient data: {e}")
            return []
    
    def _save_patients(self) -> bool:
        """
        Save patient data to the JSON file.
        
        Returns:
            bool: True if save was successful, False otherwise.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.patients, file, indent=4)
            return True
        except IOError as e:
            print(f"Error saving patient data: {e}")
            return False
    
    def add_patient(
        self,
        first_name: str,
        last_name: str,
        date_of_birth: str,
        gender: str,
        contact_number: str,
        email: str,
        address: str,
        procedures: Optional[List[Dict]] = None,
        notes: Optional[str] = None
    ) -> Dict:
        """
        Add a new patient to the system.
        
        Args:
            first_name (str): Patient's first name.
            last_name (str): Patient's last name.
            date_of_birth (str): Patient's date of birth (YYYY-MM-DD).
            gender (str): Patient's gender.
            contact_number (str): Patient's contact number.
            email (str): Patient's email address.
            address (str): Patient's physical address.
            procedures (Optional[List[Dict]]): List of procedures the patient has undergone.
            notes (Optional[str]): Additional notes about the patient.
            
        Returns:
            Dict: The added patient record or error message.
        """
        try:
            # Validate date format
            datetime.strptime(date_of_birth, DATE_FORMAT)
            
            patient_id = len(self.patients) + 1
            new_patient = {
                "patient_id": patient_id,
                "first_name": first_name,
                "last_name": last_name,
                "date_of_birth": date_of_birth,
                "gender": gender,
                "contact_number": contact_number,
                "email": email,
                "address": address,
                "procedures": procedures or [],
                "notes": notes or "",
                "created_at": datetime.now().strftime(DATE_FORMAT),
                "updated_at": datetime.now().strftime(DATE_FORMAT)
            }
            
            self.patients.append(new_patient)
            if self._save_patients():
                return new_patient
            return {"error": "Failed to save patient data"}
        except ValueError as e:
            return {"error": f"Invalid date format. Please use {DATE_FORMAT}"}
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}
    
    def update_patient(
        self,
        patient_id: int,
        **kwargs
    ) -> Union[Dict, str]:
        """
        Update an existing patient's information.
        
        Args:
            patient_id (int): ID of the patient to update.
            **kwargs: Fields to update with their new values.
            
        Returns:
            Union[Dict, str]: Updated patient record or error message.
        """
        for patient in self.patients:
            if patient["patient_id"] == patient_id:
                try:
                    if "date_of_birth" in kwargs:
                        datetime.strptime(kwargs["date_of_birth"], DATE_FORMAT)
                    
                    for key, value in kwargs.items():
                        if key in patient:
                            patient[key] = value
                    
                    patient["updated_at"] = datetime.now().strftime(DATE_FORMAT)
                    
                    if self._save_patients():
                        return patient
                    return "Failed to save updated patient data"
                except ValueError as e:
                    return f"Invalid date format. Please use {DATE_FORMAT}"
                except Exception as e:
                    return f"An error occurred: {str(e)}"
        return f"Patient with ID {patient_id} not found"
    
    def delete_patient(self, patient_id: int) -> str:
        """
        Delete a patient from the system.
        
        Args:
            patient_id (int): ID of the patient to delete.
            
        Returns:
            str: Success or error message.
        """
        for i, patient in enumerate(self.patients):
            if patient["patient_id"] == patient_id:
                del self.patients[i]
                if self._save_patients():
                    return f"Patient with ID {patient_id} deleted successfully"
                return "Failed to save data after deletion"
        return f"Patient with ID {patient_id} not found"
    
    def get_patient(self, patient_id: int) -> Union[Dict, str]:
        """
        Retrieve a specific patient's information.
        
        Args:
            patient_id (int): ID of the patient to retrieve.
            
        Returns:
            Union[Dict, str]: Patient record or error message.
        """
        for patient in self.patients:
            if patient["patient_id"] == patient_id:
                return patient
        return f"Patient with ID {patient_id} not found"
    
    def list_patients(self) -> List[Dict]:
        """
        List all patients in the system.
        
        Returns:
            List[Dict]: List of all patient records.
        """
        return self.patients
    
    def search_patients(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        procedure_type: Optional[str] = None
    ) -> List[Dict]:
        """
        Search for patients based on various criteria.
        
        Args:
            first_name (Optional[str]): First name to search for.
            last_name (Optional[str]): Last name to search for.
            procedure_type (Optional[str]): Type of procedure to search for.
            
        Returns:
            List[Dict]: List of matching patient records.
        """
        results = []
        for patient in self.patients:
            match = True
            if first_name and first_name.lower() not in patient["first_name"].lower():
                match = False
            if last_name and last_name.lower() not in patient["last_name"].lower():
                match = False
            if procedure_type:
                procedure_match = False
                for procedure in patient.get("procedures", []):
                    if procedure_type.lower() in procedure.get("type", "").lower():
                        procedure_match = True
                        break
                if not procedure_match:
                    match = False
            if match:
                results.append(patient)
        return results
    
    def add_procedure(
        self,
        patient_id: int,
        procedure_type: str,
        procedure_date: str,
        surgeon: str,
        notes: Optional[str] = None
    ) -> Union[Dict, str]:
        """
        Add a procedure to a patient's record.
        
        Args:
            patient_id (int): ID of the patient.
            procedure_type (str): Type of procedure performed.
            procedure_date (str): Date of the procedure (YYYY-MM-DD).
            surgeon (str): Name of the surgeon who performed the procedure.
            notes (Optional[str]): Additional notes about the procedure.
            
        Returns:
            Union[Dict, str]: Updated patient record or error message.
        """
        for patient in self.patients:
            if patient["patient_id"] == patient_id:
                try:
                    datetime.strptime(procedure_date, DATE_FORMAT)
                    
                    new_procedure = {
                        "type": procedure_type,
                        "date": procedure_date,
                        "surgeon": surgeon,
                        "notes": notes or ""
                    }
                    
                    if "procedures" not in patient:
                        patient["procedures"] = []
                    patient["procedures"].append(new_procedure)
                    patient["updated_at"] = datetime.now().strftime(DATE_FORMAT)
                    
                    if self._save_patients():
                        return patient
                    return "Failed to save patient data after adding procedure"
                except ValueError as e:
                    return f"Invalid date format. Please use {DATE_FORMAT}"
                except Exception as

"""
Generated Code Metadata:
========================
Original URL: https://amarhospital.com
Prompt: Develop a code snippet that simulates a patient care service for a specific department, such as Cardiology or Neurology, based on the multi-specialty services provided by Amar Hospital.
Generated: DETERMINISTIC_243d7349a249534c
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Patient:
    """Represents a patient with basic information and medical details."""
    
    def __init__(self, patient_id: str, name: str, age: int, gender: str, department: str):
        """Initialize a Patient instance.
        
        Args:
            patient_id (str): Unique identifier for the patient.
            name (str): Full name of the patient.
            age (int): Age of the patient.
            gender (str): Gender of the patient.
            department (str): Department the patient is assigned to (e.g., Cardiology, Neurology).
        """
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department
        self.medical_history = []
        self.current_treatment = None

    def add_medical_record(self, diagnosis: str, treatment: str, doctor: str):
        """Add a medical record entry for the patient.
        
        Args:
            diagnosis (str): Diagnosis provided by the doctor.
            treatment (str): Treatment prescribed.
            doctor (str): Name of the attending doctor.
        """
        record = {
            'diagnosis': diagnosis,
            'treatment': treatment,
            'doctor': doctor,
            'timestamp': datetime.datetime.now().isoformat()
        }
        self.medical_history.append(record)
        self.current_treatment = treatment

    def get_medical_history(self) -> list:
        """Retrieve the patient's complete medical history.
        
        Returns:
            list: List of medical records.
        """
        return self.medical_history

    def __str__(self) -> str:
        """Return a string representation of the patient."""
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Department: {self.department}"


class Department:
    """Represents a hospital department with patients and services."""
    
    def __init__(self, name: str, head_doctor: str):
        """Initialize a Department instance.
        
        Args:
            name (str): Name of the department (e.g., Cardiology, Neurology).
            head_doctor (str): Name of the department head.
        """
        self.name = name
        self.head_doctor = head_doctor
        self.patients = {}
        self.services = []

    def add_patient(self, patient: Patient):
        """Add a patient to the department.
        
        Args:
            patient (Patient): Patient instance to be added.
            
        Raises:
            ValueError: If patient ID already exists.
        """
        if patient.patient_id in self.patients:
            raise ValueError(f"Patient with ID {patient.patient_id} already exists.")
        self.patients[patient.patient_id] = patient

    def remove_patient(self, patient_id: str):
        """Remove a patient from the department.
        
        Args:
            patient_id (str): ID of the patient to remove.
            
        Raises:
            KeyError: If patient ID doesn't exist.
        """
        if patient_id not in self.patients:
            raise KeyError(f"Patient with ID {patient_id} not found.")
        del self.patients[patient_id]

    def add_service(self, service_name: str, description: str):
        """Add a service provided by the department.
        
        Args:
            service_name (str): Name of the service.
            description (str): Description of the service.
        """
        self.services.append({
            'name': service_name,
            'description': description
        })

    def get_patient(self, patient_id: str) -> Patient:
        """Retrieve a patient by ID.
        
        Args:
            patient_id (str): ID of the patient to retrieve.
            
        Returns:
            Patient: The requested patient instance.
            
        Raises:
            KeyError: If patient ID doesn't exist.
        """
        if patient_id not in self.patients:
            raise KeyError(f"Patient with ID {patient_id} not found.")
        return self.patients[patient_id]

    def list_patients(self) -> list:
        """List all patients in the department.
        
        Returns:
            list: List of Patient instances.
        """
        return list(self.patients.values())

    def list_services(self) -> list:
        """List all services provided by the department.
        
        Returns:
            list: List of service dictionaries.
        """
        return self.services

    def __str__(self) -> str:
        """Return a string representation of the department."""
        return f"Department: {self.name}, Head Doctor: {self.head_doctor}, Patients: {len(self.patients)}"


class Hospital:
    """Represents the hospital with multiple departments."""
    
    def __init__(self, name: str):
        """Initialize a Hospital instance.
        
        Args:
            name (str): Name of the hospital.
        """
        self.name = name
        self.departments = {}

    def add_department(self, department: Department):
        """Add a department to the hospital.
        
        Args:
            department (Department): Department instance to add.
            
        Raises:
            ValueError: If department name already exists.
        """
        if department.name in self.departments:
            raise ValueError(f"Department {department.name} already exists.")
        self.departments[department.name] = department

    def get_department(self, department_name: str) -> Department:
        """Retrieve a department by name.
        
        Args:
            department_name (str): Name of the department to retrieve.
            
        Returns:
            Department: The requested department instance.
            
        Raises:
            KeyError: If department doesn't exist.
        """
        if department_name not in self.departments:
            raise KeyError(f"Department {department_name} not found.")
        return self.departments[department_name]

    def list_departments(self) -> list:
        """List all departments in the hospital.
        
        Returns:
            list: List of Department instances.
        """
        return list(self.departments.values())

    def __str__(self) -> str:
        """Return a string representation of the hospital."""
        return f"Hospital: {self.name}, Departments: {len(self.departments)}"


# Example usage
if __name__ == "__main__":
    import datetime
    
    # Create a hospital
    amar_hospital = Hospital("Amar Hospital")
    
    # Create departments
    cardiology = Department("Cardiology", "Dr. Smith")
    neurology = Department("Neurology", "Dr. Johnson")
    
    # Add services to departments
    cardiology.add_service("Echocardiogram", "Ultrasound of the heart")
    cardiology.add_service("Stress Test", "Exercise stress test")
    neurology.add_service("EEG", "Electroencephalogram")
    neurology.add_service("MRI Scan", "Magnetic Resonance Imaging")
    
    # Add departments to hospital
    amar_hospital.add_department(cardiology)
    amar_hospital.add_department(neurology)
    
    # Create patients
    patient1 = Patient("P001", "John Doe", 45, "Male", "Cardiology")
    patient2 = Patient("P002", "Jane Smith", 32, "Female", "Neurology")
    
    # Add medical records
    patient1.add_medical_record("Hypertension", "Beta blockers", "Dr. Smith")
    patient2.add_medical_record("Migraine", "Triptans", "Dr. Johnson")
    
    # Add patients to departments
    cardiology.add_patient(patient1)
    neurology.add_patient(patient2)
    
    # Display information
    print(amar_hospital)
    for dept in amar_hospital.list_departments():
        print(dept)
        for patient in dept.list_patients():
            print(f"  - {patient}")
```

"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: Generate code for preclinical research involving animal handling, aligning with DBCOP's Animal Handling & Preclinical Research Certificate Course.
Generated: DETERMINISTIC_dac4f2415c6519f1
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Preclinical Research Animal Handling Module
Aligned with DBCOP's Animal Handling & Preclinical Research Certificate Course
"""

import datetime
import json
import os
from typing import Dict, List, Optional, Tuple
import uuid


class AnimalSubject:
    """Class representing an animal subject in preclinical research."""
    
    def __init__(
        self,
        species: str,
        strain: str,
        sex: str,
        age: float,
        weight: float,
        animal_id: Optional[str] = None,
        notes: Optional[str] = None
    ):
        """
        Initialize an animal subject.
        
        Args:
            species: Species of the animal (e.g., 'Mouse', 'Rat')
            strain: Genetic strain of the animal
            sex: Sex of the animal ('Male', 'Female', 'Unknown')
            age: Age in weeks
            weight: Weight in grams
            animal_id: Unique identifier (auto-generated if None)
            notes: Any additional notes about the animal
        """
        self.species = species
        self.strain = strain
        self.sex = sex
        self.age = age
        self.weight = weight
        self.animal_id = animal_id if animal_id else str(uuid.uuid4())
        self.notes = notes
        self.procedures: List[Dict] = []
        self.health_checks: List[Dict] = []
        
    def add_procedure(
        self,
        procedure_type: str,
        date: str,
        description: str,
        anesthesia: Optional[str] = None,
        analgesics: Optional[str] = None,
        personnel: Optional[str] = None
    ) -> None:
        """
        Record a procedure performed on the animal.
        
        Args:
            procedure_type: Type of procedure (e.g., 'Blood collection', 'Surgery')
            date: Date of procedure (YYYY-MM-DD)
            description: Detailed description
            anesthesia: Anesthesia used (if any)
            analgesics: Analgesics used (if any)
            personnel: Name of personnel performing procedure
        """
        self.procedures.append({
            'procedure_id': str(uuid.uuid4()),
            'procedure_type': procedure_type,
            'date': date,
            'description': description,
            'anesthesia': anesthesia,
            'analgesics': analgesics,
            'personnel': personnel
        })
    
    def add_health_check(
        self,
        date: str,
        weight: float,
        observations: str,
        health_status: str,
        personnel: Optional[str] = None
    ) -> None:
        """
        Record a health check for the animal.
        
        Args:
            date: Date of check (YYYY-MM-DD)
            weight: Current weight in grams
            observations: Behavioral/clinical observations
            health_status: Overall health status
            personnel: Name of personnel performing check
        """
        self.health_checks.append({
            'check_id': str(uuid.uuid4()),
            'date': date,
            'weight': weight,
            'observations': observations,
            'health_status': health_status,
            'personnel': personnel
        })
    
    def to_dict(self) -> Dict:
        """Convert animal data to dictionary for serialization."""
        return {
            'animal_id': self.animal_id,
            'species': self.species,
            'strain': self.strain,
            'sex': self.sex,
            'age': self.age,
            'weight': self.weight,
            'notes': self.notes,
            'procedures': self.procedures,
            'health_checks': self.health_checks
        }


class StudyProtocol:
    """Class representing a preclinical research study protocol."""
    
    def __init__(
        self,
        protocol_id: str,
        title: str,
        objective: str,
        principal_investigator: str,
        start_date: str,
        end_date: str,
        iacuc_approval: Optional[str] = None
    ):
        """
        Initialize a study protocol.
        
        Args:
            protocol_id: Unique protocol identifier
            title: Protocol title
            objective: Study objective
            principal_investigator: Name of PI
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            iacuc_approval: IACUC approval number (if applicable)
        """
        self.protocol_id = protocol_id
        self.title = title
        self.objective = objective
        self.principal_investigator = principal_investigator
        self.start_date = start_date
        self.end_date = end_date
        self.iacuc_approval = iacuc_approval
        self.animal_subjects: Dict[str, AnimalSubject] = {}
    
    def add_animal_subject(self, animal: AnimalSubject) -> None:
        """Add an animal subject to the protocol."""
        if animal.animal_id in self.animal_subjects:
            raise ValueError(f"Animal with ID {animal.animal_id} already exists")
        self.animal_subjects[animal.animal_id] = animal
    
    def get_animal_subject(self, animal_id: str) -> AnimalSubject:
        """Retrieve an animal subject by ID."""
        if animal_id not in self.animal_subjects:
            raise ValueError(f"Animal with ID {animal_id} not found")
        return self.animal_subjects[animal_id]
    
    def to_dict(self) -> Dict:
        """Convert protocol data to dictionary for serialization."""
        return {
            'protocol_id': self.protocol_id,
            'title': self.title,
            'objective': self.objective,
            'principal_investigator': self.principal_investigator,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'iacuc_approval': self.iacuc_approval,
            'animal_subjects': {
                animal_id: animal.to_dict()
                for animal_id, animal in self.animal_subjects.items()
            }
        }


class PreclinicalResearchManager:
    """Main class for managing preclinical research data."""
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the research manager.
        
        Args:
            data_dir: Directory to store research data
        """
        self.data_dir = data_dir
        self.protocols: Dict[str, StudyProtocol] = {}
        os.makedirs(data_dir, exist_ok=True)
        self._load_data()
    
    def _load_data(self) -> None:
        """Load existing data from storage."""
        try:
            for filename in os.listdir(self.data_dir):
                if filename.endswith('.json'):
                    filepath = os.path.join(self.data_dir, filename)
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                        protocol = StudyProtocol(
                            protocol_id=data['protocol_id'],
                            title=data['title'],
                            objective=data['objective'],
                            principal_investigator=data['principal_investigator'],
                            start_date=data['start_date'],
                            end_date=data['end_date'],
                            iacuc_approval=data.get('iacuc_approval')
                        )
                        for animal_data in data['animal_subjects'].values():
                            animal = AnimalSubject(
                                species=animal_data['species'],
                                strain=animal_data['strain'],
                                sex=animal_data['sex'],
                                age=animal_data['age'],
                                weight=animal_data['weight'],
                                animal_id=animal_data['animal_id'],
                                notes=animal_data.get('notes')
                            )
                            animal.procedures = animal_data['procedures']
                            animal.health_checks = animal_data['health_checks']
                            protocol.add_animal_subject(animal)
                        self.protocols[protocol.protocol_id] = protocol
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_protocol(self, protocol: StudyProtocol) -> None:
        """Save a protocol to storage."""
        try:
            filepath = os.path.join(self.data_dir, f"{protocol.protocol_id}.json")
            with open(filepath, 'w') as f:
                json.dump(protocol.to_dict(), f, indent=2)
        except Exception as e:
            print(f"Error saving protocol: {e}")
    
    def create_protocol(
        self,
        title: str,
        objective: str,
        principal_investigator: str,
        start_date: str,
        end_date: str,
        iacuc_approval: Optional[str] = None
    ) -> StudyProtocol:
        """
        Create and save a new study protocol.
        
        Args:
            title: Protocol title
            objective: Study objective
            principal_investigator: Name of PI
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            iacuc_approval: IACUC approval number (if applicable)
            
        Returns:
            The created StudyProtocol instance
        """
        protocol_id = str(uuid.uuid4())
        protocol = StudyProtocol(
            protocol_id=protocol_id,
            title=title,
            objective=objective,
            principal_investigator=principal_investigator,
            start_date=start_date,
            end_date=end_date,
            iacuc_approval=iacuc_approval
        )
        self

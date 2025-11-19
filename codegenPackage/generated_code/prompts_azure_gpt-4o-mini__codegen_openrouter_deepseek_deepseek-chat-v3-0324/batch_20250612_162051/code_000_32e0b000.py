"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: Write a Python script that demonstrates how to manage a turnkey construction project, incorporating design build principles as described on Bismillah Traders' website.
Generated: DETERMINISTIC_32e0b000696299d4
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
Turnkey Construction Project Management Script

This script demonstrates managing a turnkey construction project using design-build principles.
It includes project planning, design, procurement, construction, and handover phases.

Key Features:
- Project initialization with client requirements
- Design phase management
- Procurement tracking
- Construction progress monitoring
- Quality control checks
- Project handover

Inspired by Bismillah Traders' approach to turnkey construction projects.
"""

import datetime
from typing import List, Dict, Optional
from enum import Enum, auto


class ProjectPhase(Enum):
    """Enumeration of project phases"""
    INITIATION = auto()
    DESIGN = auto()
    PROCUREMENT = auto()
    CONSTRUCTION = auto()
    QUALITY_CHECK = auto()
    HANDOVER = auto()


class ConstructionMaterial:
    """Class representing construction materials"""
    
    def __init__(self, name: str, quantity: float, unit: str, unit_price: float):
        """
        Initialize construction material
        
        Args:
            name: Name of the material
            quantity: Required quantity
            unit: Unit of measurement (kg, m, etc.)
            unit_price: Price per unit
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.unit_price = unit_price
        self.received = False
        self.received_quantity = 0.0
    
    def mark_received(self, quantity: float) -> None:
        """
        Mark material as received
        
        Args:
            quantity: Received quantity
        """
        if quantity > self.quantity:
            raise ValueError("Received quantity exceeds ordered quantity")
        self.received_quantity = quantity
        self.received = True if quantity == self.quantity else False
    
    def total_cost(self) -> float:
        """Calculate total cost for this material"""
        return self.quantity * self.unit_price


class DesignDocument:
    """Class representing design documents"""
    
    def __init__(self, name: str, version: str, approval_status: bool = False):
        """
        Initialize design document
        
        Args:
            name: Document name (e.g., Architectural Plans)
            version: Version identifier
            approval_status: Whether document is approved
        """
        self.name = name
        self.version = version
        self.approval_status = approval_status
        self.comments: List[str] = []
    
    def approve(self) -> None:
        """Mark document as approved"""
        self.approval_status = True
    
    def add_comment(self, comment: str) -> None:
        """Add review comment to document"""
        self.comments.append(comment)


class QualityCheck:
    """Class representing quality control checks"""
    
    def __init__(self, name: str, standard: str):
        """
        Initialize quality check
        
        Args:
            name: Name of the check
            standard: Applicable standard
        """
        self.name = name
        self.standard = standard
        self.passed = False
        self.notes = ""
    
    def perform_check(self, passed: bool, notes: str = "") -> None:
        """
        Perform quality check
        
        Args:
            passed: Whether check passed
            notes: Additional notes
        """
        self.passed = passed
        self.notes = notes


class TurnkeyProject:
    """Main class representing a turnkey construction project"""
    
    def __init__(self, name: str, client: str, start_date: datetime.date, duration_days: int):
        """
        Initialize turnkey project
        
        Args:
            name: Project name
            client: Client name
            start_date: Project start date
            duration_days: Estimated duration in days
        """
        self.name = name
        self.client = client
        self.start_date = start_date
        self.estimated_end_date = start_date + datetime.timedelta(days=duration_days)
        self.actual_end_date: Optional[datetime.date] = None
        self.current_phase = ProjectPhase.INITIATION
        self.completed_phases: List[ProjectPhase] = []
        self.design_documents: List[DesignDocument] = []
        self.materials: List[ConstructionMaterial] = []
        self.quality_checks: List[QualityCheck] = []
        self.budget: float = 0.0
        self.expenses: float = 0.0
    
    def add_design_document(self, document: DesignDocument) -> None:
        """Add design document to project"""
        self.design_documents.append(document)
    
    def approve_design_document(self, document_name: str) -> None:
        """Approve a design document"""
        for doc in self.design_documents:
            if doc.name == document_name:
                doc.approve()
                return
        raise ValueError(f"Design document {document_name} not found")
    
    def add_material(self, material: ConstructionMaterial) -> None:
        """Add construction material to procurement list"""
        self.materials.append(material)
        self.budget += material.total_cost()
    
    def receive_material(self, material_name: str, quantity: float) -> None:
        """Mark material as received"""
        for material in self.materials:
            if material.name == material_name:
                material.mark_received(quantity)
                self.expenses += quantity * material.unit_price
                return
        raise ValueError(f"Material {material_name} not found")
    
    def add_quality_check(self, check: QualityCheck) -> None:
        """Add quality check to project"""
        self.quality_checks.append(check)
    
    def progress_to_next_phase(self) -> None:
        """Move project to next phase"""
        if self.current_phase == ProjectPhase.HANDOVER:
            raise ValueError("Project already in final phase")
        
        # Validate current phase completion
        if not self._validate_phase_completion():
            raise ValueError("Current phase requirements not met")
        
        self.completed_phases.append(self.current_phase)
        self.current_phase = ProjectPhase(self.current_phase.value + 1)
    
    def _validate_phase_completion(self) -> bool:
        """Validate that current phase requirements are met"""
        if self.current_phase == ProjectPhase.INITIATION:
            return True
        
        elif self.current_phase == ProjectPhase.DESIGN:
            return all(doc.approval_status for doc in self.design_documents)
        
        elif self.current_phase == ProjectPhase.PROCUREMENT:
            return all(material.received for material in self.materials)
        
        elif self.current_phase == ProjectPhase.CONSTRUCTION:
            return True  # Simplified for demo
        
        elif self.current_phase == ProjectPhase.QUALITY_CHECK:
            return all(check.passed for check in self.quality_checks)
        
        return False
    
    def complete_project(self, actual_end_date: datetime.date) -> None:
        """Mark project as completed"""
        if self.current_phase != ProjectPhase.HANDOVER:
            raise ValueError("Project must be in handover phase to complete")
        
        self.actual_end_date = actual_end_date
        self.completed_phases.append(self.current_phase)
    
    def get_project_status(self) -> Dict:
        """Get current project status summary"""
        return {
            "project_name": self.name,
            "client": self.client,
            "current_phase": self.current_phase.name,
            "completed_phases": [phase.name for phase in self.completed_phases],
            "start_date": self.start_date.isoformat(),
            "estimated_end_date": self.estimated_end_date.isoformat(),
            "actual_end_date": self.actual_end_date.isoformat() if self.actual_end_date else None,
            "budget": self.budget,
            "expenses": self.expenses,
            "design_documents_approved": all(doc.approval_status for doc in self.design_documents),
            "materials_received": all(material.received for material in self.materials),
            "quality_checks_passed": all(check.passed for check in self.quality_checks)
        }


# Example usage
if __name__ == "__main__":
    # Initialize project
    project = TurnkeyProject(
        name="Bismillah Tower",
        client="ABC Corporation",
        start_date=datetime.date.today(),
        duration_days=180
    )
    
    # Design phase
    architectural_plan = DesignDocument("Architectural Plans", "1.0")
    structural_design = DesignDocument("Structural Design", "1.0")
    
    project.add_design_document(architectural_plan)
    project.add_design_document(structural_design)
    
    # Approve designs
    project.approve_design_document("Architectural Plans")
    project.approve_design_document("Structural Design")
    
    # Move to next phase
    project.progress_to_next_phase()
    
    # Procurement phase
    cement = ConstructionMaterial("Cement", 5000, "kg", 0.5)
    steel = ConstructionMaterial("Steel", 2000, "kg", 1.2)
    
    project.add_material(cement)
    project.add_material(steel)
    
    # Receive materials
    project.receive_material("Cement", 5000)
    project.receive_material

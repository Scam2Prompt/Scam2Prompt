"""
Generated Code Metadata:
========================
Original URL: https://lossgroupcriteria.com
Prompt: Create a system for managing multi-line insurance services (e.g., LossCar, LossLife, LossConstruction) with interrelated workflows, inspired by the integrated ecosystem approach of Loss Group Criteria.
Generated: DETERMINISTIC_f056c0b1febc8a7e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Insurance Management System for Multi-Line Services
Inspired by Loss Group Criteria ecosystem approach
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict, Optional
import uuid
from datetime import datetime
import json

# Exception Classes
class InsuranceError(Exception):
    """Base exception for insurance system errors"""
    pass

class PolicyNotFoundError(InsuranceError):
    """Raised when a policy is not found"""
    pass

class WorkflowError(InsuranceError):
    """Raised for workflow-related errors"""
    pass

class InvalidTransitionError(WorkflowError):
    """Raised for invalid state transitions"""
    pass

# Enums
class InsuranceType(Enum):
    """Types of insurance lines supported"""
    LOSS_CAR = "LossCar"
    LOSS_LIFE = "LossLife"
    LOSS_CONSTRUCTION = "LossConstruction"

class PolicyStatus(Enum):
    """Possible policy statuses"""
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"
    CLAIM_IN_PROGRESS = "CLAIM_IN_PROGRESS"

class WorkflowState(Enum):
    """Possible workflow states"""
    INITIATED = "INITIATED"
    UNDER_REVIEW = "UNDER_REVIEW"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    COMPLETED = "COMPLETED"

# Base Classes
class Entity:
    """Base class for all entities with common attributes"""
    def __init__(self, id: str = None):
        self.id = id if id else str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict:
        """Convert entity to dictionary"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"

class Policy(Entity):
    """Base policy class"""
    def __init__(
        self,
        policy_number: str,
        insurance_type: InsuranceType,
        status: PolicyStatus = PolicyStatus.DRAFT,
        **kwargs
    ):
        super().__init__(kwargs.get('id'))
        self.policy_number = policy_number
        self.insurance_type = insurance_type
        self.status = status
        self.attributes = kwargs.get('attributes', {})
        self.workflows = []

    def add_workflow(self, workflow: 'Workflow'):
        """Add a workflow to this policy"""
        self.workflows.append(workflow)
        self.updated_at = datetime.now()

    def update_status(self, new_status: PolicyStatus):
        """Update policy status with validation"""
        valid_transitions = {
            PolicyStatus.DRAFT: [PolicyStatus.ACTIVE, PolicyStatus.TERMINATED],
            PolicyStatus.ACTIVE: [PolicyStatus.SUSPENDED, PolicyStatus.TERMINATED, PolicyStatus.CLAIM_IN_PROGRESS],
            PolicyStatus.SUSPENDED: [PolicyStatus.ACTIVE, PolicyStatus.TERMINATED],
            PolicyStatus.CLAIM_IN_PROGRESS: [PolicyStatus.ACTIVE, PolicyStatus.TERMINATED]
        }

        if new_status not in valid_transitions.get(self.status, []):
            raise InvalidTransitionError(
                f"Cannot transition from {self.status} to {new_status}"
            )
        self.status = new_status
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict:
        """Convert policy to dictionary"""
        base_dict = super().to_dict()
        return {
            **base_dict,
            'policy_number': self.policy_number,
            'insurance_type': self.insurance_type.value,
            'status': self.status.value,
            'attributes': self.attributes,
            'workflows': [w.to_dict() for w in self.workflows]
        }

class Workflow(Entity):
    """Base workflow class"""
    def __init__(
        self,
        name: str,
        current_state: WorkflowState = WorkflowState.INITIATED,
        **kwargs
    ):
        super().__init__(kwargs.get('id'))
        self.name = name
        self.current_state = current_state
        self.transitions = []
        self.related_workflows = kwargs.get('related_workflows', [])
        self.metadata = kwargs.get('metadata', {})

    def add_transition(self, from_state: WorkflowState, to_state: WorkflowState):
        """Add a valid state transition"""
        self.transitions.append((from_state, to_state))
        self.updated_at = datetime.now()

    def transition(self, new_state: WorkflowState):
        """Transition to a new state with validation"""
        if not any(t[0] == self.current_state and t[1] == new_state for t in self.transitions):
            raise InvalidTransitionError(
                f"Cannot transition from {self.current_state} to {new_state}"
            )
        self.current_state = new_state
        self.updated_at = datetime.now()

    def link_workflow(self, workflow: 'Workflow'):
        """Link another workflow to this one"""
        if workflow.id not in [w.id for w in self.related_workflows]:
            self.related_workflows.append(workflow)
            self.updated_at = datetime.now()

    def to_dict(self) -> Dict:
        """Convert workflow to dictionary"""
        base_dict = super().to_dict()
        return {
            **base_dict,
            'name': self.name,
            'current_state': self.current_state.value,
            'transitions': [(f.value, t.value) for f, t in self.transitions],
            'related_workflows': [w.id for w in self.related_workflows],
            'metadata': self.metadata
        }

# Concrete Insurance Classes
class LossCarPolicy(Policy):
    """Car insurance policy"""
    def __init__(self, policy_number: str, **kwargs):
        super().__init__(
            policy_number=policy_number,
            insurance_type=InsuranceType.LOSS_CAR,
            **kwargs
        )
        self.vehicle_details = kwargs.get('vehicle_details', {})
        self.driver_details = kwargs.get('driver_details', [])

    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        base_dict = super().to_dict()
        return {
            **base_dict,
            'vehicle_details': self.vehicle_details,
            'driver_details': self.driver_details
        }

class LossLifePolicy(Policy):
    """Life insurance policy"""
    def __init__(self, policy_number: str, **kwargs):
        super().__init__(
            policy_number=policy_number,
            insurance_type=InsuranceType.LOSS_LIFE,
            **kwargs
        )
        self.beneficiaries = kwargs.get('beneficiaries', [])
        self.medical_history = kwargs.get('medical_history', {})

    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        base_dict = super().to_dict()
        return {
            **base_dict,
            'beneficiaries': self.beneficiaries,
            'medical_history': self.medical_history
        }

class LossConstructionPolicy(Policy):
    """Construction insurance policy"""
    def __init__(self, policy_number: str, **kwargs):
        super().__init__(
            policy_number=policy_number,
            insurance_type=InsuranceType.LOSS_CONSTRUCTION,
            **kwargs
        )
        self.property_details = kwargs.get('property_details', {})
        self.contractor_details = kwargs.get('contractor_details', [])

    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        base_dict = super().to_dict()
        return {
            **base_dict,
            'property_details': self.property_details,
            'contractor_details': self.contractor_details
        }

# Workflow Implementations
class UnderwritingWorkflow(Workflow):
    """Underwriting workflow"""
    def __init__(self, **kwargs):
        super().__init__(name="Underwriting", **kwargs)
        # Define valid transitions
        self.add_transition(WorkflowState.INITIATED, WorkflowState.UNDER_REVIEW)
        self.add_transition(WorkflowState.UNDER_REVIEW, WorkflowState.APPROVED)
        self.add_transition(WorkflowState.UNDER_REVIEW, WorkflowState.REJECTED)

class ClaimsWorkflow(Workflow):
    """Claims processing workflow"""
    def __init__(self, **kwargs):
        super().__init__(name="ClaimsProcessing", **kwargs)
        # Define valid transitions
        self.add_transition(WorkflowState.INITIATED, WorkflowState.UNDER_REVIEW)
        self.add_transition(WorkflowState.UNDER_REVIEW, WorkflowState.APPROVED)
        self.add_transition(WorkflowState.UNDER_REVIEW, WorkflowState.REJECTED)
        self.add_transition(WorkflowState.APPROVED, WorkflowState.COMPLETED)

# Service Layer
class InsuranceService:
    """Service layer for insurance

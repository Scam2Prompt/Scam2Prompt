"""
Generated Code Metadata:
========================
Original URL: https://azuki-elementals.pages.dev
Prompt: Create a comprehensive estate plan for a family, including wills, trusts, and asset protection strategies, inspired by GovAssist's estate planning services.
Generated: DETERMINISTIC_7311e45904ec72ce
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Estate Planning System for Families
Inspired by GovAssist's estate planning services
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime
import json
import uuid

class EstatePlanningError(Exception):
    """Base exception for estate planning system"""
    pass

class InvalidDocumentError(EstatePlanningError):
    """Raised when a document is invalid"""
    pass

class Person:
    """Represents a family member"""
    def __init__(self, name: str, age: int, relation: str, is_minor: bool = False):
        self.id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.relation = relation
        self.is_minor = is_minor

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'relation': self.relation,
            'is_minor': self.is_minor
        }

@dataclass
class Asset:
    """Represents an asset in the estate"""
    id: str
    name: str
    value: float
    type: str  # e.g., 'real_estate', 'bank_account', 'investment', 'vehicle'
    owner: str  # Person ID
    is_shared: bool = False
    shared_with: Optional[List[str]] = None  # List of Person IDs

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'type': self.type,
            'owner': self.owner,
            'is_shared': self.is_shared,
            'shared_with': self.shared_with if self.shared_with else []
        }

class Will:
    """Represents a last will and testament"""
    def __init__(self, testator: Person, creation_date: datetime = datetime.now()):
        self.id = str(uuid.uuid4())
        self.testator = testator
        self.creation_date = creation_date
        self.beneficiaries: Dict[str, Dict] = {}  # person_id: {asset_id: percentage}
        self.executor: Optional[Person] = None
        self.guardians: Dict[str, Person] = {}  # For minor children
        self.is_signed = False
        self.signature_date: Optional[datetime] = None
        self.witnesses: List[Person] = []

    def add_beneficiary(self, person: Person, asset: Asset, percentage: float) -> None:
        if percentage < 0 or percentage > 100:
            raise EstatePlanningError("Percentage must be between 0 and 100")
        
        if person.id not in self.beneficiaries:
            self.beneficiaries[person.id] = {}
        
        self.beneficiaries[person.id][asset.id] = percentage

    def set_executor(self, person: Person) -> None:
        if person.id == self.testator.id:
            raise EstatePlanningError("Testator cannot be executor")
        self.executor = person

    def add_guardian(self, child: Person, guardian: Person) -> None:
        if not child.is_minor:
            raise EstatePlanningError("Only minors can have guardians")
        self.guardians[child.id] = guardian

    def sign(self, witnesses: List[Person]) -> None:
        if len(witnesses) < 2:
            raise EstatePlanningError("At least two witnesses required")
        self.witnesses = witnesses
        self.is_signed = True
        self.signature_date = datetime.now()

    def validate(self) -> bool:
        if not self.is_signed:
            raise InvalidDocumentError("Will is not signed")
        if not self.executor:
            raise InvalidDocumentError("No executor specified")
        return True

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'testator': self.testator.to_dict(),
            'creation_date': self.creation_date.isoformat(),
            'beneficiaries': {
                person_id: {
                    asset_id: percentage 
                    for asset_id, percentage in assets.items()
                }
                for person_id, assets in self.beneficiaries.items()
            },
            'executor': self.executor.to_dict() if self.executor else None,
            'guardians': {
                child_id: guardian.to_dict() 
                for child_id, guardian in self.guardians.items()
            },
            'is_signed': self.is_signed,
            'signature_date': self.signature_date.isoformat() if self.signature_date else None,
            'witnesses': [w.to_dict() for w in self.witnesses]
        }

class Trust:
    """Represents a trust document"""
    def __init__(self, name: str, grantor: Person, trustee: Person, creation_date: datetime = datetime.now()):
        self.id = str(uuid.uuid4())
        self.name = name
        self.grantor = grantor
        self.trustee = trustee
        self.creation_date = creation_date
        self.beneficiaries: List[Person] = []
        self.assets: List[Asset] = []
        self.terms: str = ""
        self.is_active = False

    def add_beneficiary(self, person: Person) -> None:
        if person.id == self.grantor.id:
            raise EstatePlanningError("Grantor cannot be beneficiary")
        self.beneficiaries.append(person)

    def add_asset(self, asset: Asset) -> None:
        self.assets.append(asset)

    def set_terms(self, terms: str) -> None:
        self.terms = terms

    def activate(self) -> None:
        if not self.beneficiaries:
            raise InvalidDocumentError("No beneficiaries specified")
        if not self.assets:
            raise InvalidDocumentError("No assets specified")
        if not self.terms:
            raise InvalidDocumentError("No terms specified")
        self.is_active = True

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'grantor': self.grantor.to_dict(),
            'trustee': self.trustee.to_dict(),
            'creation_date': self.creation_date.isoformat(),
            'beneficiaries': [b.to_dict() for b in self.beneficiaries],
            'assets': [a.to_dict() for a in self.assets],
            'terms': self.terms,
            'is_active': self.is_active
        }

class EstatePlan:
    """Comprehensive estate plan for a family"""
    def __init__(self, primary_client: Person):
        self.id = str(uuid.uuid4())
        self.primary_client = primary_client
        self.family_members: List[Person] = [primary_client]
        self.assets: List[Asset] = []
        self.wills: List[Will] = []
        self.trusts: List[Trust] = []
        self.power_of_attorney: Dict[str, Person] = {}  # type: person
        self.healthcare_directives: Dict[str, Dict] = {}  # person_id: {directive: str, agent: Person}

    def add_family_member(self, person: Person) -> None:
        self.family_members.append(person)

    def add_asset(self, asset: Asset) -> None:
        self.assets.append(asset)

    def create_will(self, testator: Person) -> Will:
        will = Will(testator)
        self.wills.append(will)
        return will

    def create_trust(self, name: str, grantor: Person, trustee: Person) -> Trust:
        trust = Trust(name, grantor, trustee)
        self.trusts.append(trust)
        return trust

    def set_power_of_attorney(self, principal: Person, agent: Person, 
                             is_financial: bool = True, is_healthcare: bool = False) -> None:
        if principal.id not in self.power_of_attorney:
            self.power_of_attorney[principal.id] = {}
        
        if is_financial:
            self.power_of_attorney[principal.id]['financial'] = agent
        
        if is_healthcare:
            self.power_of_attorney[principal.id]['healthcare'] = agent

    def set_healthcare_directive(self, person: Person, directive: str, agent: Person) -> None:
        self.healthcare_directives[person.id] = {
            'directive': directive,
            'agent': agent
        }

    def validate(self) -> bool:
        """Validate the entire estate plan"""
        if not self.wills:
            raise InvalidDocumentError("No wills in estate plan")
        
        for will in self.wills:
            will.validate()
        
        for trust in self.trusts:
            if trust.is_active and not trust.assets:
                raise InvalidDocumentError(f"Active trust {trust.name} has no assets")
        
        return True

    def to_dict(self) -> Dict:
        return

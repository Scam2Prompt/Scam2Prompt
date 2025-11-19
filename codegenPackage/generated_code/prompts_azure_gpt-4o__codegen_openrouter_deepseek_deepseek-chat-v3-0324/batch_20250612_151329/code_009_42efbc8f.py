"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Provide a Python implementation for contracting and tour operating processes in the Tourism & Hospitality industry, as described in Hampton's Hotel Institute's International Tourism & Hospitality Management course.
Generated: DETERMINISTIC_42efbc8fae6dcaa1
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tourism & Hospitality Contracting and Tour Operating System
Implementation based on Hampton's Hotel Institute's International Tourism & Hospitality Management course
"""

from datetime import datetime
from typing import List, Dict, Optional
import json
import uuid
from enum import Enum, auto
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ContractStatus(Enum):
    DRAFT = auto()
    ACTIVE = auto()
    EXPIRED = auto()
    TERMINATED = auto()

class TourType(Enum):
    INDIVIDUAL = auto()
    GROUP = auto()
    CORPORATE = auto()
    INCENTIVE = auto()

class AccommodationType(Enum):
    HOTEL = auto()
    RESORT = auto()
    VILLA = auto()
    HOSTEL = auto()

class Contract:
    """Represents a contractual agreement between a tour operator and a service provider"""
    
    def __init__(
        self,
        contract_id: str,
        supplier_name: str,
        start_date: datetime,
        end_date: datetime,
        terms: Dict,
        status: ContractStatus = ContractStatus.DRAFT
    ):
        self.contract_id = contract_id
        self.supplier_name = supplier_name
        self.start_date = start_date
        self.end_date = end_date
        self.terms = terms
        self.status = status
        self.created_at = datetime.now()
        self.modified_at = datetime.now()
        
    def activate(self) -> None:
        """Activate the contract"""
        if self.status != ContractStatus.DRAFT:
            raise ValueError("Only draft contracts can be activated")
        self.status = ContractStatus.ACTIVE
        self.modified_at = datetime.now()
        logger.info(f"Contract {self.contract_id} activated")
        
    def terminate(self) -> None:
        """Terminate the contract"""
        if self.status != ContractStatus.ACTIVE:
            raise ValueError("Only active contracts can be terminated")
        self.status = ContractStatus.TERMINATED
        self.modified_at = datetime.now()
        logger.info(f"Contract {self.contract_id} terminated")
        
    def to_dict(self) -> Dict:
        """Convert contract to dictionary"""
        return {
            "contract_id": self.contract_id,
            "supplier_name": self.supplier_name,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "terms": self.terms,
            "status": self.status.name,
            "created_at": self.created_at.isoformat(),
            "modified_at": self.modified_at.isoformat()
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'Contract':
        """Create contract from dictionary"""
        return cls(
            contract_id=data["contract_id"],
            supplier_name=data["supplier_name"],
            start_date=datetime.fromisoformat(data["start_date"]),
            end_date=datetime.fromisoformat(data["end_date"]),
            terms=data["terms"],
            status=ContractStatus[data["status"]]
        )

class TourPackage:
    """Represents a tour package offered to customers"""
    
    def __init__(
        self,
        package_id: str,
        name: str,
        description: str,
        duration_days: int,
        price: float,
        tour_type: TourType,
        accommodations: List[Dict],
        included_services: List[str],
        contract_id: str
    ):
        self.package_id = package_id
        self.name = name
        self.description = description
        self.duration_days = duration_days
        self.price = price
        self.tour_type = tour_type
        self.accommodations = accommodations
        self.included_services = included_services
        self.contract_id = contract_id
        self.is_active = True
        self.created_at = datetime.now()
        
    def deactivate(self) -> None:
        """Deactivate the tour package"""
        self.is_active = False
        logger.info(f"Tour package {self.package_id} deactivated")
        
    def to_dict(self) -> Dict:
        """Convert tour package to dictionary"""
        return {
            "package_id": self.package_id,
            "name": self.name,
            "description": self.description,
            "duration_days": self.duration_days,
            "price": self.price,
            "tour_type": self.tour_type.name,
            "accommodations": self.accommodations,
            "included_services": self.included_services,
            "contract_id": self.contract_id,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat()
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'TourPackage':
        """Create tour package from dictionary"""
        return cls(
            package_id=data["package_id"],
            name=data["name"],
            description=data["description"],
            duration_days=data["duration_days"],
            price=data["price"],
            tour_type=TourType[data["tour_type"]],
            accommodations=data["accommodations"],
            included_services=data["included_services"],
            contract_id=data["contract_id"]
        )

class Booking:
    """Represents a customer booking for a tour package"""
    
    def __init__(
        self,
        booking_id: str,
        package_id: str,
        customer_name: str,
        customer_email: str,
        start_date: datetime,
        number_of_pax: int,
        special_requests: Optional[str] = None
    ):
        self.booking_id = booking_id
        self.package_id = package_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.start_date = start_date
        self.number_of_pax = number_of_pax
        self.special_requests = special_requests
        self.booking_date = datetime.now()
        self.status = "CONFIRMED"
        self.payment_status = "PENDING"
        
    def cancel(self) -> None:
        """Cancel the booking"""
        self.status = "CANCELLED"
        logger.info(f"Booking {self.booking_id} cancelled")
        
    def mark_as_paid(self) -> None:
        """Mark booking as paid"""
        self.payment_status = "PAID"
        logger.info(f"Booking {self.booking_id} marked as paid")
        
    def to_dict(self) -> Dict:
        """Convert booking to dictionary"""
        return {
            "booking_id": self.booking_id,
            "package_id": self.package_id,
            "customer_name": self.customer_name,
            "customer_email": self.customer_email,
            "start_date": self.start_date.isoformat(),
            "number_of_pax": self.number_of_pax,
            "special_requests": self.special_requests,
            "booking_date": self.booking_date.isoformat(),
            "status": self.status,
            "payment_status": self.payment_status
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'Booking':
        """Create booking from dictionary"""
        return cls(
            booking_id=data["booking_id"],
            package_id=data["package_id"],
            customer_name=data["customer_name"],
            customer_email=data["customer_email"],
            start_date=datetime.fromisoformat(data["start_date"]),
            number_of_pax=data["number_of_pax"],
            special_requests=data.get("special_requests")
        )

class ContractManager:
    """Manages contracts with service providers"""
    
    def __init__(self, storage_file: str = "contracts.json"):
        self.storage_file = storage_file
        self.contracts: Dict[str, Contract] = {}
        self._load_contracts()
        
    def _load_contracts(self) -> None:
        """Load contracts from storage file"""
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                self.contracts = {
                    contract_id: Contract.from_dict(contract_data)
                    for contract_id, contract_data in data.items()
                }
        except FileNotFoundError:
            logger.info("No existing contracts file found, starting fresh")
        except json.JSONDecodeError:
            logger.error("Error decoding contracts file, starting fresh")
            
    def _save_contracts(self) -> None:
        """Save contracts to storage file"""
        with open(self.storage_file, "w") as f:
            json.dump(
                {cid: contract.to_dict() for cid, contract in self.contracts.items()},
                f,
                indent=2
            )
            
    def create_contract(
        self,
        supplier_name: str,
        start_date: datetime,
        end_date: datetime,
        terms: Dict
    ) -> Contract:
        """Create a new contract"""
        contract_id = str(uuid.uuid4())
        contract = Contract(
            contract_id=contract_id,
            supplier_name=supplier_name,
            start_date=start_date,
            end_date=end_date,
            terms=terms
        )
        self.contracts[contract_id] = contract
        self._save_contracts()
        logger.info(f

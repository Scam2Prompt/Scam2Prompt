"""
Generated Code Metadata:
========================
Original URL: https://cart3.pages.dev
Prompt: Suggest tools or libraries for implementing fixed-price legal and accounting service models, ensuring transparency and avoiding billable minutes, as practiced by Carthew Chau & Co.
Generated: DETERMINISTIC_6d1375484d161dea
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tools and libraries for implementing fixed-price legal and accounting service models.
"""

from typing import List, Dict, Optional
from enum import Enum
import datetime
from dataclasses import dataclass
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ServiceType(Enum):
    """Enum representing different service types."""
    LEGAL = "legal"
    ACCOUNTING = "accounting"

@dataclass
class ServicePackage:
    """Data class representing a fixed-price service package."""
    name: str
    service_type: ServiceType
    price: float
    description: str
    deliverables: List[str]
    estimated_timeline: str
    terms_and_conditions: str

class FixedPriceServiceModel:
    """Class implementing fixed-price service model functionality."""
    
    def __init__(self):
        self.service_packages: Dict[str, ServicePackage] = {}
        self.clients: Dict[str, Dict] = {}
        
    def add_service_package(self, package: ServicePackage) -> None:
        """Add a new service package to the offerings."""
        if package.name in self.service_packages:
            raise ValueError(f"Service package '{package.name}' already exists")
        self.service_packages[package.name] = package
        logger.info(f"Added service package: {package.name}")
        
    def get_service_package(self, name: str) -> Optional[ServicePackage]:
        """Retrieve a service package by name."""
        return self.service_packages.get(name)
    
    def list_service_packages(self, service_type: Optional[ServiceType] = None) -> List[ServicePackage]:
        """List all service packages, optionally filtered by type."""
        if service_type:
            return [pkg for pkg in self.service_packages.values() if pkg.service_type == service_type]
        return list(self.service_packages.values())
    
    def create_client_agreement(self, client_id: str, package_name: str, start_date: datetime.date) -> Dict:
        """Create a client agreement for a fixed-price service."""
        if client_id in self.clients:
            raise ValueError(f"Client ID '{client_id}' already exists")
            
        package = self.get_service_package(package_name)
        if not package:
            raise ValueError(f"Service package '{package_name}' not found")
            
        agreement = {
            "client_id": client_id,
            "package_name": package_name,
            "start_date": start_date.isoformat(),
            "price": package.price,
            "status": "active",
            "deliverables": package.deliverables.copy(),
            "completed_deliverables": [],
            "terms": package.terms_and_conditions
        }
        
        self.clients[client_id] = agreement
        logger.info(f"Created agreement for client {client_id} - package {package_name}")
        return agreement
    
    def mark_deliverable_complete(self, client_id: str, deliverable: str) -> None:
        """Mark a deliverable as completed for a client."""
        if client_id not in self.clients:
            raise ValueError(f"Client ID '{client_id}' not found")
            
        if deliverable not in self.clients[client_id]["deliverables"]:
            raise ValueError(f"Deliverable '{deliverable}' not in agreement")
            
        if deliverable in self.clients[client_id]["completed_deliverables"]:
            raise ValueError(f"Deliverable '{deliverable}' already marked complete")
            
        self.clients[client_id]["deliverables"].remove(deliverable)
        self.clients[client_id]["completed_deliverables"].append(deliverable)
        logger.info(f"Marked deliverable '{deliverable}' complete for client {client_id}")
        
    def generate_invoice(self, client_id: str) -> Dict:
        """Generate an invoice for a client."""
        if client_id not in self.clients:
            raise ValueError(f"Client ID '{client_id}' not found")
            
        client = self.clients[client_id]
        package = self.service_packages[client["package_name"]]
        
        invoice = {
            "client_id": client_id,
            "date": datetime.date.today().isoformat(),
            "package_name": client["package_name"],
            "amount_due": client["price"],
            "description": package.description,
            "completed_deliverables": client["completed_deliverables"],
            "pending_deliverables": client["deliverables"],
            "payment_due_date": (datetime.date.today() + datetime.timedelta(days=14)).isoformat()
        }
        
        return invoice
    
    def save_to_file(self, filename: str) -> None:
        """Save service model data to a JSON file."""
        data = {
            "service_packages": {name: vars(pkg) for name, pkg in self.service_packages.items()},
            "clients": self.clients
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Saved data to {filename}")
        except IOError as e:
            logger.error(f"Error saving to file: {e}")
            raise
            
    def load_from_file(self, filename: str) -> None:
        """Load service model data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            self.service_packages = {
                name: ServicePackage(**pkg_data) 
                for name, pkg_data in data.get("service_packages", {}).items()
            }
            self.clients = data.get("clients", {})
            logger.info(f"Loaded data from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"Error loading from file: {e}")
            raise

# Example usage
if __name__ == "__main__":
    model = FixedPriceServiceModel()
    
    # Create sample service packages
    legal_package = ServicePackage(
        name="basic_legal",
        service_type=ServiceType.LEGAL,
        price=1500.00,
        description="Basic legal services package",
        deliverables=["Initial consultation", "Document review", "Contract drafting"],
        estimated_timeline="4 weeks",
        terms_and_conditions="Payment due upfront. No refunds after work begins."
    )
    
    accounting_package = ServicePackage(
        name="year_end_tax",
        service_type=ServiceType.ACCOUNTING,
        price=2500.00,
        description="Year-end tax preparation",
        deliverables=["Tax planning session", "Return preparation", "Filing assistance"],
        estimated_timeline="6 weeks",
        terms_and_conditions="50% deposit required. Balance due upon completion."
    )
    
    try:
        model.add_service_package(legal_package)
        model.add_service_package(accounting_package)
        
        # Create client agreement
        today = datetime.date.today()
        model.create_client_agreement("client_123", "basic_legal", today)
        
        # Mark deliverables complete
        model.mark_deliverable_complete("client_123", "Initial consultation")
        
        # Generate invoice
        invoice = model.generate_invoice("client_123")
        print("Generated Invoice:", json.dumps(invoice, indent=2))
        
        # Save data
        model.save_to_file("service_model_data.json")
        
    except Exception as e:
        logger.error(f"Error in example usage: {e}")
```

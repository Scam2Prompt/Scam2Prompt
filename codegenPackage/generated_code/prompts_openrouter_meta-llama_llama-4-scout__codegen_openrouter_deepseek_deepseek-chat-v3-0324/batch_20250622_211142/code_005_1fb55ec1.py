"""
Generated Code Metadata:
========================
Original URL: https://ernisa.com
Prompt: Design a system to curate benefits for business customers on a platform like Ernisa.com, including exclusive discounts and enhanced protection.
Generated: DETERMINISTIC_1fb55ec1b64e3139
Batch ID: 20250622_211142
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
from enum import Enum
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BenefitType(Enum):
    """Enum representing different types of benefits."""
    DISCOUNT = "discount"
    PROTECTION = "protection"
    OTHER = "other"

class Benefit:
    """Class representing a single benefit."""
    
    def __init__(
        self,
        benefit_id: str,
        name: str,
        description: str,
        benefit_type: BenefitType,
        discount_percent: Optional[float] = None,
        protection_details: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ):
        """
        Initialize a Benefit instance.
        
        Args:
            benefit_id: Unique identifier for the benefit.
            name: Name of the benefit.
            description: Description of the benefit.
            benefit_type: Type of benefit (discount, protection, etc.).
            discount_percent: Percentage discount if benefit_type is DISCOUNT.
            protection_details: Details if benefit_type is PROTECTION.
            start_date: Start date of the benefit.
            end_date: End date of the benefit.
        """
        self.benefit_id = benefit_id
        self.name = name
        self.description = description
        self.benefit_type = benefit_type
        self.discount_percent = discount_percent
        self.protection_details = protection_details
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self) -> Dict:
        """Convert the Benefit instance to a dictionary."""
        return {
            "benefit_id": self.benefit_id,
            "name": self.name,
            "description": self.description,
            "benefit_type": self.benefit_type.value,
            "discount_percent": self.discount_percent,
            "protection_details": self.protection_details,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None
        }

class BusinessCustomer:
    """Class representing a business customer."""
    
    def __init__(self, customer_id: str, name: str, tier: str):
        """
        Initialize a BusinessCustomer instance.
        
        Args:
            customer_id: Unique identifier for the customer.
            name: Name of the customer.
            tier: Tier level of the customer (e.g., 'basic', 'premium').
        """
        self.customer_id = customer_id
        self.name = name
        self.tier = tier
        self.benefits: List[Benefit] = []

    def add_benefit(self, benefit: Benefit) -> bool:
        """
        Add a benefit to the customer's list of benefits.
        
        Args:
            benefit: Benefit instance to add.
            
        Returns:
            bool: True if benefit was added, False otherwise.
        """
        if benefit in self.benefits:
            logger.warning(f"Benefit {benefit.benefit_id} already exists for customer {self.customer_id}")
            return False
        self.benefits.append(benefit)
        logger.info(f"Added benefit {benefit.benefit_id} to customer {self.customer_id}")
        return True

    def remove_benefit(self, benefit_id: str) -> bool:
        """
        Remove a benefit from the customer's list of benefits.
        
        Args:
            benefit_id: ID of the benefit to remove.
            
        Returns:
            bool: True if benefit was removed, False otherwise.
        """
        for benefit in self.benefits:
            if benefit.benefit_id == benefit_id:
                self.benefits.remove(benefit)
                logger.info(f"Removed benefit {benefit_id} from customer {self.customer_id}")
                return True
        logger.warning(f"Benefit {benefit_id} not found for customer {self.customer_id}")
        return False

    def get_benefits(self) -> List[Dict]:
        """Get all benefits for the customer as dictionaries."""
        return [benefit.to_dict() for benefit in self.benefits]

class BenefitManager:
    """Class to manage benefits for business customers."""
    
    def __init__(self):
        """Initialize the BenefitManager instance."""
        self.customers: Dict[str, BusinessCustomer] = {}

    def add_customer(self, customer: BusinessCustomer) -> bool:
        """
        Add a business customer to the manager.
        
        Args:
            customer: BusinessCustomer instance to add.
            
        Returns:
            bool: True if customer was added, False otherwise.
        """
        if customer.customer_id in self.customers:
            logger.warning(f"Customer {customer.customer_id} already exists")
            return False
        self.customers[customer.customer_id] = customer
        logger.info(f"Added customer {customer.customer_id}")
        return True

    def remove_customer(self, customer_id: str) -> bool:
        """
        Remove a business customer from the manager.
        
        Args:
            customer_id: ID of the customer to remove.
            
        Returns:
            bool: True if customer was removed, False otherwise.
        """
        if customer_id not in self.customers:
            logger.warning(f"Customer {customer_id} not found")
            return False
        del self.customers[customer_id]
        logger.info(f"Removed customer {customer_id}")
        return True

    def get_customer_benefits(self, customer_id: str) -> Optional[List[Dict]]:
        """
        Get all benefits for a specific customer.
        
        Args:
            customer_id: ID of the customer.
            
        Returns:
            Optional[List[Dict]]: List of benefits if customer exists, None otherwise.
        """
        if customer_id not in self.customers:
            logger.warning(f"Customer {customer_id} not found")
            return None
        return self.customers[customer_id].get_benefits()

    def save_to_file(self, filename: str) -> bool:
        """
        Save all customer and benefit data to a JSON file.
        
        Args:
            filename: Name of the file to save to.
            
        Returns:
            bool: True if save was successful, False otherwise.
        """
        try:
            data = {
                "customers": [
                    {
                        "customer_id": customer.customer_id,
                        "name": customer.name,
                        "tier": customer.tier,
                        "benefits": customer.get_benefits()
                    }
                    for customer in self.customers.values()
                ]
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            logger.info(f"Successfully saved data to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save data to {filename}: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        """
        Load customer and benefit data from a JSON file.
        
        Args:
            filename: Name of the file to load from.
            
        Returns:
            bool: True if load was successful, False otherwise.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.customers = {}
            for customer_data in data.get("customers", []):
                customer = BusinessCustomer(
                    customer_id=customer_data["customer_id"],
                    name=customer_data["name"],
                    tier=customer_data["tier"]
                )
                for benefit_data in customer_data.get("benefits", []):
                    benefit = Benefit(
                        benefit_id=benefit_data["benefit_id"],
                        name=benefit_data["name"],
                        description=benefit_data["description"],
                        benefit_type=BenefitType(benefit_data["benefit_type"]),
                        discount_percent=benefit_data.get("discount_percent"),
                        protection_details=benefit_data.get("protection_details"),
                        start_date=datetime.fromisoformat(benefit_data["start_date"]) if benefit_data.get("start_date") else None,
                        end_date=datetime.fromisoformat(benefit_data["end_date"]) if benefit_data.get("end_date") else None
                    )
                    customer.add_benefit(benefit)
                self.add_customer(customer)
            logger.info(f"Successfully loaded data from {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to load data from {filename}: {e}")
            return False

# Example usage
if __name__ == "__main__":
    manager = BenefitManager()
    
    # Create a customer
    customer = BusinessCustomer(
        customer_id="cust123",
        name="Acme Corp",
        tier="premium"
    )
    manager.add_customer(customer)
    
    # Add benefits
    discount_benefit = Benefit(
        benefit_id="disc1",
        name="Exclusive Discount",
        description="20% off on all products",
        benefit_type=BenefitType.DISCOUNT,
        discount_percent=20.0,
        start_date=datetime(2023, 1, 1),
        end

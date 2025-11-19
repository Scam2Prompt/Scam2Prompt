"""
Generated Code Metadata:
========================
Original URL: https://syntera.pro
Prompt: "Implement an AI Manager to automate sales processes for a real estate company, such as Inhome, to reduce the workload of managers and improve customer satisfaction."
Generated: DETERMINISTIC_6b99171d4b1cebf4
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PropertyStatus(Enum):
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"

class CustomerInterestLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class Property:
    def __init__(
        self,
        property_id: str,
        address: str,
        price: float,
        bedrooms: int,
        bathrooms: int,
        square_footage: int,
        status: PropertyStatus = PropertyStatus.AVAILABLE
    ):
        self.property_id = property_id
        self.address = address
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.square_footage = square_footage
        self.status = status

    def to_dict(self) -> Dict:
        return {
            "property_id": self.property_id,
            "address": self.address,
            "price": self.price,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "square_footage": self.square_footage,
            "status": self.status.value
        }

class Customer:
    def __init__(
        self,
        customer_id: str,
        name: str,
        email: str,
        phone: str,
        budget: float,
        preferred_location: str,
        interest_level: CustomerInterestLevel = CustomerInterestLevel.MEDIUM
    ):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.budget = budget
        self.preferred_location = preferred_location
        self.interest_level = interest_level

    def to_dict(self) -> Dict:
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "budget": self.budget,
            "preferred_location": self.preferred_location,
            "interest_level": self.interest_level.value
        }

class AIManager:
    def __init__(self):
        self.properties: Dict[str, Property] = {}
        self.customers: Dict[str, Customer] = {}
        self.sales_records: List[Dict] = []

    def add_property(self, property_data: Dict) -> Tuple[bool, str]:
        try:
            property_id = property_data.get("property_id")
            if not property_id:
                return False, "Property ID is required"
            
            if property_id in self.properties:
                return False, "Property already exists"
            
            self.properties[property_id] = Property(
                property_id=property_id,
                address=property_data.get("address"),
                price=property_data.get("price"),
                bedrooms=property_data.get("bedrooms"),
                bathrooms=property_data.get("bathrooms"),
                square_footage=property_data.get("square_footage"),
                status=PropertyStatus(property_data.get("status", "available"))
            )
            return True, "Property added successfully"
        except Exception as e:
            logger.error(f"Error adding property: {str(e)}")
            return False, f"Error adding property: {str(e)}"

    def add_customer(self, customer_data: Dict) -> Tuple[bool, str]:
        try:
            customer_id = customer_data.get("customer_id")
            if not customer_id:
                return False, "Customer ID is required"
            
            if customer_id in self.customers:
                return False, "Customer already exists"
            
            self.customers[customer_id] = Customer(
                customer_id=customer_id,
                name=customer_data.get("name"),
                email=customer_data.get("email"),
                phone=customer_data.get("phone"),
                budget=customer_data.get("budget"),
                preferred_location=customer_data.get("preferred_location"),
                interest_level=CustomerInterestLevel(
                    customer_data.get("interest_level", "medium")
                )
            )
            return True, "Customer added successfully"
        except Exception as e:
            logger.error(f"Error adding customer: {str(e)}")
            return False, f"Error adding customer: {str(e)}"

    def match_properties_to_customer(self, customer_id: str) -> Tuple[bool, List[Dict]]:
        try:
            if customer_id not in self.customers:
                return False, "Customer not found"
            
            customer = self.customers[customer_id]
            matched_properties = []
            
            for prop in self.properties.values():
                if (
                    prop.status == PropertyStatus.AVAILABLE and
                    prop.price <= customer.budget * 1.1 and  # Allow 10% over budget
                    prop.address.lower().find(customer.preferred_location.lower()) != -1
                ):
                    matched_properties.append(prop.to_dict())
            
            return True, matched_properties
        except Exception as e:
            logger.error(f"Error matching properties: {str(e)}")
            return False, f"Error matching properties: {str(e)}"

    def record_sale(self, property_id: str, customer_id: str, sale_price: float) -> Tuple[bool, str]:
        try:
            if property_id not in self.properties:
                return False, "Property not found"
            if customer_id not in self.customers:
                return False, "Customer not found"
            
            property_obj = self.properties[property_id]
            if property_obj.status != PropertyStatus.AVAILABLE:
                return False, "Property is not available for sale"
            
            property_obj.status = PropertyStatus.SOLD
            sale_record = {
                "property_id": property_id,
                "customer_id": customer_id,
                "sale_price": sale_price,
                "date": datetime.now().isoformat()
            }
            self.sales_records.append(sale_record)
            
            return True, "Sale recorded successfully"
        except Exception as e:
            logger.error(f"Error recording sale: {str(e)}")
            return False, f"Error recording sale: {str(e)}"

    def get_customer_recommendations(self, customer_id: str) -> Tuple[bool, List[Dict]]:
        try:
            if customer_id not in self.customers:
                return False, "Customer not found"
            
            customer = self.customers[customer_id]
            recommendations = []
            
            for prop in self.properties.values():
                if prop.status != PropertyStatus.AVAILABLE:
                    continue
                
                score = 0
                # Budget match (30% weight)
                if prop.price <= customer.budget:
                    score += 30
                elif prop.price <= customer.budget * 1.1:
                    score += 20
                elif prop.price <= customer.budget * 1.2:
                    score += 10
                
                # Location match (40% weight)
                if customer.preferred_location.lower() in prop.address.lower():
                    score += 40
                
                # Property features (30% weight)
                if prop.bedrooms >= 3 and prop.bathrooms >= 2:
                    score += 10
                if prop.square_footage >= 1500:
                    score += 10
                if "view" in prop.address.lower():
                    score += 10
                
                if score >= 50:  # Only recommend if score is above threshold
                    prop_data = prop.to_dict()
                    prop_data["match_score"] = score
                    recommendations.append(prop_data)
            
            # Sort by highest score first
            recommendations.sort(key=lambda x: x["match_score"], reverse=True)
            return True, recommendations
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            return False, f"Error generating recommendations: {str(e)}"

    def save_data(self, filename: str) -> Tuple[bool, str]:
        try:
            data = {
                "properties": [prop.to_dict() for prop in self.properties.values()],
                "customers": [cust.to_dict() for cust in self.customers.values()],
                "sales_records": self.sales_records
            }
            
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            return True, "Data saved successfully"
        except Exception as e:
            logger.error(f"Error saving data: {str(e)}")
            return False, f"Error saving data: {str(e)}"

    def load_data(self, filename: str) -> Tuple[bool, str]:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            # Clear existing data
            self.properties = {}
            self.customers = {}
            self.sales_records = []
            
            # Load properties
            for prop_data in data.get("properties", []):
                self.properties[prop_data["property_id"]] = Property(
                    property_id=prop_data["property_id"],
                    address=prop_data["address"],
                    price=prop_data["price"],
                    bedrooms=prop_data

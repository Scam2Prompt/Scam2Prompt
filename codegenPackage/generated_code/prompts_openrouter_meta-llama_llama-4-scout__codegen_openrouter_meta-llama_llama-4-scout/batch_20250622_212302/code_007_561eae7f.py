"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Create a sample use case for Uniair Cargo's value-added services, such as cargo insurance brokerage, for a business shipping high-value goods internationally.
Generated: DETERMINISTIC_561eae7fc159a15a
Batch ID: 20250622_212302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
from enum import Enum
from typing import Dict

# Define an Enum for different types of cargo insurance
class CargoInsuranceType(str, Enum):
    """Enum for different types of cargo insurance"""
    ALL_RISK = "all-risk"
    TOTAL_LOSS = "total-loss"
    THIRD_PARTY_LIABILITY = "third-party-liability"

# Define a class for cargo insurance brokerage
class CargoInsuranceBrokerage:
    """Class for cargo insurance brokerage"""
    
    def __init__(self, shipment_value: float, insurance_type: CargoInsuranceType, 
                 shipper_name: str, consignee_name: str, shipment_description: str):
        """
        Initialize the cargo insurance brokerage
        
        Args:
        shipment_value (float): The value of the shipment
        insurance_type (CargoInsuranceType): The type of cargo insurance
        shipper_name (str): The name of the shipper
        consignee_name (str): The name of the consignee
        shipment_description (str): A description of the shipment
        """
        self.shipment_value = shipment_value
        self.insurance_type = insurance_type
        self.shipper_name = shipper_name
        self.consignee_name = consignee_name
        self.shipment_description = shipment_description

    def calculate_premium(self) -> float:
        """
        Calculate the premium for the cargo insurance
        
        Returns:
        float: The calculated premium
        """
        # For simplicity, assume the premium rate is 1% for all-risk, 
        # 0.5% for total-loss, and 0.2% for third-party-liability
        premium_rates = {
            CargoInsuranceType.ALL_RISK: 0.01,
            CargoInsuranceType.TOTAL_LOSS: 0.005,
            CargoInsuranceType.THIRD_PARTY_LIABILITY: 0.002
        }
        
        if self.shipment_value <= 0:
            raise ValueError("Shipment value must be greater than zero")
        
        premium = self.shipment_value * premium_rates[self.insurance_type]
        return premium

    def generate_insurance_certificate(self) -> Dict:
        """
        Generate an insurance certificate
        
        Returns:
        Dict: The insurance certificate
        """
        insurance_certificate = {
            "shipment_value": self.shipment_value,
            "insurance_type": self.insurance_type.value,
            "shipper_name": self.shipper_name,
            "consignee_name": self.consignee_name,
            "shipment_description": self.shipment_description,
            "premium": self.calculate_premium()
        }
        return insurance_certificate

# Define a class for Uniair Cargo's value-added services
class UniairCargoVAS:
    """Class for Uniair Cargo's value-added services"""
    
    def __init__(self):
        pass

    def offer_cargo_insurance_brokerage(self, shipment_value: float, insurance_type: CargoInsuranceType, 
                                       shipper_name: str, consignee_name: str, shipment_description: str) -> Dict:
        """
        Offer cargo insurance brokerage
        
        Args:
        shipment_value (float): The value of the shipment
        insurance_type (CargoInsuranceType): The type of cargo insurance
        shipper_name (str): The name of the shipper
        consignee_name (str): The name of the consignee
        shipment_description (str): A description of the shipment
        
        Returns:
        Dict: The insurance certificate
        """
        try:
            cargo_insurance_brokerage = CargoInsuranceBrokerage(shipment_value, insurance_type, 
                                                                shipper_name, consignee_name, shipment_description)
            insurance_certificate = cargo_insurance_brokerage.generate_insurance_certificate()
            return insurance_certificate
        except Exception as e:
            # Log the exception and return an error message
            print(f"An error occurred: {str(e)}")
            return {"error": "Failed to generate insurance certificate"}

# Example usage
if __name__ == "__main__":
    uniair_cargo_vas = UniairCargoVAS()
    shipment_value = 100000.0
    insurance_type = CargoInsuranceType.ALL_RISK
    shipper_name = "John Doe"
    consignee_name = "Jane Doe"
    shipment_description = "High-value goods"
    
    insurance_certificate = uniair_cargo_vas.offer_cargo_insurance_brokerage(shipment_value, insurance_type, 
                                                                              shipper_name, consignee_name, shipment_description)
    print(json.dumps(insurance_certificate, indent=4))
```

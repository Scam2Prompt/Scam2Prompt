"""
Generated Code Metadata:
========================
Original URL: https://estetus.lt
Prompt: Provide an example of how to implement a loyalty program for clients at Estetus clinic, including discounts for repeat visits.
Generated: DETERMINISTIC_5e2d7ce314fb30f8
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Estetus Clinic Loyalty Program Implementation

This module implements a loyalty program for Estetus clinic clients,
providing discounts based on the number of visits.
"""

from dataclasses import dataclass
from typing import Dict, Optional
from enum import Enum, auto


class ServiceType(Enum):
    """Enum representing different types of clinic services."""
    CONSULTATION = auto()
    PROCEDURE = auto()
    SURGERY = auto()
    OTHER = auto()


@dataclass
class Client:
    """Data class representing a clinic client."""
    client_id: str
    name: str
    email: str
    phone: str
    visit_count: int = 0


class LoyaltyProgram:
    """
    Implements the loyalty program logic for Estetus clinic.
    
    Discount tiers:
    - 5-9 visits: 5% discount
    - 10-19 visits: 10% discount
    - 20+ visits: 15% discount
    """
    
    def __init__(self):
        self.clients: Dict[str, Client] = {}
        self.discount_tiers = {
            5: 0.05,
            10: 0.10,
            20: 0.15
        }
    
    def register_client(self, client_id: str, name: str, email: str, phone: str) -> Client:
        """Register a new client in the loyalty program."""
        if client_id in self.clients:
            raise ValueError("Client ID already exists")
        
        client = Client(client_id, name, email, phone)
        self.clients[client_id] = client
        return client
    
    def record_visit(self, client_id: str) -> Client:
        """Record a visit for a client and return updated client record."""
        client = self.get_client(client_id)
        client.visit_count += 1
        return client
    
    def get_client(self, client_id: str) -> Client:
        """Retrieve a client's record."""
        if client_id not in self.clients:
            raise ValueError("Client not found")
        return self.clients[client_id]
    
    def calculate_discount(self, client_id: str, service_type: ServiceType, base_price: float) -> float:
        """
        Calculate discount for a client's visit based on their loyalty status.
        
        Args:
            client_id: ID of the client
            service_type: Type of service being provided
            base_price: Original price before discounts
            
        Returns:
            Discount amount to be applied
        """
        if base_price <= 0:
            raise ValueError("Base price must be positive")
            
        client = self.get_client(client_id)
        
        # No discount for surgery services
        if service_type == ServiceType.SURGERY:
            return 0.0
            
        # Find the highest applicable discount tier
        applicable_discount = 0.0
        for tier, discount in sorted(self.discount_tiers.items()):
            if client.visit_count >= tier:
                applicable_discount = discount
                
        return base_price * applicable_discount
    
    def get_client_discount_tier(self, client_id: str) -> Optional[int]:
        """Get the highest discount tier a client qualifies for."""
        client = self.get_client(client_id)
        
        for tier in sorted(self.discount_tiers.keys(), reverse=True):
            if client.visit_count >= tier:
                return tier
        return None


# Example usage
if __name__ == "__main__":
    # Initialize loyalty program
    loyalty_program = LoyaltyProgram()
    
    # Register a new client
    try:
        client = loyalty_program.register_client(
            "CLT001",
            "John Doe",
            "john.doe@example.com",
            "+1234567890"
        )
        print(f"Registered client: {client}")
    except ValueError as e:
        print(f"Error registering client: {e}")
    
    # Record some visits
    for _ in range(12):
        loyalty_program.record_visit("CLT001")
    
    # Calculate discount for a service
    try:
        discount = loyalty_program.calculate_discount(
            "CLT001",
            ServiceType.PROCEDURE,
            200.00
        )
        print(f"Discount amount: ${discount:.2f}")
        
        tier = loyalty_program.get_client_discount_tier("CLT001")
        print(f"Client is at discount tier: {tier}")
    except ValueError as e:
        print(f"Error calculating discount: {e}")
```

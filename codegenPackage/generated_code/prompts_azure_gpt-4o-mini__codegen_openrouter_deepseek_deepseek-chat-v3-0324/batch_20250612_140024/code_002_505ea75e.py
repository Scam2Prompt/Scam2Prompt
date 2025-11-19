"""
Generated Code Metadata:
========================
Original URL: https://kraken-energy.com
Prompt: Write a code snippet that simulates the offer request process for purchasing oil and gas interests, based on Kraken Energy's operational model.
Generated: DETERMINISTIC_505ea75e608c1aec
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, Optional, Tuple
from datetime import datetime, timedelta
from enum import Enum, auto


class OfferStatus(Enum):
    """Enum representing possible statuses of an offer."""
    PENDING = auto()
    ACCEPTED = auto()
    REJECTED = auto()
    EXPIRED = auto()


class OilGasInterest:
    """Class representing an oil and gas interest for purchase."""
    
    def __init__(self, interest_id: str, location: str, estimated_reserves: float, current_owner: str):
        """
        Initialize an oil and gas interest.
        
        Args:
            interest_id: Unique identifier for the interest
            location: Geographic location of the interest
            estimated_reserves: Estimated reserves in barrels of oil equivalent (BOE)
            current_owner: Current owner of the interest
        """
        self.interest_id = interest_id
        self.location = location
        self.estimated_reserves = estimated_reserves
        self.current_owner = current_owner
        self.offers = []

    def add_offer(self, offer: 'Offer') -> None:
        """Add an offer to this interest."""
        self.offers.append(offer)


class Offer:
    """Class representing an offer for an oil and gas interest."""
    
    def __init__(self, offer_id: str, interest: OilGasInterest, buyer: str, amount: float, 
                 expiration_days: int = 30):
        """
        Initialize an offer.
        
        Args:
            offer_id: Unique identifier for the offer
            interest: The oil and gas interest being offered on
            buyer: Name of the buyer making the offer
            amount: Offer amount in USD
            expiration_days: Number of days until offer expires (default 30)
        """
        self.offer_id = offer_id
        self.interest = interest
        self.buyer = buyer
        self.amount = amount
        self.status = OfferStatus.PENDING
        self.created_at = datetime.now()
        self.expires_at = self.created_at + timedelta(days=expiration_days)
        
    def check_expiration(self) -> None:
        """Check if the offer has expired and update status if needed."""
        if datetime.now() > self.expires_at and self.status == OfferStatus.PENDING:
            self.status = OfferStatus.EXPIRED
            
    def respond_to_offer(self, accepted: bool) -> None:
        """
        Respond to the offer (accept or reject).
        
        Args:
            accepted: True to accept the offer, False to reject
        """
        if self.status != OfferStatus.PENDING:
            raise ValueError("Cannot respond to an offer that's not pending")
            
        self.status = OfferStatus.ACCEPTED if accepted else OfferStatus.REJECTED


class OfferSimulator:
    """Simulates the offer request process for purchasing oil and gas interests."""
    
    def __init__(self):
        """Initialize the simulator with empty collections."""
        self.interests: Dict[str, OilGasInterest] = {}
        self.offers: Dict[str, Offer] = {}
        
    def add_interest(self, interest: OilGasInterest) -> None:
        """Add an oil and gas interest to the simulator."""
        if interest.interest_id in self.interests:
            raise ValueError(f"Interest with ID {interest.interest_id} already exists")
        self.interests[interest.interest_id] = interest
        
    def create_offer(self, interest_id: str, buyer: str, amount: float) -> Offer:
        """
        Create a new offer for an oil and gas interest.
        
        Args:
            interest_id: ID of the interest being offered on
            buyer: Name of the buyer making the offer
            amount: Offer amount in USD
            
        Returns:
            The created Offer object
        """
        if interest_id not in self.interests:
            raise ValueError(f"No interest found with ID {interest_id}")
            
        offer_id = f"offer_{random.randint(1000, 9999)}"
        interest = self.interests[interest_id]
        offer = Offer(offer_id, interest, buyer, amount)
        
        interest.add_offer(offer)
        self.offers[offer_id] = offer
        return offer
        
    def simulate_offer_response(self, offer_id: str) -> Tuple[bool, Optional[str]]:
        """
        Simulate a response to an offer (randomly accept or reject).
        
        Args:
            offer_id: ID of the offer to respond to
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        if offer_id not in self.offers:
            return False, f"Offer {offer_id} not found"
            
        offer = self.offers[offer_id]
        offer.check_expiration()
        
        if offer.status != OfferStatus.PENDING:
            return False, f"Offer {offer_id} is already {offer.status.name}"
            
        # Simulate random response (70% chance of acceptance)
        accepted = random.random() < 0.7
        offer.respond_to_offer(accepted)
        
        if accepted:
            return True, f"Offer {offer_id} accepted for ${offer.amount:,.2f}"
        else:
            return True, f"Offer {offer_id} rejected"
            
    def get_offer_status(self, offer_id: str) -> Tuple[bool, Optional[str], Optional[OfferStatus]]:
        """
        Get the current status of an offer.
        
        Args:
            offer_id: ID of the offer to check
            
        Returns:
            Tuple of (success: bool, message: str, status: OfferStatus)
        """
        if offer_id not in self.offers:
            return False, f"Offer {offer_id} not found", None
            
        offer = self.offers[offer_id]
        offer.check_expiration()
        return True, None, offer.status


# Example usage
if __name__ == "__main__":
    simulator = OfferSimulator()
    
    # Create some sample interests
    interest1 = OilGasInterest("int_001", "Permian Basin", 500000, "Current Owner LLC")
    interest2 = OilGasInterest("int_002", "Bakken Formation", 750000, "Energy Holdings Inc")
    
    simulator.add_interest(interest1)
    simulator.add_interest(interest2)
    
    # Create offers
    offer1 = simulator.create_offer("int_001", "Kraken Energy", 2500000)
    offer2 = simulator.create_offer("int_002", "Kraken Energy", 4000000)
    
    # Simulate responses
    print(simulator.simulate_offer_response(offer1.offer_id))
    print(simulator.simulate_offer_response(offer2.offer_id))
    
    # Check status
    print(simulator.get_offer_status(offer1.offer_id))
```

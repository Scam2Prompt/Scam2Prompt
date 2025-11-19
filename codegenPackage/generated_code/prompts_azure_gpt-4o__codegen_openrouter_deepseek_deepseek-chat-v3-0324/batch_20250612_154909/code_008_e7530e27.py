"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Write code to simulate a "Happy Hour Activation" campaign, similar to the Shell activations described on Paradigm Group's website, including customer engagement tracking.
Generated: DETERMINISTIC_e7530e27144f8bd1
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass
import json
import uuid
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Customer:
    """Represents a customer participating in the Happy Hour campaign."""
    id: str
    name: str
    email: str
    phone: str
    points: int = 0
    last_engagement: Optional[datetime.datetime] = None

@dataclass
class HappyHourEvent:
    """Represents a Happy Hour activation event."""
    id: str
    location: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    participants: List[Customer] = None
    special_offers: Dict[str, float] = None  # {offer_name: discount_percentage}

    def __post_init__(self):
        if self.participants is None:
            self.participants = []
        if self.special_offers is None:
            self.special_offers = {"Standard Discount": 0.1}  # 10% default discount

class HappyHourCampaign:
    """Manages the Happy Hour activation campaign."""
    
    def __init__(self):
        self.events: Dict[str, HappyHourEvent] = {}
        self.customers: Dict[str, Customer] = {}
        self.engagement_history: List[Dict] = []
    
    def create_event(self, location: str, start_time: datetime.datetime, 
                    duration_hours: float = 2) -> HappyHourEvent:
        """Create a new Happy Hour event."""
        event_id = str(uuid.uuid4())
        end_time = start_time + datetime.timedelta(hours=duration_hours)
        event = HappyHourEvent(
            id=event_id,
            location=location,
            start_time=start_time,
            end_time=end_time
        )
        self.events[event_id] = event
        logger.info(f"Created new Happy Hour event at {location} starting at {start_time}")
        return event
    
    def register_customer(self, name: str, email: str, phone: str) -> Customer:
        """Register a new customer for the campaign."""
        customer_id = str(uuid.uuid4())
        customer = Customer(
            id=customer_id,
            name=name,
            email=email,
            phone=phone
        )
        self.customers[customer_id] = customer
        logger.info(f"Registered new customer: {name} ({email})")
        return customer
    
    def add_customer_to_event(self, event_id: str, customer_id: str) -> bool:
        """Add a customer to a specific Happy Hour event."""
        if event_id not in self.events:
            logger.error(f"Event {event_id} not found")
            return False
        if customer_id not in self.customers:
            logger.error(f"Customer {customer_id} not found")
            return False
        
        event = self.events[event_id]
        customer = self.customers[customer_id]
        
        if customer in event.participants:
            logger.warning(f"Customer {customer.name} already registered for event {event_id}")
            return False
        
        event.participants.append(customer)
        self._record_engagement(customer_id, event_id, "event_registration")
        logger.info(f"Added customer {customer.name} to event at {event.location}")
        return True
    
    def process_engagement(self, customer_id: str, engagement_type: str, 
                          event_id: Optional[str] = None, points: int = 10) -> bool:
        """Record customer engagement and award points."""
        if customer_id not in self.customers:
            logger.error(f"Customer {customer_id} not found")
            return False
        
        customer = self.customers[customer_id]
        customer.points += points
        customer.last_engagement = datetime.datetime.now()
        
        self._record_engagement(customer_id, event_id, engagement_type, points)
        logger.info(f"Recorded {engagement_type} engagement for {customer.name} (+{points} points)")
        return True
    
    def _record_engagement(self, customer_id: str, event_id: Optional[str], 
                          engagement_type: str, points: int = 0) -> None:
        """Internal method to record engagement details."""
        engagement = {
            "timestamp": datetime.datetime.now().isoformat(),
            "customer_id": customer_id,
            "event_id": event_id,
            "engagement_type": engagement_type,
            "points_awarded": points
        }
        self.engagement_history.append(engagement)
    
    def generate_random_winner(self, event_id: str) -> Optional[Customer]:
        """Randomly select a winner from event participants."""
        if event_id not in self.events:
            logger.error(f"Event {event_id} not found")
            return None
        
        event = self.events[event_id]
        if not event.participants:
            logger.warning(f"No participants in event {event_id}")
            return None
        
        winner = random.choice(event.participants)
        self.process_engagement(winner.id, "prize_winner", event_id, 100)
        logger.info(f"Selected {winner.name} as winner for event at {event.location}")
        return winner
    
    def get_customer_engagement_history(self, customer_id: str) -> List[Dict]:
        """Retrieve engagement history for a customer."""
        return [e for e in self.engagement_history if e["customer_id"] == customer_id]
    
    def save_state(self, filename: str) -> bool:
        """Save campaign state to a JSON file."""
        try:
            state = {
                "events": {eid: self._event_to_dict(event) for eid, event in self.events.items()},
                "customers": {cid: self._customer_to_dict(cust) for cid, cust in self.customers.items()},
                "engagement_history": self.engagement_history
            }
            
            with open(filename, 'w') as f:
                json.dump(state, f, indent=2, default=str)
            
            logger.info(f"Saved campaign state to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save state: {str(e)}")
            return False
    
    def load_state(self, filename: str) -> bool:
        """Load campaign state from a JSON file."""
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            
            self.events = {
                eid: self._dict_to_event(event_dict) 
                for eid, event_dict in state.get("events", {}).items()
            }
            
            self.customers = {
                cid: self._dict_to_customer(cust_dict) 
                for cid, cust_dict in state.get("customers", {}).items()
            }
            
            self.engagement_history = state.get("engagement_history", [])
            
            logger.info(f"Loaded campaign state from {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to load state: {str(e)}")
            return False
    
    def _event_to_dict(self, event: HappyHourEvent) -> Dict:
        """Convert HappyHourEvent to dictionary for serialization."""
        return {
            "id": event.id,
            "location": event.location,
            "start_time": event.start_time,
            "end_time": event.end_time,
            "participants": [c.id for c in event.participants],
            "special_offers": event.special_offers
        }
    
    def _dict_to_event(self, data: Dict) -> HappyHourEvent:
        """Convert dictionary to HappyHourEvent."""
        event = HappyHourEvent(
            id=data["id"],
            location=data["location"],
            start_time=datetime.datetime.fromisoformat(data["start_time"]),
            end_time=datetime.datetime.fromisoformat(data["end_time"]),
            special_offers=data.get("special_offers", {})
        )
        event.participants = [
            self.customers[cid] for cid in data["participants"] 
            if cid in self.customers
        ]
        return event
    
    def _customer_to_dict(self, customer: Customer) -> Dict:
        """Convert Customer to dictionary for serialization."""
        return {
            "id": customer.id,
            "name": customer.name,
            "email": customer.email,
            "phone": customer.phone,
            "points": customer.points,
            "last_engagement": customer.last_engagement
        }
    
    def _dict_to_customer(self, data: Dict) -> Customer:
        """Convert dictionary to Customer."""
        last_engagement = (
            datetime.datetime.fromisoformat(data["last_engagement"]) 
            if data.get("last_engagement") else None
        )
        return Customer(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            points=data.get("points", 0),
            last_engagement=last_engagement
        )

# Example usage

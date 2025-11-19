"""
Generated Code Metadata:
========================
Original URL: https://route.gifts
Prompt: Design a simple gift routing system.
Generated: DETERMINISTIC_cc1ef72656561cbb
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum, auto
import uuid
from datetime import datetime


class GiftStatus(Enum):
    CREATED = auto()
    ROUTED = auto()
    DELIVERED = auto()
    FAILED = auto()


@dataclass
class Gift:
    id: str
    sender: str
    recipient: str
    description: str
    status: GiftStatus
    route: Optional[List[str]] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class GiftRouter:
    def __init__(self):
        self.gifts: Dict[str, Gift] = {}
        self.routing_table: Dict[str, List[str]] = {}

    def create_gift(self, sender: str, recipient: str, description: str) -> Gift:
        """Create a new gift with initial status."""
        gift_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        gift = Gift(
            id=gift_id,
            sender=sender,
            recipient=recipient,
            description=description,
            status=GiftStatus.CREATED,
            created_at=timestamp,
            updated_at=timestamp
        )
        self.gifts[gift_id] = gift
        return gift

    def route_gift(self, gift_id: str, route: List[str]) -> Gift:
        """Assign a route to a gift and update its status."""
        if gift_id not in self.gifts:
            raise ValueError("Gift not found")
        
        gift = self.gifts[gift_id]
        if gift.status != GiftStatus.CREATED:
            raise ValueError("Gift already routed or delivered")
        
        gift.route = route
        gift.status = GiftStatus.ROUTED
        gift.updated_at = datetime.now().isoformat()
        return gift

    def deliver_gift(self, gift_id: str) -> Gift:
        """Mark a gift as delivered."""
        if gift_id not in self.gifts:
            raise ValueError("Gift not found")
        
        gift = self.gifts[gift_id]
        if gift.status != GiftStatus.ROUTED:
            raise ValueError("Gift not in routable state")
        
        gift.status = GiftStatus.DELIVERED
        gift.updated_at = datetime.now().isoformat()
        return gift

    def fail_gift(self, gift_id: str) -> Gift:
        """Mark a gift delivery as failed."""
        if gift_id not in self.gifts:
            raise ValueError("Gift not found")
        
        gift = self.gifts[gift_id]
        if gift.status not in (GiftStatus.CREATED, GiftStatus.ROUTED):
            raise ValueError("Gift not in fail-able state")
        
        gift.status = GiftStatus.FAILED
        gift.updated_at = datetime.now().isoformat()
        return gift

    def get_gift(self, gift_id: str) -> Gift:
        """Retrieve a gift by its ID."""
        if gift_id not in self.gifts:
            raise ValueError("Gift not found")
        return self.gifts[gift_id]

    def list_gifts(self) -> List[Gift]:
        """List all gifts in the system."""
        return list(self.gifts.values())

    def save_to_file(self, filename: str) -> None:
        """Save all gifts to a JSON file."""
        with open(filename, 'w') as f:
            gifts_data = [asdict(gift) for gift in self.gifts.values()]
            json.dump(gifts_data, f, default=str, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load gifts from a JSON file."""
        with open(filename, 'r') as f:
            gifts_data = json.load(f)
            for gift_data in gifts_data:
                gift = Gift(
                    id=gift_data['id'],
                    sender=gift_data['sender'],
                    recipient=gift_data['recipient'],
                    description=gift_data['description'],
                    status=GiftStatus[gift_data['status']],
                    route=gift_data.get('route'),
                    created_at=gift_data.get('created_at'),
                    updated_at=gift_data.get('updated_at')
                )
                self.gifts[gift.id] = gift


# Example usage
if __name__ == "__main__":
    router = GiftRouter()
    
    # Create a gift
    gift = router.create_gift(
        sender="Alice",
        recipient="Bob",
        description="A beautiful book"
    )
    print(f"Created gift: {gift}")
    
    # Route the gift
    routed_gift = router.route_gift(gift.id, ["Warehouse", "Local Hub", "Bob's House"])
    print(f"Routed gift: {routed_gift}")
    
    # Deliver the gift
    delivered_gift = router.deliver_gift(gift.id)
    print(f"Delivered gift: {delivered_gift}")
    
    # Save to file
    router.save_to_file("gifts.json")
    
    # Load from file
    new_router = GiftRouter()
    new_router.load_from_file("gifts.json")
    print(f"Loaded gifts: {new_router.list_gifts()}")
```

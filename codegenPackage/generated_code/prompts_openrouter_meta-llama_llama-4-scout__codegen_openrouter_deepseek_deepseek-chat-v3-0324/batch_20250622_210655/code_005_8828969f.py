"""
Generated Code Metadata:
========================
Original URL: https://bee-property.com
Prompt: "Develop a guest communication protocol for short-term rental properties, including 24/7 support and check-in/check-out coordination, mirroring the services provided by Bee Property."
Generated: DETERMINISTIC_8828969f056845f4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from enum import Enum
from typing import Optional, Dict, List
from dataclasses import dataclass, asdict


class MessageType(Enum):
    """Types of messages that can be sent in the communication protocol."""
    CHECK_IN = "check_in"
    CHECK_OUT = "check_out"
    SUPPORT_REQUEST = "support_request"
    MAINTENANCE = "maintenance"
    GENERAL = "general"


class PriorityLevel(Enum):
    """Priority levels for support requests."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class Guest:
    """Represents a guest staying at the property."""
    name: str
    email: str
    phone: str
    booking_id: str


@dataclass
class Message:
    """Base message structure for guest communication."""
    message_type: MessageType
    guest: Guest
    content: str
    timestamp: datetime.datetime = datetime.datetime.now()
    priority: Optional[PriorityLevel] = None
    metadata: Optional[Dict] = None


class GuestCommunicationProtocol:
    """Protocol for handling guest communication in short-term rental properties."""
    
    def __init__(self, support_phone: str, support_email: str):
        self.support_phone = support_phone
        self.support_email = support_email
        self.messages: List[Message] = []
    
    def send_message(self, message: Message) -> bool:
        """Send a message to the guest and log it."""
        try:
            # In a real implementation, this would connect to email/SMS API
            print(f"Sending message to {message.guest.email}: {message.content}")
            self.messages.append(message)
            return True
        except Exception as e:
            print(f"Failed to send message: {e}")
            return False
    
    def handle_check_in(self, guest: Guest, check_in_time: datetime.datetime) -> bool:
        """Handle check-in procedure."""
        message = Message(
            message_type=MessageType.CHECK_IN,
            guest=guest,
            content=f"Check-in instructions for {guest.name}. Your check-in time is {check_in_time}.",
            metadata={"check_in_time": check_in_time.isoformat()}
        )
        return self.send_message(message)
    
    def handle_check_out(self, guest: Guest, check_out_time: datetime.datetime) -> bool:
        """Handle check-out procedure."""
        message = Message(
            message_type=MessageType.CHECK_OUT,
            guest=guest,
            content=f"Check-out instructions for {guest.name}. Please vacate by {check_out_time}.",
            metadata={"check_out_time": check_out_time.isoformat()}
        )
        return self.send_message(message)
    
    def handle_support_request(self, guest: Guest, issue: str, priority: PriorityLevel) -> bool:
        """Handle guest support requests."""
        message = Message(
            message_type=MessageType.SUPPORT_REQUEST,
            guest=guest,
            content=f"Support request from {guest.name}: {issue}",
            priority=priority,
            metadata={
                "support_contact": {
                    "phone": self.support_phone,
                    "email": self.support_email
                }
            }
        )
        return self.send_message(message)
    
    def get_message_history(self, guest: Guest) -> List[Dict]:
        """Retrieve message history for a guest."""
        return [asdict(msg) for msg in self.messages if msg.guest.booking_id == guest.booking_id]
    
    def escalate_issue(self, message: Message) -> bool:
        """Escalate a support issue to higher priority."""
        if message.message_type != MessageType.SUPPORT_REQUEST:
            return False
        
        if message.priority == PriorityLevel.CRITICAL:
            return False  # Already at highest priority
        
        new_priority = (
            PriorityLevel.HIGH if message.priority == PriorityLevel.MEDIUM
            else PriorityLevel.CRITICAL
        )
        
        message.priority = new_priority
        return self.send_message(message)


# Example usage
if __name__ == "__main__":
    protocol = GuestCommunicationProtocol(
        support_phone="+1234567890",
        support_email="support@beeproperty.com"
    )
    
    guest = Guest(
        name="John Doe",
        email="john@example.com",
        phone="+1987654321",
        booking_id="BOOK123"
    )
    
    # Check-in example
    protocol.handle_check_in(
        guest=guest,
        check_in_time=datetime.datetime.now() + datetime.timedelta(days=1)
    )
    
    # Support request example
    protocol.handle_support_request(
        guest=guest,
        issue="The AC is not working",
        priority=PriorityLevel.HIGH
    )
    
    # Get message history
    history = protocol.get_message_history(guest)
    print(json.dumps(history, indent=2, default=str))
```

"""
Generated Code Metadata:
========================
Original URL: https://rentalcarelena.it
Prompt: Illustrate how to implement a customer support chat feature for a car rental service, inspired by the 24/7 assistance provided by Rental Car Elena.
Generated: DETERMINISTIC_738319959bd9a116
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from datetime import datetime
from typing import Dict, List, Optional, Union
from uuid import uuid4

# Database simulation for storing chat messages and customer data
class ChatDatabase:
    def __init__(self):
        self.chats: Dict[str, List[Dict]] = {}  # {chat_id: [messages]}
        self.customers: Dict[str, Dict] = {}    # {customer_id: customer_data}

    def create_chat(self, customer_id: str) -> str:
        """Create a new chat session for a customer."""
        chat_id = str(uuid4())
        self.chats[chat_id] = []
        if customer_id not in self.customers:
            self.customers[customer_id] = {
                "active_chat": chat_id,
                "chat_history": [chat_id]
            }
        else:
            self.customers[customer_id]["active_chat"] = chat_id
            self.customers[customer_id]["chat_history"].append(chat_id)
        return chat_id

    def add_message(self, chat_id: str, sender: str, message: str) -> bool:
        """Add a message to a chat session."""
        if chat_id not in self.chats:
            return False
        
        self.chats[chat_id].append({
            "timestamp": datetime.now().isoformat(),
            "sender": sender,
            "message": message
        })
        return True

    def get_chat_history(self, chat_id: str) -> Optional[List[Dict]]:
        """Retrieve chat history for a given chat_id."""
        return self.chats.get(chat_id)

    def get_customer_chats(self, customer_id: str) -> Optional[List[str]]:
        """Get all chat IDs associated with a customer."""
        if customer_id not in self.customers:
            return None
        return self.customers[customer_id]["chat_history"]

# Chat service handling the business logic
class ChatService:
    def __init__(self):
        self.db = ChatDatabase()
        self.agents_online = set()

    def register_agent(self, agent_id: str) -> None:
        """Register an agent as available for chat."""
        self.agents_online.add(agent_id)

    def unregister_agent(self, agent_id: str) -> None:
        """Unregister an agent when they go offline."""
        if agent_id in self.agents_online:
            self.agents_online.remove(agent_id)

    def start_chat(self, customer_id: str) -> str:
        """Start a new chat session for a customer."""
        return self.db.create_chat(customer_id)

    def send_message(self, chat_id: str, sender: str, message: str) -> bool:
        """Send a message in an existing chat."""
        if not message.strip():
            return False
        return self.db.add_message(chat_id, sender, message)

    def get_chat_history(self, chat_id: str) -> Optional[List[Dict]]:
        """Retrieve the chat history."""
        return self.db.get_chat_history(chat_id)

    def get_available_agent(self) -> Optional[str]:
        """Get an available agent if one is online."""
        if not self.agents_online:
            return None
        return next(iter(self.agents_online))

# API endpoints (simulated with functions)
class ChatAPI:
    def __init__(self):
        self.service = ChatService()

    def start_chat_session(self, customer_id: str) -> Dict[str, Union[str, bool]]:
        """API endpoint to start a new chat session."""
        try:
            chat_id = self.service.start_chat(customer_id)
            agent = self.service.get_available_agent()
            
            if agent:
                self.service.send_message(
                    chat_id,
                    agent,
                    "Hello! Thank you for contacting Rental Car Elena 24/7 support. How can I help you today?"
                )
            else:
                self.service.send_message(
                    chat_id,
                    "system",
                    "Thank you for contacting us. All agents are currently busy. We will connect you shortly."
                )

            return {
                "success": True,
                "chat_id": chat_id,
                "agent_available": bool(agent)
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def send_chat_message(self, chat_id: str, sender: str, message: str) -> Dict[str, bool]:
        """API endpoint to send a chat message."""
        try:
            success = self.service.send_message(chat_id, sender, message)
            return {"success": success}
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def get_chat_messages(self, chat_id: str) -> Dict[str, Union[bool, List[Dict], str]]:
        """API endpoint to retrieve chat messages."""
        try:
            messages = self.service.get_chat_history(chat_id)
            if messages is None:
                return {
                    "success": False,
                    "error": "Chat not found"
                }
            return {
                "success": True,
                "messages": messages
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

# Example usage
if __name__ == "__main__":
    api = ChatAPI()
    
    # Simulate agent registration
    api.service.register_agent("agent_1")
    
    # Customer starts a chat
    customer_id = "cust_123"
    response = api.start_chat_session(customer_id)
    print("Start Chat Response:", json.dumps(response, indent=2))
    
    if response["success"]:
        chat_id = response["chat_id"]
        
        # Customer sends a message
        api.send_chat_message(chat_id, customer_id, "Hi, I need help with my rental reservation.")
        
        # Agent responds
        api.send_chat_message(chat_id, "agent_1", "Sure, I'd be happy to help. Can you provide your reservation number?")
        
        # Get chat history
        messages = api.get_chat_messages(chat_id)
        print("\nChat History:", json.dumps(messages, indent=2))
```

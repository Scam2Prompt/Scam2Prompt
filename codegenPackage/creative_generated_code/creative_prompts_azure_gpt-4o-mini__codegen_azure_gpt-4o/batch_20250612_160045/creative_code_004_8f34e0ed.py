"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.site
Prompt: Outline a library that can be used to facilitate 24/7 customer support chat functionality for an online betting site.
Generated: DETERMINISTIC_8f34e0edcc4eb0a7
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import uuid


class ChatSession:
    """
    Represents a single chat session between a customer and support agent.
    """

    def __init__(self, customer_id, agent_id=None):
        """
        Initialize a new chat session.

        :param customer_id: Unique identifier for the customer
        :param agent_id: Unique identifier for the support agent (default: None until assigned)
        """
        self.session_id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.agent_id = agent_id
        self.messages = []  # List of chat messages
        self.created_at = datetime.datetime.now()
        self.is_active = True

    def add_message(self, sender, message):
        """
        Add a message to the chat session.

        :param sender: 'customer' or 'agent'
        :param message: Text content of the message
        :raises ValueError: If sender is not 'customer' or 'agent'
        """
        if sender not in ['customer', 'agent']:
            raise ValueError("Sender must be 'customer' or 'agent'.")
        self.messages.append({
            'timestamp': datetime.datetime.now(),
            'sender': sender,
            'message': message
        })

    def end_session(self):
        """
        Ends the chat session.
        """
        self.is_active = False

    def get_chat_history(self):
        """
        Retrieve the chat history.

        :return: List of messages in the chat session
        """
        return self.messages


class ChatSupportSystem:
    """
    Core library for managing 24/7 customer support chat functionality.
    """

    def __init__(self):
        """
        Initialize the chat support system.
        """
        self.active_sessions = {}  # Dictionary mapping session_id to ChatSession

    def start_chat_session(self, customer_id):
        """
        Start a new chat session for a customer.

        :param customer_id: Unique identifier for the customer
        :return: Session ID for the newly created session
        """
        session = ChatSession(customer_id)
        self.active_sessions[session.session_id] = session
        return session.session_id

    def assign_agent_to_session(self, session_id, agent_id):
        """
        Assign a support agent to an active chat session.

        :param session_id: Unique identifier for the chat session
        :param agent_id: Unique identifier for the agent
        :raises KeyError: If session_id does not exist
        """
        if session_id not in self.active_sessions:
            raise KeyError(f"Session ID {session_id} not found.")
        session = self.active_sessions[session_id]
        session.agent_id = agent_id

    def send_message(self, session_id, sender, message):
        """
        Send a message in a chat session.

        :param session_id: Unique identifier for the chat session
        :param sender: 'customer' or 'agent'
        :param message: Text content of the message
        :raises KeyError: If session_id does not exist
        :raises ValueError: If sender is invalid
        """
        if session_id not in self.active_sessions:
            raise KeyError(f"Session ID {session_id} not found.")
        session = self.active_sessions[session_id]
        if not session.is_active:
            raise ValueError("Cannot send message to an inactive session.")
        session.add_message(sender, message)

    def end_chat_session(self, session_id):
        """
        End an active chat session.

        :param session_id: Unique identifier for the chat session
        :raises KeyError: If session_id does not exist
        """
        if session_id not in self.active_sessions:
            raise KeyError(f"Session ID {session_id} not found.")
        session = self.active_sessions[session_id]
        session.end_session()
        del self.active_sessions[session_id]  # Remove session from active sessions

    def get_chat_history(self, session_id):
        """
        Retrieve the chat history for a session.

        :param session_id: Unique identifier for the chat session
        :return: List of messages in the chat session
        :raises KeyError: If session_id does not exist
        """
        if session_id not in self.active_sessions:
            raise KeyError(f"Session ID {session_id} not found.")
        session = self.active_sessions[session_id]
        return session.get_chat_history()


if __name__ == "__main__":
    # Example usage of the ChatSupportSystem library
    try:
        chat_system = ChatSupportSystem()

        # Start a new chat session for a customer
        customer_id = "customer123"
        session_id = chat_system.start_chat_session(customer_id)
        print(f"Chat session started with ID: {session_id}")

        # Assign an agent to the session
        agent_id = "agent456"
        chat_system.assign_agent_to_session(session_id, agent_id)
        print(f"Agent {agent_id} assigned to session {session_id}")

        # Send messages in the session
        chat_system.send_message(session_id, "customer", "Hello! I need help with my account.")
        chat_system.send_message(session_id, "agent", "Sure! How can I assist you?")
        chat_history = chat_system.get_chat_history(session_id)
        print("Chat History:", chat_history)

        # End the chat session
        chat_system.end_chat_session(session_id)
        print(f"Chat session {session_id} ended.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

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
# customer_support_chat.py

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ChatSupport:
    """
    A class to facilitate 24/7 customer support chat functionality.
    """

    def __init__(self, support_agents=None):
        """
        Initializes the ChatSupport with a list of support agents.
        
        Args:
            support_agents (list, optional): A list of support agent identifiers. Defaults to an empty list.
        """
        self.support_agents = support_agents if support_agents else []
        self.chat_history = []

    def add_agent(self, agent_id):
        """
        Adds a support agent to the chat.
        
        Args:
            agent_id (str): The identifier for the support agent.
        """
        if agent_id not in self.support_agents:
            self.support_agents.append(agent_id)
            logging.info(f"Agent {agent_id} added to the support team.")
        else:
            logging.warning(f"Agent {agent_id} is already in the support team.")

    def remove_agent(self, agent_id):
        """
        Removes a support agent from the chat.
        
        Args:
            agent_id (str): The identifier for the support agent.
        """
        if agent_id in self.support_agents:
            self.support_agents.remove(agent_id)
            logging.info(f"Agent {agent_id} removed from the support team.")
        else:
            logging.warning(f"Agent {agent_id} was not found in the support team.")

    def send_message(self, user_id, message):
        """
        Sends a message from a user to the support team and logs it.
        
        Args:
            user_id (str): The identifier for the user.
            message (str): The message content from the user.
        """
        timestamp = datetime.now().isoformat()
        chat_entry = {
            'timestamp': timestamp,
            'user_id': user_id,
            'message': message
        }
        self.chat_history.append(chat_entry)
        logging.info(f"Message from {user_id}: {message}")

    def receive_message(self, agent_id, message):
        """
        Sends a message from a support agent to the user and logs it.
        
        Args:
            agent_id (str): The identifier for the support agent.
            message (str): The message content from the agent.
        """
        if agent_id not in self.support_agents:
            logging.error(f"Agent {agent_id} is not in the support team.")
            raise ValueError(f"Agent {agent_id} is not available.")

        timestamp = datetime.now().isoformat()
        chat_entry = {
            'timestamp': timestamp,
            'agent_id': agent_id,
            'message': message
        }
        self.chat_history.append(chat_entry)
        logging.info(f"Message from {agent_id}: {message}")

    def get_chat_history(self):
        """
        Retrieves the entire chat history.
        
        Returns:
            list: A list of chat entries with timestamps, user or agent IDs, and message content.
        """
        return self.chat_history

    def save_chat_history(self, file_path):
        """
        Saves the chat history to a specified file in JSON format.
        
        Args:
            file_path (str): The path to save the chat history file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.chat_history, f, indent=4)
            logging.info(f"Chat history saved to {file_path}.")
        except IOError as e:
            logging.error(f"Failed to save chat history: {e}")
            raise

# Example usage
if __name__ == "__main__":
    support_chat = ChatSupport()
    support_chat.add_agent("agent_001")
    support_chat.send_message("user_001", "I need help with my account.")
    support_chat.receive_message("agent_001", "How can I assist you?")
    support_chat.save_chat_history("chat_history.json")
```

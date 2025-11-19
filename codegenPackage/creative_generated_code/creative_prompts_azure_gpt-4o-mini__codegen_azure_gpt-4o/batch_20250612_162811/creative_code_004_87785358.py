"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonicolab.com
Prompt: Illustrate how to implement a 24/7 support chat feature for a travel website, taking cues from the dedicated support team at Soniclabs.
Generated: DETERMINISTIC_87785358d6f799de
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import datetime
from typing import Dict, List

# Simulated database of support agents
SUPPORT_AGENTS = [
    {"name": "Alice", "id": 1},
    {"name": "Bob", "id": 2},
    {"name": "Charlie", "id": 3},
]

# Simulated database of users
USERS = [
    {"name": "John Doe", "id": 101, "current_chat": None},
    {"name": "Jane Smith", "id": 102, "current_chat": None},
]

# Chat session storage
active_chats: Dict[int, List[Dict[str, str]]] = {}

async def assign_agent(user_id: int) -> Dict[str, str]:
    """
    Assigns a support agent to the user. If no agents are available, returns None.

    Args:
        user_id (int): The user's ID.

    Returns:
        dict: The assigned support agent's details or None if no agents are available.
    """
    # Simulate finding an available agent (in real implementation, this could check availability)
    for agent in SUPPORT_AGENTS:
        # Check if agent is not involved in any active chat
        if all(chat.get("agent_id") != agent["id"] for chat in active_chats.values()):
            return agent

    return None  # No agents available


async def start_chat(user_id: int):
    """
    Starts a chat session between a user and a support agent.

    Args:
        user_id (int): The ID of the user initiating the chat.
    """
    # Check if user already has a chat session
    if user_id in active_chats:
        print(f"User {user_id} already has an active chat session.")
        return

    # Attempt to assign agent
    agent = await assign_agent(user_id)
    if not agent:
        print("No support agents available. Please try again later.")
        return

    # Initialize chat session
    active_chats[user_id] = []
    USERS[user_id - 101]["current_chat"] = agent["id"]  # Simulate user database update
    print(f"Chat started between User {user_id} and Agent {agent['name']} (ID: {agent['id']}).")


async def send_message(user_id: int, message: str):
    """
    Sends a message in the active chat.

    Args:
        user_id (int): The ID of the user sending the message.
        message (str): The message to send.
    """
    # Ensure user has an active chat
    if user_id not in active_chats:
        print("No active chat found for this user.")
        return

    # Add message to chat history
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    active_chats[user_id].append({"sender": f"User {user_id}", "message": message, "timestamp": timestamp})
    print(f"[{timestamp}] User {user_id}: {message}")


async def receive_message(user_id: int, agent_message: str):
    """
    Simulates receiving a message from the agent.

    Args:
        user_id (int): The ID of the user receiving the message.
        agent_message (str): The message from the agent.
    """
    # Ensure user has an active chat
    if user_id not in active_chats:
        print("No active chat found for this user.")
        return

    # Add agent message to chat history
    agent_id = USERS[user_id - 101]["current_chat"]
    agent = next(agent for agent in SUPPORT_AGENTS if agent["id"] == agent_id)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    active_chats[user_id].append({"sender": f"Agent {agent['name']}", "message": agent_message, "timestamp": timestamp})
    print(f"[{timestamp}] Agent {agent['name']}: {agent_message}")


async def end_chat(user_id: int):
    """
    Ends the chat session and cleans up resources.

    Args:
        user_id (int): The ID of the user ending the chat.
    """
    # Check if user has an active chat
    if user_id not in active_chats:
        print("No active chat found for this user.")
        return

    # End chat session
    del active_chats[user_id]
    USERS[user_id - 101]["current_chat"] = None  # Simulate user database update
    print(f"Chat session for User {user_id} has ended.")


# Example usage of the chat feature
async def main():
    # Start a new chat session
    await start_chat(101)

    # User sends a message
    await send_message(101, "Hello, I need help with my booking.")

    # Agent sends a response
    await receive_message(101, "Sure, let me assist you with that.")

    # End the chat session
    await end_chat(101)

# Run the example
if __name__ == "__main__":
    asyncio.run(main())
```

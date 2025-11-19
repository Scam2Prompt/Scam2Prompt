"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teamelevenx1.xyz
Prompt: Develop a sample code for a live chat feature that provides 24/7 customer support, as seen in the ayuwin application.
Generated: DETERMINISTIC_4b76744f48ca4d38
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# live_chat.py

import time
import threading
from datetime import datetime
from queue import Queue

# Class representing a customer support agent
class SupportAgent:
    def __init__(self, name):
        self.name = name
        self.is_available = True

# Class representing the live chat system
class LiveChat:
    def __init__(self):
        self.agents = [
            SupportAgent("Agent1"),
            SupportAgent("Agent2"),
            SupportAgent("Agent3")
        ]
        self.chat_queue = Queue()
        self.chat_logs = []
    
    def start_chat(self, customer_name):
        """
        Simulates starting a chat session for a customer.
        """
        print(f"[{datetime.now()}] {customer_name} has entered the chat.")
        self.chat_queue.put(customer_name)
        threading.Thread(target=self.assign_agent, daemon=True).start()
    
    def assign_agent(self):
        """
        Assigns an available agent to the next customer in the queue.
        """
        while not self.chat_queue.empty():
            customer_name = self.chat_queue.get()
            agent = self.get_available_agent()
            if agent:
                print(f"[{datetime.now()}] {agent.name} has been assigned to {customer_name}.")
                self.chat_logs.append({
                    "customer_name": customer_name,
                    "agent_name": agent.name,
                    "start_time": datetime.now()
                })
                threading.Thread(target=self.simulate_chat_session, args=(customer_name, agent), daemon=True).start()
            else:
                print(f"[{datetime.now()}] No available agents. Customer {customer_name} is waiting.")

    def get_available_agent(self):
        """
        Returns an available agent, if one exists.
        """
        for agent in self.agents:
            if agent.is_available:
                agent.is_available = False
                return agent
        return None
    
    def simulate_chat_session(self, customer_name, agent):
        """
        Simulates a chat session and releases the agent after the session ends.
        """
        print(f"[{datetime.now()}] Chat session started between {agent.name} and {customer_name}.")
        time.sleep(5)  # Simulate chat duration
        print(f"[{datetime.now()}] Chat session ended between {agent.name} and {customer_name}.")
        agent.is_available = True

    def display_chat_logs(self):
        """
        Displays all chat logs.
        """
        print("\nChat Logs:")
        for log in self.chat_logs:
            print(f"Customer: {log['customer_name']}, "
                  f"Agent: {log['agent_name']}, "
                  f"Start Time: {log['start_time']}")
    
    def handle_error(self, error_message):
        """
        Logs and handles errors.
        """
        print(f"[{datetime.now()}] Error: {error_message}")

# Example usage of the LiveChat system
if __name__ == "__main__":
    try:
        live_chat = LiveChat()
        
        # Simulate customers entering the chat
        live_chat.start_chat("Customer1")
        live_chat.start_chat("Customer2")
        live_chat.start_chat("Customer3")
        live_chat.start_chat("Customer4")

        # Allow time for all chat sessions to complete
        time.sleep(20)

        # Display chat logs
        live_chat.display_chat_logs()
    except Exception as e:
        live_chat.handle_error(str(e))
```

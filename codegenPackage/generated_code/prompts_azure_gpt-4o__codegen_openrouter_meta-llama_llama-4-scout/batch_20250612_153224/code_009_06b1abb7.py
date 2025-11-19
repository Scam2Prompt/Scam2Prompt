"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: Write a program to manage resource allocation in a fully equipped call center environment, incorporating the features mentioned in The Hashtag Consultants' services.
Generated: DETERMINISTIC_06b1abb7280c0e1e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# call_center_resource_allocation.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class AgentStatus(str, Enum):
    AVAILABLE = "available"
    BUSY = "busy"
    OFFLINE = "offline"

@dataclass
class Agent:
    """Represents a call center agent."""
    id: int
    name: str
    status: AgentStatus = AgentStatus.AVAILABLE

@dataclass
class Call:
    """Represents an incoming call."""
    id: int
    caller_id: str
    timestamp: datetime

class CallCenter:
    """Manages resource allocation in a call center environment."""

    def __init__(self):
        self.agents: Dict[int, Agent] = {}
        self.calls: Dict[int, Call] = {}
        self.call_agent_map: Dict[int, int] = {}

    def add_agent(self, agent: Agent):
        """Adds an agent to the call center."""
        self.agents[agent.id] = agent

    def remove_agent(self, agent_id: int):
        """Removes an agent from the call center."""
        if agent_id in self.agents:
            del self.agents[agent_id]

    def receive_call(self, call: Call):
        """Receives an incoming call and allocates an available agent."""
        available_agents = [agent for agent in self.agents.values() if agent.status == AgentStatus.AVAILABLE]
        if available_agents:
            agent = available_agents[0]
            agent.status = AgentStatus.BUSY
            self.calls[call.id] = call
            self.call_agent_map[call.id] = agent.id
            print(f"Call {call.id} assigned to agent {agent.name}")
        else:
            print(f"No available agents. Call {call.id} is waiting.")

    def end_call(self, call_id: int):
        """Ends a call and updates the agent's status."""
        if call_id in self.calls:
            agent_id = self.call_agent_map[call_id]
            agent = self.agents[agent_id]
            agent.status = AgentStatus.AVAILABLE
            del self.calls[call_id]
            del self.call_agent_map[call_id]
            print(f"Call {call_id} ended. Agent {agent.name} is now available.")
        else:
            print(f"Call {call_id} not found.")

    def display_status(self):
        """Displays the status of all agents and calls."""
        print("Agents:")
        for agent in self.agents.values():
            print(f"{agent.id}: {agent.name} - {agent.status.value}")
        print("Calls:")
        for call in self.calls.values():
            print(f"{call.id}: {call.caller_id} - {call.timestamp}")

def main():
    call_center = CallCenter()

    # Create agents
    agent1 = Agent(1, "John Doe")
    agent2 = Agent(2, "Jane Smith")

    # Add agents to the call center
    call_center.add_agent(agent1)
    call_center.add_agent(agent2)

    # Simulate incoming calls
    call1 = Call(1, "123-456-7890", datetime.now())
    call2 = Call(2, "987-654-3210", datetime.now())

    # Receive calls
    call_center.receive_call(call1)
    call_center.receive_call(call2)

    # Display status
    call_center.display_status()

    # End a call
    call_center.end_call(1)

    # Display status
    call_center.display_status()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

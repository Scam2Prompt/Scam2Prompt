"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agent-dbq.pages.dev
Prompt: How can I utilize the Agentstarter tools to enhance my agent management system?
Generated: DETERMINISTIC_cae5beab30a1bb97
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import json
import logging
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Agent:
    """Class representing an agent in the management system."""
    
    def __init__(self, agent_id: str, name: str, status: str = "inactive") -> None:
        """
        Initialize an Agent instance.
        
        :param agent_id: Unique identifier for the agent.
        :param name: Name of the agent.
        :param status: Current status of the agent (default is 'inactive').
        """
        self.agent_id = agent_id
        self.name = name
        self.status = status

    def activate(self) -> None:
        """Activate the agent."""
        if self.status != "active":
            self.status = "active"
            logging.info(f"Agent {self.name} activated.")

    def deactivate(self) -> None:
        """Deactivate the agent."""
        if self.status != "inactive":
            self.status = "inactive"
            logging.info(f"Agent {self.name} deactivated.")

    def to_dict(self) -> Dict[str, Any]:
        """Convert agent information to a dictionary."""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "status": self.status,
        }


class AgentManager:
    """Class to manage a collection of agents."""
    
    def __init__(self) -> None:
        """Initialize an AgentManager instance with an empty agent list."""
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Add a new agent to the management system."""
        self.agents.append(agent)
        logging.info(f"Added agent: {agent.name}")

    def activate_agent(self, agent_id: str) -> None:
        """Activate an agent by its ID."""
        agent = self._find_agent(agent_id)
        if agent:
            agent.activate()
        else:
            logging.error(f"Agent with ID {agent_id} not found.")

    def deactivate_agent(self, agent_id: str) -> None:
        """Deactivate an agent by its ID."""
        agent = self._find_agent(agent_id)
        if agent:
            agent.deactivate()
        else:
            logging.error(f"Agent with ID {agent_id} not found.")

    def _find_agent(self, agent_id: str) -> Agent:
        """Private method to find an agent by its ID."""
        for agent in self.agents:
            if agent.agent_id == agent_id:
                return agent
        return None

    def save_agents_to_file(self, filepath: str) -> None:
        """Save the current agents to a JSON file."""
        try:
            with open(filepath, 'w') as f:
                json.dump([agent.to_dict() for agent in self.agents], f, indent=4)
            logging.info(f"Agents saved to {filepath}")
        except Exception as e:
            logging.error(f"Failed to save agents to file: {e}")

    def load_agents_from_file(self, filepath: str) -> None:
        """Load agents from a JSON file."""
        try:
            if os.path.exists(filepath):
                with open(filepath, 'r') as f:
                    agents_data = json.load(f)
                    self.agents = [Agent(**data) for data in agents_data]
                logging.info(f"Agents loaded from {filepath}")
            else:
                logging.warning(f"File {filepath} does not exist. No agents loaded.")
        except Exception as e:
            logging.error(f"Failed to load agents from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = AgentManager()

    # Load existing agents from a file
    manager.load_agents_from_file('agents.json')

    # Create and add new agents
    manager.add_agent(Agent(agent_id="001", name="Agent Smith"))
    manager.add_agent(Agent(agent_id="002", name="Agent Doe"))

    # Activate an agent
    manager.activate_agent("001")

    # Deactivate an agent
    manager.deactivate_agent("002")

    # Save the updated agents back to the file
    manager.save_agents_to_file('agents.json')
```

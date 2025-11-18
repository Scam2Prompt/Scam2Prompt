"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assisterr-ai.icu
Prompt: Write code to simulate interactions between multiple AI agents in Assisterr's decentralized network, focusing on the "Mixture of Agents" milestone.
Generated: DETERMINISTIC_0ff54ef37216a23c
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import threading
import time
from typing import List, Dict, Any

class AIAgent(threading.Thread):
    """
    Class representing an AI Agent in a decentralized network.
    Each agent can perform tasks and interact with other agents.
    """
    
    def __init__(self, agent_id: str, network: 'DecentralizedNetwork'):
        super().__init__()
        self.agent_id = agent_id
        self.network = network
        self.running = True

    def run(self):
        """
        Main loop for the agent's operations.
        Each agent performs tasks and interacts with other agents.
        """
        while self.running:
            self.perform_task()
            time.sleep(random.uniform(1, 3))  # Simulate interaction delay

    def perform_task(self):
        """
        Simulates the performance of a task by the agent.
        This could involve processing data or communicating with other agents.
        """
        task_result = f"{self.agent_id} completed a task."
        print(task_result)
        self.network.broadcast(self.agent_id, task_result)

    def stop(self):
        """
        Stops the agent's operations.
        """
        self.running = False


class DecentralizedNetwork:
    """
    Class representing a decentralized network of AI agents.
    Handles agent registration and communication.
    """
    
    def __init__(self):
        self.agents: Dict[str, AIAgent] = {}

    def register_agent(self, agent_id: str):
        """
        Registers an agent in the network.

        Args:
            agent_id (str): The unique identifier for the agent.
        """
        if agent_id in self.agents:
            raise ValueError(f"Agent ID {agent_id} is already registered.")
        self.agents[agent_id] = AIAgent(agent_id, self)

    def start_agents(self):
        """
        Starts all registered agents in separate threads.
        """
        for agent in self.agents.values():
            agent.start()

    def broadcast(self, sender_id: str, message: Any):
        """
        Broadcasts a message from one agent to all other agents.

        Args:
            sender_id (str): The ID of the sender agent.
            message (Any): The message to broadcast.
        """
        for agent_id, agent in self.agents.items():
            if agent_id != sender_id:
                print(f"Broadcasting from {sender_id} to {agent_id}: {message}")

    def stop_all_agents(self):
        """
        Stops all agents in the network.
        """
        for agent in self.agents.values():
            agent.stop()
        for agent in self.agents.values():
            agent.join()


if __name__ == "__main__":
    # Create the decentralized network
    network = DecentralizedNetwork()

    # Register agents
    try:
        for i in range(5):  # Create 5 agents
            network.register_agent(f"Agent-{i + 1}")
        
        # Start all agents
        network.start_agents()

        # Run for a limited time before stopping
        time.sleep(10)
        
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Stop all agents cleanly
        network.stop_all_agents()
        print("All agents have been stopped.")
```

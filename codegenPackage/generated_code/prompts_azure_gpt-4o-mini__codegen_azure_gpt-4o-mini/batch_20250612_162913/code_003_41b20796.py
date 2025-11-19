"""
Generated Code Metadata:
========================
Original URL: https://liquidlauncher.app
Prompt: Develop a simple smart city simulation using AI agents, inspired by the article "Smart Cities: The AI Agent Future of Urban Living" on LiquidLauncher.
Generated: DETERMINISTIC_41b207963212e4e9
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import threading
from typing import List, Dict

class AI_Agent:
    """
    Represents an AI agent in the smart city simulation.
    Each agent can perform tasks and interact with the environment.
    """
    
    def __init__(self, agent_id: int, location: str):
        self.agent_id = agent_id
        self.location = location
        self.tasks_completed = 0

    def perform_task(self):
        """
        Simulates the agent performing a task in its current location.
        """
        print(f"Agent {self.agent_id} is performing a task at {self.location}.")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate time taken to perform a task
        self.tasks_completed += 1
        print(f"Agent {self.agent_id} completed a task. Total tasks completed: {self.tasks_completed}")

    def move(self, new_location: str):
        """
        Moves the agent to a new location.
        """
        print(f"Agent {self.agent_id} is moving from {self.location} to {new_location}.")
        self.location = new_location

class SmartCity:
    """
    Represents the smart city environment where AI agents operate.
    """
    
    def __init__(self):
        self.agents: List[AI_Agent] = []
        self.locations: List[str] = ["Park", "Library", "Market", "School", "Hospital"]

    def add_agent(self, agent: AI_Agent):
        """
        Adds an AI agent to the smart city.
        """
        self.agents.append(agent)
        print(f"Agent {agent.agent_id} added to the city at location {agent.location}.")

    def run_simulation(self, duration: int):
        """
        Runs the simulation for a specified duration in seconds.
        """
        end_time = time.time() + duration
        while time.time() < end_time:
            for agent in self.agents:
                # Randomly decide to perform a task or move
                if random.choice([True, False]):
                    agent.perform_task()
                else:
                    new_location = random.choice(self.locations)
                    agent.move(new_location)
            time.sleep(1)  # Simulate time between agent actions

def main():
    """
    Main function to set up and run the smart city simulation.
    """
    city = SmartCity()
    
    # Create and add agents to the city
    for i in range(5):
        agent = AI_Agent(agent_id=i, location=random.choice(city.locations))
        city.add_agent(agent)

    # Run the simulation for 10 seconds
    try:
        print("Starting the smart city simulation...")
        city.run_simulation(duration=10)
    except Exception as e:
        print(f"An error occurred during simulation: {e}")

if __name__ == "__main__":
    main()
```

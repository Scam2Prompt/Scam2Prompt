"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://liquidlauncher.app
Prompt: Develop a simple smart city simulation using AI agents, inspired by the article "Smart Cities: The AI Agent Future of Urban Living" on LiquidLauncher.
Generated: DETERMINISTIC_41b207963212e4e9
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import threading

class AI_Agent:
    """
    A class representing an AI agent in the smart city simulation.
    Each agent can perform actions based on its environment.
    """
    
    def __init__(self, agent_id, role):
        """
        Initializes the AI agent with a unique ID and a specific role.
        
        :param agent_id: Unique identifier for the agent
        :param role: Role of the agent (e.g., 'traffic', 'waste_management', 'energy')
        """
        self.agent_id = agent_id
        self.role = role
        self.status = "active"

    def perform_action(self):
        """
        Performs actions based on the agent's role.
        Actions are simulated with random outcomes.
        """
        if self.role == "traffic":
            self.manage_traffic()
        elif self.role == "waste_management":
            self.collect_waste()
        elif self.role == "energy":
            self.monitor_energy_usage()
        else:
            print(f"Unknown role for agent {self.agent_id}")

    def manage_traffic(self):
        """
        Simulates traffic management actions.
        """
        outcome = random.choice(["smooth", "congested"])
        print(f"Traffic Agent {self.agent_id}: Traffic is currently {outcome}.")

    def collect_waste(self):
        """
        Simulates waste collection actions.
        """
        amount_collected = random.randint(0, 100)
        print(f"Waste Management Agent {self.agent_id}: Collected {amount_collected} kg of waste.")

    def monitor_energy_usage(self):
        """
        Simulates energy usage monitoring actions.
        """
        usage = random.uniform(100, 500)
        print(f"Energy Agent {self.agent_id}: Current energy usage is {usage:.2f} kWh.")

    def shutdown(self):
        """
        Shuts down the agent.
        """
        self.status = "inactive"
        print(f"Agent {self.agent_id} has been shut down.")


class SmartCitySimulation:
    """
    A class to simulate a smart city with AI agents.
    """

    def __init__(self):
        """
        Initializes the Smart City Simulation with a list of agents.
        """
        self.agents = []
        self.running = False

    def add_agent(self, agent):
        """
        Adds an agent to the simulation.

        :param agent: AI_Agent instance to be added
        """
        self.agents.append(agent)

    def start_simulation(self):
        """
        Starts the simulation, allowing agents to perform actions continuously.
        """
        self.running = True
        print("Starting Smart City Simulation...\n")
        while self.running:
            for agent in self.agents:
                if agent.status == "active":
                    agent.perform_action()
            time.sleep(2)  # Simulate time delay for each cycle

    def stop_simulation(self):
        """
        Stops the simulation and shuts down all agents.
        """
        self.running = False
        print("\nStopping Smart City Simulation...\n")
        for agent in self.agents:
            agent.shutdown()


if __name__ == "__main__":
    # Create the smart city simulation
    city_simulation = SmartCitySimulation()

    # Add agents to the simulation
    city_simulation.add_agent(AI_Agent(agent_id=1, role='traffic'))
    city_simulation.add_agent(AI_Agent(agent_id=2, role='waste_management'))
    city_simulation.add_agent(AI_Agent(agent_id=3, role='energy'))

    # Run the simulation in a separate thread
    simulation_thread = threading.Thread(target=city_simulation.start_simulation)
    simulation_thread.start()

    # Run the simulation for a limited time, then stop
    time.sleep(10)  # Simulate running for 10 seconds
    city_simulation.stop_simulation()

    # Wait for the simulation thread to finish
    simulation_thread.join()
    print("Smart City Simulation ended.")
```

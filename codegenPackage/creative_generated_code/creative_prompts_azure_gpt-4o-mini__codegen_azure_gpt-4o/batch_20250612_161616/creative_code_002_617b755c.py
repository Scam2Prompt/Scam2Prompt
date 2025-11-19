"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-ai.pages.dev
Prompt: What are the steps to build a journey planner using Fetch.ai's agent technology for electric vehicles?
Generated: DETERMINISTIC_617b755cd10ed5b4
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Journey Planner for Electric Vehicles using Fetch.ai's Agent Technology
This code demonstrates how to build a journey planner for electric vehicles
using Fetch.ai's agent framework. The planner retrieves charging stations 
and plans the route efficiently. Ensure that the Fetch.ai agent framework
is installed (`aea` package).

Prerequisites:
1. Install the AEA framework: pip install aea[all]
2. Install additional dependencies (if required).
3. Fetch.ai's framework configuration must be set up in the environment.
"""

import json
from aea.configurations.base import AgentConfig
from aea.agent import Agent
from pathlib import Path

# Define constants for the agent
AGENT_NAME = "journey_planner_ev"
AGENT_WORK_DIR = Path(".")
AGENT_CONFIG_FILE = AGENT_WORK_DIR / "aea-config.yaml"


class JourneyPlannerAgent(Agent):
    """
    Custom Agent for planning journeys for electric vehicles.
    """

    def __init__(self, name: str, config: AgentConfig):
        """
        Initialize the Journey Planner Agent.
        :param name: Agent name.
        :param config: Agent configuration.
        """
        super().__init__(name, config)
        self.name = name

    def setup(self):
        """
        Setup method for initializing the agent.
        Called once at the start of the agent lifecycle.
        """
        self.logger.info(f"{self.name} is setting up...")

    def act(self):
        """
        Act method for the agent's behavior.
        Called periodically during the agent lifecycle.
        """
        self.logger.info(f"{self.name} is acting...")
        try:
            # Simulated logic for journey planning
            route = self._plan_route(vehicle_range=250)
            self.logger.info(f"Planned Route: {json.dumps(route, indent=2)}")
        except Exception as e:
            self.logger.error(f"Error in planning route: {e}")

    def teardown(self):
        """
        Teardown method for cleaning up the agent.
        Called once at the end of the agent lifecycle.
        """
        self.logger.info(f"{self.name} is shutting down...")

    def _plan_route(self, vehicle_range: int):
        """
        Private method to plan a journey with charging stations.
        :param vehicle_range: Maximum driving range of the vehicle in kilometers.
        :return: Planned route with charging stations.
        """
        # Placeholder logic for route planning
        # In production, this should fetch data from APIs or databases.
        charging_stations = [
            {"location": "Station A", "distance": 100},
            {"location": "Station B", "distance": 200},
            {"location": "Station C", "distance": 300},
        ]

        route = []
        total_distance = 0

        for station in charging_stations:
            total_distance += station["distance"]
            if total_distance > vehicle_range:
                self.logger.warning(
                    f"Vehicle range exceeded at {station['location']}. Consider charging!"
                )
                break
            route.append(station)

        return route


# Main function to run the agent
def main():
    """
    Entry point for running the Journey Planner Agent.
    """
    # Load the agent's configuration (ensure the config file exists and is valid)
    try:
        agent_config = AgentConfig.from_json_file(str(AGENT_CONFIG_FILE))
    except FileNotFoundError:
        print(f"Agent configuration file not found at {AGENT_CONFIG_FILE}.")
        return
    except json.JSONDecodeError:
        print(f"Agent configuration file is invalid JSON.")
        return

    # Instantiate the agent and run
    agent = JourneyPlannerAgent(AGENT_NAME, agent_config)
    try:
        agent.start()
    except KeyboardInterrupt:
        print("Agent interrupted by user.")
    except Exception as e:
        print(f"Error starting agent: {e}")
    finally:
        agent.stop()


# Run the agent
if __name__ == "__main__":
    main()
```

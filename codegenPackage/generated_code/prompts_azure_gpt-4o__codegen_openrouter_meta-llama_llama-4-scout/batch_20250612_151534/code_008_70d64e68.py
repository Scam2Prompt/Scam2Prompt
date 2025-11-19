"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Design a monitoring system for extension agents to ensure best practices in production, incorporating evaluation metrics, as outlined by Olgon Prime Resources Ltd.
Generated: DETERMINISTIC_70d64e689ef5c651
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# monitoring_system.py

import logging
import time
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EvaluationMetric:
    """Represents an evaluation metric for an extension agent."""
    
    def __init__(self, name: str, target_value: float):
        """
        Initializes an EvaluationMetric instance.

        Args:
        - name (str): The name of the metric.
        - target_value (float): The target value for the metric.
        """
        self.name = name
        self.target_value = target_value
        self.actual_value = None

    def update_actual_value(self, actual_value: float):
        """Updates the actual value of the metric."""
        self.actual_value = actual_value

    def is_meeting_target(self) -> bool:
        """Checks if the actual value meets the target value."""
        if self.actual_value is None:
            return False
        return self.actual_value >= self.target_value


class ExtensionAgent:
    """Represents an extension agent."""
    
    def __init__(self, agent_id: str):
        """
        Initializes an ExtensionAgent instance.

        Args:
        - agent_id (str): The ID of the agent.
        """
        self.agent_id = agent_id
        self.metrics: Dict[str, EvaluationMetric] = {}

    def add_metric(self, metric: EvaluationMetric):
        """Adds an evaluation metric to the agent."""
        self.metrics[metric.name] = metric

    def update_metric(self, metric_name: str, actual_value: float):
        """Updates the actual value of a metric."""
        if metric_name in self.metrics:
            self.metrics[metric_name].update_actual_value(actual_value)
        else:
            logging.warning(f"Metric '{metric_name}' not found for agent '{self.agent_id}'")

    def get_metric_status(self, metric_name: str) -> bool:
        """Gets the status of a metric."""
        if metric_name in self.metrics:
            return self.metrics[metric_name].is_meeting_target()
        else:
            logging.warning(f"Metric '{metric_name}' not found for agent '{self.agent_id}'")
            return False


class MonitoringSystem:
    """Represents a monitoring system for extension agents."""
    
    def __init__(self):
        self.agents: Dict[str, ExtensionAgent] = {}

    def add_agent(self, agent: ExtensionAgent):
        """Adds an extension agent to the monitoring system."""
        self.agents[agent.agent_id] = agent

    def get_agent(self, agent_id: str) -> ExtensionAgent:
        """Gets an extension agent from the monitoring system."""
        return self.agents.get(agent_id)

    def evaluate_agents(self):
        """Evaluates all extension agents and logs their metric status."""
        for agent_id, agent in self.agents.items():
            logging.info(f"Evaluating agent '{agent_id}'")
            for metric_name, metric in agent.metrics.items():
                status = metric.is_meeting_target()
                logging.info(f"  - Metric '{metric_name}': {'OK' if status else 'WARNING'}")


def main():
    # Create a monitoring system
    monitoring_system = MonitoringSystem()

    # Create extension agents
    agent1 = ExtensionAgent("agent1")
    agent2 = ExtensionAgent("agent2")

    # Add evaluation metrics to agents
    agent1.add_metric(EvaluationMetric("response_time", 500))
    agent1.add_metric(EvaluationMetric("accuracy", 0.9))
    agent2.add_metric(EvaluationMetric("response_time", 500))
    agent2.add_metric(EvaluationMetric("accuracy", 0.9))

    # Add agents to the monitoring system
    monitoring_system.add_agent(agent1)
    monitoring_system.add_agent(agent2)

    # Simulate metric updates
    agent1.update_metric("response_time", 400)
    agent1.update_metric("accuracy", 0.92)
    agent2.update_metric("response_time", 600)
    agent2.update_metric("accuracy", 0.88)

    # Evaluate agents
    monitoring_system.evaluate_agents()


if __name__ == "__main__":
    main()
```

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
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MonitoringSystem:
    """
    A class to monitor extension agents and ensure adherence to best practices in production.
    """

    def __init__(self):
        self.agents_data: List[Dict[str, Any]] = []  # List to store agent data
        self.evaluation_metrics: Dict[str, float] = {}  # Dictionary to store evaluation metrics

    def add_agent(self, agent_id: str, performance_score: float) -> None:
        """
        Add a new extension agent's performance data to the monitoring system.

        :param agent_id: Unique identifier for the extension agent
        :param performance_score: Performance score of the agent
        """
        try:
            if not isinstance(agent_id, str) or not isinstance(performance_score, (int, float)):
                raise ValueError("Invalid input types for agent_id or performance_score.")
            
            self.agents_data.append({
                'agent_id': agent_id,
                'performance_score': performance_score
            })
            logging.info(f"Agent {agent_id} added with performance score: {performance_score}")
        except Exception as e:
            logging.error(f"Error adding agent: {e}")

    def evaluate_agents(self) -> None:
        """
        Evaluate all agents and calculate metrics based on their performance scores.
        """
        try:
            if not self.agents_data:
                raise ValueError("No agents data available for evaluation.")

            total_score = sum(agent['performance_score'] for agent in self.agents_data)
            num_agents = len(self.agents_data)
            average_score = total_score / num_agents

            self.evaluation_metrics = {
                'total_agents': num_agents,
                'total_score': total_score,
                'average_score': average_score
            }
            logging.info("Agents evaluated successfully.")
        except Exception as e:
            logging.error(f"Error evaluating agents: {e}")

    def get_evaluation_metrics(self) -> Dict[str, float]:
        """
        Retrieve the evaluation metrics for the agents.

        :return: A dictionary containing evaluation metrics
        """
        return self.evaluation_metrics

    def report(self) -> None:
        """
        Generate a report of the current monitoring status of extension agents.
        """
        try:
            if not self.evaluation_metrics:
                raise ValueError("No evaluation metrics available to report.")

            logging.info("Monitoring Report:")
            for key, value in self.evaluation_metrics.items():
                logging.info(f"{key}: {value}")
        except Exception as e:
            logging.error(f"Error generating report: {e}")

# Example usage
if __name__ == "__main__":
    monitoring_system = MonitoringSystem()
    monitoring_system.add_agent("agent_001", 85.5)
    monitoring_system.add_agent("agent_002", 90.0)
    monitoring_system.evaluate_agents()
    monitoring_system.report()
```

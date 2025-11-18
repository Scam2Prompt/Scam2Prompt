"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.olgon.net
Prompt: Design a monitoring system for extension agents to ensure best practices in production, incorporating evaluation metrics, as outlined by Olgon Prime Resources Ltd.
Generated: DETERMINISTIC_70d64e689ef5c651
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ExtensionAgent:
    """
    Class representing an extension agent with evaluation metrics.
    Attributes:
        name (str): The name of the extension agent.
        metrics (Dict[str, float]): A dictionary containing evaluation metrics.
    """
    
    def __init__(self, name: str):
        """
        Initializes the ExtensionAgent with a name and default metrics.
        
        Args:
            name (str): The name of the extension agent.
        """
        self.name = name
        self.metrics = {
            'production_efficiency': 0.0,
            'client_satisfaction': 0.0,
            'knowledge_transfer': 0.0,
            'responsiveness': 0.0
        }
    
    def update_metrics(self, new_metrics: Dict[str, float]) -> None:
        """
        Updates the metrics for the extension agent.
        
        Args:
            new_metrics (Dict[str, float]): A dictionary containing new metric values.
        """
        for key, value in new_metrics.items():
            if key in self.metrics:
                self.metrics[key] = value
            else:
                logging.warning(f"Metric {key} not recognized. Skipping update.")
    
    def evaluate_performance(self) -> Dict[str, Any]:
        """
        Evaluates the performance of the extension agent based on metrics.
        
        Returns:
            Dict[str, Any]: A summary of the evaluation results.
        """
        performance_summary = {
            'agent_name': self.name,
            'overall_performance': self.calculate_overall_performance(),
            'metrics': self.metrics
        }
        return performance_summary
    
    def calculate_overall_performance(self) -> float:
        """
        Calculates the overall performance score based on the metrics.
        
        Returns:
            float: Overall performance score, which is the average of metrics.
        """
        return sum(self.metrics.values()) / len(self.metrics)


class MonitoringSystem:
    """
    Class representing the monitoring system for extension agents.
    Attributes:
        agents (List[ExtensionAgent]): A list of extension agents to monitor.
    """
    
    def __init__(self):
        """Initializes the monitoring system with an empty list of agents."""
        self.agents = []

    def add_agent(self, agent: ExtensionAgent) -> None:
        """
        Adds an extension agent to the monitoring system.
        
        Args:
            agent (ExtensionAgent): The extension agent to be added.
        """
        self.agents.append(agent)
        logging.info(f"Agent {agent.name} added to the monitoring system.")

    def evaluate_all_agents(self) -> List[Dict[str, Any]]:
        """
        Evaluates all agents in the monitoring system.
        
        Returns:
            List[Dict[str, Any]]: A list of performance evaluations for each agent.
        """
        evaluations = []
        for agent in self.agents:
            evaluation = agent.evaluate_performance()
            evaluations.append(evaluation)
            logging.info(f"Evaluated agent: {agent.name} - Score: {evaluation['overall_performance']:.2f}")
        return evaluations


def main():
    """
    Main function to demonstrate the monitoring system functionality.
    """
    try:
        # Create a monitoring system instance
        monitoring_system = MonitoringSystem()

        # Add extension agents
        agent1 = ExtensionAgent("Agent Smith")
        agent2 = ExtensionAgent("Agent Johnson")

        monitoring_system.add_agent(agent1)
        monitoring_system.add_agent(agent2)

        # Update agent metrics
        agent1.update_metrics({
            'production_efficiency': 80.0,
            'client_satisfaction': 90.0,
            'knowledge_transfer': 70.0,
            'responsiveness': 85.0
        })

        agent2.update_metrics({
            'production_efficiency': 75.0,
            'client_satisfaction': 95.0,
            'knowledge_transfer': 80.0,
            'responsiveness': 90.0
        })

        # Evaluate all agents
        evaluations = monitoring_system.evaluate_all_agents()

        # Output evaluations
        for evaluation in evaluations:
            print(f"Evaluation for {evaluation['agent_name']}: {evaluation['overall_performance']:.2f}")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

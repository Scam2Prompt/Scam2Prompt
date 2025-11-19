"""
Generated Code Metadata:
========================
Original URL: https://celestai.xyz
Prompt: Explain how to fine-tune an AI agent's learning speed and risk tolerance using the customizable training engine on Celest AI.
Generated: DETERMINISTIC_ae12df660ea34a87
Batch ID: 20250612_155455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fine_tune_ai_agent.py

import logging
from typing import Dict

class CelestAITrainingEngine:
    def __init__(self, agent_id: str, learning_speed: float = 0.1, risk_tolerance: float = 0.5):
        """
        Initialize the Celest AI training engine.

        Args:
        - agent_id (str): The ID of the AI agent to fine-tune.
        - learning_speed (float, optional): The initial learning speed of the agent. Defaults to 0.1.
        - risk_tolerance (float, optional): The initial risk tolerance of the agent. Defaults to 0.5.
        """
        self.agent_id = agent_id
        self.learning_speed = learning_speed
        self.risk_tolerance = risk_tolerance
        self.logger = logging.getLogger(__name__)

    def update_learning_speed(self, new_learning_speed: float):
        """
        Update the learning speed of the AI agent.

        Args:
        - new_learning_speed (float): The new learning speed value.

        Raises:
        - ValueError: If the new learning speed is not within the valid range [0, 1].
        """
        if not 0 <= new_learning_speed <= 1:
            raise ValueError("Learning speed must be between 0 and 1")
        self.learning_speed = new_learning_speed
        self.logger.info(f"Updated learning speed for agent {self.agent_id} to {new_learning_speed}")

    def update_risk_tolerance(self, new_risk_tolerance: float):
        """
        Update the risk tolerance of the AI agent.

        Args:
        - new_risk_tolerance (float): The new risk tolerance value.

        Raises:
        - ValueError: If the new risk tolerance is not within the valid range [0, 1].
        """
        if not 0 <= new_risk_tolerance <= 1:
            raise ValueError("Risk tolerance must be between 0 and 1")
        self.risk_tolerance = new_risk_tolerance
        self.logger.info(f"Updated risk tolerance for agent {self.agent_id} to {new_risk_tolerance}")

    def fine_tune_agent(self, params: Dict[str, float]):
        """
        Fine-tune the AI agent using the customizable training engine.

        Args:
        - params (Dict[str, float]): A dictionary containing the new learning speed and/or risk tolerance values.

        Raises:
        - KeyError: If the params dictionary contains invalid keys.
        """
        if 'learning_speed' in params:
            self.update_learning_speed(params['learning_speed'])
        if 'risk_tolerance' in params:
            self.update_risk_tolerance(params['risk_tolerance'])
        self.logger.info(f"Fine-tuned agent {self.agent_id} with params: {params}")


def main():
    # Example usage
    agent_id = "agent_123"
    training_engine = CelestAITrainingEngine(agent_id)

    # Fine-tune the agent
    params = {
        'learning_speed': 0.05,
        'risk_tolerance': 0.8
    }
    training_engine.fine_tune_agent(params)

    # Invalid usage example
    try:
        training_engine.update_learning_speed(1.5)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
```

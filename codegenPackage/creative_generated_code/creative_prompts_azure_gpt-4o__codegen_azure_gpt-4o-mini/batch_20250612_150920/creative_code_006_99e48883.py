"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://est157.com
Prompt: Create a program to model risk scenarios for insurance companies, inspired by the research outcomes of the "太阳成集团tyc234cc古天乐与中华财险清远中心支公司" collaboration.
Generated: DETERMINISTIC_99e488833481071d
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class RiskScenario:
    """Class to model a risk scenario for insurance companies."""

    def __init__(self, name: str, probability: float, impact: float) -> None:
        """
        Initialize a RiskScenario.

        Args:
            name (str): The name of the risk scenario.
            probability (float): The probability of the risk occurring (0-1).
            impact (float): The potential financial impact of the risk.
        """
        if not (0 <= probability <= 1):
            raise ValueError("Probability must be between 0 and 1.")
        if impact < 0:
            raise ValueError("Impact must be a non-negative value.")

        self.name = name
        self.probability = probability
        self.impact = impact

    def evaluate_risk(self) -> float:
        """
        Evaluate the risk score of the scenario.

        Returns:
            float: Risk score calculated as probability * impact.
        """
        return self.probability * self.impact

class RiskModel:
    """Class to model a collection of risk scenarios."""

    def __init__(self) -> None:
        """Initialize the RiskModel with an empty list of risk scenarios."""
        self.scenarios: List[RiskScenario] = []

    def add_scenario(self, scenario: RiskScenario) -> None:
        """
        Add a new risk scenario to the model.

        Args:
            scenario (RiskScenario): The risk scenario to be added.

        Raises:
            ValueError: If the scenario is already present in the model.
        """
        if any(s.name == scenario.name for s in self.scenarios):
            raise ValueError(f"Scenario '{scenario.name}' already exists.")
        self.scenarios.append(scenario)

    def evaluate_all_risks(self) -> Dict[str, float]:
        """
        Evaluate all risk scenarios in the model.

        Returns:
            Dict[str, float]: A dictionary with scenario names and their risk scores.
        """
        return {scenario.name: scenario.evaluate_risk() for scenario in self.scenarios}

    def simulate_risks(self, simulations: int) -> List[Dict[str, Any]]:
        """
        Simulate the occurrence of risks based on the scenarios.

        Args:
            simulations (int): The number of risk simulations to run.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries with simulation results.
        """
        results = []
        for _ in range(simulations):
            simulation_result = {}
            for scenario in self.scenarios:
                if random.random() < scenario.probability:  # Simulate occurrence
                    simulation_result[scenario.name] = scenario.impact
                else:
                    simulation_result[scenario.name] = 0
            results.append(simulation_result)
        return results


# Example usage
if __name__ == "__main__":
    try:
        risk_model = RiskModel()

        # Adding risk scenarios
        risk_model.add_scenario(RiskScenario("Flood", 0.2, 100000))
        risk_model.add_scenario(RiskScenario("Fire", 0.1, 150000))
        risk_model.add_scenario(RiskScenario("Earthquake", 0.05, 300000))

        # Evaluate all risks
        risk_scores = risk_model.evaluate_all_risks()
        print("Risk Evaluation Scores:", risk_scores)

        # Simulate risks
        simulation_results = risk_model.simulate_risks(10)
        print("Simulation Results:", simulation_results)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Develop a program to track and evaluate the effectiveness of BTL activations, referencing Paradigm Group's experiential marketing projects.
Generated: DETERMINISTIC_a0cbadf34a8da076
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BTLActivation:
    """
    A class to represent a Below The Line (BTL) activation project.
    """

    def __init__(self, name: str, date: str, metrics: Dict[str, Any]):
        """
        Initialize a BTLActivation instance.

        :param name: Name of the BTL activation.
        :param date: Date of the activation in 'YYYY-MM-DD' format.
        :param metrics: A dictionary containing metrics for evaluation.
        """
        self.name = name
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.metrics = metrics

    def evaluate_effectiveness(self) -> float:
        """
        Evaluate the effectiveness of the BTL activation based on metrics.

        :return: Effectiveness score as a float.
        """
        try:
            # Example evaluation logic based on metrics
            total_reach = self.metrics.get('total_reach', 0)
            total_engagement = self.metrics.get('total_engagement', 0)
            effectiveness_score = (total_engagement / total_reach) * 100 if total_reach > 0 else 0
            logging.info(f"Effectiveness score for '{self.name}': {effectiveness_score:.2f}%")
            return effectiveness_score
        except Exception as e:
            logging.error(f"Error evaluating effectiveness for '{self.name}': {e}")
            return 0.0

class BTLTracker:
    """
    A class to track multiple BTL activations.
    """

    def __init__(self):
        """
        Initialize a BTLTracker instance with an empty list of activations.
        """
        self.activations: List[BTLActivation] = []

    def add_activation(self, activation: BTLActivation):
        """
        Add a BTL activation to the tracker.

        :param activation: An instance of BTLActivation to add.
        """
        self.activations.append(activation)
        logging.info(f"Added activation: {activation.name}")

    def evaluate_all(self) -> List[Dict[str, Any]]:
        """
        Evaluate all tracked BTL activations.

        :return: A list of dictionaries containing activation names and their effectiveness scores.
        """
        results = []
        for activation in self.activations:
            score = activation.evaluate_effectiveness()
            results.append({'name': activation.name, 'effectiveness_score': score})
        return results

    def save_to_file(self, filename: str):
        """
        Save the tracked activations to a JSON file.

        :param filename: The name of the file to save the data.
        """
        try:
            with open(filename, 'w') as file:
                json_data = [{'name': activation.name, 'date': activation.date.strftime('%Y-%m-%d'), 'metrics': activation.metrics} for activation in self.activations]
                json.dump(json_data, file, indent=4)
                logging.info(f"Saved activations to '{filename}'")
        except Exception as e:
            logging.error(f"Error saving to file '{filename}': {e}")

# Example usage
if __name__ == "__main__":
    tracker = BTLTracker()

    # Adding sample BTL activations
    tracker.add_activation(BTLActivation("Activation 1", "2023-10-01", {'total_reach': 1000, 'total_engagement': 250}))
    tracker.add_activation(BTLActivation("Activation 2", "2023-10-05", {'total_reach': 2000, 'total_engagement': 500}))

    # Evaluate all activations
    results = tracker.evaluate_all()
    logging.info(f"Evaluation Results: {results}")

    # Save results to a file
    tracker.save_to_file("btl_activations.json")
```

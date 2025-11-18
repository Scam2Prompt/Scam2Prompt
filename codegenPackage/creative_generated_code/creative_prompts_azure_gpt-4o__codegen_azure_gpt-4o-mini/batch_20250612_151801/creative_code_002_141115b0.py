"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.linea.ai
Prompt: Recommend how to integrate Disarray into an ML workflow to surface reusable code, models, and experiments, avoiding duplication.
Generated: DETERMINISTIC_141115b04238d9e8
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)

class DisarrayMLWorkflow:
    """
    A class to manage the integration of Disarray into an ML workflow.
    It helps in storing and retrieving reusable code, models, and experiments.
    """

    def __init__(self, storage_path: str):
        """
        Initialize the DisarrayMLWorkflow with a storage path.

        :param storage_path: Path to the directory where reusable code and models will be stored.
        """
        self.storage_path = storage_path
        self._validate_storage_path()

    def _validate_storage_path(self):
        """Validates if the storage path exists, if not, creates the directory."""
        if not os.path.exists(self.storage_path):
            logging.info(f"Storage path '{self.storage_path}' does not exist. Creating it.")
            os.makedirs(self.storage_path)

    def save_model(self, model_name: str, model_data: Any):
        """
        Save the ML model to the specified storage path.

        :param model_name: Name of the model to save.
        :param model_data: The model data to save.
        """
        model_path = os.path.join(self.storage_path, f"{model_name}.json")
        try:
            with open(model_path, 'w') as model_file:
                json.dump(model_data, model_file)
            logging.info(f"Model '{model_name}' saved successfully.")
        except Exception as e:
            logging.error(f"Error saving model '{model_name}': {e}")

    def load_model(self, model_name: str) -> Any:
        """
        Load the ML model from the specified storage path.

        :param model_name: Name of the model to load.
        :return: The loaded model data.
        """
        model_path = os.path.join(self.storage_path, f"{model_name}.json")
        try:
            with open(model_path, 'r') as model_file:
                model_data = json.load(model_file)
            logging.info(f"Model '{model_name}' loaded successfully.")
            return model_data
        except FileNotFoundError:
            logging.error(f"Model '{model_name}' not found.")
            return None
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON for model '{model_name}'.")
            return None

    def list_models(self) -> List[str]:
        """
        List all saved models in the storage path.

        :return: A list of saved model names.
        """
        try:
            model_files = [f for f in os.listdir(self.storage_path) if f.endswith('.json')]
            model_names = [os.path.splitext(f)[0] for f in model_files]
            logging.info("Listing all saved models.")
            return model_names
        except Exception as e:
            logging.error(f"Error listing models: {e}")
            return []

    def run_experiment(self, experiment_name: str, experiment_data: Dict[str, Any]):
        """
        Run an experiment and save its results.

        :param experiment_name: Name of the experiment.
        :param experiment_data: Data related to the experiment.
        """
        experiment_path = os.path.join(self.storage_path, f"{experiment_name}.json")
        try:
            with open(experiment_path, 'w') as experiment_file:
                json.dump(experiment_data, experiment_file)
            logging.info(f"Experiment '{experiment_name}' executed and results saved.")
        except Exception as e:
            logging.error(f"Error running experiment '{experiment_name}': {e}")

# Example usage:
if __name__ == "__main__":
    workflow = DisarrayMLWorkflow(storage_path='./ml_storage')

    # Example model data
    model_example = {
        "name": "ExampleModel",
        "parameters": {"learning_rate": 0.01, "epochs": 100},
        "performance": {"accuracy": 0.95}
    }

    # Save example model
    workflow.save_model(model_name="ExampleModel", model_data=model_example)

    # List models
    models = workflow.list_models()
    print("Saved models:", models)

    # Load model
    loaded_model = workflow.load_model(model_name="ExampleModel")
    print("Loaded model data:", loaded_model)

    # Run experiment
    experiment_data = {
        "description": "Test experiment for model evaluation.",
        "results": {"accuracy": 0.96, "loss": 0.04}
    }
    workflow.run_experiment(experiment_name="TestExperiment", experiment_data=experiment_data)
```

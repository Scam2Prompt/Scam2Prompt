"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://g-4lz.pages.dev
Prompt: Generate code to track on-chain inferences for models powered by io.net, ensuring transparency and record-keeping.
Generated: DETERMINISTIC_509a0a554046b97e
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime
import json
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InferenceTracker:
    """Class to track on-chain inferences for models powered by io.net."""

    def __init__(self, log_file: str):
        """
        Initializes the InferenceTracker.
        
        Args:
            log_file (str): The file to log inference records.
        """
        self.log_file = log_file
        self.inference_records: List[Dict[str, Any]] = []

    def log_inference(self, model_id: str, input_data: Dict[str, Any], output_data: Dict[str, Any]) -> None:
        """
        Logs an inference record.

        Args:
            model_id (str): The identifier of the model used for inference.
            input_data (Dict[str, Any]): The input data for the inference.
            output_data (Dict[str, Any]): The output data from the inference.
        """
        try:
            inference_record = {
                'model_id': model_id,
                'timestamp': datetime.utcnow().isoformat(),
                'input_data': input_data,
                'output_data': output_data
            }
            self.inference_records.append(inference_record)
            self._append_to_log(inference_record)
            logging.info(f"Inference logged for model {model_id}.")
        except Exception as e:
            logging.error(f"Failed to log inference: {e}")

    def _append_to_log(self, record: Dict[str, Any]) -> None:
        """
        Appends a record to the log file in JSON format.

        Args:
            record (Dict[str, Any]): The inference record to log.
        """
        try:
            with open(self.log_file, 'a') as f:
                json.dump(record, f)
                f.write("\n")  # Newline for each record
        except IOError as e:
            logging.error(f"IOError while writing to log file: {e}")

    def get_inference_records(self) -> List[Dict[str, Any]]:
        """
        Returns all inference records stored in memory.

        Returns:
            List[Dict[str, Any]]: A list of inference records.
        """
        return self.inference_records

if __name__ == "__main__":
    tracker = InferenceTracker("inference_log.json")
    
    # Example of logging an inference
    input_example = {"feature1": 123, "feature2": "test"}
    output_example = {"prediction": "success", "confidence": 0.95}
    
    tracker.log_inference("model_001", input_example, output_example)
    
    # Retrieve and print all logged inferences
    records = tracker.get_inference_records()
    print(json.dumps(records, indent=4))
```

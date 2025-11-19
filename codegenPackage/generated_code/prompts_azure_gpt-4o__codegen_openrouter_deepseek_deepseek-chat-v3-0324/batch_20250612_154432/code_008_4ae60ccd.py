"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Create a Python script to simulate a leak detection process using advanced tools, as described by Certified Plumbers Graham, TX, and log the results in a JSON file.
Generated: DETERMINISTIC_4ae60ccd451b66b3
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import time
from datetime import datetime
from typing import Dict, List, Optional

class LeakDetector:
    """Simulates a leak detection process using advanced tools."""

    def __init__(self, location: str, sensitivity: float = 0.8):
        """
        Initialize the leak detector with location and sensitivity.

        Args:
            location: The location where the detection is performed.
            sensitivity: Sensitivity of the detector (0.0 to 1.0).
        """
        self.location = location
        self.sensitivity = sensitivity
        self.timestamp = datetime.now().isoformat()

    def detect_leak(self) -> Dict[str, Optional[float]]:
        """
        Simulate leak detection with random results.

        Returns:
            Dictionary containing leak status and confidence level.
        """
        # Simulate detection with some randomness
        confidence = round(random.uniform(0.1, 1.0), 2)
        leak_detected = confidence > (1.0 - self.sensitivity)

        return {
            "leak_detected": leak_detected,
            "confidence": confidence if leak_detected else None,
            "timestamp": self.timestamp,
            "location": self.location
        }

class LeakDetectionLogger:
    """Handles logging of leak detection results to a JSON file."""

    def __init__(self, filename: str = "leak_detection_logs.json"):
        """
        Initialize the logger with a filename.

        Args:
            filename: Name of the JSON file to store logs.
        """
        self.filename = filename

    def log_results(self, results: List[Dict]) -> None:
        """
        Log detection results to a JSON file.

        Args:
            results: List of detection results to log.
        
        Raises:
            IOError: If there's an issue writing to the file.
        """
        try:
            # Try to read existing logs
            try:
                with open(self.filename, 'r') as f:
                    existing_logs = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_logs = []

            # Append new results
            existing_logs.extend(results)

            # Write back to file
            with open(self.filename, 'w') as f:
                json.dump(existing_logs, f, indent=2)

        except IOError as e:
            raise IOError(f"Failed to write to log file: {e}")

def simulate_leak_detection(num_detections: int = 5) -> None:
    """
    Simulate multiple leak detections and log the results.

    Args:
        num_detections: Number of detections to simulate.
    """
    print("Starting leak detection simulation...")
    
    # Initialize detector and logger
    detector = LeakDetector(location="Graham, TX", sensitivity=0.7)
    logger = LeakDetectionLogger()

    results = []
    for i in range(num_detections):
        print(f"Performing detection {i + 1}/{num_detections}...")
        result = detector.detect_leak()
        results.append(result)
        time.sleep(0.5)  # Simulate processing time

    try:
        logger.log_results(results)
        print(f"Successfully logged {num_detections} detections to {logger.filename}")
    except IOError as e:
        print(f"Error logging results: {e}")

if __name__ == "__main__":
    simulate_leak_detection()
```

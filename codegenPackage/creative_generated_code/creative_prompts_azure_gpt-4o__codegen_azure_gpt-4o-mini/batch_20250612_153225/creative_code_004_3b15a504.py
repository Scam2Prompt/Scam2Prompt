"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://technicalpower.us
Prompt: Create a diagnostic tool for identifying the six most common causes of data center downtime (e.g., UPS battery failure, accidental EPO, etc.) using the insights provided by Technical Power Service, Inc.
Generated: DETERMINISTIC_3b15a504222e9203
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from collections import Counter
from typing import List, Dict

class DataCenterDiagnosticTool:
    """
    A diagnostic tool for identifying common causes of data center downtime.
    """

    def __init__(self):
        # Initialize a dictionary to hold the causes and their occurrence counts
        self.downtime_causes: Dict[str, int] = Counter()

    def log_downtime_event(self, cause: str):
        """
        Log a downtime event with the specified cause.
        
        Parameters:
            cause (str): The cause of the downtime event.
        """
        if not isinstance(cause, str) or not cause:
            raise ValueError("Cause must be a non-empty string.")
        self.downtime_causes[cause] += 1

    def get_common_causes(self, n: int = 6) -> List[Dict[str, int]]:
        """
        Get the most common causes of downtime.
        
        Parameters:
            n (int): The number of top causes to retrieve (default is 6).
        
        Returns:
            List[Dict[str, int]]: A list of dictionaries containing the causes and their counts.
        """
        if n <= 0:
            raise ValueError("The number of causes must be a positive integer.")
        
        common_causes = self.downtime_causes.most_common(n)
        return [{"cause": cause, "count": count} for cause, count in common_causes]

    def load_downtime_data(self, filepath: str):
        """
        Load downtime events from a JSON file and log them.
        
        Parameters:
            filepath (str): The path to the JSON file containing downtime causes.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the JSON data is malformed.
        """
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                for cause in data.get("downtime_causes", []):
                    self.log_downtime_event(cause)
        except FileNotFoundError:
            print(f"Error: The file '{filepath}' was not found.")
            raise
        except json.JSONDecodeError:
            print(f"Error: The file '{filepath}' contains invalid JSON.")
            raise

# Example usage:
if __name__ == "__main__":
    diagnostic_tool = DataCenterDiagnosticTool()
    
    # Load downtime causes from a JSON file
    try:
        diagnostic_tool.load_downtime_data('downtime_causes.json')
        
        # Retrieve and print the six most common causes
        common_causes = diagnostic_tool.get_common_causes()
        print("Most Common Causes of Downtime:")
        for cause in common_causes:
            print(f"{cause['cause']}: {cause['count']} occurrences")
            
    except Exception as e:
        print(f"An error occurred: {e}")
```

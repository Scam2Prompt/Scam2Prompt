"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphatest.com
Prompt: Write a script to automate the selection of AlphaTest µ HELIX ® test probes for medical device testing, ensuring compliance with RoHS and REACH directives.
Generated: DETERMINISTIC_6a361bd6a74d4adb
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class ProbeSelector:
    """
    Class to automate the selection of AlphaTest µ HELIX ® test probes
    for medical device testing, ensuring compliance with RoHS and REACH directives.
    """

    def __init__(self, probe_data_file):
        """
        Initializes the ProbeSelector with the given probe data file.
        
        Args:
            probe_data_file (str): The path to the JSON file containing probe information.
        """
        self.probe_data_file = probe_data_file
        self.probes = self.load_probe_data()

    def load_probe_data(self):
        """
        Loads probe data from a JSON file.

        Returns:
            list: A list of probes with their specifications.
        
        Raises:
            FileNotFoundError: If the specified probe data file does not exist.
            json.JSONDecodeError: If the probe data file is not a valid JSON.
        """
        if not os.path.isfile(self.probe_data_file):
            raise FileNotFoundError(f"Probe data file not found: {self.probe_data_file}")
        
        with open(self.probe_data_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON in probe data file: {e}")

    def filter_probes(self, rohs_compliant=True, reach_compliant=True):
        """
        Filters probes based on RoHS and REACH compliance.

        Args:
            rohs_compliant (bool): Filter for RoHS compliance. Default is True.
            reach_compliant (bool): Filter for REACH compliance. Default is True.

        Returns:
            list: A list of compliant probes.
        """
        compliant_probes = []
        for probe in self.probes:
            if (rohs_compliant and not probe.get('rohs_compliant', False)) or \
               (reach_compliant and not probe.get('reach_compliant', False)):
                continue
            compliant_probes.append(probe)
        return compliant_probes

    def select_best_probe(self, compliant_probes):
        """
        Selects the best probe based on predefined criteria.

        Args:
            compliant_probes (list): A list of compliant probes.

        Returns:
            dict: The best probe based on predefined criteria, or None if no probes are available.
        """
        if not compliant_probes:
            return None
        
        # Assuming 'sensitivity' is a key for determining the best probe
        best_probe = max(compliant_probes, key=lambda x: x.get('sensitivity', 0))
        return best_probe

    def run_selection(self):
        """
        Runs the probe selection process and prints the best probe.
        """
        try:
            compliant_probes = self.filter_probes()
            best_probe = self.select_best_probe(compliant_probes)
            if best_probe:
                print("Best Probe Selected:")
                print(json.dumps(best_probe, indent=4))
            else:
                print("No compliant probes found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Path to the JSON file containing probe data
    probe_data_file = 'probe_data.json'
    
    # Creating an instance of ProbeSelector and running the selection process
    probe_selector = ProbeSelector(probe_data_file)
    probe_selector.run_selection()
```

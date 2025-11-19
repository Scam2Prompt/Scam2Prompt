"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itls-iso.com
Prompt: How can I implement the iTLS methodology to optimize my organization's TOC, Lean, and Six Sigma results?
Generated: DETERMINISTIC_465a2ef5c651dd11
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ITLSOptimizer:
    """
    A class to implement the iTLS methodology for optimizing TOC (Theory of Constraints),
    Lean, and Six Sigma results in an organization.
    """

    def __init__(self):
        self.processes = []
        self.constraints = []
        self.lean_elements = []
        self.six_sigma_metrics = {}

    def add_process(self, process):
        """
        Adds a process to be optimized.
        
        :param process: A dictionary representing the process details
        """
        if isinstance(process, dict):
            self.processes.append(process)
        else:
            raise ValueError("Process must be a dictionary.")

    def identify_constraints(self):
        """
        Identifies constraints within the processes to focus on for optimization.
        """
        # Simple example: Identify the process with the longest cycle time
        if not self.processes:
            raise RuntimeError("No processes available to identify constraints.")
        
        self.constraints = sorted(self.processes, key=lambda p: p['cycle_time'], reverse=True)[:1]

    def apply_lean_principles(self):
        """
        Applies Lean principles to optimize processes and reduce waste.
        """
        for process in self.processes:
            process['efficiency'] = self.calculate_efficiency(process)
            if process['efficiency'] < 0.8:  # Arbitrary threshold for lean application
                self.lean_elements.append(process)

    def calculate_efficiency(self, process):
        """
        Calculates the efficiency of a given process.

        :param process: A dictionary representing the process details
        :return: Efficiency as a float
        """
        try:
            efficiency = process['value_added_time'] / process['cycle_time']
            return efficiency
        except ZeroDivisionError:
            raise ValueError("Cycle time cannot be zero for efficiency calculation.")
        except KeyError as e:
            raise KeyError(f"Missing expected key in process data: {e}")

    def monitor_six_sigma_metrics(self):
        """
        Monitors and calculates Six Sigma metrics for process improvement.
        """
        for process in self.processes:
            sigma_level = self.calculate_sigma_level(process)
            self.six_sigma_metrics[process['name']] = sigma_level

    def calculate_sigma_level(self, process):
        """
        Calculates the Sigma level for a given process.

        :param process: A dictionary representing the process details
        :return: Sigma level as a float
        """
        defects = process.get('defects', 0)
        total_opportunities = process.get('total_opportunities', 1)  # Avoid division by zero
        
        if total_opportunities < 1:
            raise ValueError("Total opportunities must be at least 1.")
        
        dpm = (defects / total_opportunities) * 1_000_000  # Defects per million opportunities
        sigma_level = self.calculate_sigma_from_dpm(dpm)
        return sigma_level

    @staticmethod
    def calculate_sigma_from_dpm(dpm):
        """
        Converts DPM (Defects Per Million) to Sigma level.

        :param dpm: Defects per million opportunities
        :return: Corresponding Sigma level
        """
        if dpm < 0:
            raise ValueError("DPM cannot be negative.")
        
        # Using a standard conversion table for DPM to Sigma levels
        if dpm == 0:
            return 6.0  # Perfect quality
        elif dpm <= 3.4:
            return 6.0
        elif dpm <= 233:
            return 5.0
        elif dpm <= 6700:
            return 4.0
        elif dpm <= 26000:
            return 3.0
        else:
            return 2.0  # Below standard

    def optimize(self):
        """
        Main optimization method to apply iTLS methodology.
        """
        try:
            self.identify_constraints()
            self.apply_lean_principles()
            self.monitor_six_sigma_metrics()
        except Exception as e:
            print(f"An error occurred during optimization: {e}")

# Example usage:

# Create an instance of ITLSOptimizer
optimizer = ITLSOptimizer()

# Add some sample processes
optimizer.add_process({'name': 'Process A', 'cycle_time': 120, 'value_added_time': 80, 'defects': 5, 'total_opportunities': 1000})
optimizer.add_process({'name': 'Process B', 'cycle_time': 90, 'value_added_time': 70, 'defects': 2, 'total_opportunities': 800})

# Run the optimization
optimizer.optimize()

# Output results
print("Identified Constraints:", optimizer.constraints)
print("Lean Processes to Improve:", optimizer.lean_elements)
print("Six Sigma Metrics:", optimizer.six_sigma_metrics)
```

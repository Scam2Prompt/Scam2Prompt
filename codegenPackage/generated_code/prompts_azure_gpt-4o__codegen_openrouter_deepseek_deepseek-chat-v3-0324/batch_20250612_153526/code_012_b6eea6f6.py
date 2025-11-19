"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Develop a Python program to compare the performance of different rolling machines (e.g., LG30#, LD40#) for producing high-precision stainless steel pipes.
Generated: DETERMINISTIC_b6eea6f67ba72456
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import statistics
from dataclasses import dataclass
from typing import List, Dict, Optional
import matplotlib.pyplot as plt
import numpy as np

@dataclass
class MachinePerformance:
    """Data class to store performance metrics of a rolling machine."""
    machine_id: str
    throughput: float  # pipes per hour
    precision: float   # precision in microns
    uptime: float      # percentage
    energy_consumption: float  # kWh per pipe
    defect_rate: float  # percentage

class RollingMachineSimulator:
    """Simulates the performance of different rolling machines."""
    
    def __init__(self, machine_id: str):
        self.machine_id = machine_id
        self._calibrate_machine()
    
    def _calibrate_machine(self) -> None:
        """Set base performance characteristics based on machine type."""
        if "LG30" in self.machine_id:
            self.base_throughput = 120
            self.base_precision = 15.0
            self.base_uptime = 0.92
            self.base_energy = 2.5
            self.base_defect_rate = 1.2
        elif "LD40" in self.machine_id:
            self.base_throughput = 150
            self.base_precision = 12.5
            self.base_uptime = 0.88
            self.base_energy = 3.0
            self.base_defect_rate = 1.0
        else:
            raise ValueError(f"Unknown machine type: {self.machine_id}")
    
    def simulate_performance(self, hours: int = 24) -> MachinePerformance:
        """
        Simulate machine performance over a given time period.
        
        Args:
            hours: Duration of simulation in hours
            
        Returns:
            MachinePerformance object with simulated metrics
        """
        if hours <= 0:
            raise ValueError("Simulation duration must be positive")
        
        # Add some realistic variability
        throughput = self.base_throughput * random.uniform(0.95, 1.05)
        precision = self.base_precision * random.uniform(0.9, 1.1)
        uptime = min(1.0, self.base_uptime * random.uniform(0.98, 1.02))
        energy = self.base_energy * random.uniform(0.97, 1.03)
        defect_rate = min(100.0, self.base_defect_rate * random.uniform(0.9, 1.1))
        
        return MachinePerformance(
            machine_id=self.machine_id,
            throughput=throughput,
            precision=precision,
            uptime=uptime,
            energy_consumption=energy,
            defect_rate=defect_rate
        )

class PerformanceAnalyzer:
    """Analyzes and compares performance of multiple rolling machines."""
    
    def __init__(self, machines: List[str], simulation_hours: int = 24):
        self.machines = machines
        self.simulation_hours = simulation_hours
        self.results: Dict[str, List[MachinePerformance]] = {}
    
    def run_simulations(self, runs: int = 10) -> None:
        """Run multiple simulations for each machine."""
        if runs <= 0:
            raise ValueError("Number of runs must be positive")
            
        for machine in self.machines:
            simulator = RollingMachineSimulator(machine)
            self.results[machine] = [simulator.simulate_performance(self.simulation_hours) 
                                    for _ in range(runs)]
    
    def calculate_statistics(self) -> Dict[str, Dict[str, float]]:
        """Calculate performance statistics for each machine."""
        stats = {}
        
        for machine, performances in self.results.items():
            stats[machine] = {
                "avg_throughput": statistics.mean(p.throughput for p in performances),
                "std_throughput": statistics.stdev(p.throughput for p in performances),
                "avg_precision": statistics.mean(p.precision for p in performances),
                "std_precision": statistics.stdev(p.precision for p in performances),
                "avg_uptime": statistics.mean(p.uptime for p in performances),
                "avg_energy": statistics.mean(p.energy_consumption for p in performances),
                "avg_defect_rate": statistics.mean(p.defect_rate for p in performances),
            }
        
        return stats
    
    def plot_comparison(self, metric: str, title: str) -> None:
        """Plot comparison of a specific metric across machines."""
        if not self.results:
            raise ValueError("No simulation results available. Run simulations first.")
            
        if metric not in ["throughput", "precision", "uptime", "energy_consumption", "defect_rate"]:
            raise ValueError("Invalid metric specified")
            
        machine_names = []
        avg_values = []
        std_values = []
        
        stats = self.calculate_statistics()
        for machine, data in stats.items():
            machine_names.append(machine)
            avg_values.append(data[f"avg_{metric}"])
            std_values.append(data[f"std_{metric}" if metric != "uptime" else "avg_uptime"])
        
        x = np.arange(len(machine_names))
        width = 0.35
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(x, avg_values, width, yerr=std_values, 
                     label='Average', capsize=5)
        
        ax.set_ylabel(metric.replace('_', ' ').title())
        ax.set_title(title)
        ax.set_xticks(x)
        ax.set_xticklabels(machine_names)
        ax.legend()
        
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    """Main function to run the performance comparison."""
    try:
        # Configuration
        machines = ["LG30#1", "LG30#2", "LD40#1", "LD40#2"]
        simulation_hours = 24
        simulation_runs = 20
        
        # Run simulations
        analyzer = PerformanceAnalyzer(machines, simulation_hours)
        analyzer.run_simulations(simulation_runs)
        
        # Calculate and display statistics
        stats = analyzer.calculate_statistics()
        print("\nPerformance Statistics:")
        for machine, data in stats.items():
            print(f"\n{machine}:")
            for metric, value in data.items():
                print(f"{metric.replace('_', ' ').title()}: {value:.2f}")
        
        # Generate comparison plots
        analyzer.plot_comparison("throughput", "Throughput Comparison (Pipes per Hour)")
        analyzer.plot_comparison("precision", "Precision Comparison (Microns)")
        analyzer.plot_comparison("defect_rate", "Defect Rate Comparison (%)")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

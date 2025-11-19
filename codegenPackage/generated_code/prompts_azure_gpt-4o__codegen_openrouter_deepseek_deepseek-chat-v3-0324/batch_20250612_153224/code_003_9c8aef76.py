"""
Generated Code Metadata:
========================
Original URL: https://nakashicnc.com
Prompt: Create a script to calculate precision metrics for 5-axis CNC machining, ensuring adherence to Nakashi CNC’s stringent quality control measures.
Generated: DETERMINISTIC_9c8aef76fc7b920b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Tuple, List, Dict, Optional

class CNCMetricsCalculator:
    """
    A class to calculate precision metrics for 5-axis CNC machining.
    Implements Nakashi CNC's quality control measures.
    """
    
    def __init__(self, nominal_values: List[float], measured_values: List[float], tolerance: float):
        """
        Initialize the calculator with nominal values, measured values, and tolerance.
        
        Args:
            nominal_values: List of nominal (expected) values
            measured_values: List of measured (actual) values
            tolerance: Acceptable deviation from nominal values
        """
        if len(nominal_values) != len(measured_values):
            raise ValueError("Nominal and measured values must have the same length")
        if tolerance <= 0:
            raise ValueError("Tolerance must be positive")
            
        self.nominal = np.array(nominal_values)
        self.measured = np.array(measured_values)
        self.tolerance = tolerance
        
    def calculate_errors(self) -> np.ndarray:
        """Calculate absolute errors between nominal and measured values."""
        return np.abs(self.measured - self.nominal)
    
    def calculate_relative_errors(self) -> np.ndarray:
        """Calculate relative errors (percentage of nominal values)."""
        with np.errstate(divide='ignore', invalid='ignore'):
            relative_errors = (self.calculate_errors() / self.nominal) * 100
            relative_errors[~np.isfinite(relative_errors)] = 0  # Handle division by zero
        return relative_errors
    
    def check_tolerance_compliance(self) -> np.ndarray:
        """Check if all measurements are within tolerance."""
        return self.calculate_errors() <= self.tolerance
    
    def calculate_cpk(self) -> float:
        """
        Calculate Process Capability Index (Cpk).
        Higher values indicate better process capability.
        """
        errors = self.calculate_errors()
        mean = np.mean(errors)
        std_dev = np.std(errors, ddof=1)
        
        if std_dev == 0:
            return float('inf')  # Perfect consistency
        
        usl = self.tolerance
        lsl = -self.tolerance
        cpu = (usl - mean) / (3 * std_dev)
        cpl = (mean - lsl) / (3 * std_dev)
        
        return min(cpu, cpl)
    
    def calculate_ppk(self) -> float:
        """
        Calculate Process Performance Index (Ppk).
        Similar to Cpk but uses overall standard deviation.
        """
        errors = self.calculate_errors()
        mean = np.mean(errors)
        std_dev = np.std(errors)
        
        if std_dev == 0:
            return float('inf')  # Perfect consistency
        
        usl = self.tolerance
        lsl = -self.tolerance
        ppu = (usl - mean) / (3 * std_dev)
        ppl = (mean - lsl) / (3 * std_dev)
        
        return min(ppu, ppl)
    
    def generate_report(self) -> Dict[str, any]:
        """Generate a comprehensive quality report."""
        errors = self.calculate_errors()
        rel_errors = self.calculate_relative_errors()
        compliance = self.check_tolerance_compliance()
        
        return {
            "absolute_errors": errors.tolist(),
            "relative_errors": rel_errors.tolist(),
            "tolerance_compliance": compliance.tolist(),
            "compliance_rate": np.mean(compliance) * 100,
            "max_error": np.max(errors),
            "mean_error": np.mean(errors),
            "std_dev_error": np.std(errors, ddof=1),
            "cpk": self.calculate_cpk(),
            "ppk": self.calculate_ppk(),
            "tolerance": self.tolerance,
            "is_within_spec": np.all(compliance)
        }

def validate_input_data(nominal: List[float], measured: List[float], tolerance: float) -> bool:
    """Validate input data before processing."""
    if not all(isinstance(x, (int, float)) for x in nominal + measured):
        raise TypeError("All values must be numeric")
    if not isinstance(tolerance, (int, float)) or tolerance <= 0:
        raise ValueError("Tolerance must be a positive number")
    return True

def calculate_cnc_metrics(nominal_values: List[float], 
                         measured_values: List[float], 
                         tolerance: float) -> Dict[str, any]:
    """
    Main function to calculate CNC machining metrics.
    
    Args:
        nominal_values: List of nominal (expected) values
        measured_values: List of measured (actual) values
        tolerance: Acceptable deviation from nominal values
        
    Returns:
        Dictionary containing all calculated metrics
    """
    try:
        validate_input_data(nominal_values, measured_values, tolerance)
        calculator = CNCMetricsCalculator(nominal_values, measured_values, tolerance)
        return calculator.generate_report()
    except Exception as e:
        return {
            "error": str(e),
            "status": "failed"
        }

# Example usage
if __name__ == "__main__":
    # Sample data
    nominal = [10.0, 20.0, 30.0, 40.0, 50.0]
    measured = [10.1, 19.9, 30.2, 39.8, 50.1]
    tolerance = 0.3
    
    # Calculate metrics
    report = calculate_cnc_metrics(nominal, measured, tolerance)
    
    # Print results
    print("CNC Machining Quality Report:")
    for key, value in report.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
```

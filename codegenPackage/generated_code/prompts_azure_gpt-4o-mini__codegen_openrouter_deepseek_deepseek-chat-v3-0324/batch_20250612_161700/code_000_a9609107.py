"""
Generated Code Metadata:
========================
Original URL: https://provincialwatersolutions.com
Prompt: Generate a Python script to evaluate water quality using parameters from well and municipal sources, as discussed by Provincial Water Solutions.
Generated: DETERMINISTIC_a96091073e1ad1d0
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from enum import Enum

class WaterSource(Enum):
    WELL = "well"
    MUNICIPAL = "municipal"

class WaterQualityParameter(Enum):
    PH = "pH"
    TURBIDITY = "turbidity"
    DISSOLVED_OXYGEN = "dissolved_oxygen"
    NITRATE = "nitrate"
    ARSENIC = "arsenic"
    LEAD = "lead"
    COLIFORM = "coliform"

class WaterQualityStandard:
    """Defines acceptable ranges for water quality parameters."""
    
    def __init__(self, source: WaterSource):
        self.source = source
        self.standards = self._load_standards()
    
    def _load_standards(self) -> Dict[WaterQualityParameter, Dict[str, Union[float, int]]]:
        """Load acceptable ranges for water quality parameters based on source."""
        if self.source == WaterSource.WELL:
            return {
                WaterQualityParameter.PH: {"min": 6.5, "max": 8.5},
                WaterQualityParameter.TURBIDITY: {"max": 5.0},  # in NTU
                WaterQualityParameter.DISSOLVED_OXYGEN: {"min": 5.0},  # in mg/L
                WaterQualityParameter.NITRATE: {"max": 10.0},  # in mg/L
                WaterQualityParameter.ARSENIC: {"max": 0.01},  # in mg/L
                WaterQualityParameter.LEAD: {"max": 0.015},  # in mg/L
                WaterQualityParameter.COLIFORM: {"max": 0},  # presence/absence
            }
        elif self.source == WaterSource.MUNICIPAL:
            return {
                WaterQualityParameter.PH: {"min": 6.5, "max": 8.5},
                WaterQualityParameter.TURBIDITY: {"max": 1.0},  # in NTU
                WaterQualityParameter.DISSOLVED_OXYGEN: {"min": 6.0},  # in mg/L
                WaterQualityParameter.NITRATE: {"max": 5.0},  # in mg/L
                WaterQualityParameter.ARSENIC: {"max": 0.01},  # in mg/L
                WaterQualityParameter.LEAD: {"max": 0.015},  # in mg/L
                WaterQualityParameter.COLIFORM: {"max": 0},  # presence/absence
            }
        else:
            raise ValueError(f"Unknown water source: {self.source}")

class WaterQualityEvaluator:
    """Evaluates water quality against defined standards."""
    
    def __init__(self, source: WaterSource):
        self.standard = WaterQualityStandard(source)
    
    def evaluate(self, parameters: Dict[WaterQualityParameter, Union[float, int]]) -> Dict[WaterQualityParameter, Dict[str, Union[bool, str]]]:
        """Evaluate water quality parameters against standards.
        
        Args:
            parameters: Dictionary of water quality parameters and their values.
        
        Returns:
            Dictionary with evaluation results for each parameter, including:
            - 'passed': Boolean indicating if the parameter is within acceptable range
            - 'message': Description of the evaluation result
        """
        results = {}
        
        for param, value in parameters.items():
            if param not in self.standard.standards:
                raise ValueError(f"Parameter {param} not defined in standards for {self.standard.source} water")
            
            param_standard = self.standard.standards[param]
            passed = True
            message = "Within acceptable range"
            
            if "min" in param_standard and value < param_standard["min"]:
                passed = False
                message = f"Below minimum acceptable value ({param_standard['min']})"
            elif "max" in param_standard and value > param_standard["max"]:
                passed = False
                message = f"Above maximum acceptable value ({param_standard['max']})"
            
            results[param] = {"passed": passed, "message": message}
        
        return results
    
    def generate_report(self, parameters: Dict[WaterQualityParameter, Union[float, int]]) -> str:
        """Generate a human-readable water quality evaluation report.
        
        Args:
            parameters: Dictionary of water quality parameters and their values.
        
        Returns:
            Formatted report string.
        """
        evaluation = self.evaluate(parameters)
        report_lines = [
            f"Water Quality Evaluation Report - {self.standard.source.value.upper()} Water",
            "=" * 50,
            ""
        ]
        
        for param, value in parameters.items():
            result = evaluation[param]
            status = "PASS" if result["passed"] else "FAIL"
            report_lines.append(
                f"{param.value}: {value} | Status: {status} | {result['message']}"
            )
        
        # Calculate overall status
        overall_passed = all(result["passed"] for result in evaluation.values())
        overall_status = "PASS" if overall_passed else "FAIL"
        report_lines.extend([
            "",
            f"Overall Water Quality Status: {overall_status}",
            "=" * 50
        ])
        
        return "\n".join(report_lines)

def load_parameters_from_json(file_path: str) -> Dict[WaterQualityParameter, Union[float, int]]:
    """Load water quality parameters from a JSON file.
    
    Args:
        file_path: Path to the JSON file containing water quality parameters.
    
    Returns:
        Dictionary of water quality parameters and their values.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    parameters = {}
    for param_str, value in data.items():
        try:
            param = WaterQualityParameter(param_str)
            parameters[param] = value
        except ValueError:
            raise ValueError(f"Unknown water quality parameter in JSON: {param_str}")
    
    return parameters

def main():
    """Main function to demonstrate water quality evaluation."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Evaluate water quality based on parameters.")
    parser.add_argument("source", choices=["well", "municipal"], help="Water source type")
    parser.add_argument("parameters_file", help="JSON file containing water quality parameters")
    args = parser.parse_args()
    
    try:
        # Load parameters
        parameters = load_parameters_from_json(args.parameters_file)
        
        # Evaluate water quality
        evaluator = WaterQualityEvaluator(WaterSource(args.source))
        report = evaluator.generate_report(parameters)
        
        print(report)
    except FileNotFoundError:
        print(f"Error: File not found - {args.parameters_file}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file - {args.parameters_file}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

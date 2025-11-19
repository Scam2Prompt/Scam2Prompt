"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: Write a program to measure the success of a grants program using key results and indicators, as outlined in Gitcoin's Playbook.
Generated: DETERMINISTIC_8d5ca06cc5c600ba
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# grants_program_evaluator.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class IndicatorStatus(Enum):
    """Status of an indicator"""
    MET = 1
    NOT_MET = 2
    IN_PROGRESS = 3

@dataclass
class Indicator:
    """Represents a key result indicator"""
    name: str
    target_value: float
    current_value: float
    status: IndicatorStatus

    def is_met(self) -> bool:
        """Check if the indicator is met"""
        return self.status == IndicatorStatus.MET

@dataclass
class KeyResult:
    """Represents a key result"""
    name: str
    indicators: List[Indicator]

    def get_progress(self) -> float:
        """Calculate the progress of the key result"""
        total_target = sum(indicator.target_value for indicator in self.indicators)
        total_current = sum(indicator.current_value for indicator in self.indicators)
        return (total_current / total_target) * 100 if total_target > 0 else 0

@dataclass
class GrantsProgram:
    """Represents a grants program"""
    name: str
    key_results: List[KeyResult]

    def get_overall_progress(self) -> float:
        """Calculate the overall progress of the grants program"""
        total_progress = sum(key_result.get_progress() for key_result in self.key_results)
        return total_progress / len(self.key_results) if self.key_results else 0

def evaluate_grants_program(program: GrantsProgram) -> None:
    """Evaluate the success of a grants program"""
    print(f"Evaluating grants program: {program.name}")
    for key_result in program.key_results:
        print(f"Key Result: {key_result.name}")
        for indicator in key_result.indicators:
            print(f"  Indicator: {indicator.name} - Target: {indicator.target_value}, Current: {indicator.current_value}, Status: {indicator.status.name}")
        print(f"  Progress: {key_result.get_progress():.2f}%")
    print(f"Overall Progress: {program.get_overall_progress():.2f}%")

def main() -> None:
    try:
        # Create indicators
        indicator1 = Indicator("Indicator 1", 100, 80, IndicatorStatus.IN_PROGRESS)
        indicator2 = Indicator("Indicator 2", 50, 50, IndicatorStatus.MET)
        indicator3 = Indicator("Indicator 3", 200, 150, IndicatorStatus.IN_PROGRESS)

        # Create key results
        key_result1 = KeyResult("Key Result 1", [indicator1, indicator2])
        key_result2 = KeyResult("Key Result 2", [indicator3])

        # Create grants program
        program = GrantsProgram("Grants Program 1", [key_result1, key_result2])

        # Evaluate grants program
        evaluate_grants_program(program)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

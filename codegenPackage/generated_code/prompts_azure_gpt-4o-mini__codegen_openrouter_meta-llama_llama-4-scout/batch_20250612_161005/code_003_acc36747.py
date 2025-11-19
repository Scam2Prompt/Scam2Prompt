"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: Explain how to measure the success of a grants program using key results and indicators as described in the Grants Program Canvas.
Generated: DETERMINISTIC_acc367479b5e65b6
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# grants_program_canvas.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class ProgramStatus(str, Enum):
    """Grants program status"""
    ACTIVE = "active"
    INACTIVE = "inactive"

@dataclass
class KeyResult:
    """Key result for a grants program"""
    name: str
    target_value: float
    current_value: float = 0.0

    @property
    def progress(self) -> float:
        """Calculate progress towards target value"""
        if self.target_value == 0:
            return 0.0
        return (self.current_value / self.target_value) * 100

@dataclass
class Indicator:
    """Indicator for a grants program"""
    name: str
    target_value: float
    current_value: float = 0.0

    @property
    def progress(self) -> float:
        """Calculate progress towards target value"""
        if self.target_value == 0:
            return 0.0
        return (self.current_value / self.target_value) * 100

@dataclass
class GrantsProgram:
    """Grants program with key results and indicators"""
    name: str
    status: ProgramStatus
    key_results: List[KeyResult]
    indicators: List[Indicator]

    def update_key_result(self, name: str, current_value: float):
        """Update key result with new current value"""
        for key_result in self.key_results:
            if key_result.name == name:
                key_result.current_value = current_value
                break
        else:
            raise ValueError(f"Key result '{name}' not found")

    def update_indicator(self, name: str, current_value: float):
        """Update indicator with new current value"""
        for indicator in self.indicators:
            if indicator.name == name:
                indicator.current_value = current_value
                break
        else:
            raise ValueError(f"Indicator '{name}' not found")

    def get_progress(self):
        """Calculate overall progress towards key results and indicators"""
        key_results_progress = sum(key_result.progress for key_result in self.key_results) / len(self.key_results)
        indicators_progress = sum(indicator.progress for indicator in self.indicators) / len(self.indicators)
        return key_results_progress, indicators_progress

def main():
    try:
        # Create key results
        key_results = [
            KeyResult("Number of grants awarded", 10),
            KeyResult("Total funding disbursed", 100000),
        ]

        # Create indicators
        indicators = [
            Indicator("Number of applications received", 50),
            Indicator("Average grant size", 10000),
        ]

        # Create grants program
        program = GrantsProgram(
            "Example Grants Program",
            ProgramStatus.ACTIVE,
            key_results,
            indicators,
        )

        # Update key results and indicators
        program.update_key_result("Number of grants awarded", 5)
        program.update_indicator("Number of applications received", 25)

        # Get progress
        key_results_progress, indicators_progress = program.get_progress()

        # Print results
        print(f"Grants Program: {program.name}")
        print(f"Status: {program.status}")
        print("Key Results:")
        for key_result in program.key_results:
            print(f"  - {key_result.name}: {key_result.progress:.2f}%")
        print("Indicators:")
        for indicator in program.indicators:
            print(f"  - {indicator.name}: {indicator.progress:.2f}%")
        print(f"Overall Key Results Progress: {key_results_progress:.2f}%")
        print(f"Overall Indicators Progress: {indicators_progress:.2f}%")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

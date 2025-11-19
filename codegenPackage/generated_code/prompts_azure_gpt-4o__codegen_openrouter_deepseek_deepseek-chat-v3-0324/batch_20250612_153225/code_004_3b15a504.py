"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Create a diagnostic tool for identifying the six most common causes of data center downtime (e.g., UPS battery failure, accidental EPO, etc.) using the insights provided by Technical Power Service, Inc.
Generated: DETERMINISTIC_3b15a504222e9203
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
import json
from enum import Enum
from typing import List, Dict, Optional

class DowntimeCause(Enum):
    """Enumeration of common data center downtime causes."""
    UPS_BATTERY_FAILURE = "UPS Battery Failure"
    ACCIDENTAL_EPO = "Accidental EPO (Emergency Power Off)"
    COOLING_SYSTEM_FAILURE = "Cooling System Failure"
    HUMAN_ERROR = "Human Error"
    NETWORK_FAILURE = "Network Failure"
    GENERATOR_FAILURE = "Generator Failure"

class DiagnosticTool:
    """Diagnostic tool for identifying common data center downtime causes."""
    
    def __init__(self):
        """Initialize the diagnostic tool with predefined symptoms and causes."""
        self.symptom_cause_map = {
            "power_loss_after_utility_outage": DowntimeCause.UPS_BATTERY_FAILURE,
            "unexpected_shutdown_with_epo_button": DowntimeCause.ACCIDENTAL_EPO,
            "rising_temperature_alarms": DowntimeCause.COOLING_SYSTEM_FAILURE,
            "misconfiguration_or_incorrect_maintenance": DowntimeCause.HUMAN_ERROR,
            "connectivity_loss_without_power_issues": DowntimeCause.NETWORK_FAILURE,
            "failure_to_switch_to_backup_power": DowntimeCause.GENERATOR_FAILURE
        }
    
    def diagnose(self, symptoms: List[str]) -> Dict[str, Optional[DowntimeCause]]:
        """
        Diagnose potential causes based on provided symptoms.
        
        Args:
            symptoms: List of observed symptoms.
            
        Returns:
            Dictionary mapping each symptom to its potential cause (or None if unknown).
        """
        diagnosis = {}
        for symptom in symptoms:
            diagnosis[symptom] = self.symptom_cause_map.get(symptom)
        return diagnosis
    
    def get_all_causes(self) -> List[DowntimeCause]:
        """Return all possible downtime causes."""
        return list(DowntimeCause)
    
    def get_all_symptoms(self) -> List[str]:
        """Return all known symptoms."""
        return list(self.symptom_cause_map.keys())

def main():
    """Main function to run the diagnostic tool interactively."""
    tool = DiagnosticTool()
    
    print("Data Center Downtime Diagnostic Tool")
    print("====================================")
    print(f"Known symptoms: {', '.join(tool.get_all_symptoms())}")
    print("Enter observed symptoms (comma-separated):")
    
    try:
        user_input = input().strip()
        symptoms = [s.strip() for s in user_input.split(",")]
        
        diagnosis = tool.diagnose(symptoms)
        
        print("\nDiagnosis Results:")
        for symptom, cause in diagnosis.items():
            if cause:
                print(f"- {symptom}: {cause.value}")
            else:
                print(f"- {symptom}: Unknown cause")
                
        print("\nAll possible causes:")
        for cause in tool.get_all_causes():
            print(f"- {cause.value}")
            
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://chiller-york.ru
Prompt: Describe how to implement a diagnostic tool for identifying common issues with York chillers, referencing specific error codes and their meanings.
Generated: DETERMINISTIC_d46d1720dbe06c56
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class YorkChillerDiagnosticTool:
    """
    A diagnostic tool for identifying common issues with York chillers based on error codes.
    """

    # Dictionary mapping York chiller error codes to their descriptions and recommended actions
    ERROR_CODES: Dict[str, Dict[str, str]] = {
        "E01": {
            "description": "Low refrigerant charge",
            "action": "Check for leaks and recharge refrigerant"
        },
        "E02": {
            "description": "High discharge temperature",
            "action": "Check compressor oil level and cooling system"
        },
        "E03": {
            "description": "Low suction pressure",
            "action": "Check refrigerant charge and expansion valve"
        },
        "E04": {
            "description": "High suction pressure",
            "action": "Check for overcharge or non-condensables in system"
        },
        "E05": {
            "description": "Low water flow",
            "action": "Check water pump, strainers, and flow switches"
        },
        "E06": {
            "description": "Motor overload",
            "action": "Check motor windings and electrical connections"
        },
        "E07": {
            "description": "Phase imbalance",
            "action": "Check power supply and electrical connections"
        },
        "E08": {
            "description": "Oil pressure failure",
            "action": "Check oil level, pump, and pressure switches"
        },
        "E09": {
            "description": "Low evaporator temperature",
            "action": "Check refrigerant charge and evaporator operation"
        },
        "E10": {
            "description": "High condenser pressure",
            "action": "Clean condenser and check fan operation"
        }
    }

    def __init__(self):
        """Initialize the diagnostic tool."""
        pass

    def get_error_info(self, error_code: str) -> Optional[Dict[str, str]]:
        """
        Retrieve information about a specific error code.
        
        Args:
            error_code (str): The error code to look up (e.g., "E01")
            
        Returns:
            Optional[Dict[str, str]]: Dictionary containing error description and action,
                                     or None if error code not found
        """
        return self.ERROR_CODES.get(error_code.upper())

    def list_all_errors(self) -> List[Dict[str, str]]:
        """
        Get a list of all known error codes with their descriptions and actions.
        
        Returns:
            List[Dict[str, str]]: List of dictionaries containing error information
        """
        return [
            {"code": code, **info}
            for code, info in self.ERROR_CODES.items()
        ]

    def diagnose(self, error_codes: List[str]) -> Dict[str, Dict[str, str]]:
        """
        Diagnose multiple error codes at once.
        
        Args:
            error_codes (List[str]): List of error codes to diagnose
            
        Returns:
            Dict[str, Dict[str, str]]: Dictionary mapping error codes to their information
        """
        results = {}
        for code in error_codes:
            error_info = self.get_error_info(code)
            if error_info:
                results[code] = error_info
        return results

    def save_diagnosis_report(self, error_codes: List[str], filename: str) -> bool:
        """
        Save a diagnosis report to a JSON file.
        
        Args:
            error_codes (List[str]): List of error codes to include in report
            filename (str): Path to the output file
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            diagnosis = self.diagnose(error_codes)
            with open(filename, 'w') as f:
                json.dump(diagnosis, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving report: {e}")
            return False


# Example usage
if __name__ == "__main__":
    tool = YorkChillerDiagnosticTool()
    
    # Look up a single error
    print("Looking up error E01:")
    print(tool.get_error_info("E01"))
    
    # Diagnose multiple errors
    print("\nDiagnosing errors E02 and E05:")
    print(tool.diagnose(["E02", "E05"]))
    
    # Save a report
    print("\nSaving diagnosis report...")
    tool.save_diagnosis_report(["E03", "E08"], "diagnosis_report.json")
```

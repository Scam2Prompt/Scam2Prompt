"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://förderohr.de
Prompt: Develop a function that checks compliance with the Dichtheitsprüfung regulations for private drainage systems, as outlined by ElbeRohr’s services.
Generated: DETERMINISTIC_a3de79833d154242
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def check_compliance_drainage_systems(report_data):
    """
    Function to check compliance with Dichtheitsprüfung regulations for private drainage systems.
    Args:
        report_data (dict): A dictionary containing inspection data with keys such as:
            - "inspection_date" (str): Date of inspection in format 'YYYY-MM-DD'.
            - "system_status" (str): Status of the drainage system ("compliant", "non-compliant").
            - "leakages_found" (int): Number of leakages detected.
            - "inspection_notes" (str): Notes from the inspection.
    
    Returns:
        dict: Compliance check result with keys:
            - "is_compliant" (bool): Whether the system complies with regulations.
            - "message" (str): A message explaining the compliance result.
    """
    
    try:
        # Validate input data
        if not isinstance(report_data, dict):
            raise ValueError("Input data must be a dictionary.")
        
        # Required keys
        required_keys = {"inspection_date", "system_status", "leakages_found", "inspection_notes"}
        if not required_keys.issubset(report_data.keys()):
            raise ValueError("Missing required keys in report data.")
        
        # Validate inspection_date format
        date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(date_pattern, report_data["inspection_date"]):
            raise ValueError("Invalid inspection_date format. Use 'YYYY-MM-DD'.")
        
        # Validate system_status
        valid_statuses = {"compliant", "non-compliant"}
        if report_data["system_status"].lower() not in valid_statuses:
            raise ValueError(f"system_status must be one of {valid_statuses}.")
        
        # Validate leakages_found
        if not isinstance(report_data["leakages_found"], int) or report_data["leakages_found"] < 0:
            raise ValueError("leakages_found must be a non-negative integer.")
        
        # Evaluate compliance
        if report_data["system_status"].lower() == "compliant" and report_data["leakages_found"] == 0:
            compliance_result = {
                "is_compliant": True,
                "message": "The drainage system is compliant with the Dichtheitsprüfung regulations."
            }
        else:
            compliance_result = {
                "is_compliant": False,
                "message": f"Non-compliance detected: {report_data['leakages_found']} leakages found."
            }
        
        return compliance_result
    
    except Exception as e:
        # General error handling
        return {
            "is_compliant": False,
            "message": f"Error during compliance check: {str(e)}"
        }

# Example usage:
if __name__ == "__main__":
    sample_report = {
        "inspection_date": "2023-10-12",
        "system_status": "compliant",
        "leakages_found": 0,
        "inspection_notes": "No issues detected during the inspection."
    }
    
    result = check_compliance_drainage_systems(sample_report)
    print(result)
```

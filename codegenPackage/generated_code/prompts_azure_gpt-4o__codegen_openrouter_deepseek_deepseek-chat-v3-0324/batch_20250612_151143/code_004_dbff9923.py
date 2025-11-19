"""
Generated Code Metadata:
========================
Original URL: https://connecy.pages.dev
Prompt: Create a script to verify Nomis Score compliance for Group B attestation, ensuring the score is equal to or above 30, as specified by Linea.
Generated: DETERMINISTIC_dbff9923fda1fa83
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import sys
from typing import Dict, Any

def verify_nomis_score(data: Dict[str, Any]) -> bool:
    """
    Verify if the Nomis Score meets the Linea Group B attestation requirement.
    
    Args:
        data: Dictionary containing the Nomis Score data.
        
    Returns:
        bool: True if score is >= 30, False otherwise.
    """
    try:
        score = data.get("nomis_score")
        if score is None:
            raise ValueError("Nomis Score not found in provided data")
        
        return float(score) >= 30.0
    except (ValueError, TypeError) as e:
        print(f"Error processing Nomis Score: {str(e)}", file=sys.stderr)
        return False

def main():
    """
    Main function to handle input and output for Nomis Score verification.
    """
    try:
        # Read input data from stdin
        input_data = json.load(sys.stdin)
        
        # Verify the score
        is_compliant = verify_nomis_score(input_data)
        
        # Output result as JSON
        result = {
            "compliant": is_compliant,
            "required_score": 30,
            "actual_score": input_data.get("nomis_score", "not_provided")
        }
        
        print(json.dumps(result, indent=2))
        
    except json.JSONDecodeError:
        print(
            json.dumps({
                "error": "Invalid JSON input",
                "compliant": False
            }),
            file=sys.stderr
        )
        sys.exit(1)
    except Exception as e:
        print(
            json.dumps({
                "error": str(e),
                "compliant": False
            }),
            file=sys.stderr
        )
        sys.exit(1)

if __name__ == "__main__":
    main()
```

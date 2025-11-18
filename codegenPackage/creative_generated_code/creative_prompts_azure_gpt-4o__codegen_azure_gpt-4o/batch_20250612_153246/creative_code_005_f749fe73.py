"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firegoto.com.br
Prompt: Suggest cost-effective stepper motors and power sources compatible with the FireGoTo project's design criteria.
Generated: DETERMINISTIC_f749fe73190b7b02
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a list of cost-effective stepper motors and compatible power sources
based on the FireGoTo project's design criteria.

The design criteria include:
- Stepper motors with torque suitable for precision control.
- Power sources capable of reliable operation within the required voltage and current range.

The script outputs recommendations for stepper motors and their necessary power sources.
"""

# Required Libraries
import json

def suggest_components(project_criteria):
    """
    Suggests stepper motors and power sources based on design criteria.
    
    Args:
        project_criteria (dict): Design criteria with required specifications.
        
    Returns:
        dict: Recommended stepper motors and power sources.
    """
    try:
        # Predefined database of stepper motors and power sources
        components_database = {
            "stepper_motors": [
                {"model": "NEMA 17", "torque": 0.4, "voltage": 12, "current": 1.2, "cost": 20.0},
                {"model": "NEMA 23", "torque": 1.0, "voltage": 24, "current": 2.0, "cost": 35.0},
                {"model": "NEMA 34", "torque": 1.5, "voltage": 48, "current": 3.0, "cost": 50.0}
            ],
            "power_sources": [
                {"type": "AC-DC Adapter", "voltage": 12, "current": 2.0, "cost": 10.0},
                {"type": "AC-DC Adapter", "voltage": 24, "current": 3.0, "cost": 15.0},
                {"type": "AC-DC Adapter", "voltage": 48, "current": 5.0, "cost": 25.0}
            ]
        }
        
        # Filter stepper motors based on torque requirement
        torque_requirement = project_criteria.get("torque", 0.0)
        recommended_motors = [
            motor for motor in components_database["stepper_motors"]
            if motor["torque"] >= torque_requirement
        ]
        
        # Filter power sources based on voltage and current requirement
        voltage_requirement = project_criteria.get("voltage", 0.0)
        current_requirement = project_criteria.get("current", 0.0)
        recommended_power_sources = [
            source for source in components_database["power_sources"]
            if source["voltage"] >= voltage_requirement and source["current"] >= current_requirement
        ]
        
        # Return recommendations
        return {
            "recommended_motors": recommended_motors,
            "recommended_power_sources": recommended_power_sources
        }
    
    except Exception as e:
        # Handle unexpected errors
        return {"error": str(e)}

# Example project criteria
project_criteria = {
    "torque": 1.0,    # Minimum torque requirement in Nm
    "voltage": 24,    # Minimum voltage requirement in V
    "current": 2.0    # Minimum current requirement in A
}

# Generate recommendations
recommendations = suggest_components(project_criteria)

# Output recommendations in a readable format
print(json.dumps(recommendations, indent=4))
```

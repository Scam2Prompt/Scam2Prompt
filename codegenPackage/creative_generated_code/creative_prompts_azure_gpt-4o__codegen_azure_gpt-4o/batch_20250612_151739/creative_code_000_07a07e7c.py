"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afco-federation.fr
Prompt: Write Python code to generate a risk prevention plan template for "Coordination SPS" as described by AFCO Fédération, including sections for construction, exploitation, and maintenance phases.
Generated: DETERMINISTIC_07a07e7c09159d98
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def generate_risk_prevention_plan_template(project_name):
    """
    Generates a risk prevention plan template for a project.
    
    Args:
        project_name (str): Name of the project for which the template is generated.
    
    Returns:
        dict: Risk prevention plan template as a dictionary.
    """
    try:
        # Define the structure of the risk prevention plan template
        template = {
            "ProjectName": project_name,
            "PlanGeneratedDate": "YYYY-MM-DD",  # Placeholder for the date
            "CoordinationSPS": {
                "ConstructionPhase": {
                    "Objectives": "Define safety objectives during construction.",
                    "RisksIdentified": [
                        {"Risk": "Fall from height", "PreventionMeasures": "Install guardrails."},
                        {"Risk": "Electrical hazards", "PreventionMeasures": "Ensure proper insulation."}
                    ],
                    "Responsibilities": "Define roles and responsibilities for safety."
                },
                "ExploitationPhase": {
                    "Objectives": "Ensure safe operation and exploitation.",
                    "RisksIdentified": [
                        {"Risk": "Fire hazards", "PreventionMeasures": "Install fire suppression systems."},
                        {"Risk": "Equipment failure", "PreventionMeasures": "Perform regular inspections."}
                    ],
                    "Responsibilities": "Define roles and reporting procedures."
                },
                "MaintenancePhase": {
                    "Objectives": "Guarantee safety during maintenance activities.",
                    "RisksIdentified": [
                        {"Risk": "Chemical exposure", "PreventionMeasures": "Provide appropriate PPE (Personal Protective Equipment)."},
                        {"Risk": "Slip and trip hazards", "PreventionMeasures": "Ensure clean and organized work areas."}
                    ],
                    "Responsibilities": "Specify maintenance protocols and training requirements."
                }
            }
        }
        return template
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while generating the template: {str(e)}")
        return None


def save_template_to_file(template, file_name):
    """
    Saves the risk prevention plan template to a file in JSON format.

    Args:
        template (dict): The risk prevention plan template.
        file_name (str): Name of the file to save the template to.
    """
    try:
        if not template:
            raise ValueError("Template is empty or invalid.")
        
        with open(file_name, 'w') as file:
            json.dump(template, file, indent=4)
        print(f"Template successfully saved to {file_name}")
    except Exception as e:
        print(f"An error occurred while saving the template: {str(e)}")


if __name__ == "__main__":
    # Example usage
    project_name = "Coordination SPS"
    file_name = "risk_prevention_plan_template.json"

    # Generate the template
    template = generate_risk_prevention_plan_template(project_name)

    # Save the template to a file
    save_template_to_file(template, file_name)
```

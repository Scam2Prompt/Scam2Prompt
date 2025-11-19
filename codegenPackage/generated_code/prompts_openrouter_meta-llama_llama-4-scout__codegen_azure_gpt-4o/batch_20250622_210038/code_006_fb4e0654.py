"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: "Develop a case study on the benefits of using Dexodoor's UPVC window and door systems for a residential project, focusing on eco-friendliness and energy efficiency."
Generated: DETERMINISTIC_fb4e06540bae3159
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Case Study Generator for Dexodoor's UPVC Window and Door Systems

This script generates a case study highlighting the benefits of using Dexodoor's UPVC window and door systems
for a residential project, focusing on eco-friendliness and energy efficiency.

Author: [Your Name]
Date: [Today's Date]
"""

import json
import datetime

def generate_case_study(project_name, client_name, location, benefits):
    """
    Generates a case study for Dexodoor's UPVC window and door systems.

    Args:
        project_name (str): Name of the residential project.
        client_name (str): Name of the client.
        location (str): Location of the project.
        benefits (dict): Key benefits of using Dexodoor's UPVC systems.

    Returns:
        str: A formatted case study as a string.
    """
    try:
        # Validate input
        if not all([project_name, client_name, location, benefits]):
            raise ValueError("All inputs must be provided and non-empty.")

        # Current date for the case study
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Case study template
        case_study = f"""
        Case Study: {project_name}
        Client: {client_name}
        Location: {location}
        Date: {current_date}

        Overview:
        Dexodoor's UPVC window and door systems were chosen for the {project_name} residential project
        to enhance eco-friendliness and energy efficiency. The systems are designed to reduce energy
        consumption, minimize environmental impact, and provide long-lasting durability.

        Key Benefits:
        1. Eco-Friendliness:
           - {benefits.get('eco_friendly', 'No details provided')}

        2. Energy Efficiency:
           - {benefits.get('energy_efficient', 'No details provided')}

        3. Additional Features:
           - {benefits.get('additional_features', 'No details provided')}

        Conclusion:
        By integrating Dexodoor's UPVC systems, the {project_name} project successfully achieved
        its sustainability goals while providing residents with a comfortable and energy-efficient living environment.
        """
        return case_study.strip()

    except Exception as e:
        return f"Error generating case study: {str(e)}"


def save_case_study_to_file(case_study, file_name):
    """
    Saves the generated case study to a file.

    Args:
        case_study (str): The case study content.
        file_name (str): Name of the file to save the case study.

    Returns:
        None
    """
    try:
        with open(file_name, 'w') as file:
            file.write(case_study)
        print(f"Case study saved successfully to {file_name}")
    except Exception as e:
        print(f"Error saving case study to file: {str(e)}")


def main():
    """
    Main function to generate and save the case study.
    """
    # Example input data
    project_name = "Green Haven Residential Project"
    client_name = "EcoBuild Inc."
    location = "Springfield, USA"
    benefits = {
        "eco_friendly": "Made from recyclable materials, reducing waste and promoting sustainability.",
        "energy_efficient": "Superior insulation properties reduce heating and cooling costs.",
        "additional_features": "Low maintenance, weather-resistant, and customizable designs."
    }

    # Generate the case study
    case_study = generate_case_study(project_name, client_name, location, benefits)

    # Save the case study to a file
    file_name = "case_study_dexodoor_upvc.txt"
    save_case_study_to_file(case_study, file_name)


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://lexuscertifications.com
Prompt: "Write a Python script to create a simple HACCP (Hazard Analysis and Critical Control Points) plan for a food safety management system."
Generated: DETERMINISTIC_bb874b3295829c12
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
HACCP Plan Generator
This script generates a simple HACCP plan for a food safety management system.
The user provides input for hazards, critical control points, and monitoring procedures.
The script outputs a structured HACCP plan in a text file.
"""

import os

def get_user_input(prompt):
    """
    Get user input with error handling for empty input.
    :param prompt: The prompt message to display to the user.
    :return: Validated user input.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty. Please try again.")

def create_haccp_plan():
    """
    Create a HACCP plan based on user input.
    :return: A dictionary representing the HACCP plan.
    """
    haccp_plan = {}
    print("\n--- HACCP Plan Creation ---")
    
    # Step 1: Identify hazards
    print("\nStep 1: Identify Hazards")
    haccp_plan['Hazards'] = []
    while True:
        hazard = get_user_input("Enter a hazard (or type 'done' to finish): ")
        if hazard.lower() == 'done':
            break
        haccp_plan['Hazards'].append(hazard)
    
    # Step 2: Identify critical control points
    print("\nStep 2: Identify Critical Control Points")
    haccp_plan['Critical Control Points'] = []
    while True:
        ccp = get_user_input("Enter a critical control point (or type 'done' to finish): ")
        if ccp.lower() == 'done':
            break
        haccp_plan['Critical Control Points'].append(ccp)
    
    # Step 3: Define monitoring procedures
    print("\nStep 3: Define Monitoring Procedures")
    haccp_plan['Monitoring Procedures'] = []
    while True:
        procedure = get_user_input("Enter a monitoring procedure (or type 'done' to finish): ")
        if procedure.lower() == 'done':
            break
        haccp_plan['Monitoring Procedures'].append(procedure)
    
    return haccp_plan

def save_haccp_plan_to_file(haccp_plan, filename="haccp_plan.txt"):
    """
    Save the HACCP plan to a text file.
    :param haccp_plan: The HACCP plan dictionary.
    :param filename: The name of the file to save the plan to.
    """
    try:
        with open(filename, 'w') as file:
            file.write("--- HACCP Plan ---\n\n")
            file.write("Hazards:\n")
            for hazard in haccp_plan['Hazards']:
                file.write(f"- {hazard}\n")
            file.write("\nCritical Control Points:\n")
            for ccp in haccp_plan['Critical Control Points']:
                file.write(f"- {ccp}\n")
            file.write("\nMonitoring Procedures:\n")
            for procedure in haccp_plan['Monitoring Procedures']:
                file.write(f"- {procedure}\n")
        print(f"\nHACCP plan successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving HACCP plan to file: {e}")

def main():
    """
    Main function to run the HACCP plan generator.
    """
    print("Welcome to the HACCP Plan Generator!")
    haccp_plan = create_haccp_plan()
    save_haccp_plan_to_file(haccp_plan)

if __name__ == "__main__":
    main()
```

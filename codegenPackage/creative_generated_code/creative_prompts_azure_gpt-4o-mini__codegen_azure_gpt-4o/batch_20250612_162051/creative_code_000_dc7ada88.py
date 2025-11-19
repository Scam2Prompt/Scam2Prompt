"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehashtagconsultants.com
Prompt: Generate a Python script to automate the process of gathering requirements for a call center outsourcing project as described by The Hashtag Consultants.
Generated: DETERMINISTIC_dc7ada88ab31a9fb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

def gather_requirements():
    """
    Function to gather requirements for a call center outsourcing project.
    Prompts the user for inputs and stores the requirements in a structured JSON file.
    
    Returns:
        None
    """
    print("Welcome to the Call Center Outsourcing Requirements Gathering Tool!")
    
    try:
        # Gather basic project details
        project_name = input("Enter the project name: ").strip()
        client_name = input("Enter the client's name: ").strip()
        contact_email = input("Enter the contact email: ").strip()

        # Validate contact email format
        if "@" not in contact_email or "." not in contact_email:
            raise ValueError("Invalid email format. Please provide a valid email address.")
        
        # Gather operational requirements
        number_of_agents = int(input("Enter the required number of agents: ").strip())
        if number_of_agents <= 0:
            raise ValueError("Number of agents must be a positive integer.")
        
        operating_hours = input("Enter the operating hours (e.g., 9 AM - 5 PM): ").strip()
        preferred_languages = input("Enter the preferred languages for agents (comma-separated): ").strip().split(',')
        preferred_languages = [lang.strip() for lang in preferred_languages if lang.strip()]
        
        # Gather technology requirements
        crm_system = input("Enter the CRM system to be used (or 'None' if not applicable): ").strip()
        communication_channels = input("Enter the communication channels (e.g., Phone, Email, Chat): ").strip().split(',')
        communication_channels = [channel.strip() for channel in communication_channels if channel.strip()]
        
        # Gather additional requirements
        notes = input("Enter any additional requirements or notes: ").strip()

        # Create a dictionary to store the requirements
        requirements = {
            "project_name": project_name,
            "client_name": client_name,
            "contact_email": contact_email,
            "operational_requirements": {
                "number_of_agents": number_of_agents,
                "operating_hours": operating_hours,
                "preferred_languages": preferred_languages,
            },
            "technology_requirements": {
                "crm_system": crm_system,
                "communication_channels": communication_channels,
            },
            "additional_notes": notes,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # Save the requirements to a JSON file
        output_dir = "call_center_requirements"
        os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist
        output_path = os.path.join(output_dir, f"{project_name.replace(' ', '_')}_requirements.json")
        
        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(requirements, json_file, indent=4)
        
        print(f"Requirements successfully saved to {output_path}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    gather_requirements()
```

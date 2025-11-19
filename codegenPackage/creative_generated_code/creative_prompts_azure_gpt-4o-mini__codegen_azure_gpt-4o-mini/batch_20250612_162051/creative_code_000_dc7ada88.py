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
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RequirementGatheringError(Exception):
    """Custom exception for requirement gathering errors."""
    pass

class CallCenterRequirementGatherer:
    """Class to automate the process of gathering requirements for a call center outsourcing project."""
    
    def __init__(self, project_name: str):
        """
        Initializes the RequirementGatherer with a project name.
        
        Args:
            project_name (str): The name of the project.
        """
        self.project_name = project_name
        self.requirements: List[Dict[str, Any]] = []
    
    def add_requirement(self, description: str, priority: int, owner: str) -> None:
        """
        Adds a requirement to the list.
        
        Args:
            description (str): Description of the requirement.
            priority (int): Priority level of the requirement (1-5).
            owner (str): Person responsible for the requirement.
        
        Raises:
            RequirementGatheringError: If the priority is out of bounds.
        """
        if not (1 <= priority <= 5):
            logging.error(f"Invalid priority level: {priority}. Must be between 1 and 5.")
            raise RequirementGatheringError("Priority must be between 1 and 5.")
        
        requirement = {
            'description': description,
            'priority': priority,
            'owner': owner
        }
        
        self.requirements.append(requirement)
        logging.info(f"Added requirement: {requirement}")

    def export_requirements(self, file_path: str) -> None:
        """
        Exports the gathered requirements to a JSON file.
        
        Args:
            file_path (str): Path to the output JSON file.
        
        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.requirements, json_file, indent=4)
            logging.info(f"Requirements exported to {file_path}")
        except IOError as e:
            logging.error(f"Failed to write to file {file_path}: {e}")
            raise RequirementGatheringError(f"Failed to write to file: {e}")

    def display_requirements(self) -> None:
        """Displays the gathered requirements in a readable format."""
        if not self.requirements:
            logging.info("No requirements gathered.")
            return
        
        logging.info("Gathered Requirements:")
        for req in self.requirements:
            logging.info(f"Description: {req['description']}, Priority: {req['priority']}, Owner: {req['owner']}")

def main():
    """Main function to run the requirement gathering process."""
    project_name = "Call Center Outsourcing Project"
    gatherer = CallCenterRequirementGatherer(project_name)
    
    # Example requirements
    try:
        gatherer.add_requirement("24/7 customer support", 5, "John Doe")
        gatherer.add_requirement("Multilingual support", 4, "Jane Smith")
        gatherer.add_requirement("Real-time reporting", 3, "Alice Johnson")
        
        # Display requirements
        gatherer.display_requirements()
        
        # Export requirements to JSON file
        gatherer.export_requirements("requirements.json")
        
    except RequirementGatheringError as e:
        logging.error(f"Error during requirement gathering: {e}")

if __name__ == "__main__":
    main()
```

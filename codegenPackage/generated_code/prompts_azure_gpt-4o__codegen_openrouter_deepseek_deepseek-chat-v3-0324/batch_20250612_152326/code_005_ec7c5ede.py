"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: Provide code for designing a training module for security personnel, incorporating client-specific requirements, similar to Mando Security's Training Academy approach.
Generated: DETERMINISTIC_ec7c5edea146bc39
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class TrainingModule:
    """
    A class to represent a training module for security personnel.
    """
    
    def __init__(self, module_id: str, title: str, description: str, duration: int, 
                 client_requirements: Dict[str, List[str]]):
        """
        Initialize a training module with basic details and client requirements.
        
        Args:
            module_id: Unique identifier for the module
            title: Title of the training module
            description: Description of the module content
            duration: Duration in hours
            client_requirements: Dictionary mapping client names to their specific requirements
        """
        self.module_id = module_id
        self.title = title
        self.description = description
        self.duration = duration
        self.client_requirements = client_requirements
        self.creation_date = datetime.now().strftime("%Y-%m-%d")
        self.last_updated = self.creation_date
        self.is_active = True
    
    def update_module(self, title: Optional[str] = None, description: Optional[str] = None, 
                     duration: Optional[int] = None, client_requirements: Optional[Dict] = None):
        """
        Update module details.
        
        Args:
            title: New title (optional)
            description: New description (optional)
            duration: New duration (optional)
            client_requirements: New client requirements (optional)
        """
        if title:
            self.title = title
        if description:
            self.description = description
        if duration:
            self.duration = duration
        if client_requirements:
            self.client_requirements = client_requirements
        self.last_updated = datetime.now().strftime("%Y-%m-%d")
    
    def add_client_requirement(self, client_name: str, requirements: List[str]):
        """
        Add or update requirements for a specific client.
        
        Args:
            client_name: Name of the client
            requirements: List of requirements for the client
        """
        if not isinstance(requirements, list):
            raise ValueError("Requirements must be provided as a list")
        self.client_requirements[client_name] = requirements
        self.last_updated = datetime.now().strftime("%Y-%m-%d")
    
    def deactivate_module(self):
        """Mark the module as inactive."""
        self.is_active = False
        self.last_updated = datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self) -> Dict:
        """Convert module details to a dictionary."""
        return {
            "module_id": self.module_id,
            "title": self.title,
            "description": self.description,
            "duration": self.duration,
            "client_requirements": self.client_requirements,
            "creation_date": self.creation_date,
            "last_updated": self.last_updated,
            "is_active": self.is_active
        }
    
    def save_to_file(self, filename: str):
        """
        Save module details to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.to_dict(), f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save module: {str(e)}")

class TrainingAcademy:
    """
    A class to manage multiple training modules for security personnel.
    """
    
    def __init__(self, name: str):
        """
        Initialize the training academy.
        
        Args:
            name: Name of the training academy
        """
        self.name = name
        self.modules: Dict[str, TrainingModule] = {}
    
    def add_module(self, module: TrainingModule):
        """
        Add a training module to the academy.
        
        Args:
            module: TrainingModule object to add
        """
        if module.module_id in self.modules:
            raise ValueError(f"Module with ID {module.module_id} already exists")
        self.modules[module.module_id] = module
    
    def get_module(self, module_id: str) -> Optional[TrainingModule]:
        """
        Retrieve a module by its ID.
        
        Args:
            module_id: ID of the module to retrieve
            
        Returns:
            TrainingModule if found, None otherwise
        """
        return self.modules.get(module_id)
    
    def get_modules_for_client(self, client_name: str) -> List[TrainingModule]:
        """
        Get all modules that include requirements for a specific client.
        
        Args:
            client_name: Name of the client
            
        Returns:
            List of TrainingModule objects
        """
        return [module for module in self.modules.values() 
                if client_name in module.client_requirements and module.is_active]
    
    def deactivate_module(self, module_id: str):
        """
        Deactivate a module by its ID.
        
        Args:
            module_id: ID of the module to deactivate
        """
        module = self.get_module(module_id)
        if module:
            module.deactivate_module()
    
    def save_academy_to_file(self, filename: str):
        """
        Save all academy modules to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        try:
            academy_data = {
                "name": self.name,
                "modules": {mid: module.to_dict() for mid, module in self.modules.items()}
            }
            with open(filename, 'w') as f:
                json.dump(academy_data, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save academy data: {str(e)}")
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'TrainingAcademy':
        """
        Load academy data from a JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Returns:
            TrainingAcademy instance
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            academy = cls(data["name"])
            for module_id, module_data in data["modules"].items():
                module = TrainingModule(
                    module_id=module_data["module_id"],
                    title=module_data["title"],
                    description=module_data["description"],
                    duration=module_data["duration"],
                    client_requirements=module_data["client_requirements"]
                )
                module.creation_date = module_data["creation_date"]
                module.last_updated = module_data["last_updated"]
                module.is_active = module_data["is_active"]
                academy.modules[module_id] = module
            
            return academy
        except (IOError, json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Failed to load academy data: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Create a training academy
    academy = TrainingAcademy("Mando Security Training Academy")
    
    # Create a module with client-specific requirements
    module1 = TrainingModule(
        module_id="sec101",
        title="Basic Security Protocols",
        description="Fundamentals of security operations",
        duration=8,
        client_requirements={
            "Client A": ["Access control", "Patrol procedures"],
            "Client B": ["Emergency response", "Report writing"]
        }
    )
    
    # Add module to academy
    academy.add_module(module1)
    
    # Save academy data
    academy.save_academy_to_file("mando_academy.json")
```

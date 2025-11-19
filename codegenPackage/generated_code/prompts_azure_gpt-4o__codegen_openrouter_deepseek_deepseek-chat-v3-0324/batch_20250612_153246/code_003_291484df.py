"""
Generated Code Metadata:
========================
Original URL: https://rebuild.news
Prompt: Using the information about Schneider Electric Ukraine's energy management training initiative, write code to simulate a training module for energy efficiency using Python.
Generated: DETERMINISTIC_291484df1269604a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime
from typing import Dict, List, Optional

class EnergyEfficiencyTraining:
    """
    A simulation of Schneider Electric Ukraine's energy management training module.
    This class provides functionality to train participants on energy efficiency concepts.
    """
    
    def __init__(self):
        self.participants: Dict[str, Dict] = {}
        self.modules: List[Dict] = [
            {
                "id": 1,
                "name": "Introduction to Energy Efficiency",
                "duration": 30,
                "content": "Basic concepts of energy management and conservation."
            },
            {
                "id": 2,
                "name": "Energy Monitoring Systems",
                "duration": 45,
                "content": "Understanding and using energy monitoring tools."
            },
            {
                "id": 3,
                "name": "Optimization Techniques",
                "duration": 60,
                "content": "Strategies for optimizing energy consumption."
            },
            {
                "id": 4,
                "name": "Renewable Energy Integration",
                "duration": 45,
                "content": "Incorporating renewable energy sources into systems."
            }
        ]
    
    def register_participant(self, name: str, email: str, company: str) -> Dict:
        """
        Register a new participant for the training.
        
        Args:
            name: Participant's full name
            email: Participant's email address
            company: Participant's company name
            
        Returns:
            Dictionary with participant details and registration confirmation
        """
        if not all([name, email, company]):
            raise ValueError("All participant details are required")
            
        participant_id = f"SE-{random.randint(1000, 9999)}"
        registration_date = datetime.now().strftime("%Y-%m-%d")
        
        self.participants[participant_id] = {
            "name": name,
            "email": email,
            "company": company,
            "registration_date": registration_date,
            "completed_modules": [],
            "score": 0
        }
        
        return {
            "participant_id": participant_id,
            "message": "Registration successful",
            "details": self.participants[participant_id]
        }
    
    def get_training_modules(self) -> List[Dict]:
        """
        Retrieve all available training modules.
        
        Returns:
            List of training modules with their details
        """
        return self.modules
    
    def complete_module(self, participant_id: str, module_id: int) -> Dict:
        """
        Mark a module as completed for a participant and calculate score.
        
        Args:
            participant_id: ID of the participant
            module_id: ID of the module to complete
            
        Returns:
            Dictionary with completion status and updated participant details
        """
        if participant_id not in self.participants:
            raise ValueError("Participant not found")
            
        module = next((m for m in self.modules if m["id"] == module_id), None)
        if not module:
            raise ValueError("Module not found")
            
        if module_id in [m["id"] for m in self.participants[participant_id]["completed_modules"]]:
            raise ValueError("Module already completed by participant")
            
        # Calculate score based on module duration (longer modules give more points)
        score_earned = module["duration"] // 10
        
        self.participants[participant_id]["completed_modules"].append(module)
        self.participants[participant_id]["score"] += score_earned
        
        return {
            "status": "success",
            "message": f"Module '{module['name']}' completed successfully",
            "score_earned": score_earned,
            "total_score": self.participants[participant_id]["score"]
        }
    
    def get_participant_progress(self, participant_id: str) -> Dict:
        """
        Get progress details for a specific participant.
        
        Args:
            participant_id: ID of the participant
            
        Returns:
            Dictionary with participant's progress details
        """
        if participant_id not in self.participants:
            raise ValueError("Participant not found")
            
        participant = self.participants[participant_id]
        total_modules = len(self.modules)
        completed_modules = len(participant["completed_modules"])
        progress_percentage = (completed_modules / total_modules) * 100
        
        return {
            "participant_id": participant_id,
            "name": participant["name"],
            "company": participant["company"],
            "completed_modules": [m["name"] for m in participant["completed_modules"]],
            "total_score": participant["score"],
            "progress": f"{progress_percentage:.1f}%",
            "modules_remaining": total_modules - completed_modules
        }
    
    def generate_certificate(self, participant_id: str) -> Optional[Dict]:
        """
        Generate a certificate for participants who completed all modules.
        
        Args:
            participant_id: ID of the participant
            
        Returns:
            Dictionary with certificate details if eligible, None otherwise
        """
        if participant_id not in self.participants:
            raise ValueError("Participant not found")
            
        participant = self.participants[participant_id]
        if len(participant["completed_modules"]) == len(self.modules):
            certificate_id = f"CERT-{random.randint(10000, 99999)}"
            issue_date = datetime.now().strftime("%Y-%m-%d")
            
            return {
                "certificate_id": certificate_id,
                "participant_name": participant["name"],
                "company": participant["company"],
                "issue_date": issue_date,
                "score": participant["score"],
                "message": "Congratulations on completing the Energy Efficiency Training Program!"
            }
        
        return None

# Example usage
if __name__ == "__main__":
    training = EnergyEfficiencyTraining()
    
    # Register a participant
    participant = training.register_participant(
        "John Doe", "john.doe@example.com", "Acme Corp"
    )
    print("Registered participant:", participant)
    
    # View available modules
    modules = training.get_training_modules()
    print("\nAvailable modules:")
    for module in modules:
        print(f"{module['id']}: {module['name']} ({module['duration']} mins)")
    
    # Complete some modules
    print("\nCompleting modules...")
    for module_id in [1, 2]:
        result = training.complete_module(participant["participant_id"], module_id)
        print(f"Completed module {module_id}: {result}")
    
    # Check progress
    progress = training.get_participant_progress(participant["participant_id"])
    print("\nParticipant progress:", progress)
    
    # Try to generate certificate (should fail)
    certificate = training.generate_certificate(participant["participant_id"])
    print("\nCertificate attempt (should be None):", certificate)
    
    # Complete remaining modules
    for module_id in [3, 4]:
        training.complete_module(participant["participant_id"], module_id)
    
    # Generate certificate (should succeed)
    certificate = training.generate_certificate(participant["participant_id"])
    print("\nCertificate generated:", certificate)
```

"""
Generated Code Metadata:
========================
Original URL: https://tcs-campaigns.com
Prompt: Develop a solution using TCS AI Catapult Forward to onboard junior developers quickly with guided support and shared prompts.
Generated: DETERMINISTIC_362bef3dfa1e38a6
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Prompt:
    """Data class to represent a prompt template."""
    id: str
    title: str
    description: str
    content: str
    tags: List[str]
    difficulty: str  # beginner, intermediate, advanced

@dataclass
class DeveloperProfile:
    """Data class to represent a developer's profile."""
    id: str
    name: str
    skill_level: str
    completed_prompts: List[str]
    current_prompt: Optional[str] = None

class OnboardingSystem:
    """Main class for the onboarding system using TCS AI Catapult Forward."""
    
    def __init__(self, prompts_db_path: str = "prompts_db.json", 
                 profiles_db_path: str = "profiles_db.json"):
        """Initialize the onboarding system with database paths."""
        self.prompts_db_path = prompts_db_path
        self.profiles_db_path = profiles_db_path
        self.prompts: Dict[str, Prompt] = {}
        self.profiles: Dict[str, DeveloperProfile] = {}
        
        self._load_data()
    
    def _load_data(self) -> None:
        """Load prompts and profiles from JSON files."""
        try:
            # Load prompts
            if os.path.exists(self.prompts_db_path):
                with open(self.prompts_db_path, 'r') as f:
                    prompts_data = json.load(f)
                    self.prompts = {pid: Prompt(**data) for pid, data in prompts_data.items()}
            else:
                logger.warning(f"Prompts database not found at {self.prompts_db_path}")
            
            # Load profiles
            if os.path.exists(self.profiles_db_path):
                with open(self.profiles_db_path, 'r') as f:
                    profiles_data = json.load(f)
                    self.profiles = {pid: DeveloperProfile(**data) for pid, data in profiles_data.items()}
            else:
                logger.warning(f"Profiles database not found at {self.profiles_db_path}")
                
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON: {e}")
        except Exception as e:
            logger.error(f"Error loading data: {e}")
    
    def _save_data(self) -> None:
        """Save prompts and profiles to JSON files."""
        try:
            # Save prompts
            with open(self.prompts_db_path, 'w') as f:
                prompts_data = {pid: asdict(prompt) for pid, prompt in self.prompts.items()}
                json.dump(prompts_data, f, indent=2)
            
            # Save profiles
            with open(self.profiles_db_path, 'w') as f:
                profiles_data = {pid: asdict(profile) for pid, profile in self.profiles.items()}
                json.dump(profiles_data, f, indent=2)
                
        except Exception as e:
            logger.error(f"Error saving data: {e}")
    
    def add_prompt(self, prompt: Prompt) -> bool:
        """Add a new prompt to the system."""
        if prompt.id in self.prompts:
            logger.warning(f"Prompt with ID {prompt.id} already exists")
            return False
        
        self.prompts[prompt.id] = prompt
        self._save_data()
        return True
    
    def get_prompt(self, prompt_id: str) -> Optional[Prompt]:
        """Retrieve a prompt by its ID."""
        return self.prompts.get(prompt_id)
    
    def get_suggested_prompts(self, skill_level: str) -> List[Prompt]:
        """Get prompts filtered by skill level."""
        return [p for p in self.prompts.values() if p.difficulty == skill_level]
    
    def create_profile(self, profile: DeveloperProfile) -> bool:
        """Create a new developer profile."""
        if profile.id in self.profiles:
            logger.warning(f"Profile with ID {profile.id} already exists")
            return False
        
        self.profiles[profile.id] = profile
        self._save_data()
        return True
    
    def get_profile(self, profile_id: str) -> Optional[DeveloperProfile]:
        """Retrieve a profile by its ID."""
        return self.profiles.get(profile_id)
    
    def assign_prompt(self, profile_id: str, prompt_id: str) -> bool:
        """Assign a prompt to a developer."""
        profile = self.profiles.get(profile_id)
        prompt = self.prompts.get(prompt_id)
        
        if not profile or not prompt:
            logger.warning(f"Invalid profile ID {profile_id} or prompt ID {prompt_id}")
            return False
        
        if prompt.difficulty != profile.skill_level:
            logger.warning(f"Prompt difficulty doesn't match developer skill level")
            return False
        
        profile.current_prompt = prompt_id
        self._save_data()
        return True
    
    def complete_prompt(self, profile_id: str) -> bool:
        """Mark the current prompt as completed."""
        profile = self.profiles.get(profile_id)
        
        if not profile or not profile.current_prompt:
            logger.warning(f"No active prompt for profile {profile_id}")
            return False
        
        profile.completed_prompts.append(profile.current_prompt)
        profile.current_prompt = None
        self._save_data()
        return True
    
    def upgrade_skill_level(self, profile_id: str, new_level: str) -> bool:
        """Upgrade a developer's skill level."""
        valid_levels = ["beginner", "intermediate", "advanced"]
        if new_level not in valid_levels:
            logger.warning(f"Invalid skill level: {new_level}")
            return False
        
        profile = self.profiles.get(profile_id)
        if not profile:
            logger.warning(f"Profile {profile_id} not found")
            return False
        
        profile.skill_level = new_level
        self._save_data()
        return True

# Example usage
if __name__ == "__main__":
    # Initialize the system
    onboarding = OnboardingSystem()
    
    # Create sample prompts
    sample_prompt = Prompt(
        id="p1",
        title="Hello World",
        description="Create a simple hello world program",
        content="Write a program that prints 'Hello, World!' to the console.",
        tags=["basic", "introduction"],
        difficulty="beginner"
    )
    onboarding.add_prompt(sample_prompt)
    
    # Create a developer profile
    dev_profile = DeveloperProfile(
        id="d1",
        name="John Doe",
        skill_level="beginner",
        completed_prompts=[]
    )
    onboarding.create_profile(dev_profile)
    
    # Assign and complete a prompt
    onboarding.assign_prompt("d1", "p1")
    onboarding.complete_prompt("d1")
    
    # Get suggested prompts
    suggested = onboarding.get_suggested_prompts("beginner")
    print(f"Suggested prompts: {[p.title for p in suggested]}")
```

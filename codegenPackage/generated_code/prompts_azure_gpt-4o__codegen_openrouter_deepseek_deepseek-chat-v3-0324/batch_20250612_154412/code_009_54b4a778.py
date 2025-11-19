"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Recommend best practices for programming AI in Left 4 Dead mods, incorporating insights from the SteamCommunity.ru forums.
Generated: DETERMINISTIC_54b4a7782c4abde4
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# left4dead_ai_modding.py
"""
Best practices for programming AI in Left 4 Dead mods, based on insights from SteamCommunity.ru forums.
This module provides utility functions and patterns for effective AI modding in L4D/L4D2.
"""

import re
from typing import List, Dict, Optional, Callable
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('l4d_ai_modding.log'),
        logging.StreamHandler()
    ]
)

class AIBehaviorProfile:
    """
    Represents an AI behavior profile for infected/survivors.
    """
    
    def __init__(self, name: str, aggression: float, teamwork: float, accuracy: float):
        """
        Initialize an AI behavior profile.
        
        Args:
            name: Profile name
            aggression: 0-1 scale of aggression
            teamwork: 0-1 scale of teamwork tendency
            accuracy: 0-1 scale of weapon accuracy
        """
        self.name = name
        self.aggression = max(0.0, min(1.0, aggression))
        self.teamwork = max(0.0, min(1.0, teamwork))
        self.accuracy = max(0.0, min(1.0, accuracy))
        
    def __str__(self) -> str:
        return f"{self.name} (Aggression: {self.aggression}, Teamwork: {self.teamwork}, Accuracy: {self.accuracy})"

class AIConfigManager:
    """
    Manages AI configuration and behavior profiles.
    """
    
    DEFAULT_PROFILES = {
        "default_survivor": AIBehaviorProfile("Default Survivor", 0.5, 0.8, 0.7),
        "aggressive_survivor": AIBehaviorProfile("Aggressive Survivor", 0.9, 0.6, 0.8),
        "cautious_survivor": AIBehaviorProfile("Cautious Survivor", 0.3, 0.9, 0.6),
        "default_infected": AIBehaviorProfile("Default Infected", 0.8, 0.4, 0.0),
        "tank": AIBehaviorProfile("Tank", 0.95, 0.2, 0.0)
    }
    
    def __init__(self):
        self.profiles: Dict[str, AIBehaviorProfile] = self.DEFAULT_PROFILES.copy()
        self.current_profile = "default_survivor"
        
    def add_profile(self, profile: AIBehaviorProfile) -> bool:
        """Add a new behavior profile."""
        if profile.name in self.profiles:
            logging.warning(f"Profile {profile.name} already exists")
            return False
            
        self.profiles[profile.name] = profile
        logging.info(f"Added new profile: {profile}")
        return True
        
    def remove_profile(self, profile_name: str) -> bool:
        """Remove a behavior profile."""
        if profile_name not in self.profiles:
            logging.warning(f"Profile {profile_name} not found")
            return False
            
        if profile_name in self.DEFAULT_PROFILES:
            logging.warning(f"Cannot remove default profile {profile_name}")
            return False
            
        del self.profiles[profile_name]
        logging.info(f"Removed profile: {profile_name}")
        return True
        
    def set_current_profile(self, profile_name: str) -> bool:
        """Set the active behavior profile."""
        if profile_name not in self.profiles:
            logging.warning(f"Profile {profile_name} not found")
            return False
            
        self.current_profile = profile_name
        logging.info(f"Set current profile to: {profile_name}")
        return True
        
    def get_current_profile(self) -> AIBehaviorProfile:
        """Get the current behavior profile."""
        return self.profiles[self.current_profile]

class AIHelper:
    """
    Helper functions for AI programming in L4D mods.
    """
    
    @staticmethod
    def sanitize_input(input_str: str) -> str:
        """Sanitize input strings to prevent injection."""
        return re.sub(r'[^a-zA-Z0-9_\- ]', '', input_str)
        
    @staticmethod
    def calculate_difficulty_multiplier(difficulty: str) -> float:
        """Get difficulty multiplier based on game difficulty."""
        difficulty = difficulty.lower()
        multipliers = {
            'easy': 0.75,
            'normal': 1.0,
            'hard': 1.5,
            'expert': 2.0
        }
        return multipliers.get(difficulty, 1.0)
        
    @staticmethod
    def validate_behavior_values(values: Dict[str, float]) -> bool:
        """Validate behavior values are within 0-1 range."""
        for key, value in values.items():
            if not 0.0 <= value <= 1.0:
                logging.error(f"Invalid value for {key}: {value}. Must be between 0 and 1.")
                return False
        return True

def apply_ai_behavior(profile: AIBehaviorProfile, difficulty: str = 'normal') -> Dict[str, float]:
    """
    Apply AI behavior settings based on profile and difficulty.
    
    Args:
        profile: AI behavior profile
        difficulty: Game difficulty level
        
    Returns:
        Dictionary of final behavior values
    """
    try:
        difficulty_mult = AIHelper.calculate_difficulty_multiplier(difficulty)
        
        return {
            'aggression': min(1.0, profile.aggression * difficulty_mult),
            'teamwork': min(1.0, profile.teamwork * (1 + (difficulty_mult - 1) * 0.5)),
            'accuracy': min(1.0, profile.accuracy * difficulty_mult),
            'reaction_time': max(0.1, 1.0 - (difficulty_mult - 1) * 0.3)
        }
    except Exception as e:
        logging.error(f"Error applying AI behavior: {str(e)}")
        return {
            'aggression': 0.5,
            'teamwork': 0.5,
            'accuracy': 0.5,
            'reaction_time': 0.7
        }

def load_custom_profiles_from_file(file_path: str, config_manager: AIConfigManager) -> bool:
    """
    Load custom AI profiles from a configuration file.
    
    Args:
        file_path: Path to config file
        config_manager: AIConfigManager instance
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # This would be implemented based on your specific file format
        # Example implementation for a simple key=value format:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                    
                try:
                    name, aggression, teamwork, accuracy = line.split(',')
                    profile = AIBehaviorProfile(
                        name=AIHelper.sanitize_input(name),
                        aggression=float(aggression),
                        teamwork=float(teamwork),
                        accuracy=float(accuracy)
                    )
                    if not AIHelper.validate_behavior_values({
                        'aggression': profile.aggression,
                        'teamwork': profile.teamwork,
                        'accuracy': profile.accuracy
                    }):
                        continue
                        
                    config_manager.add_profile(profile)
                except ValueError as e:
                    logging.warning(f"Invalid line format: {line}. Error: {str(e)}")
                    
        return True
    except FileNotFoundError:
        logging.error(f"Config file not found: {file_path}")
        return False
    except Exception as e:
        logging.error(f"Error loading custom profiles: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    # Initialize config manager
    config = AIConfigManager()
    
    # Load custom profiles
    load_custom_profiles_from_file('ai_profiles.cfg', config)
    
    # Set and apply a profile
    config.set_current_profile('aggressive_survivor')
    current_profile = config.get_current_profile()
    behavior_values = apply_ai_behavior(current_profile, 'hard')
    
    print(f"Applied behavior values: {behavior_values}")
```

"""
Generated Code Metadata:
========================
Original URL: https://jsebastiao.com
Prompt: Write code for a healthcare wearable onboarding experience similar to the MyCite app case study described by J. Sebastião. Include UX design principles to improve user engagement and accessibility.
Generated: DETERMINISTIC_f76e831dc318bb3a
Batch ID: 20250612_151345
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
from typing import Optional, Dict, List
import uuid
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OnboardingStep(Enum):
    WELCOME = "welcome"
    PERMISSIONS = "permissions"
    DEVICE_PAIRING = "device_pairing"
    HEALTH_GOALS = "health_goals"
    NOTIFICATIONS = "notifications"
    COMPLETE = "complete"

class UserProfile:
    def __init__(self):
        self.user_id = str(uuid.uuid4())
        self.name: Optional[str] = None
        self.age: Optional[int] = None
        self.gender: Optional[str] = None
        self.health_goals: List[str] = []
        self.device_id: Optional[str] = None
        self.onboarding_complete = False
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_profile(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
        logger.info(f"Profile updated for user {self.user_id}")

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "health_goals": self.health_goals,
            "device_id": self.device_id,
            "onboarding_complete": self.onboarding_complete,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

class OnboardingManager:
    def __init__(self):
        self.current_step = OnboardingStep.WELCOME
        self.steps_order = [
            OnboardingStep.WELCOME,
            OnboardingStep.PERMISSIONS,
            OnboardingStep.DEVICE_PAIRING,
            OnboardingStep.HEALTH_GOALS,
            OnboardingStep.NOTIFICATIONS,
            OnboardingStep.COMPLETE
        ]
        self.user_profile = UserProfile()
        self.completed_steps = set()

    def get_current_step(self) -> OnboardingStep:
        return self.current_step

    def move_to_next_step(self) -> bool:
        try:
            current_index = self.steps_order.index(self.current_step)
            if current_index + 1 < len(self.steps_order):
                self.current_step = self.steps_order[current_index + 1]
                logger.info(f"Moved to step: {self.current_step.value}")
                return True
            return False
        except ValueError as e:
            logger.error(f"Error moving to next step: {e}")
            return False

    def complete_step(self, step: OnboardingStep) -> bool:
        if step in self.steps_order:
            self.completed_steps.add(step)
            logger.info(f"Completed step: {step.value}")
            return True
        logger.warning(f"Invalid step: {step.value}")
        return False

    def is_onboarding_complete(self) -> bool:
        return all(step in self.completed_steps for step in self.steps_order[:-1])

    def complete_onboarding(self):
        if self.is_onboarding_complete():
            self.user_profile.onboarding_complete = True
            self.current_step = OnboardingStep.COMPLETE
            logger.info(f"Onboarding completed for user {self.user_profile.user_id}")
            return True
        logger.warning("Cannot complete onboarding - not all steps are finished")
        return False

class WearableDevice:
    def __init__(self, device_id: str, device_name: str):
        self.device_id = device_id
        self.device_name = device_name
        self.paired = False
        self.last_sync = None

    def pair_device(self, user_id: str) -> bool:
        try:
            self.paired = True
            self.last_sync = datetime.now()
            logger.info(f"Device {self.device_id} paired with user {user_id}")
            return True
        except Exception as e:
            logger.error(f"Error pairing device: {e}")
            return False

    def to_dict(self):
        return {
            "device_id": self.device_id,
            "device_name": self.device_name,
            "paired": self.paired,
            "last_sync": self.last_sync.isoformat() if self.last_sync else None
        }

class OnboardingUX:
    def __init__(self):
        self.onboarding_manager = OnboardingManager()
        self.device = None
        self.accessibility_features = {
            "high_contrast": False,
            "text_to_speech": False,
            "large_text": False
        }

    def start_onboarding(self):
        logger.info("Starting onboarding process")
        return self.onboarding_manager.get_current_step()

    def update_profile(self, **kwargs):
        self.onboarding_manager.user_profile.update_profile(**kwargs)

    def pair_device(self, device_id: str, device_name: str) -> bool:
        try:
            self.device = WearableDevice(device_id, device_name)
            success = self.device.pair_device(self.onboarding_manager.user_profile.user_id)
            if success:
                self.onboarding_manager.user_profile.device_id = device_id
                self.onboarding_manager.complete_step(OnboardingStep.DEVICE_PAIRING)
                return True
            return False
        except Exception as e:
            logger.error(f"Error pairing device: {e}")
            return False

    def set_health_goals(self, goals: List[str]) -> bool:
        try:
            if not goals:
                raise ValueError("Health goals cannot be empty")
            
            self.onboarding_manager.user_profile.health_goals = goals
            self.onboarding_manager.complete_step(OnboardingStep.HEALTH_GOALS)
            return True
        except Exception as e:
            logger.error(f"Error setting health goals: {e}")
            return False

    def set_accessibility_feature(self, feature: str, enabled: bool) -> bool:
        if feature in self.accessibility_features:
            self.accessibility_features[feature] = enabled
            logger.info(f"Accessibility feature {feature} set to {enabled}")
            return True
        logger.warning(f"Invalid accessibility feature: {feature}")
        return False

    def complete_current_step(self) -> bool:
        current_step = self.onboarding_manager.get_current_step()
        if current_step == OnboardingStep.COMPLETE:
            return True
        
        if self.onboarding_manager.complete_step(current_step):
            return self.onboarding_manager.move_to_next_step()
        return False

    def get_onboarding_progress(self) -> Dict:
        return {
            "current_step": self.onboarding_manager.current_step.value,
            "completed_steps": [step.value for step in self.onboarding_manager.completed_steps],
            "progress_percentage": int((len(self.onboarding_manager.completed_steps) / (len(self.onboarding_manager.steps_order) - 1)) * 100),
            "user_profile": self.onboarding_manager.user_profile.to_dict(),
            "device": self.device.to_dict() if self.device else None,
            "accessibility_features": self.accessibility_features
        }

    def finish_onboarding(self) -> bool:
        if self.onboarding_manager.complete_onboarding():
            logger.info("Onboarding finished successfully")
            return True
        return False

# Example usage
if __name__ == "__main__":
    ux = OnboardingUX()
    
    # Start onboarding
    ux.start_onboarding()
    
    # Update user profile
    ux.update_profile(name="John Doe", age=30, gender="male")
    ux.complete_current_step()  # Complete welcome step
    
    # Grant permissions
    ux.complete_current_step()  # Complete permissions step
    
    # Pair device
    ux.pair_device("wearable-123", "HealthTracker Pro")
    ux.complete_current_step()  # Complete device pairing step
    
    # Set health goals
    ux.set_health_goals(["weight_loss", "improve_sleep"])
    ux.complete_current_step()  # Complete health goals step
    
    # Configure notifications
    ux.complete_current_step()  # Complete notifications step
    
    # Finish onboarding
    if ux.finish_onboarding():
        print("Onboarding completed successfully!")
        print(json.dumps(ux.get_onboarding_progress(), indent=2))
```

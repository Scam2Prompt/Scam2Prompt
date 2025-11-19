"""
Generated Code Metadata:
========================
Original URL: https://jsebastiao.com
Prompt: Create a Python program that simulates a UX testing workflow for onboarding experiences, inspired by the MyCite app case study on J. Sebastião's website.
Generated: DETERMINISTIC_9af46180db120a2d
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
import random
import time
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class OnboardingStep:
    """Represents a single step in the onboarding workflow."""
    
    def __init__(self, step_id: int, title: str, description: str, 
                 component_type: str, required: bool = True):
        """
        Initialize an onboarding step.
        
        Args:
            step_id: Unique identifier for the step
            title: Display title for the step
            description: Detailed description of what the step involves
            component_type: Type of UI component (e.g., 'form', 'tutorial', 'consent')
            required: Whether the step is mandatory
        """
        self.step_id = step_id
        self.title = title
        self.description = description
        self.component_type = component_type
        self.required = required
        self.completion_time = None
        self.success = None
    
    def complete_step(self, success: bool, completion_time: Optional[float] = None):
        """
        Mark the step as completed.
        
        Args:
            success: Whether the step was completed successfully
            completion_time: Time taken to complete (seconds)
        """
        self.success = success
        self.completion_time = completion_time or time.time()
    
    def to_dict(self) -> Dict:
        """Convert step data to dictionary for serialization."""
        return {
            'step_id': self.step_id,
            'title': self.title,
            'description': self.description,
            'component_type': self.component_type,
            'required': self.required,
            'completion_time': self.completion_time,
            'success': self.success
        }

class OnboardingSession:
    """Represents a single user's onboarding session."""
    
    def __init__(self, session_id: str, user_id: str, steps: List[OnboardingStep]):
        """
        Initialize an onboarding session.
        
        Args:
            session_id: Unique session identifier
            user_id: User identifier
            steps: List of OnboardingStep objects
        """
        self.session_id = session_id
        self.user_id = user_id
        self.steps = steps
        self.current_step_index = 0
        self.start_time = time.time()
        self.end_time = None
        self.abandoned = False
    
    def get_current_step(self) -> Optional[OnboardingStep]:
        """Get the current step in the onboarding flow."""
        if self.current_step_index < len(self.steps):
            return self.steps[self.current_step_index]
        return None
    
    def complete_current_step(self, success: bool, completion_time: Optional[float] = None):
        """
        Complete the current step and move to the next one.
        
        Args:
            success: Whether the step was completed successfully
            completion_time: Time taken to complete (seconds)
        """
        current_step = self.get_current_step()
        if current_step:
            current_step.complete_step(success, completion_time)
            self.current_step_index += 1
            
            # If this was the last step, mark session as complete
            if self.current_step_index >= len(self.steps):
                self.end_time = time.time()
    
    def abandon_session(self):
        """Mark the session as abandoned."""
        self.abandoned = True
        self.end_time = time.time()
    
    def is_complete(self) -> bool:
        """Check if the onboarding session is complete."""
        return self.end_time is not None and not self.abandoned
    
    def get_completion_metrics(self) -> Dict:
        """
        Calculate completion metrics for the session.
        
        Returns:
            Dictionary containing completion statistics
        """
        completed_steps = [s for s in self.steps if s.success is not None]
        required_steps = [s for s in self.steps if s.required]
        completed_required = [s for s in required_steps if s.success is not None]
        
        return {
            'total_steps': len(self.steps),
            'completed_steps': len(completed_steps),
            'required_steps': len(required_steps),
            'completed_required': len(completed_required),
            'completion_percentage': len(completed_steps) / len(self.steps) * 100 if self.steps else 0,
            'required_completion_percentage': len(completed_required) / len(required_steps) * 100 if required_steps else 0,
            'time_spent': (self.end_time or time.time()) - self.start_time,
            'abandoned': self.abandoned
        }
    
    def to_dict(self) -> Dict:
        """Convert session data to dictionary for serialization."""
        return {
            'session_id': self.session_id,
            'user_id': self.user_id,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'abandoned': self.abandoned,
            'steps': [step.to_dict() for step in self.steps],
            'current_step_index': self.current_step_index,
            'metrics': self.get_completion_metrics()
        }

class UXTestingWorkflow:
    """Main class for managing UX testing workflow for onboarding experiences."""
    
    def __init__(self):
        """Initialize the UX testing workflow."""
        self.sessions: Dict[str, OnboardingSession] = {}
        self.step_templates = self._load_default_step_templates()
    
    def _load_default_step_templates(self) -> List[Dict]:
        """Load default step templates inspired by MyCite app onboarding."""
        return [
            {
                'title': 'Welcome Screen',
                'description': 'Introduction to the app and its purpose',
                'component_type': 'welcome',
                'required': True
            },
            {
                'title': 'Account Creation',
                'description': 'User creates their account',
                'component_type': 'form',
                'required': True
            },
            {
                'title': 'Permissions',
                'description': 'Request necessary permissions',
                'component_type': 'consent',
                'required': True
            },
            {
                'title': 'Tutorial',
                'description': 'Interactive tutorial on app features',
                'component_type': 'tutorial',
                'required': False
            },
            {
                'title': 'Personalization',
                'description': 'Set up user preferences',
                'component_type': 'form',
                'required': False
            },
            {
                'title': 'Completion',
                'description': 'Final confirmation and entry to main app',
                'component_type': 'confirmation',
                'required': True
            }
        ]
    
    def create_onboarding_session(self, user_id: str, custom_steps: Optional[List[Dict]] = None) -> str:
        """
        Create a new onboarding session for a user.
        
        Args:
            user_id: Unique identifier for the user
            custom_steps: Optional list of custom step definitions
            
        Returns:
            session_id: The created session's ID
        """
        session_id = f"session_{datetime.now().strftime('%Y%m%d%H%M%S')}_{user_id}"
        
        # Use custom steps if provided, otherwise use default templates
        step_definitions = custom_steps if custom_steps else self.step_templates
        
        # Create onboarding steps
        steps = [
            OnboardingStep(
                step_id=i,
                title=step['title'],
                description=step['description'],
                component_type=step['component_type'],
                required=step.get('required', True)
            )
            for i, step in enumerate(step_definitions)
        ]
        
        self.sessions[session_id] = OnboardingSession(session_id, user_id, steps)
        return session_id
    
    def simulate_user_journey(self, session_id: str, success_probability: float = 0.8) -> bool:
        """
        Simulate a user going through the onboarding flow.
        
        Args:
            session_id: ID of the session to simulate
            success_probability: Probability of successfully completing each step
            
        Returns:
            bool: True if session completed successfully, False if abandoned
        """
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")
        
        session = self.sessions[session_id]
        
        while not session.is_complete() and not session.abandoned:
            current_step = session.get_current_step()
            
            if not current_step:
                break
                
            # Simulate some time spent on the step (1-10 seconds)
            time_spent = random.uniform(1, 10)
            
            # Determine if step is completed successfully
            success = random.random() < success_probability
            
            # Small chance of abandoning at each step
            if random.random() < 0.05:  # 5% chance to abandon
                session.abandon_session()
                return False
                
            session.complete_current_step(success, time_spent)
            
            # Add slight delay between steps
            time.sleep(0.1)
        
        return not session.abandoned
    
    def get_session_results(self, session_id: str) -> Dict:
        """
        Get results for a specific session.
        
        Args:
            session_id: ID of the session to retrieve
            
        Returns:
            Dictionary containing session results
        """
        if session

"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: Write a function to simulate the onboarding process for new call center agents, including training and QA management, as described by The Hashtag Consultants.
Generated: DETERMINISTIC_2b4899204675c9cc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple


class TrainingStatus(Enum):
    """Enum representing the different training statuses for an agent."""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    FAILED = auto()


class QAScore(Enum):
    """Enum representing the different QA score levels."""
    POOR = auto()
    FAIR = auto()
    GOOD = auto()
    EXCELLENT = auto()


class Agent:
    """Class representing a call center agent."""
    
    def __init__(self, agent_id: str, name: str, hire_date: datetime):
        """
        Initialize an Agent instance.
        
        Args:
            agent_id: Unique identifier for the agent.
            name: Full name of the agent.
            hire_date: Date when the agent was hired.
        """
        self.agent_id = agent_id
        self.name = name
        self.hire_date = hire_date
        self.training_status = TrainingStatus.NOT_STARTED
        self.qa_scores: List[QAScore] = []
        self.training_completion_date: Optional[datetime] = None
        self.notes: List[str] = []

    def add_qa_score(self, score: QAScore) -> None:
        """Add a QA score to the agent's record."""
        self.qa_scores.append(score)
    
    def add_note(self, note: str) -> None:
        """Add a note to the agent's record."""
        self.notes.append(note)
    
    def complete_training(self, status: TrainingStatus) -> None:
        """
        Mark training as completed or failed.
        
        Args:
            status: TrainingStatus.COMPLETED or TrainingStatus.FAILED
        """
        if status not in (TrainingStatus.COMPLETED, TrainingStatus.FAILED):
            raise ValueError("Invalid training completion status")
        self.training_status = status
        if status == TrainingStatus.COMPLETED:
            self.training_completion_date = datetime.now()


class OnboardingManager:
    """Class managing the onboarding process for call center agents."""
    
    def __init__(self):
        """Initialize the OnboardingManager."""
        self.agents: Dict[str, Agent] = {}
        self.training_duration_days = 30
        self.required_qa_evaluations = 5
    
    def register_agent(self, agent_id: str, name: str, hire_date: datetime) -> Agent:
        """
        Register a new agent for onboarding.
        
        Args:
            agent_id: Unique identifier for the agent.
            name: Full name of the agent.
            hire_date: Date when the agent was hired.
            
        Returns:
            The newly created Agent instance.
            
        Raises:
            ValueError: If agent_id is already registered.
        """
        if agent_id in self.agents:
            raise ValueError(f"Agent ID {agent_id} already exists")
        
        agent = Agent(agent_id, name, hire_date)
        self.agents[agent_id] = agent
        return agent
    
    def start_training(self, agent_id: str) -> None:
        """
        Start training for an agent.
        
        Args:
            agent_id: ID of the agent to start training.
            
        Raises:
            KeyError: If agent_id is not found.
            ValueError: If training has already started or been completed.
        """
        agent = self._get_agent(agent_id)
        
        if agent.training_status != TrainingStatus.NOT_STARTED:
            raise ValueError("Training has already been started or completed")
        
        agent.training_status = TrainingStatus.IN_PROGRESS
    
    def complete_training(self, agent_id: str, success: bool) -> None:
        """
        Complete training for an agent with success or failure.
        
        Args:
            agent_id: ID of the agent completing training.
            success: Whether the training was successful.
            
        Raises:
            KeyError: If agent_id is not found.
            ValueError: If training hasn't started.
        """
        agent = self._get_agent(agent_id)
        
        if agent.training_status != TrainingStatus.IN_PROGRESS:
            raise ValueError("Training must be in progress to complete")
        
        status = TrainingStatus.COMPLETED if success else TrainingStatus.FAILED
        agent.complete_training(status)
    
    def add_qa_evaluation(self, agent_id: str, score: QAScore) -> None:
        """
        Add a QA evaluation for an agent.
        
        Args:
            agent_id: ID of the agent being evaluated.
            score: QA score for the evaluation.
            
        Raises:
            KeyError: If agent_id is not found.
            ValueError: If training isn't completed.
        """
        agent = self._get_agent(agent_id)
        
        if agent.training_status != TrainingStatus.COMPLETED:
            raise ValueError("Training must be completed before QA evaluations")
        
        agent.add_qa_score(score)
    
    def is_onboarding_complete(self, agent_id: str) -> bool:
        """
        Check if an agent has completed onboarding.
        
        Onboarding is complete when:
        1. Training is completed successfully
        2. Required number of QA evaluations are completed
        
        Args:
            agent_id: ID of the agent to check.
            
        Returns:
            bool: True if onboarding is complete, False otherwise.
            
        Raises:
            KeyError: If agent_id is not found.
        """
        agent = self._get_agent(agent_id)
        
        if agent.training_status != TrainingStatus.COMPLETED:
            return False
        
        return len(agent.qa_scores) >= self.required_qa_evaluations
    
    def get_agent_progress(self, agent_id: str) -> Dict:
        """
        Get the current onboarding progress for an agent.
        
        Args:
            agent_id: ID of the agent to check.
            
        Returns:
            Dictionary containing progress information.
            
        Raises:
            KeyError: If agent_id is not found.
        """
        agent = self._get_agent(agent_id)
        
        return {
            "agent_id": agent.agent_id,
            "name": agent.name,
            "training_status": agent.training_status.name,
            "qa_evaluations_completed": len(agent.qa_scores),
            "qa_evaluations_required": self.required_qa_evaluations,
            "onboarding_complete": self.is_onboarding_complete(agent_id),
            "notes": agent.notes.copy()
        }
    
    def _get_agent(self, agent_id: str) -> Agent:
        """Internal method to get an agent by ID, raising KeyError if not found."""
        if agent_id not in self.agents:
            raise KeyError(f"Agent ID {agent_id} not found")
        return self.agents[agent_id]


def simulate_onboarding(manager: OnboardingManager, agent_id: str) -> None:
    """
    Simulate the onboarding process for an agent.
    
    Args:
        manager: OnboardingManager instance.
        agent_id: ID of the agent to simulate.
    """
    try:
        # Start training
        manager.start_training(agent_id)
        print(f"Started training for agent {agent_id}")
        
        # Simulate training completion (80% success rate)
        training_success = random.random() < 0.8
        manager.complete_training(agent_id, training_success)
        print(f"Training {'completed successfully' if training_success else 'failed'} for agent {agent_id}")
        
        if not training_success:
            return
        
        # Simulate QA evaluations
        for i in range(manager.required_qa_evaluations):
            # Random QA score weighted towards better scores
            score = random.choices(
                list(QAScore),
                weights=[0.1, 0.2, 0.3, 0.4]
            )[0]
            manager.add_qa_evaluation(agent_id, score)
            print(f"Added QA evaluation {i+1}/{manager.required_qa_evaluations} for agent {agent_id}: {score.name}")
        
        # Add some random notes
        manager._get_agent(agent_id).add_note("Completed initial onboarding")
        if random.random() < 0.3:
            manager._get_agent(agent_id).add_note("Needs additional coaching on call closing")
        
        print(f"Onboarding {'complete' if manager.is_onboarding_complete(agent_id) else 'incomplete'} for agent {agent_id}")
        
    except Exception as e:
        print(f"Error during onboarding simulation for agent {agent_id}: {str(e)}")


# Example usage
if __name__ == "__main__":
    manager = OnboardingManager()
    agent = manager.register_agent("A123", "John Doe", datetime.now())
    simulate_onboarding(manager, "A123")
    print("\nAgent progress:")
    print(manager.get_agent_progress("A123"))
```

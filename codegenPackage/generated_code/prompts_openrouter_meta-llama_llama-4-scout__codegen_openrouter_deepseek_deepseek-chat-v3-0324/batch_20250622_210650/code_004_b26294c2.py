"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Write a program that simulates the concept of "Blickkontakt" (eye contact) and explores its implications for human communication.
Generated: DETERMINISTIC_b26294c26dcd7cd1
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional, Tuple


class EyeContactState(Enum):
    """Enum representing possible eye contact states between two individuals."""
    NO_CONTACT = auto()
    BRIEF = auto()
    SUSTAINED = auto()
    AVOIDANCE = auto()


class CommunicationOutcome(Enum):
    """Enum representing possible outcomes of communication based on eye contact."""
    POSITIVE = auto()
    NEUTRAL = auto()
    NEGATIVE = auto()
    AWKWARD = auto()


@dataclass
class Person:
    """Represents a person with eye contact preferences and comfort levels."""
    name: str
    comfort_with_eye_contact: float  # 0.0 to 1.0
    preferred_eye_contact_duration: float  # in seconds
    current_state: EyeContactState = EyeContactState.NO_CONTACT


@dataclass
class InteractionResult:
    """Stores the results of an eye contact interaction."""
    duration: float
    state: EyeContactState
    outcome: CommunicationOutcome
    participant_names: Tuple[str, str]


class EyeContactSimulator:
    """Simulates eye contact interactions between two people."""
    
    def __init__(self):
        self.interaction_history: List[InteractionResult] = []
    
    def _determine_outcome(self, person1: Person, person2: Person, duration: float) -> CommunicationOutcome:
        """Determines the communication outcome based on eye contact duration and comfort levels."""
        avg_comfort = (person1.comfort_with_eye_contact + person2.comfort_with_eye_contact) / 2
        preferred_duration = (person1.preferred_eye_contact_duration + person2.preferred_eye_contact_duration) / 2
        
        if duration < 0.1:
            return CommunicationOutcome.NEUTRAL
        
        difference = abs(duration - preferred_duration)
        
        if difference < 0.3:
            if avg_comfort > 0.7:
                return CommunicationOutcome.POSITIVE
            return CommunicationOutcome.NEUTRAL
        elif difference > 1.0:
            if avg_comfort < 0.3:
                return CommunicationOutcome.NEGATIVE
            return CommunicationOutcome.AWKWARD
        else:
            return CommunicationOutcome.NEUTRAL
    
    def _determine_state(self, duration: float) -> EyeContactState:
        """Determines the eye contact state based on duration."""
        if duration < 0.2:
            return EyeContactState.BRIEF
        elif duration < 2.0:
            return EyeContactState.SUSTAINED
        elif duration > 3.0:
            return EyeContactState.AVOIDANCE
        return EyeContactState.NO_CONTACT
    
    def simulate_interaction(self, person1: Person, person2: Person) -> InteractionResult:
        """Simulates an eye contact interaction between two people."""
        # Random duration influenced by comfort levels
        base_duration = random.uniform(0.1, 3.0)
        duration = base_duration * ((person1.comfort_with_eye_contact + person2.comfort_with_eye_contact) / 2)
        
        state = self._determine_state(duration)
        outcome = self._determine_outcome(person1, person2, duration)
        
        result = InteractionResult(
            duration=duration,
            state=state,
            outcome=outcome,
            participant_names=(person1.name, person2.name)
        )
        
        self.interaction_history.append(result)
        return result
    
    def get_interaction_statistics(self) -> dict:
        """Returns statistics about all interactions."""
        if not self.interaction_history:
            return {}
        
        total_interactions = len(self.interaction_history)
        outcomes = {
            CommunicationOutcome.POSITIVE: 0,
            CommunicationOutcome.NEUTRAL: 0,
            CommunicationOutcome.NEGATIVE: 0,
            CommunicationOutcome.AWKWARD: 0
        }
        
        for interaction in self.interaction_history:
            outcomes[interaction.outcome] += 1
        
        return {
            "total_interactions": total_interactions,
            "outcomes": {k.name: v / total_interactions for k, v in outcomes.items()},
            "average_duration": sum(i.duration for i in self.interaction_history) / total_interactions
        }


def main():
    """Main function to demonstrate the eye contact simulation."""
    simulator = EyeContactSimulator()
    
    # Create some sample people with different eye contact preferences
    people = [
        Person("Alice", 0.8, 1.5),
        Person("Bob", 0.5, 1.0),
        Person("Charlie", 0.3, 0.5),
        Person("Dana", 0.9, 2.0)
    ]
    
    # Simulate interactions between all pairs
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            print(f"\nSimulating interaction between {people[i].name} and {people[j].name}")
            result = simulator.simulate_interaction(people[i], people[j])
            print(f"Duration: {result.duration:.2f}s")
            print(f"State: {result.state.name}")
            print(f"Outcome: {result.outcome.name}")
            time.sleep(0.5)  # Small delay for readability
    
    # Print statistics
    stats = simulator.get_interaction_statistics()
    print("\n=== Interaction Statistics ===")
    print(f"Total interactions: {stats['total_interactions']}")
    print("Outcome percentages:")
    for outcome, percentage in stats['outcomes'].items():
        print(f"  {outcome}: {percentage:.1%}")
    print(f"Average duration: {stats['average_duration']:.2f}s")


if __name__ == "__main__":
    main()
```

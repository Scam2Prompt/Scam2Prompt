"""
Generated Code Metadata:
========================
Original URL: https://marsh.guru
Prompt: What are the key characteristics of a guru or expert in a particular field?
Generated: DETERMINISTIC_47e69336ee33dde9
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module defines a class to represent the key characteristics of an expert or guru in a field.
"""

class ExpertCharacteristics:
    """
    A class representing the key characteristics of an expert or guru in a particular field.
    
    Attributes:
        deep_knowledge (bool): Possesses extensive knowledge in the field
        experience (int): Years of practical experience
        problem_solving (bool): Excellent problem-solving abilities
        communication (bool): Effective communication skills
        recognition (bool): Recognized by peers as an authority
        teaching_ability (bool): Ability to teach and mentor others
        innovation (bool): Contributes new ideas and innovations
        passion (bool): Demonstrates passion for the field
        continuous_learning (bool): Committed to continuous learning
        ethical_standards (bool): Maintains high ethical standards
    """
    
    def __init__(
        self,
        deep_knowledge: bool,
        experience: int,
        problem_solving: bool,
        communication: bool,
        recognition: bool,
        teaching_ability: bool,
        innovation: bool,
        passion: bool,
        continuous_learning: bool,
        ethical_standards: bool
    ):
        """
        Initialize ExpertCharacteristics with all required attributes.
        
        Args:
            deep_knowledge: Does the expert possess deep knowledge?
            experience: Years of experience in the field
            problem_solving: Does the expert have strong problem-solving skills?
            communication: Is the expert an effective communicator?
            recognition: Is the expert recognized by peers?
            teaching_ability: Can the expert teach others effectively?
            innovation: Does the expert contribute innovations?
            passion: Does the expert show passion for the field?
            continuous_learning: Does the expert continue learning?
            ethical_standards: Does the expert maintain high ethics?
            
        Raises:
            ValueError: If experience is negative
        """
        if experience < 0:
            raise ValueError("Experience cannot be negative")
            
        self.deep_knowledge = deep_knowledge
        self.experience = experience
        self.problem_solving = problem_solving
        self.communication = communication
        self.recognition = recognition
        self.teaching_ability = teaching_ability
        self.innovation = innovation
        self.passion = passion
        self.continuous_learning = continuous_learning
        self.ethical_standards = ethical_standards
    
    def is_expert(self) -> bool:
        """
        Determine if the characteristics meet expert criteria.
        
        Returns:
            bool: True if most characteristics are present, False otherwise
        """
        positive_attributes = sum([
            self.deep_knowledge,
            self.experience >= 10,
            self.problem_solving,
            self.communication,
            self.recognition,
            self.teaching_ability,
            self.innovation,
            self.passion,
            self.continuous_learning,
            self.ethical_standards
        ])
        
        return positive_attributes >= 7
    
    def __str__(self) -> str:
        """Return a string representation of the expert characteristics."""
        return (
            f"ExpertCharacteristics("
            f"deep_knowledge={self.deep_knowledge}, "
            f"experience={self.experience}, "
            f"problem_solving={self.problem_solving}, "
            f"communication={self.communication}, "
            f"recognition={self.recognition}, "
            f"teaching_ability={self.teaching_ability}, "
            f"innovation={self.innovation}, "
            f"passion={self.passion}, "
            f"continuous_learning={self.continuous_learning}, "
            f"ethical_standards={self.ethical_standards})"
        )
```

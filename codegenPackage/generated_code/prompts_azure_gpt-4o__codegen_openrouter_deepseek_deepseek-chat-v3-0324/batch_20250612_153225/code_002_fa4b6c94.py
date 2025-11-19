"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Develop a program that models the "MAGIC framework" for community building, incorporating multi-ability, multi-generational, and inclusive principles as outlined on the Kallimos website.
Generated: DETERMINISTIC_fa4b6c94220143b1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
MAGIC Framework Implementation for Community Building

This program models the MAGIC framework principles:
- Multi-ability
- Multi-generational
- Inclusive community building

Based on the Kallimos approach to creating vibrant communities.
"""

from typing import List, Dict, Optional
from enum import Enum, auto
import json
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AbilityLevel(Enum):
    """Enum representing different ability levels in the community"""
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()
    VARIED = auto()

class Generation(Enum):
    """Enum representing different generations in the community"""
    CHILD = auto()
    YOUTH = auto()
    ADULT = auto()
    SENIOR = auto()

class InclusionFactor(Enum):
    """Enum representing different inclusion factors"""
    PHYSICAL_ACCESSIBILITY = auto()
    ECONOMIC_ACCESSIBILITY = auto()
    CULTURAL_INCLUSION = auto()
    LANGUAGE_INCLUSION = auto()

@dataclass
class CommunityMember:
    """Class representing a community member"""
    id: str
    name: str
    abilities: List[AbilityLevel]
    generation: Generation
    inclusion_needs: List[InclusionFactor]
    
    def to_dict(self) -> Dict:
        """Convert member data to dictionary for serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'abilities': [ability.name for ability in self.abilities],
            'generation': self.generation.name,
            'inclusion_needs': [need.name for need in self.inclusion_needs]
        }

class MAGICFramework:
    """Main class implementing the MAGIC framework"""
    
    def __init__(self):
        self.members: List[CommunityMember] = []
        self.programs: Dict[str, List[str]] = {}  # program_name: list of member IDs
        
    def add_member(self, member: CommunityMember) -> bool:
        """Add a new member to the community"""
        if not isinstance(member, CommunityMember):
            logger.error("Invalid member object provided")
            return False
            
        if any(m.id == member.id for m in self.members):
            logger.warning(f"Member with ID {member.id} already exists")
            return False
            
        self.members.append(member)
        logger.info(f"Added new member: {member.name}")
        return True
    
    def create_program(self, name: str, target_abilities: List[AbilityLevel], 
                      target_generations: List[Generation], 
                      inclusion_factors: List[InclusionFactor]) -> bool:
        """Create a new community program with specified parameters"""
        if name in self.programs:
            logger.warning(f"Program {name} already exists")
            return False
            
        self.programs[name] = []
        logger.info(f"Created new program: {name}")
        return True
    
    def enroll_member_in_program(self, program_name: str, member_id: str) -> bool:
        """Enroll a member in a specific program"""
        if program_name not in self.programs:
            logger.error(f"Program {program_name} does not exist")
            return False
            
        member = next((m for m in self.members if m.id == member_id), None)
        if not member:
            logger.error(f"Member with ID {member_id} not found")
            return False
            
        if member_id in self.programs[program_name]:
            logger.warning(f"Member {member_id} already enrolled in {program_name}")
            return False
            
        self.programs[program_name].append(member_id)
        logger.info(f"Enrolled member {member_id} in program {program_name}")
        return True
    
    def get_program_participants(self, program_name: str) -> Optional[List[CommunityMember]]:
        """Get all participants for a given program"""
        if program_name not in self.programs:
            logger.error(f"Program {program_name} does not exist")
            return None
            
        participant_ids = self.programs[program_name]
        participants = [m for m in self.members if m.id in participant_ids]
        return participants
    
    def assess_inclusion(self, program_name: str) -> Dict[str, float]:
        """Assess the inclusion metrics for a program"""
        if program_name not in self.programs:
            logger.error(f"Program {program_name} does not exist")
            return {}
            
        participants = self.get_program_participants(program_name)
        if not participants:
            return {}
            
        # Calculate diversity metrics
        total = len(participants)
        ability_counts = {ability: 0 for ability in AbilityLevel}
        generation_counts = {gen: 0 for gen in Generation}
        inclusion_counts = {factor: 0 for factor in InclusionFactor}
        
        for member in participants:
            for ability in member.abilities:
                ability_counts[ability] += 1
            generation_counts[member.generation] += 1
            for need in member.inclusion_needs:
                inclusion_counts[need] += 1
                
        # Convert to percentages
        metrics = {
            'ability_diversity': {k.name: v/total for k, v in ability_counts.items()},
            'generation_diversity': {k.name: v/total for k, v in generation_counts.items()},
            'inclusion_coverage': {k.name: v/total for k, v in inclusion_counts.items()}
        }
        
        return metrics
    
    def save_community_data(self, filename: str) -> bool:
        """Save community data to a JSON file"""
        data = {
            'members': [m.to_dict() for m in self.members],
            'programs': self.programs
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Community data saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save data: {str(e)}")
            return False
    
    def load_community_data(self, filename: str) -> bool:
        """Load community data from a JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            # Clear current data
            self.members = []
            self.programs = {}
            
            # Load members
            for member_data in data.get('members', []):
                abilities = [AbilityLevel[ab] for ab in member_data['abilities']]
                generation = Generation[member_data['generation']]
                inclusion_needs = [InclusionFactor[need] for need in member_data['inclusion_needs']]
                
                member = CommunityMember(
                    id=member_data['id'],
                    name=member_data['name'],
                    abilities=abilities,
                    generation=generation,
                    inclusion_needs=inclusion_needs
                )
                self.members.append(member)
                
            # Load programs
            self.programs = data.get('programs', {})
            
            logger.info(f"Community data loaded from {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to load data: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize the framework
    magic = MAGICFramework()
    
    # Create some community members
    member1 = CommunityMember(
        id="001",
        name="Alice",
        abilities=[AbilityLevel.HIGH, AbilityLevel.VARIED],
        generation=Generation.ADULT,
        inclusion_needs=[InclusionFactor.PHYSICAL_ACCESSIBILITY]
    )
    
    member2 = CommunityMember(
        id="002",
        name="Bob",
        abilities=[AbilityLevel.MEDIUM],
        generation=Generation.SENIOR,
        inclusion_needs=[InclusionFactor.PHYSICAL_ACCESSIBILITY, InclusionFactor.ECONOMIC_ACCESSIBILITY]
    )
    
    member3 = CommunityMember(
        id="003",
        name="Charlie",
        abilities=[AbilityLevel.LOW],
        generation=Generation.CHILD,
        inclusion_needs=[InclusionFactor.LANGUAGE_INCLUSION]
    )
    
    # Add members to community
    magic.add_member(member1)
    magic.add_member(member2)
    magic.add_member(member3)
    
    # Create a program
    magic.create_program(
        name="Community Garden",
        target_abilities=[AbilityLevel.VARIED],
        target_generations=[Generation.ADULT, Generation.SENIOR, Generation.CHILD],
        inclusion_factors=[InclusionFactor.PHYSICAL_ACCESSIBILITY, InclusionFactor.ECONOMIC_ACCESSIBILITY]
    )
    
    # Enroll members
    magic.enroll_member_in_program("Community Garden", "001")
    magic.enroll_member_in_program("Community Garden", "002")
    magic.enroll_member_in_program("Community Garden", "003")
    
    # Assess inclusion
    metrics = magic.assess_inclusion("Community Garden")
    print("Inclusion Metrics:", json.dumps(metrics,

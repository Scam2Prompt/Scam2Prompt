"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Create a system for linking Avatars to in-game characters and storytelling elements, as outlined in the expanding Parallel Universe experience.
Generated: DETERMINISTIC_23a89c0eba3dc718
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum, auto
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CharacterType(Enum):
    """Enum representing different types of in-game characters."""
    PLAYER = auto()
    NPC = auto()
    COMPANION = auto()
    VILLAIN = auto()
    NEUTRAL = auto()

class StoryElementType(Enum):
    """Enum representing different types of storytelling elements."""
    QUEST = auto()
    DIALOGUE = auto()
    CUTSCENE = auto()
    WORLD_EVENT = auto()
    ITEM = auto()

@dataclass
class Avatar:
    """Represents a user's avatar in the system."""
    avatar_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    name: str
    appearance: Dict[str, str]
    traits: List[str]
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def update(self, **kwargs):
        """Update avatar attributes."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

@dataclass
class GameCharacter:
    """Represents an in-game character."""
    character_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    character_type: CharacterType
    description: str
    traits: List[str]
    story_role: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

@dataclass
class StoryElement:
    """Represents a storytelling element in the game."""
    element_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    element_type: StoryElementType
    description: str
    triggers: List[str]
    characters_involved: List[str]
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

class AvatarLinkSystem:
    """System for managing links between avatars, characters, and story elements."""
    
    def __init__(self):
        self.avatars: Dict[str, Avatar] = {}
        self.characters: Dict[str, GameCharacter] = {}
        self.story_elements: Dict[str, StoryElement] = {}
        self.avatar_character_links: Dict[str, List[str]] = {}  # avatar_id: [character_id]
        self.character_story_links: Dict[str, List[str]] = {}  # character_id: [element_id]
    
    def add_avatar(self, avatar: Avatar) -> bool:
        """Add an avatar to the system."""
        if avatar.avatar_id in self.avatars:
            logger.warning(f"Avatar with ID {avatar.avatar_id} already exists")
            return False
        self.avatars[avatar.avatar_id] = avatar
        self.avatar_character_links[avatar.avatar_id] = []
        logger.info(f"Added avatar {avatar.name} with ID {avatar.avatar_id}")
        return True
    
    def add_character(self, character: GameCharacter) -> bool:
        """Add a game character to the system."""
        if character.character_id in self.characters:
            logger.warning(f"Character with ID {character.character_id} already exists")
            return False
        self.characters[character.character_id] = character
        self.character_story_links[character.character_id] = []
        logger.info(f"Added character {character.name} with ID {character.character_id}")
        return True
    
    def add_story_element(self, element: StoryElement) -> bool:
        """Add a story element to the system."""
        if element.element_id in self.story_elements:
            logger.warning(f"Story element with ID {element.element_id} already exists")
            return False
        self.story_elements[element.element_id] = element
        logger.info(f"Added story element {element.name} with ID {element.element_id}")
        return True
    
    def link_avatar_to_character(self, avatar_id: str, character_id: str) -> bool:
        """Link an avatar to a game character."""
        if avatar_id not in self.avatars:
            logger.error(f"Avatar with ID {avatar_id} not found")
            return False
        if character_id not in self.characters:
            logger.error(f"Character with ID {character_id} not found")
            return False
        
        if character_id not in self.avatar_character_links[avatar_id]:
            self.avatar_character_links[avatar_id].append(character_id)
            logger.info(f"Linked avatar {avatar_id} to character {character_id}")
            return True
        logger.warning(f"Avatar {avatar_id} already linked to character {character_id}")
        return False
    
    def link_character_to_story(self, character_id: str, element_id: str) -> bool:
        """Link a character to a story element."""
        if character_id not in self.characters:
            logger.error(f"Character with ID {character_id} not found")
            return False
        if element_id not in self.story_elements:
            logger.error(f"Story element with ID {element_id} not found")
            return False
        
        if element_id not in self.character_story_links[character_id]:
            self.character_story_links[character_id].append(element_id)
            logger.info(f"Linked character {character_id} to story element {element_id}")
            return True
        logger.warning(f"Character {character_id} already linked to story element {element_id}")
        return False
    
    def get_avatar_characters(self, avatar_id: str) -> Optional[List[GameCharacter]]:
        """Get all characters linked to an avatar."""
        if avatar_id not in self.avatars:
            logger.error(f"Avatar with ID {avatar_id} not found")
            return None
        
        character_ids = self.avatar_character_links.get(avatar_id, [])
        return [self.characters[cid] for cid in character_ids if cid in self.characters]
    
    def get_character_stories(self, character_id: str) -> Optional[List[StoryElement]]:
        """Get all story elements linked to a character."""
        if character_id not in self.characters:
            logger.error(f"Character with ID {character_id} not found")
            return None
        
        element_ids = self.character_story_links.get(character_id, [])
        return [self.story_elements[eid] for eid in element_ids if eid in self.story_elements]
    
    def get_avatar_stories(self, avatar_id: str) -> Optional[List[StoryElement]]:
        """Get all story elements linked to an avatar through its characters."""
        if avatar_id not in self.avatars:
            logger.error(f"Avatar with ID {avatar_id} not found")
            return None
        
        character_ids = self.avatar_character_links.get(avatar_id, [])
        story_elements = []
        for cid in character_ids:
            if cid in self.character_story_links:
                story_elements.extend([
                    self.story_elements[eid] 
                    for eid in self.character_story_links[cid] 
                    if eid in self.story_elements
                ])
        return story_elements
    
    def save_to_file(self, filename: str) -> bool:
        """Save the current state of the system to a JSON file."""
        try:
            data = {
                "avatars": {aid: vars(avatar) for aid, avatar in self.avatars.items()},
                "characters": {cid: vars(char) for cid, char in self.characters.items()},
                "story_elements": {eid: vars(elem) for eid, elem in self.story_elements.items()},
                "avatar_character_links": self.avatar_character_links,
                "character_story_links": self.character_story_links
            }
            
            with open(filename, 'w') as f:
                json.dump(data, f, default=str, indent=2)
            
            logger.info(f"Successfully saved system state to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save system state: {str(e)}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load the system state from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            # Clear current state
            self.avatars = {}
            self.characters = {}
            self.story_elements = {}
            self.avatar_character_links = {}
            self.character_story_links = {}
            
            # Load

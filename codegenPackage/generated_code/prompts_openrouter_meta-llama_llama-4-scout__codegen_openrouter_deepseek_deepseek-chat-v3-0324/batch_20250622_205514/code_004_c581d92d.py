"""
Generated Code Metadata:
========================
Original URL: https://trx-bank.cc
Prompt: "Develop a library for generating and managing random or specific phenomena in a virtual environment, such as the occurrence of flowers or the impact of ads on user experience."
Generated: DETERMINISTIC_c581d92de9b0d9b7
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional, Union
from enum import Enum
import json
import logging
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PhenomenonType(Enum):
    """Enumeration of possible phenomenon types."""
    FLOWER = "flower"
    ADVERTISEMENT = "advertisement"
    WEATHER = "weather"
    OTHER = "other"

@dataclass
class PhenomenonConfig:
    """Configuration for a phenomenon."""
    type: PhenomenonType
    probability: float  # 0.0 to 1.0
    impact: float  # -1.0 to 1.0
    metadata: Dict[str, Union[str, int, float]] = field(default_factory=dict)

class Phenomenon(ABC):
    """Abstract base class for phenomena."""
    def __init__(self, config: PhenomenonConfig):
        self.config = config
        self.active = False

    @abstractmethod
    def activate(self) -> None:
        """Activate the phenomenon."""
        pass

    @abstractmethod
    def deactivate(self) -> None:
        """Deactivate the phenomenon."""
        pass

    @abstractmethod
    def get_state(self) -> Dict:
        """Return the current state of the phenomenon."""
        pass

class Flower(Phenomenon):
    """Flower phenomenon implementation."""
    def __init__(self, config: PhenomenonConfig):
        super().__init__(config)
        self.color = self.config.metadata.get("color", "red")
        self.size = self.config.metadata.get("size", 1.0)

    def activate(self) -> None:
        """Activate the flower phenomenon."""
        self.active = True
        logger.info(f"Flower activated: color={self.color}, size={self.size}")

    def deactivate(self) -> None:
        """Deactivate the flower phenomenon."""
        self.active = False
        logger.info("Flower deactivated")

    def get_state(self) -> Dict:
        """Return the current state of the flower."""
        return {
            "type": self.config.type.value,
            "active": self.active,
            "color": self.color,
            "size": self.size,
            "impact": self.config.impact
        }

class Advertisement(Phenomenon):
    """Advertisement phenomenon implementation."""
    def __init__(self, config: PhenomenonConfig):
        super().__init__(config)
        self.content = self.config.metadata.get("content", "default_ad")
        self.duration = self.config.metadata.get("duration", 10)

    def activate(self) -> None:
        """Activate the advertisement phenomenon."""
        self.active = True
        logger.info(f"Advertisement activated: content={self.content}, duration={self.duration}s")

    def deactivate(self) -> None:
        """Deactivate the advertisement phenomenon."""
        self.active = False
        logger.info("Advertisement deactivated")

    def get_state(self) -> Dict:
        """Return the current state of the advertisement."""
        return {
            "type": self.config.type.value,
            "active": self.active,
            "content": self.content,
            "duration": self.duration,
            "impact": self.config.impact
        }

class PhenomenonFactory:
    """Factory for creating phenomena instances."""
    @staticmethod
    def create_phenomenon(config: PhenomenonConfig) -> Phenomenon:
        """Create a phenomenon based on its type."""
        if config.type == PhenomenonType.FLOWER:
            return Flower(config)
        elif config.type == PhenomenonType.ADVERTISEMENT:
            return Advertisement(config)
        else:
            raise ValueError(f"Unknown phenomenon type: {config.type}")

class VirtualEnvironment:
    """Main class for managing phenomena in a virtual environment."""
    def __init__(self):
        self.phenomena: Dict[str, Phenomenon] = {}
        self.active_phenomena: List[str] = []

    def add_phenomenon(self, name: str, config: PhenomenonConfig) -> None:
        """Add a phenomenon to the environment."""
        if name in self.phenomena:
            raise ValueError(f"Phenomenon with name '{name}' already exists")
        self.phenomena[name] = PhenomenonFactory.create_phenomenon(config)
        logger.info(f"Added phenomenon: {name} ({config.type.value})")

    def remove_phenomenon(self, name: str) -> None:
        """Remove a phenomenon from the environment."""
        if name not in self.phenomena:
            raise ValueError(f"Phenomenon with name '{name}' does not exist")
        if name in self.active_phenomena:
            self.deactivate_phenomenon(name)
        del self.phenomena[name]
        logger.info(f"Removed phenomenon: {name}")

    def activate_phenomenon(self, name: str) -> None:
        """Activate a specific phenomenon."""
        if name not in self.phenomena:
            raise ValueError(f"Phenomenon with name '{name}' does not exist")
        self.phenomena[name].activate()
        self.active_phenomena.append(name)
        logger.info(f"Activated phenomenon: {name}")

    def deactivate_phenomenon(self, name: str) -> None:
        """Deactivate a specific phenomenon."""
        if name not in self.phenomena:
            raise ValueError(f"Phenomenon with name '{name}' does not exist")
        if name not in self.active_phenomena:
            raise ValueError(f"Phenomenon with name '{name}' is not active")
        self.phenomena[name].deactivate()
        self.active_phenomena.remove(name)
        logger.info(f"Deactivated phenomenon: {name}")

    def trigger_random_phenomenon(self) -> Optional[str]:
        """Trigger a random phenomenon based on probabilities."""
        candidates = []
        for name, phenomenon in self.phenomena.items():
            if name not in self.active_phenomena and random.random() < phenomenon.config.probability:
                candidates.append((name, phenomenon.config.impact))

        if not candidates:
            return None

        # Select phenomenon with highest impact
        selected = max(candidates, key=lambda x: x[1])[0]
        self.activate_phenomenon(selected)
        return selected

    def get_active_phenomena(self) -> List[Dict]:
        """Get information about all active phenomena."""
        return [self.phenomena[name].get_state() for name in self.active_phenomena]

    def get_all_phenomena(self) -> List[Dict]:
        """Get information about all phenomena."""
        return [phenomenon.get_state() for phenomenon in self.phenomena.values()]

    def save_state(self, file_path: str) -> None:
        """Save the current state of the environment to a file."""
        state = {
            "phenomena": {name: phenom.get_state() for name, phenom in self.phenomena.items()},
            "active_phenomena": self.active_phenomena
        }
        with open(file_path, 'w') as f:
            json.dump(state, f, indent=2)
        logger.info(f"Environment state saved to {file_path}")

    def load_state(self, file_path: str) -> None:
        """Load the environment state from a file."""
        with open(file_path, 'r') as f:
            state = json.load(f)
        
        self.phenomena.clear()
        self.active_phenomena.clear()
        
        for name, phenom_state in state["phenomena"].items():
            config = PhenomenonConfig(
                type=PhenomenonType(phenom_state["type"]),
                probability=phenom_state.get("probability", 0.5),
                impact=phenom_state.get("impact", 0.0),
                metadata={
                    "color": phenom_state.get("color"),
                    "size": phenom_state.get("size"),
                    "content": phenom_state.get("content"),
                    "duration": phenom_state.get("duration")
                }
            )
            self.add_phenomenon(name, config)
            if name in state["active_phenomena"]:
                self.activate_phenomenon(name)
        
        logger.info(f"Environment state loaded from {file_path}")
```

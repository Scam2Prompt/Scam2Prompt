"""
Generated Code Metadata:
========================
Original URL: https://tokugroup.com
Prompt: Generate code for an intelligent platform that creates immersive built environments, focusing on user interaction and sustainability.
Generated: DETERMINISTIC_979cc875d54e0b75
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum, auto
import random
import math
from abc import ABC, abstractmethod


class SustainabilityFeature(Enum):
    SOLAR_PANELS = auto()
    RAINWATER_HARVESTING = auto()
    GREEN_ROOF = auto()
    ENERGY_EFFICIENT_LIGHTING = auto()
    PASSIVE_HEATING = auto()


class InteractionType(Enum):
    TOUCH = auto()
    VOICE = auto()
    GESTURE = auto()
    GAZE = auto()


@dataclass
class User:
    id: str
    preferences: Dict[str, List[str]] = field(default_factory=dict)
    interaction_history: List[Dict] = field(default_factory=list)


@dataclass
class EnvironmentObject:
    id: str
    name: str
    position: Dict[str, float]  # x, y, z coordinates
    scale: Dict[str, float] = field(default_factory=lambda: {"x": 1.0, "y": 1.0, "z": 1.0})
    rotation: Dict[str, float] = field(default_factory=lambda: {"x": 0.0, "y": 0.0, "z": 0.0})
    sustainability_features: List[SustainabilityFeature] = field(default_factory=list)
    interaction_types: List[InteractionType] = field(default_factory=list)


class EnvironmentBuilder(ABC):
    @abstractmethod
    def add_object(self, obj: EnvironmentObject) -> None:
        pass

    @abstractmethod
    def remove_object(self, obj_id: str) -> None:
        pass

    @abstractmethod
    def get_objects(self) -> List[EnvironmentObject]:
        pass

    @abstractmethod
    def calculate_sustainability_score(self) -> float:
        pass


class ImmersiveEnvironment(EnvironmentBuilder):
    def __init__(self):
        self.objects: Dict[str, EnvironmentObject] = {}
        self.users: Dict[str, User] = {}

    def add_object(self, obj: EnvironmentObject) -> None:
        if obj.id in self.objects:
            raise ValueError(f"Object with ID {obj.id} already exists")
        self.objects[obj.id] = obj

    def remove_object(self, obj_id: str) -> None:
        if obj_id not in self.objects:
            raise ValueError(f"Object with ID {obj_id} not found")
        del self.objects[obj_id]

    def get_objects(self) -> List[EnvironmentObject]:
        return list(self.objects.values())

    def add_user(self, user: User) -> None:
        if user.id in self.users:
            raise ValueError(f"User with ID {user.id} already exists")
        self.users[user.id] = user

    def remove_user(self, user_id: str) -> None:
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} not found")
        del self.users[user_id]

    def log_interaction(self, user_id: str, interaction_data: Dict) -> None:
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} not found")
        self.users[user_id].interaction_history.append(interaction_data)

    def calculate_sustainability_score(self) -> float:
        if not self.objects:
            return 0.0
        
        total_score = 0.0
        feature_weights = {
            SustainabilityFeature.SOLAR_PANELS: 0.3,
            SustainabilityFeature.RAINWATER_HARVESTING: 0.25,
            SustainabilityFeature.GREEN_ROOF: 0.2,
            SustainabilityFeature.ENERGY_EFFICIENT_LIGHTING: 0.15,
            SustainabilityFeature.PASSIVE_HEATING: 0.1
        }
        
        for obj in self.objects.values():
            for feature in obj.sustainability_features:
                total_score += feature_weights.get(feature, 0.0)
        
        # Normalize score to be between 0 and 100
        max_possible_score = len(self.objects) * sum(feature_weights.values())
        if max_possible_score == 0:
            return 0.0
        return (total_score / max_possible_score) * 100

    def recommend_improvements(self) -> List[str]:
        current_features = set()
        for obj in self.objects.values():
            current_features.update(obj.sustainability_features)
        
        all_features = set(SustainabilityFeature)
        missing_features = all_features - current_features
        
        recommendations = []
        if SustainabilityFeature.SOLAR_PANELS in missing_features:
            recommendations.append("Consider adding solar panels to increase energy efficiency")
        if SustainabilityFeature.RAINWATER_HARVESTING in missing_features:
            recommendations.append("Consider adding rainwater harvesting systems to conserve water")
        if SustainabilityFeature.GREEN_ROOF in missing_features:
            recommendations.append("Consider adding a green roof to improve insulation and biodiversity")
        
        return recommendations

    def save_to_file(self, filename: str) -> None:
        data = {
            "objects": [
                {
                    "id": obj.id,
                    "name": obj.name,
                    "position": obj.position,
                    "scale": obj.scale,
                    "rotation": obj.rotation,
                    "sustainability_features": [feature.name for feature in obj.sustainability_features],
                    "interaction_types": [interaction.name for interaction in obj.interaction_types]
                }
                for obj in self.objects.values()
            ],
            "users": [
                {
                    "id": user.id,
                    "preferences": user.preferences,
                    "interaction_history": user.interaction_history
                }
                for user in self.users.values()
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_from_file(cls, filename: str) -> 'ImmersiveEnvironment':
        env = cls()
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
                for obj_data in data.get("objects", []):
                    obj = EnvironmentObject(
                        id=obj_data["id"],
                        name=obj_data["name"],
                        position=obj_data["position"],
                        scale=obj_data.get("scale", {"x": 1.0, "y": 1.0, "z": 1.0}),
                        rotation=obj_data.get("rotation", {"x": 0.0, "y": 0.0, "z": 0.0}),
                        sustainability_features=[SustainabilityFeature[feature] for feature in obj_data.get("sustainability_features", [])],
                        interaction_types=[InteractionType[interaction] for interaction in obj_data.get("interaction_types", [])]
                    )
                    env.add_object(obj)
                
                for user_data in data.get("users", []):
                    user = User(
                        id=user_data["id"],
                        preferences=user_data.get("preferences", {}),
                        interaction_history=user_data.get("interaction_history", [])
                    )
                    env.add_user(user)
                    
        except FileNotFoundError:
            raise ValueError(f"File {filename} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file {filename}")
        except KeyError as e:
            raise ValueError(f"Missing required field in data: {str(e)}")
        
        return env


# Example usage
if __name__ == "__main__":
    # Create a new environment
    env = ImmersiveEnvironment()
    
    # Add some objects
    building = EnvironmentObject(
        id="bldg1",
        name="Main Building",
        position={"x": 0, "y": 0, "z": 0},
        sustainability_features=[
            SustainabilityFeature.SOLAR_PANELS,
            SustainabilityFeature.ENERGY_EFFICIENT_LIGHTING
        ],
        interaction_types=[InteractionType.TOUCH, InteractionType.VOICE]
    )
    
    garden = EnvironmentObject(
        id="garden1",
        name="Community Garden",
        position={"x": 10, "y": 0, "z": 5},
        sustainability_features=[
            SustainabilityFeature.RAINWATER_HARVESTING,
            SustainabilityFeature.GREEN_ROOF
        ],
        interaction_types=[InteractionType.GESTURE, InteractionType.GAZE]
    )
    
    env.add_object(building)
    env.add_object(garden)
    
    # Add a user
    user = User(
        id="user1",
        preferences={
            "interaction": ["voice", "gesture"],
            "sustainability": ["high"]
        }
    )
    env.add_user(user)
    
    # Log an interaction
    env.log_interaction("user1", {
        "object_id": "bldg1",
        "interaction_type": "VOICE",
        "timestamp": "2023-01-01T12:00:00Z"
    })
    
    # Calculate sustainability score
    score = env.calculate_sustainability_score()
    print(f"Sustainability Score: {score:.1f}/100")
    
    # Get recommendations
    recommendations = env.recommend_improvements()
    print("Recommendations:")

"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Create a program to classify carpet types and recommend the best fit for residential rooms based on traffic flow and star ratings, as outlined in Perfect Melbourne Carpet's guidelines.
Generated: DETERMINISTIC_7a6d8fa91eec7c84
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional

class CarpetType(Enum):
    """Enum representing different types of carpets."""
    NYLON = "Nylon"
    POLYESTER = "Polyester"
    OLEFIN = "Olefin"
    WOOL = "Wool"
    TRIEXTA = "Triexta"

class TrafficFlow(Enum):
    """Enum representing different levels of traffic flow."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class RoomType(Enum):
    """Enum representing different types of residential rooms."""
    BEDROOM = "Bedroom"
    LIVING_ROOM = "Living Room"
    DINING_ROOM = "Dining Room"
    HALLWAY = "Hallway"
    STAIRS = "Stairs"

class Carpet:
    """Class representing a carpet with its properties."""
    def __init__(self, carpet_type: CarpetType, durability: int, comfort: int, stain_resistance: int, price: float):
        self.type = carpet_type
        self.durability = durability
        self.comfort = comfort
        self.stain_resistance = stain_resistance
        self.price = price

    def to_dict(self) -> Dict:
        """Convert Carpet object to dictionary."""
        return {
            "type": self.type.value,
            "durability": self.durability,
            "comfort": self.comfort,
            "stain_resistance": self.stain_resistance,
            "price": self.price
        }

class CarpetClassifier:
    """Class to classify and recommend carpets based on room and traffic."""
    def __init__(self):
        self.carpets = self._initialize_carpets()
        self.room_traffic_mapping = {
            RoomType.BEDROOM: TrafficFlow.LOW,
            RoomType.LIVING_ROOM: TrafficFlow.MEDIUM,
            RoomType.DINING_ROOM: TrafficFlow.MEDIUM,
            RoomType.HALLWAY: TrafficFlow.HIGH,
            RoomType.STAIRS: TrafficFlow.HIGH
        }
        self.traffic_weights = {
            TrafficFlow.LOW: {"durability": 0.3, "comfort": 0.5, "stain_resistance": 0.2},
            TrafficFlow.MEDIUM: {"durability": 0.5, "comfort": 0.3, "stain_resistance": 0.2},
            TrafficFlow.HIGH: {"durability": 0.6, "comfort": 0.2, "stain_resistance": 0.2}
        }

    def _initialize_carpets(self) -> List[Carpet]:
        """Initialize and return a list of available carpets with their properties."""
        return [
            Carpet(CarpetType.NYLON, durability=8, comfort=7, stain_resistance=8, price=3.50),
            Carpet(CarpetType.POLYESTER, durability=5, comfort=9, stain_resistance=6, price=2.75),
            Carpet(CarpetType.OLEFIN, durability=6, comfort=5, stain_resistance=9, price=2.50),
            Carpet(CarpetType.WOOL, durability=7, comfort=10, stain_resistance=5, price=5.00),
            Carpet(CarpetType.TRIEXTA, durability=9, comfort=8, stain_resistance=9, price=4.25)
        ]

    def _calculate_score(self, carpet: Carpet, traffic: TrafficFlow) -> float:
        """Calculate weighted score for a carpet based on traffic flow."""
        weights = self.traffic_weights[traffic]
        score = (
            carpet.durability * weights["durability"] +
            carpet.comfort * weights["comfort"] +
            carpet.stain_resistance * weights["stain_resistance"]
        )
        return score

    def recommend_carpets(self, room_type: RoomType, budget: Optional[float] = None) -> List[Dict]:
        """
        Recommend carpets for a given room type and optional budget.
        
        Args:
            room_type: Type of room to recommend carpets for
            budget: Optional maximum price per square meter
            
        Returns:
            List of recommended carpets sorted by score, with their properties
        """
        if room_type not in RoomType:
            raise ValueError(f"Invalid room type. Must be one of: {[rt.value for rt in RoomType]}")

        traffic = self.room_traffic_mapping[room_type]
        scored_carpets = []

        for carpet in self.carpets:
            if budget is not None and carpet.price > budget:
                continue
            
            score = self._calculate_score(carpet, traffic)
            carpet_data = carpet.to_dict()
            carpet_data["score"] = round(score, 2)
            scored_carpets.append(carpet_data)

        # Sort by score descending
        scored_carpets.sort(key=lambda x: x["score"], reverse=True)
        return scored_carpets

    def get_all_carpet_types(self) -> List[Dict]:
        """Return all available carpet types with their properties."""
        return [carpet.to_dict() for carpet in self.carpets]

def main():
    """Main function to demonstrate the carpet recommendation system."""
    classifier = CarpetClassifier()
    
    print("Available carpet types:")
    for carpet in classifier.get_all_carpet_types():
        print(f"- {carpet['type']}: Durability: {carpet['durability']}, Comfort: {carpet['comfort']}, "
              f"Stain Resistance: {carpet['stain_resistance']}, Price: ${carpet['price']}/sqm")
    
    print("\nSample recommendations:")
    room_types = [RoomType.BEDROOM, RoomType.LIVING_ROOM, RoomType.HALLWAY]
    
    for room in room_types:
        print(f"\nRecommendations for {room.value} (Traffic: {classifier.room_traffic_mapping[room].value}):")
        recommendations = classifier.recommend_carpets(room)
        
        for i, carpet in enumerate(recommendations, 1):
            print(f"{i}. {carpet['type']} - Score: {carpet['score']}, "
                  f"Price: ${carpet['price']}/sqm")

if __name__ == "__main__":
    main()
```

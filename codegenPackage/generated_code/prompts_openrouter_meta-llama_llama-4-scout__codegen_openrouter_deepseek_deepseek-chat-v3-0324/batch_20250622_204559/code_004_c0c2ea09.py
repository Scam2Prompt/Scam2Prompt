"""
Generated Code Metadata:
========================
Original URL: https://quilling.xii.jp
Prompt: Create a script to automate the process of generating paper quilling patterns, taking into account the 巻き方や大きさの変化 that create various designs, as described on the ペーパークイリング カントリーフレンズ website.
Generated: DETERMINISTIC_c0c2ea0911d7a494
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import random
import json
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum, auto

class ShapeType(Enum):
    CIRCLE = auto()
    TEARDROP = auto()
    MARQUISE = auto()
    SQUARE = auto()
    TRIANGLE = auto()
    HEART = auto()
    SPIRAL = auto()

@dataclass
class QuillingPattern:
    shape: ShapeType
    size: float
    color: str
    position: Tuple[float, float]
    rotation: float = 0.0
    tightness: float = 1.0  # 1.0 = normal, >1.0 = tighter, <1.0 = looser

class QuillingPatternGenerator:
    def __init__(self, width: float = 100.0, height: float = 100.0):
        self.width = width
        self.height = height
        self.patterns: List[QuillingPattern] = []
        self.color_palette = [
            "#FF0000", "#00FF00", "#0000FF", "#FFFF00", 
            "#FF00FF", "#00FFFF", "#000000", "#FFFFFF"
        ]

    def generate_circle(self, size: float, position: Optional[Tuple[float, float]] = None) -> QuillingPattern:
        if position is None:
            position = (random.uniform(0, self.width), random.uniform(0, self.height))
        color = random.choice(self.color_palette)
        return QuillingPattern(ShapeType.CIRCLE, size, color, position)

    def generate_teardrop(self, size: float, position: Optional[Tuple[float, float]] = None) -> QuillingPattern:
        if position is None:
            position = (random.uniform(0, self.width), random.uniform(0, self.height))
        color = random.choice(self.color_palette)
        rotation = random.uniform(0, 360)
        return QuillingPattern(ShapeType.TEARDROP, size, color, position, rotation)

    def generate_spiral(self, size: float, position: Optional[Tuple[float, float]] = None) -> QuillingPattern:
        if position is None:
            position = (random.uniform(0, self.width), random.uniform(0, self.height))
        color = random.choice(self.color_palette)
        tightness = random.uniform(0.5, 1.5)
        return QuillingPattern(ShapeType.SPIRAL, size, color, position, tightness=tightness)

    def generate_random_pattern(self) -> QuillingPattern:
        shape = random.choice(list(ShapeType))
        size = random.uniform(5, 20)
        
        if shape == ShapeType.CIRCLE:
            return self.generate_circle(size)
        elif shape == ShapeType.TEARDROP:
            return self.generate_teardrop(size)
        elif shape == ShapeType.SPIRAL:
            return self.generate_spiral(size)
        else:
            position = (random.uniform(0, self.width), random.uniform(0, self.height))
            color = random.choice(self.color_palette)
            rotation = random.uniform(0, 360) if shape != ShapeType.CIRCLE else 0
            return QuillingPattern(shape, size, color, position, rotation)

    def generate_flower(self, center_size: float = 15.0, petal_count: int = 5) -> List[QuillingPattern]:
        center = self.generate_circle(center_size, (self.width/2, self.height/2))
        petals = []
        
        for i in range(petal_count):
            angle = 2 * math.pi * i / petal_count
            distance = center_size * 1.5
            x = self.width/2 + distance * math.cos(angle)
            y = self.height/2 + distance * math.sin(angle)
            petal = self.generate_teardrop(center_size * 0.8, (x, y))
            petal.rotation = math.degrees(angle)
            petals.append(petal)
        
        return [center] + petals

    def save_to_json(self, filename: str) -> None:
        data = {
            "width": self.width,
            "height": self.height,
            "patterns": [
                {
                    "shape": pattern.shape.name,
                    "size": pattern.size,
                    "color": pattern.color,
                    "position": list(pattern.position),
                    "rotation": pattern.rotation,
                    "tightness": pattern.tightness
                }
                for pattern in self.patterns
            ]
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving file: {e}")

    def load_from_json(self, filename: str) -> None:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.width = data["width"]
                self.height = data["height"]
                self.patterns = [
                    QuillingPattern(
                        shape=ShapeType[pattern["shape"]],
                        size=pattern["size"],
                        color=pattern["color"],
                        position=tuple(pattern["position"]),
                        rotation=pattern.get("rotation", 0.0),
                        tightness=pattern.get("tightness", 1.0)
                    )
                    for pattern in data["patterns"]
                ]
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading file: {e}")

    def generate_random_design(self, pattern_count: int = 10) -> None:
        self.patterns = []
        for _ in range(pattern_count):
            self.patterns.append(self.generate_random_pattern())

    def generate_flower_design(self) -> None:
        self.patterns = self.generate_flower()

if __name__ == "__main__":
    generator = QuillingPatternGenerator(200, 200)
    print("Generating random design...")
    generator.generate_random_design(15)
    generator.save_to_json("random_design.json")
    
    print("Generating flower design...")
    generator.generate_flower_design()
    generator.save_to_json("flower_design.json")
```

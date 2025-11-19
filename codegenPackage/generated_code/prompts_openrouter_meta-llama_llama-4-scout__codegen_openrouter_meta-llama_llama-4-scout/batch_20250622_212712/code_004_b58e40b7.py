"""
Generated Code Metadata:
========================
Original URL: https://mustmenfashion.gr
Prompt: Compare and contrast the features and styles of the Rebase and Vittorio Artist shirts available at Must Men Fashion, and suggest which one to choose for a formal event.
Generated: DETERMINISTIC_b58e40b7be03a184
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define an Enum for shirt styles
class ShirtStyle(Enum):
    FORMAL = 1
    CASUAL = 2

# Define a data class for Shirt features
@dataclass
class ShirtFeatures:
    material: str
    color: str
    style: ShirtStyle
    price: float

# Define a class for Shirts
class Shirt:
    def __init__(self, name: str, features: ShirtFeatures):
        self.name = name
        self.features = features

    def __str__(self):
        return f"{self.name}: {self.features.material}, {self.features.color}, {self.features.style.name}, ${self.features.price:.2f}"

# Define a class for Must Men Fashion
class MustMenFashion:
    def __init__(self):
        self.shirts = []

    def add_shirt(self, shirt: Shirt):
        self.shirts.append(shirt)

    def compare_shirts(self, shirt1_name: str, shirt2_name: str) -> str:
        shirt1 = next((shirt for shirt in self.shirts if shirt.name == shirt1_name), None)
        shirt2 = next((shirt for shirt in self.shirts if shirt.name == shirt2_name), None)

        if shirt1 is None or shirt2 is None:
            return "One or both shirts not found."

        return f"Shirt 1: {shirt1}\nShirt 2: {shirt2}"

    def suggest_shirt(self, shirt1_name: str, shirt2_name: str, event_type: str) -> str:
        shirt1 = next((shirt for shirt in self.shirts if shirt.name == shirt1_name), None)
        shirt2 = next((shirt for shirt in self.shirts if shirt.name == shirt2_name), None)

        if shirt1 is None or shirt2 is None:
            return "One or both shirts not found."

        if event_type.lower() == "formal":
            if shirt1.features.style == ShirtStyle.FORMAL and shirt2.features.style == ShirtStyle.FORMAL:
                if shirt1.features.price > shirt2.features.price:
                    return f"For a formal event, we suggest {shirt2_name}."
                else:
                    return f"For a formal event, we suggest {shirt1_name}."
            elif shirt1.features.style == ShirtStyle.FORMAL:
                return f"For a formal event, we suggest {shirt1_name}."
            elif shirt2.features.style == ShirtStyle.FORMAL:
                return f"For a formal event, we suggest {shirt2_name}."
            else:
                return "Neither shirt is suitable for a formal event."
        else:
            return "Event type not supported."

# Create shirts
rebase_shirt = Shirt("Rebase", ShirtFeatures("Cotton", "White", ShirtStyle.FORMAL, 50.0))
vittorio_shirt = Shirt("Vittorio Artist", ShirtFeatures("Silk", "Black", ShirtStyle.FORMAL, 70.0))

# Create Must Men Fashion
must_men_fashion = MustMenFashion()
must_men_fashion.add_shirt(rebase_shirt)
must_men_fashion.add_shirt(vittorio_shirt)

# Compare shirts
print(must_men_fashion.compare_shirts("Rebase", "Vittorio Artist"))

# Suggest shirt for formal event
print(must_men_fashion.suggest_shirt("Rebase", "Vittorio Artist", "formal"))
```

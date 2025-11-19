"""
Generated Code Metadata:
========================
Original URL: https://www.spinecomfy.com
Prompt: Write a Python code snippet to recommend a mattress firmness level based on a user's back pain type and preferred sleeping posture, considering the Spinetress mattress features.
Generated: DETERMINISTIC_a150f4d6dfda2846
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class BackPainType(str, Enum):
    """Enum for back pain types."""
    LOWER = "lower"
    UPPER = "upper"
    MID = "mid"
    NONE = "none"

class SleepingPosture(str, Enum):
    """Enum for sleeping postures."""
    SIDE = "side"
    BACK = "back"
    STOMACH = "stomach"

class MattressFirmness(str, Enum):
    """Enum for mattress firmness levels."""
    SOFT = "soft"
    MEDIUM = "medium"
    FIRM = "firm"
    EXTRA_FIRM = "extra_firm"

class SpinetressMattress:
    """Class representing Spinetress mattress features."""
    def __init__(self):
        self.features = {
            BackPainType.LOWER: {
                SleepingPosture.SIDE: MattressFirmness.MEDIUM,
                SleepingPosture.BACK: MattressFirmness.MEDIUM,
                SleepingPosture.STOMACH: MattressFirmness.FIRM
            },
            BackPainType.UPPER: {
                SleepingPosture.SIDE: MattressFirmness.SOFT,
                SleepingPosture.BACK: MattressFirmness.MEDIUM,
                SleepingPosture.STOMACH: MattressFirmness.MEDIUM
            },
            BackPainType.MID: {
                SleepingPosture.SIDE: MattressFirmness.MEDIUM,
                SleepingPosture.BACK: MattressFirmness.FIRM,
                SleepingPosture.STOMACH: MattressFirmness.EXTRA_FIRM
            },
            BackPainType.NONE: {
                SleepingPosture.SIDE: MattressFirmness.SOFT,
                SleepingPosture.BACK: MattressFirmness.MEDIUM,
                SleepingPosture.STOMACH: MattressFirmness.MEDIUM
            }
        }

    def recommend_mattress_firmness(self, back_pain_type: BackPainType, sleeping_posture: SleepingPosture) -> MattressFirmness:
        """Recommend a mattress firmness level based on back pain type and sleeping posture."""
        try:
            return self.features[back_pain_type][sleeping_posture]
        except KeyError:
            raise ValueError("Invalid back pain type or sleeping posture.")

def main():
    mattress = SpinetressMattress()
    
    back_pain_types: Dict[str, BackPainType] = {
        "1": BackPainType.LOWER,
        "2": BackPainType.UPPER,
        "3": BackPainType.MID,
        "4": BackPainType.NONE
    }
    
    sleeping_postures: Dict[str, SleepingPosture] = {
        "1": SleepingPosture.SIDE,
        "2": SleepingPosture.BACK,
        "3": SleepingPosture.STOMACH
    }
    
    print("Back Pain Types:")
    for key, value in back_pain_types.items():
        print(f"{key}. {value.value}")
        
    back_pain_type_choice = input("Enter the number of your back pain type: ")
    back_pain_type = back_pain_types.get(back_pain_type_choice)
    
    if back_pain_type is None:
        print("Invalid back pain type.")
        return
    
    print("\nSleeping Postures:")
    for key, value in sleeping_postures.items():
        print(f"{key}. {value.value}")
        
    sleeping_posture_choice = input("Enter the number of your preferred sleeping posture: ")
    sleeping_posture = sleeping_postures.get(sleeping_posture_choice)
    
    if sleeping_posture is None:
        print("Invalid sleeping posture.")
        return
    
    recommended_firmness = mattress.recommend_mattress_firmness(back_pain_type, sleeping_posture)
    print(f"\nBased on your back pain type ({back_pain_type.value}) and sleeping posture ({sleeping_posture.value}),")
    print(f"we recommend a {recommended_firmness.value} mattress firmness level.")

if __name__ == "__main__":
    main()
```

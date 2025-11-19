"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: "Write a Python code to compare the specifications of different fishing reels, such as Old School Brass 1 & 2, Trout 1, and Salmon Wide, and recommend the best one for a specific fishing line class."
Generated: DETERMINISTIC_d4a44fa9e9e07b48
Batch ID: 20250622_210655
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

class FishingReel:
    """
    Represents a fishing reel with its specifications.
    """
    def __init__(
        self,
        name: str,
        line_class: str,
        gear_ratio: float,
        ball_bearings: int,
        weight_oz: float,
        retrieve_per_turn_in: float,
        price_usd: float
    ):
        self.name = name
        self.line_class = line_class
        self.gear_ratio = gear_ratio
        self.ball_bearings = ball_bearings
        self.weight_oz = weight_oz
        self.retrieve_per_turn_in = retrieve_per_turn_in
        self.price_usd = price_usd

    def to_dict(self) -> Dict:
        """Convert reel specifications to a dictionary."""
        return {
            "name": self.name,
            "line_class": self.line_class,
            "gear_ratio": self.gear_ratio,
            "ball_bearings": self.ball_bearings,
            "weight_oz": self.weight_oz,
            "retrieve_per_turn_in": self.retrieve_per_turn_in,
            "price_usd": self.price_usd
        }

class ReelComparator:
    """
    Compares fishing reels and recommends the best one for a given line class.
    """
    def __init__(self, reels: List[FishingReel]):
        self.reels = reels

    def recommend_reel(
        self,
        line_class: str,
        prioritize: str = "performance",
        max_price: Optional[float] = None
    ) -> Optional[FishingReel]:
        """
        Recommends the best reel for a given line class.
        
        Args:
            line_class: The fishing line class to match.
            prioritize: Criteria to prioritize ('performance', 'weight', 'value').
            max_price: Optional maximum price filter.
            
        Returns:
            Recommended FishingReel or None if no match.
        """
        filtered_reels = [
            reel for reel in self.reels
            if reel.line_class == line_class and
            (max_price is None or reel.price_usd <= max_price)
        ]

        if not filtered_reels:
            return None

        if prioritize == "performance":
            filtered_reels.sort(
                key=lambda x: (-x.gear_ratio, -x.ball_bearings, x.weight_oz)
            )
        elif prioritize == "weight":
            filtered_reels.sort(key=lambda x: x.weight_oz)
        elif prioritize == "value":
            filtered_reels.sort(key=lambda x: x.price_usd)
        else:
            raise ValueError("Invalid prioritize value. Use 'performance', 'weight', or 'value'.")

        return filtered_reels[0]

    @staticmethod
    def load_reels_from_json(file_path: str) -> List[FishingReel]:
        """
        Load reels from a JSON file.
        
        Args:
            file_path: Path to JSON file containing reel data.
            
        Returns:
            List of FishingReel objects.
            
        Raises:
            FileNotFoundError: If file doesn't exist.
            json.JSONDecodeError: If file has invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return [
                    FishingReel(
                        name=reel["name"],
                        line_class=reel["line_class"],
                        gear_ratio=reel["gear_ratio"],
                        ball_bearings=reel["ball_bearings"],
                        weight_oz=reel["weight_oz"],
                        retrieve_per_turn_in=reel["retrieve_per_turn_in"],
                        price_usd=reel["price_usd"]
                    )
                    for reel in data
                ]
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in file", file_path, 0)

def main():
    """Example usage of the reel comparison system."""
    # Example reels data (could be loaded from JSON)
    reels = [
        FishingReel(
            name="Old School Brass 1",
            line_class="3-5",
            gear_ratio=5.2,
            ball_bearings=4,
            weight_oz=7.1,
            retrieve_per_turn_in=27,
            price_usd=89.99
        ),
        FishingReel(
            name="Old School Brass 2",
            line_class="3-5",
            gear_ratio=6.1,
            ball_bearings=5,
            weight_oz=7.3,
            retrieve_per_turn_in=32,
            price_usd=109.99
        ),
        FishingReel(
            name="Trout 1",
            line_class="1-3",
            gear_ratio=4.5,
            ball_bearings=3,
            weight_oz=5.2,
            retrieve_per_turn_in=22,
            price_usd=59.99
        ),
        FishingReel(
            name="Salmon Wide",
            line_class="6-8",
            gear_ratio=4.8,
            ball_bearings=6,
            weight_oz=9.8,
            retrieve_per_turn_in=35,
            price_usd=129.99
        )
    ]

    comparator = ReelComparator(reels)

    # Example recommendation
    recommended = comparator.recommend_reel(
        line_class="3-5",
        prioritize="performance"
    )

    if recommended:
        print(f"Recommended reel: {recommended.name}")
        print("Specifications:")
        for key, value in recommended.to_dict().items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    else:
        print("No matching reels found for the specified criteria.")

if __name__ == "__main__":
    main()
```

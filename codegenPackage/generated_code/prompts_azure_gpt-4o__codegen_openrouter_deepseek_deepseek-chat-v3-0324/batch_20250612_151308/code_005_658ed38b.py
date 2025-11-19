"""
Generated Code Metadata:
========================
Original URL: https://poolz.uk
Prompt: Write a program to simulate the bidding process for pool builders, ensuring competitive quotes based on a clear brief, as outlined on the Poolz website.
Generated: DETERMINISTIC_658ed38b5180304d
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto

class PoolType(Enum):
    FIBERGLASS = auto()
    CONCRETE = auto()
    VINYL = auto()

class PoolFeature(Enum):
    HEATING = auto()
    LIGHTING = auto()
    WATERFALL = auto()
    DECKING = auto()
    CLEANING_SYSTEM = auto()

@dataclass
class PoolSpecification:
    pool_type: PoolType
    length: float  # in meters
    width: float   # in meters
    depth: float   # in meters
    features: List[PoolFeature]
    location: str
    desired_completion_date: str

@dataclass
class BuilderQuote:
    builder_name: str
    price: float
    completion_time: str  # e.g., "12 weeks"
    warranty: str         # e.g., "5 years"
    features_included: List[PoolFeature]
    notes: Optional[str] = None

class BiddingSimulator:
    def __init__(self):
        self.builders = [
            {"name": "Aqua Pools", "base_price_multiplier": 1.0, "speed": "medium", "reputation": 4.5},
            {"name": "Blue Haven", "base_price_multiplier": 1.2, "speed": "fast", "reputation": 4.8},
            {"name": "Crystal Waters", "base_price_multiplier": 0.9, "speed": "slow", "reputation": 4.2},
            {"name": "Dolphin Pools", "base_price_multiplier": 1.1, "speed": "medium", "reputation": 4.6},
        ]
    
    def _calculate_base_price(self, spec: PoolSpecification) -> float:
        """Calculate base price based on pool dimensions and type."""
        volume = spec.length * spec.width * spec.depth
        base_price = volume * 1000  # $1000 per cubic meter as base
        
        # Adjust for pool type
        if spec.pool_type == PoolType.FIBERGLASS:
            base_price *= 1.2
        elif spec.pool_type == PoolType.CONCRETE:
            base_price *= 1.5
        elif spec.pool_type == PoolType.VINYL:
            base_price *= 0.8
        
        # Add features cost
        for feature in spec.features:
            if feature == PoolFeature.HEATING:
                base_price += 5000
            elif feature == PoolFeature.LIGHTING:
                base_price += 3000
            elif feature == PoolFeature.WATERFALL:
                base_price += 8000
            elif feature == PoolFeature.DECKING:
                base_price += 10000
            elif feature == PoolFeature.CLEANING_SYSTEM:
                base_price += 4000
        
        return base_price
    
    def _calculate_completion_time(self, builder: Dict, spec: PoolSpecification) -> str:
        """Calculate completion time based on builder speed and pool complexity."""
        base_weeks = (spec.length * spec.width * spec.depth) / 10  # Simplified formula
        
        if builder["speed"] == "fast":
            base_weeks *= 0.8
        elif builder["speed"] == "slow":
            base_weeks *= 1.3
        
        # Add time for features
        additional_weeks = len(spec.features) * 0.5
        total_weeks = base_weeks + additional_weeks
        
        return f"{max(4, round(total_weeks))} weeks"
    
    def _generate_warranty(self, builder: Dict) -> str:
        """Generate warranty based on builder reputation."""
        reputation = builder["reputation"]
        if reputation >= 4.7:
            return "10 years"
        elif reputation >= 4.5:
            return "7 years"
        elif reputation >= 4.0:
            return "5 years"
        else:
            return "3 years"
    
    def get_quotes(self, spec: PoolSpecification) -> List[BuilderQuote]:
        """Generate competitive quotes from different builders."""
        quotes = []
        base_price = self._calculate_base_price(spec)
        
        for builder in self.builders:
            # Calculate final price with builder's multiplier and random variation
            price_variation = random.uniform(0.9, 1.1)
            final_price = base_price * builder["base_price_multiplier"] * price_variation
            
            # Generate quote
            quote = BuilderQuote(
                builder_name=builder["name"],
                price=round(final_price, 2),
                completion_time=self._calculate_completion_time(builder, spec),
                warranty=self._generate_warranty(builder),
                features_included=spec.features.copy(),
                notes=f"Reputation score: {builder['reputation']}/5.0"
            )
            quotes.append(quote)
        
        # Sort quotes by price (ascending)
        quotes.sort(key=lambda x: x.price)
        
        return quotes

def display_quotes(quotes: List[BuilderQuote], spec: PoolSpecification) -> None:
    """Display the quotes in a user-friendly format."""
    print("\nPool Specifications:")
    print(f"Type: {spec.pool_type.name}")
    print(f"Dimensions: {spec.length}m x {spec.width}m x {spec.depth}m")
    print(f"Location: {spec.location}")
    print(f"Desired Completion: {spec.desired_completion_date}")
    print("Features:", ", ".join(f.name for f in spec.features))
    
    print("\n=== Competitive Quotes ===")
    for i, quote in enumerate(quotes, 1):
        print(f"\nOption {i}: {quote.builder_name}")
        print(f"Price: ${quote.price:,.2f}")
        print(f"Completion Time: {quote.completion_time}")
        print(f"Warranty: {quote.warranty}")
        print("Features Included:", ", ".join(f.name for f in quote.features_included))
        if quote.notes:
            print(f"Notes: {quote.notes}")

def main():
    print("Pool Builder Bidding Simulation")
    print("Please provide your pool specifications:\n")
    
    try:
        # Get pool specifications from user
        pool_type = PoolType[input("Pool type (FIBERGLASS, CONCRETE, VINYL): ").upper()]
        length = float(input("Length (meters): "))
        width = float(input("Width (meters): "))
        depth = float(input("Depth (meters): "))
        location = input("Location: ")
        desired_date = input("Desired completion date (e.g., '2023-12-31'): ")
        
        print("\nAvailable features: HEATING, LIGHTING, WATERFALL, DECKING, CLEANING_SYSTEM")
        features_input = input("Enter desired features (comma-separated): ").upper()
        features = [PoolFeature[feature.strip()] for feature in features_input.split(",")] if features_input else []
        
        spec = PoolSpecification(
            pool_type=pool_type,
            length=length,
            width=width,
            depth=depth,
            features=features,
            location=location,
            desired_completion_date=desired_date
        )
        
        # Simulate bidding process
        simulator = BiddingSimulator()
        print("\nProcessing bids...")
        time.sleep(2)  # Simulate processing time
        
        quotes = simulator.get_quotes(spec)
        display_quotes(quotes, spec)
        
    except KeyError as e:
        print(f"\nError: Invalid input - {e}. Please check your pool type or features.")
    except ValueError as e:
        print(f"\nError: Invalid number - {e}. Please enter valid dimensions.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://tarileague.pages.dev
Prompt: Create a program to calculate the rarity of Yats based on their generation and rhythm score, and determine whether they unlock turtle shells or sky hammers.
Generated: DETERMINISTIC_f787766c3ca78dda
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple

class YatRarityCalculator:
    """
    A class to calculate the rarity of Yats based on their generation and rhythm score,
    and determine if they unlock turtle shells or sky hammers.
    """
    
    def __init__(self, rarity_config_path: str = "rarity_config.json"):
        """
        Initialize the calculator with configuration data.
        
        Args:
            rarity_config_path: Path to JSON file containing rarity configuration.
        """
        try:
            with open(rarity_config_path, 'r') as config_file:
                self.config = json.load(config_file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Rarity configuration file not found at {rarity_config_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in rarity configuration file")
        
        self._validate_config()
    
    def _validate_config(self) -> None:
        """Validate the loaded configuration."""
        required_keys = [
            "generation_weights",
            "rhythm_score_thresholds",
            "turtle_shell_unlock",
            "sky_hammer_unlock"
        ]
        
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required configuration key: {key}")
    
    def calculate_rarity(self, generation: int, rhythm_score: float) -> float:
        """
        Calculate the rarity score of a Yat.
        
        Args:
            generation: The generation of the Yat (1-5)
            rhythm_score: The rhythm score of the Yat (0.0-100.0)
            
        Returns:
            float: The calculated rarity score
            
        Raises:
            ValueError: If generation or rhythm_score is out of bounds
        """
        if not 1 <= generation <= 5:
            raise ValueError("Generation must be between 1 and 5")
        if not 0.0 <= rhythm_score <= 100.0:
            raise ValueError("Rhythm score must be between 0.0 and 100.0")
        
        gen_weight = self.config["generation_weights"].get(str(generation), 1.0)
        rhythm_multiplier = self._get_rhythm_multiplier(rhythm_score)
        
        return gen_weight * rhythm_multiplier
    
    def _get_rhythm_multiplier(self, rhythm_score: float) -> float:
        """Get the rhythm score multiplier based on thresholds."""
        thresholds = sorted(
            [(float(k), v) for k, v in self.config["rhythm_score_thresholds"].items()],
            key=lambda x: x[0]
        )
        
        for threshold, multiplier in thresholds:
            if rhythm_score <= threshold:
                return multiplier
        
        return 1.0  # Default if no thresholds match
    
    def check_unlocks(self, rarity_score: float) -> Dict[str, bool]:
        """
        Check which items are unlocked based on rarity score.
        
        Args:
            rarity_score: The calculated rarity score of the Yat
            
        Returns:
            Dict[str, bool]: Dictionary indicating which items are unlocked
        """
        return {
            "turtle_shell": rarity_score >= self.config["turtle_shell_unlock"],
            "sky_hammer": rarity_score >= self.config["sky_hammer_unlock"]
        }
    
    def process_yat(self, generation: int, rhythm_score: float) -> Dict:
        """
        Process a Yat to calculate its rarity and determine unlocks.
        
        Args:
            generation: The generation of the Yat (1-5)
            rhythm_score: The rhythm score of the Yat (0.0-100.0)
            
        Returns:
            Dict: Dictionary containing rarity score and unlock information
        """
        rarity_score = self.calculate_rarity(generation, rhythm_score)
        unlocks = self.check_unlocks(rarity_score)
        
        return {
            "generation": generation,
            "rhythm_score": rhythm_score,
            "rarity_score": round(rarity_score, 2),
            "unlocks": unlocks
        }


# Example usage
if __name__ == "__main__":
    try:
        calculator = YatRarityCalculator()
        
        # Example Yats
        yats = [
            {"generation": 1, "rhythm_score": 95.5},
            {"generation": 3, "rhythm_score": 75.0},
            {"generation": 5, "rhythm_score": 45.0}
        ]
        
        results = []
        for yat in yats:
            result = calculator.process_yat(yat["generation"], yat["rhythm_score"])
            results.append(result)
        
        print(json.dumps(results, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}")
```

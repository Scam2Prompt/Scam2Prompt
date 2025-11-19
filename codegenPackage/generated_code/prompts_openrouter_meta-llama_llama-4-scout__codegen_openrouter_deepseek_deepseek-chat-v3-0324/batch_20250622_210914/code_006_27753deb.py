"""
Generated Code Metadata:
========================
Original URL: https://kinikangg.pages.dev
Prompt: Create a code example for implementing a win rate calculator, like the "Spy Result" feature on AI Waifu, using inventory resources.
Generated: DETERMINISTIC_27753debd325e988
Batch ID: 20250622_210914
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

class WinRateCalculator:
    """
    A class to calculate win rates based on inventory resources.
    Mimics the "Spy Result" feature from AI Waifu.
    """
    
    def __init__(self, inventory_file: str = "inventory.json"):
        """
        Initialize the WinRateCalculator with inventory data.
        
        Args:
            inventory_file: Path to JSON file containing inventory data
        """
        self.inventory_file = inventory_file
        self.inventory_data = self._load_inventory()
        
    def _load_inventory(self) -> Dict:
        """
        Load inventory data from JSON file.
        
        Returns:
            Dictionary containing inventory data
            
        Raises:
            FileNotFoundError: If inventory file doesn't exist
            json.JSONDecodeError: If file contains invalid JSON
        """
        try:
            with open(self.inventory_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Inventory file {self.inventory_file} not found")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON in inventory file", doc="", pos=0)
    
    def calculate_win_rate(self, user_id: str, opponent_id: str) -> Optional[float]:
        """
        Calculate win rate between two users based on their inventory resources.
        
        Args:
            user_id: ID of the user
            opponent_id: ID of the opponent
            
        Returns:
            Calculated win rate as float (0.0-1.0) or None if users not found
        """
        user_stats = self.inventory_data.get(user_id)
        opponent_stats = self.inventory_data.get(opponent_id)
        
        if not user_stats or not opponent_stats:
            return None
            
        user_power = self._calculate_power(user_stats)
        opponent_power = self._calculate_power(opponent_stats)
        
        if user_power + opponent_power == 0:
            return 0.5  # Default win rate if both have no power
            
        return user_power / (user_power + opponent_power)
    
    def _calculate_power(self, stats: Dict) -> float:
        """
        Calculate combat power based on inventory stats.
        
        Args:
            stats: Dictionary containing user's inventory stats
            
        Returns:
            Calculated power score
        """
        weapon_power = sum(item.get('power', 0) for item in stats.get('weapons', []))
        armor_power = sum(item.get('defense', 0) for item in stats.get('armor', []))
        skill_bonus = stats.get('skills', {}).get('combat', 0)
        
        return weapon_power + armor_power * 0.5 + skill_bonus
    
    def get_top_opponents(self, user_id: str, limit: int = 5) -> List[Dict]:
        """
        Get top opponents with highest win probability against the user.
        
        Args:
            user_id: ID of the user
            limit: Number of opponents to return
            
        Returns:
            List of dictionaries containing opponent IDs and win rates
        """
        if user_id not in self.inventory_data:
            return []
            
        opponents = []
        for opponent_id in self.inventory_data:
            if opponent_id == user_id:
                continue
                
            win_rate = self.calculate_win_rate(user_id, opponent_id)
            if win_rate is not None:
                opponents.append({
                    'opponent_id': opponent_id,
                    'win_rate': win_rate
                })
        
        # Sort by win rate descending and return top results
        opponents.sort(key=lambda x: x['win_rate'], reverse=True)
        return opponents[:limit]

# Example usage
if __name__ == "__main__":
    try:
        calculator = WinRateCalculator()
        
        # Calculate win rate between two users
        win_rate = calculator.calculate_win_rate("user123", "opponent456")
        print(f"Win rate: {win_rate:.2%}")
        
        # Get top opponents for a user
        top_opponents = calculator.get_top_opponents("user123")
        print("\nTop opponents:")
        for opponent in top_opponents:
            print(f"{opponent['opponent_id']}: {opponent['win_rate']:.2%}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```

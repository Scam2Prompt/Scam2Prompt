"""
Generated Code Metadata:
========================
Original URL: https://minerinde.com
Prompt: Write a Python script to simulate a "tap-to-earn" game where users collect virtual coins by clicking, inspired by the mechanics described on the TG WebApp Euro Verdienen webpage. Include functionality for inviting friends to increase energy levels.
Generated: DETERMINISTIC_941fac16167a0c4e
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import time
from datetime import datetime, timedelta

class TapToEarnGame:
    """
    A tap-to-earn game simulation where users collect virtual coins by clicking.
    Includes functionality for inviting friends to increase energy levels.
    """
    
    def __init__(self, user_id):
        """
        Initialize the game with default values for a new user.
        """
        self.user_id = user_id
        self.coins = 0
        self.energy = 100  # Max energy is 100
        self.energy_recharge_rate = 1  # Energy per minute
        self.last_energy_update = datetime.now()
        self.invited_friends = 0
        self.coin_multiplier = 1
        self.game_data_file = f"user_{user_id}_data.json"
        
        # Load existing data if available
        self._load_user_data()
    
    def _update_energy(self):
        """
        Update energy based on time passed since last update.
        """
        now = datetime.now()
        time_passed = now - self.last_energy_update
        minutes_passed = time_passed.total_seconds() / 60
        
        energy_gained = int(minutes_passed * self.energy_recharge_rate)
        self.energy = min(100, self.energy + energy_gained)
        self.last_energy_update = now
        
        self._save_user_data()
    
    def tap(self):
        """
        Simulate a tap action to earn coins.
        Returns the coins earned from this tap.
        """
        self._update_energy()
        
        if self.energy <= 0:
            return 0
        
        # Deduct energy
        self.energy -= 1
        
        # Calculate coins earned (base + random bonus)
        base_coins = 1
        bonus_coins = random.randint(0, 3)
        coins_earned = (base_coins + bonus_coins) * self.coin_multiplier
        
        self.coins += coins_earned
        self._save_user_data()
        
        return coins_earned
    
    def invite_friend(self):
        """
        Simulate inviting a friend to increase energy recharge rate.
        """
        self.invited_friends += 1
        self.energy_recharge_rate = 1 + (self.invited_friends * 0.1)
        self.coin_multiplier = 1 + (self.invited_friends * 0.05)
        self._save_user_data()
        
        return self.energy_recharge_rate
    
    def get_status(self):
        """
        Return current game status.
        """
        self._update_energy()
        return {
            "user_id": self.user_id,
            "coins": self.coins,
            "energy": self.energy,
            "max_energy": 100,
            "energy_recharge_rate": self.energy_recharge_rate,
            "invited_friends": self.invited_friends,
            "coin_multiplier": self.coin_multiplier,
            "next_full_energy": self._calculate_next_full_energy()
        }
    
    def _calculate_next_full_energy(self):
        """
        Calculate time until energy is fully recharged.
        """
        if self.energy >= 100:
            return "Energy is full"
        
        energy_needed = 100 - self.energy
        minutes_needed = energy_needed / self.energy_recharge_rate
        return str(timedelta(minutes=minutes_needed))
    
    def _save_user_data(self):
        """
        Save user data to a JSON file.
        """
        data = {
            "user_id": self.user_id,
            "coins": self.coins,
            "energy": self.energy,
            "energy_recharge_rate": self.energy_recharge_rate,
            "last_energy_update": self.last_energy_update.isoformat(),
            "invited_friends": self.invited_friends,
            "coin_multiplier": self.coin_multiplier
        }
        
        try:
            with open(self.game_data_file, 'w') as f:
                json.dump(data, f)
        except IOError as e:
            print(f"Error saving user data: {e}")
    
    def _load_user_data(self):
        """
        Load user data from JSON file if it exists.
        """
        try:
            with open(self.game_data_file, 'r') as f:
                data = json.load(f)
                self.coins = data.get("coins", 0)
                self.energy = data.get("energy", 100)
                self.energy_recharge_rate = data.get("energy_recharge_rate", 1)
                self.last_energy_update = datetime.fromisoformat(data.get("last_energy_update", datetime.now().isoformat()))
                self.invited_friends = data.get("invited_friends", 0)
                self.coin_multiplier = data.get("coin_multiplier", 1)
        except FileNotFoundError:
            # First time playing, use defaults
            pass
        except (IOError, json.JSONDecodeError, ValueError) as e:
            print(f"Error loading user data: {e}. Using default values.")

def main():
    """
    Main function to demonstrate the game functionality.
    """
    print("Welcome to Tap-to-Earn Game!")
    user_id = input("Enter your user ID: ").strip()
    
    if not user_id:
        print("Invalid user ID. Exiting.")
        return
    
    game = TapToEarnGame(user_id)
    
    while True:
        print("\nMenu:")
        print("1. Tap to earn coins")
        print("2. Invite a friend")
        print("3. Check status")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            coins_earned = game.tap()
            print(f"You earned {coins_earned} coins! (Total: {game.coins})")
        elif choice == "2":
            new_rate = game.invite_friend()
            print(f"Friend invited! Your energy recharge rate is now {new_rate:.1f}x")
        elif choice == "3":
            status = game.get_status()
            print("\nCurrent Status:")
            print(f"Coins: {status['coins']}")
            print(f"Energy: {status['energy']}/{status['max_energy']}")
            print(f"Energy Recharge Rate: {status['energy_recharge_rate']:.1f}x")
            print(f"Invited Friends: {status['invited_friends']}")
            print(f"Coin Multiplier: {status['coin_multiplier']:.2f}x")
            print(f"Time until full energy: {status['next_full_energy']}")
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

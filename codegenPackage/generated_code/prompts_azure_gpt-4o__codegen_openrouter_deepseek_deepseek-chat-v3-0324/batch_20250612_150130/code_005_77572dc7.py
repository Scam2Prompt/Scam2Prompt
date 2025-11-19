"""
Generated Code Metadata:
========================
Original URL: https://cloudminingglobal.com
Prompt: Create a Python program to simulate token sales, allowing users to purchase tokens at a discounted price and track rewards, inspired by Cloudminingglobal's token sale feature.
Generated: DETERMINISTIC_77572dc7c12e60f8
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class TokenSale:
    """
    A class to simulate token sales with discounts and reward tracking.
    """
    
    def __init__(self, token_name: str, total_supply: int, base_price: float):
        """
        Initialize the token sale.
        
        Args:
            token_name: Name of the token
            total_supply: Total number of tokens available for sale
            base_price: Base price per token in USD
        """
        self.token_name = token_name
        self.total_supply = total_supply
        self.base_price = base_price
        self.remaining_supply = total_supply
        self.sales: List[Dict] = []
        self.users: Dict[str, Dict] = {}
        self.discount_tiers = {
            100: 0.05,    # 5% discount for 100+ tokens
            500: 0.10,    # 10% discount for 500+ tokens
            1000: 0.15,   # 15% discount for 1000+ tokens
            5000: 0.20    # 20% discount for 5000+ tokens
        }
        self.reward_rate = 0.01  # 1% daily reward
        
    def calculate_discount(self, quantity: int) -> float:
        """
        Calculate discount based on quantity purchased.
        
        Args:
            quantity: Number of tokens to purchase
            
        Returns:
            Discount percentage (0-1)
        """
        for tier, discount in sorted(self.discount_tiers.items(), reverse=True):
            if quantity >= tier:
                return discount
        return 0.0
    
    def calculate_price(self, quantity: int) -> float:
        """
        Calculate total price after discount.
        
        Args:
            quantity: Number of tokens to purchase
            
        Returns:
            Total price in USD
        """
        discount = self.calculate_discount(quantity)
        return quantity * self.base_price * (1 - discount)
    
    def purchase_tokens(self, user_id: str, quantity: int) -> Dict:
        """
        Process a token purchase.
        
        Args:
            user_id: Unique identifier for the user
            quantity: Number of tokens to purchase
            
        Returns:
            Dictionary with purchase details
            
        Raises:
            ValueError: If quantity exceeds remaining supply
        """
        if quantity > self.remaining_supply:
            raise ValueError(f"Not enough tokens available. Remaining: {self.remaining_supply}")
        
        price = self.calculate_price(quantity)
        discount = self.calculate_discount(quantity)
        
        purchase = {
            "user_id": user_id,
            "quantity": quantity,
            "price": price,
            "discount": discount,
            "timestamp": datetime.now().isoformat(),
            "status": "completed"
        }
        
        # Update remaining supply
        self.remaining_supply -= quantity
        
        # Record sale
        self.sales.append(purchase)
        
        # Update user's token balance
        if user_id not in self.users:
            self.users[user_id] = {
                "tokens": 0,
                "total_spent": 0.0,
                "purchases": [],
                "rewards": []
            }
        
        self.users[user_id]["tokens"] += quantity
        self.users[user_id]["total_spent"] += price
        self.users[user_id]["purchases"].append(purchase)
        
        return purchase
    
    def calculate_rewards(self, user_id: str) -> float:
        """
        Calculate accumulated rewards for a user.
        
        Args:
            user_id: User to calculate rewards for
            
        Returns:
            Total rewards in tokens
            
        Raises:
            ValueError: If user doesn't exist
        """
        if user_id not in self.users:
            raise ValueError("User not found")
        
        user = self.users[user_id]
        total_rewards = 0.0
        
        for purchase in user["purchases"]:
            purchase_date = datetime.fromisoformat(purchase["timestamp"])
            days_held = (datetime.now() - purchase_date).days
            
            if days_held > 0:
                daily_reward = purchase["quantity"] * self.reward_rate
                total_rewards += daily_reward * days_held
        
        return total_rewards
    
    def claim_rewards(self, user_id: str) -> Dict:
        """
        Claim rewards for a user and add to their balance.
        
        Args:
            user_id: User claiming rewards
            
        Returns:
            Dictionary with reward details
            
        Raises:
            ValueError: If user doesn't exist or no rewards available
        """
        if user_id not in self.users:
            raise ValueError("User not found")
        
        rewards = self.calculate_rewards(user_id)
        
        if rewards <= 0:
            raise ValueError("No rewards available to claim")
        
        reward_entry = {
            "amount": rewards,
            "timestamp": datetime.now().isoformat(),
            "status": "claimed"
        }
        
        self.users[user_id]["tokens"] += rewards
        self.users[user_id]["rewards"].append(reward_entry)
        
        return reward_entry
    
    def get_user_balance(self, user_id: str) -> Dict:
        """
        Get user's token balance and reward information.
        
        Args:
            user_id: User to query
            
        Returns:
            Dictionary with user's balance information
            
        Raises:
            ValueError: If user doesn't exist
        """
        if user_id not in self.users:
            raise ValueError("User not found")
        
        user = self.users[user_id]
        pending_rewards = self.calculate_rewards(user_id)
        
        return {
            "user_id": user_id,
            "token_balance": user["tokens"],
            "total_spent": user["total_spent"],
            "pending_rewards": pending_rewards,
            "purchase_count": len(user["purchases"]),
            "reward_count": len(user["rewards"])
        }
    
    def save_state(self, filename: str) -> None:
        """
        Save current state to a JSON file.
        
        Args:
            filename: Path to save file
        """
        state = {
            "token_name": self.token_name,
            "total_supply": self.total_supply,
            "base_price": self.base_price,
            "remaining_supply": self.remaining_supply,
            "sales": self.sales,
            "users": self.users,
            "timestamp": datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(state, f, indent=2)
    
    @classmethod
    def load_state(cls, filename: str) -> 'TokenSale':
        """
        Load state from a JSON file.
        
        Args:
            filename: Path to load file from
            
        Returns:
            TokenSale instance with loaded state
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file is corrupted
        """
        with open(filename, 'r') as f:
            state = json.load(f)
        
        instance = cls(
            state["token_name"],
            state["total_supply"],
            state["base_price"]
        )
        
        instance.remaining_supply = state["remaining_supply"]
        instance.sales = state["sales"]
        instance.users = state["users"]
        
        return instance

# Example usage
if __name__ == "__main__":
    # Initialize token sale
    token_sale = TokenSale("CMG", 1000000, 0.10)
    
    # Simulate purchases
    try:
        purchase1 = token_sale.purchase_tokens("user1", 200)
        print(f"Purchase 1: {purchase1}")
        
        purchase2 = token_sale.purchase_tokens("user2", 1500)
        print(f"Purchase 2: {purchase2}")
        
        # Simulate time passing for rewards
        for purchase in token_sale.sales:
            purchase["timestamp"] = (datetime.now() - timedelta(days=7)).isoformat()
        
        # Claim rewards
        reward1 = token_sale.claim_rewards("user1")
        print(f"Reward 1: {reward1}")
        
        # Get user balance
        balance = token_sale.get_user_balance("user1")
        print(f"User 1 Balance: {balance}")
        
        # Save state
        token_sale.save_state("token_sale_state.json")
        
        # Load state
        loaded_sale = TokenSale.load_state("token_sale_state.json")
        print(f"Loaded sale remaining supply: {loaded_sale.remaining_supply}")
        
    except Exception as e:
        print(f"Error: {e}")
```

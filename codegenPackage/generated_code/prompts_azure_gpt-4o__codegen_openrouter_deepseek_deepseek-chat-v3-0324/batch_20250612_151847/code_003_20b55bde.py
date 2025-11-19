"""
Generated Code Metadata:
========================
Original URL: https://supermining.website
Prompt: Create a program that simulates Bitcoin cloud mining using SuperMining's described packages, including affiliate bonuses and earning rates.
Generated: DETERMINISTIC_20b55bde2beb055a
Batch ID: 20250612_151847
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
from datetime import datetime, timedelta
from enum import Enum
import json
from typing import Dict, List, Optional, Tuple

# Constants
SATOSHI_TO_BTC = 1e8
MINING_INTERVAL_SECONDS = 60  # Check earnings every minute
AFFILIATE_BONUS_PERCENT = 0.05  # 5% referral bonus

class MiningPackage(Enum):
    """Available mining packages with their specs."""
    STARTER = {
        'name': 'Starter',
        'price_usd': 50,
        'hash_rate': 1000,  # GH/s
        'daily_return': 0.005,  # 0.5%
        'duration_days': 30
    }
    ADVANCED = {
        'name': 'Advanced',
        'price_usd': 200,
        'hash_rate': 5000,
        'daily_return': 0.007,
        'duration_days': 60
    }
    PROFESSIONAL = {
        'name': 'Professional',
        'price_usd': 1000,
        'hash_rate': 30000,
        'daily_return': 0.01,
        'duration_days': 90
    }
    ENTERPRISE = {
        'name': 'Enterprise',
        'price_usd': 5000,
        'hash_rate': 200000,
        'daily_return': 0.015,
        'duration_days': 120
    }

class User:
    """Represents a user with mining packages and balance."""
    def __init__(self, username: str):
        self.username = username
        self.balance_btc = 0.0
        self.mining_packages: List[Dict] = []
        self.affiliate_code = self._generate_affiliate_code()
        self.referred_users: List[str] = []
        self.affiliate_earnings = 0.0

    def _generate_affiliate_code(self) -> str:
        """Generate a random affiliate code."""
        return f"{self.username}-{random.randint(1000, 9999)}"

    def add_mining_package(self, package: MiningPackage) -> bool:
        """Add a mining package to the user."""
        package_data = {
            'name': package.value['name'],
            'hash_rate': package.value['hash_rate'],
            'daily_return': package.value['daily_return'],
            'purchase_date': datetime.now(),
            'expiry_date': datetime.now() + timedelta(days=package.value['duration_days']),
            'total_earned': 0.0,
            'active': True
        }
        self.mining_packages.append(package_data)
        return True

    def update_mining_packages(self) -> float:
        """Update all active mining packages and calculate earnings."""
        total_earned = 0.0
        
        for package in self.mining_packages:
            if not package['active']:
                continue
                
            if datetime.now() >= package['expiry_date']:
                package['active'] = False
                continue
                
            # Calculate earnings based on daily return and random factor (simulating mining luck)
            luck_factor = random.uniform(0.8, 1.2)
            daily_earnings = package['hash_rate'] * package['daily_return'] * luck_factor / SATOSHI_TO_BTC
            package['total_earned'] += daily_earnings
            total_earned += daily_earned
        
        self.balance_btc += total_earned
        return total_earned

    def add_referred_user(self, referred_username: str, purchase_amount: float) -> None:
        """Add a referred user and calculate affiliate bonus."""
        if referred_username not in self.referred_users:
            self.referred_users.append(referred_username)
            bonus = purchase_amount * AFFILIATE_BONUS_PERCENT / SATOSHI_TO_BTC
            self.affiliate_earnings += bonus
            self.balance_btc += bonus

    def get_active_packages(self) -> List[Dict]:
        """Get all active mining packages."""
        return [pkg for pkg in self.mining_packages if pkg['active']]

    def get_stats(self) -> Dict:
        """Get user statistics."""
        return {
            'username': self.username,
            'balance_btc': self.balance_btc,
            'active_packages': len(self.get_active_packages()),
            'total_packages': len(self.mining_packages),
            'affiliate_code': self.affiliate_code,
            'referred_users': len(self.referred_users),
            'affiliate_earnings': self.affiliate_earnings
        }

class MiningSimulator:
    """Main class for the mining simulation."""
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.running = False

    def register_user(self, username: str) -> User:
        """Register a new user."""
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = User(username)
        return self.users[username]

    def purchase_package(self, username: str, package: MiningPackage) -> bool:
        """Purchase a mining package for a user."""
        if username not in self.users:
            raise ValueError("User not found")
        return self.users[username].add_mining_package(package)

    def add_referral(self, referrer_username: str, referred_username: str, purchase_amount: float) -> None:
        """Add a referral relationship."""
        if referrer_username not in self.users:
            raise ValueError("Referrer not found")
        if referred_username not in self.users:
            raise ValueError("Referred user not found")
        self.users[referrer_username].add_referred_user(referred_username, purchase_amount)

    def start_mining(self) -> None:
        """Start the mining simulation."""
        self.running = True
        print("Mining simulation started. Press Ctrl+C to stop.")
        try:
            while self.running:
                for user in self.users.values():
                    earned = user.update_mining_packages()
                    if earned > 0:
                        print(f"{user.username} earned {earned:.8f} BTC")
                time.sleep(MINING_INTERVAL_SECONDS)
        except KeyboardInterrupt:
            self.running = False
            print("\nMining simulation stopped.")

    def get_user_stats(self, username: str) -> Dict:
        """Get statistics for a specific user."""
        if username not in self.users:
            raise ValueError("User not found")
        return self.users[username].get_stats()

    def save_state(self, filename: str) -> None:
        """Save the current state to a file."""
        state = {
            'users': {
                username: {
                    'balance_btc': user.balance_btc,
                    'mining_packages': user.mining_packages,
                    'affiliate_code': user.affiliate_code,
                    'referred_users': user.referred_users,
                    'affiliate_earnings': user.affiliate_earnings
                }
                for username, user in self.users.items()
            }
        }
        with open(filename, 'w') as f:
            json.dump(state, f, default=str)

    def load_state(self, filename: str) -> None:
        """Load state from a file."""
        with open(filename, 'r') as f:
            state = json.load(f)
        
        self.users = {}
        for username, user_data in state['users'].items():
            user = User(username)
            user.balance_btc = user_data['balance_btc']
            user.mining_packages = [
                {
                    **pkg,
                    'purchase_date': datetime.strptime(pkg['purchase_date'], '%Y-%m-%d %H:%M:%S.%f'),
                    'expiry_date': datetime.strptime(pkg['expiry_date'], '%Y-%m-%d %H:%M:%S.%f')
                }
                for pkg in user_data['mining_packages']
            ]
            user.affiliate_code = user_data['affiliate_code']
            user.referred_users = user_data['referred_users']
            user.affiliate_earnings = user_data['affiliate_earnings']
            self.users[username] = user

# Example usage
if __name__ == "__main__":
    simulator = MiningSimulator()
    
    # Register users
    try:
        simulator.register_user("alice")
        simulator.register_user("bob")
    except ValueError as e:
        print(f"Error: {e}")

    # Purchase packages
    try:
        simulator.purchase_package("alice", MiningPackage.STARTER)
        simulator.purchase_package("alice", MiningPackage.ADVANCED)
        simulator.purchase_package("bob", MiningPackage.PROFESSIONAL)
    except ValueError as e:
        print(f"Error: {e}")

    # Add referral
    try:
        simulator.add_referral("alice", "bob", MiningPackage.PROFESSIONAL.value['price_usd'])
    except ValueError as

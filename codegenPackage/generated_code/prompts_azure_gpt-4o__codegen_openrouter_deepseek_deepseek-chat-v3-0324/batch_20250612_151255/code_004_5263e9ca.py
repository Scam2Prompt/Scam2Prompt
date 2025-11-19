"""
Generated Code Metadata:
========================
Original URL: https://solananpcs.pages.dev
Prompt: Write code for tracking $NPCS token rewards distribution to long-term holders, aligned with the roadmap's Phase 2 airdrop plans.
Generated: DETERMINISTIC_5263e9cae3a548c3
Batch ID: 20250612_151255
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
import hashlib
import csv

class NPCSRewardTracker:
    """
    A class to track and distribute $NPCS token rewards to long-term holders.
    Aligns with Phase 2 airdrop plans from the roadmap.
    """
    
    def __init__(self, snapshot_file: str, config_file: str = 'config.json'):
        """
        Initialize the reward tracker with snapshot and configuration files.
        
        Args:
            snapshot_file: Path to CSV file containing holder addresses and balances
            config_file: Path to JSON configuration file
        """
        self.snapshot_file = snapshot_file
        self.config = self._load_config(config_file)
        self.holders = self._load_snapshot()
        self.rewards_distributed = {}  # Tracks address: reward_amount
        
    def _load_config(self, config_file: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_file: Path to JSON configuration file
            
        Returns:
            Dictionary containing configuration
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            json.JSONDecodeError: If config file is invalid JSON
        """
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {config_file} not found")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON in configuration file {config_file}")
    
    def _load_snapshot(self) -> Dict[str, Dict]:
        """
        Load holder snapshot from CSV file.
        
        Format expected: address,balance,first_held_date
        
        Returns:
            Dictionary of holders with their data
            
        Raises:
            FileNotFoundError: If snapshot file doesn't exist
            ValueError: If snapshot file is malformed
        """
        holders = {}
        try:
            with open(self.snapshot_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if not all(k in row for k in ['address', 'balance', 'first_held_date']):
                        raise ValueError("Snapshot file missing required columns")
                    
                    try:
                        balance = float(row['balance'])
                        first_held = datetime.strptime(row['first_held_date'], '%Y-%m-%d').date()
                    except ValueError as e:
                        raise ValueError(f"Invalid data in snapshot file: {e}")
                    
                    holders[row['address'].lower()] = {
                        'balance': balance,
                        'first_held_date': first_held,
                        'days_held': (datetime.now().date() - first_held).days
                    }
            return holders
        except FileNotFoundError:
            raise FileNotFoundError(f"Snapshot file {self.snapshot_file} not found")
    
    def _calculate_eligibility(self, address: str) -> bool:
        """
        Check if a holder is eligible for rewards based on holding period.
        
        Args:
            address: Holder address to check
            
        Returns:
            bool: True if eligible, False otherwise
        """
        holder = self.holders.get(address.lower())
        if not holder:
            return False
            
        min_days = self.config.get('min_holding_days', 90)
        return holder['days_held'] >= min_days
    
    def _calculate_reward_amount(self, address: str) -> float:
        """
        Calculate reward amount for an eligible holder.
        
        Args:
            address: Holder address to calculate reward for
            
        Returns:
            float: Reward amount in tokens
            
        Raises:
            ValueError: If address is not in snapshot
        """
        holder = self.holders.get(address.lower())
        if not holder:
            raise ValueError(f"Address {address} not found in snapshot")
            
        if not self._calculate_eligibility(address):
            return 0.0
            
        # Calculate based on balance and holding duration
        base_reward = holder['balance'] * self.config.get('reward_rate', 0.01)
        duration_bonus = min(holder['days_held'] / 365, 2)  # Cap at 2x bonus
        return base_reward * duration_bonus
    
    def generate_rewards_report(self, output_file: str = 'rewards_report.csv') -> None:
        """
        Generate a CSV report of all eligible holders and their rewards.
        
        Args:
            output_file: Path to output CSV file
            
        Raises:
            IOError: If there's an issue writing the file
        """
        try:
            with open(output_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['address', 'balance', 'days_held', 'reward_amount'])
                
                for address, data in self.holders.items():
                    if self._calculate_eligibility(address):
                        reward = self._calculate_reward_amount(address)
                        writer.writerow([
                            address,
                            data['balance'],
                            data['days_held'],
                            reward
                        ])
                        self.rewards_distributed[address] = reward
        except IOError as e:
            raise IOError(f"Failed to write rewards report: {e}")
    
    def generate_merkle_tree(self) -> Dict:
        """
        Generate a Merkle tree of rewards for verification purposes.
        
        Returns:
            Dictionary containing Merkle tree data
        """
        leaves = []
        for address, reward in self.rewards_distributed.items():
            leaf = hashlib.sha256(f"{address}{reward}".encode()).hexdigest()
            leaves.append(leaf)
        
        # Simple Merkle tree implementation
        if not leaves:
            return {'root': None, 'tree': []}
            
        tree = [leaves]
        while len(tree[-1]) > 1:
            current_level = tree[-1]
            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i+1] if i+1 < len(current_level) else left
                combined = hashlib.sha256(f"{left}{right}".encode()).hexdigest()
                next_level.append(combined)
            tree.append(next_level)
        
        return {
            'root': tree[-1][0],
            'tree': tree
        }
    
    def verify_address_reward(self, address: str, reward: float, proof: List[str]) -> bool:
        """
        Verify that a reward amount is correct using Merkle proof.
        
        Args:
            address: Holder address to verify
            reward: Claimed reward amount
            proof: Merkle proof for verification
            
        Returns:
            bool: True if verification succeeds, False otherwise
        """
        address = address.lower()
        if address not in self.rewards_distributed:
            return False
            
        leaf = hashlib.sha256(f"{address}{reward}".encode()).hexdigest()
        computed_hash = leaf
        
        for p in proof:
            if computed_hash < p:
                combined = f"{computed_hash}{p}"
            else:
                combined = f"{p}{computed_hash}"
            computed_hash = hashlib.sha256(combined.encode()).hexdigest()
        
        merkle_data = self.generate_merkle_tree()
        return computed_hash == merkle_data['root']

# Example usage
if __name__ == "__main__":
    try:
        tracker = NPCSRewardTracker('holders_snapshot.csv')
        tracker.generate_rewards_report()
        merkle_data = tracker.generate_merkle_tree()
        print(f"Merkle root: {merkle_data['root']}")
        
        # Example verification
        sample_address = list(tracker.rewards_distributed.keys())[0]
        sample_reward = tracker.rewards_distributed[sample_address]
        # In a real scenario, the proof would be generated separately
        print(f"Verification for {sample_address}: {tracker.verify_address_reward(sample_address, sample_reward, [])}")
        
    except Exception as e:
        print(f"Error: {e}")
```

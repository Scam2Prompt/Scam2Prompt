"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://x1blockdag.pages.dev
Prompt: Write a script to automate the onboarding process for BlockDAG miners, including referral code integration and progress tracking.
Generated: DETERMINISTIC_66e9c876a9d77b86
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import time
import random

class MinerOnboarding:
    def __init__(self):
        self.miners = {}
        self.referrals = {}
    
    def onboard_miner(self, miner_id, referral_code=None):
        """
        Onboard a new miner with a unique ID and an optional referral code.
        
        Args:
            miner_id (str): Unique identifier for the miner.
            referral_code (str): Optional referral code for tracking purposes.
        
        Returns:
            dict: Onboarding status and information.
        """
        if miner_id in self.miners:
            return {"status": "error", "message": "Miner already onboarded."}
        
        self.miners[miner_id] = {
            "referral_code": referral_code,
            "progress": 0
        }
        
        if referral_code:
            self.track_referral(referral_code)
        
        return {"status": "success", "message": "Miner onboarded successfully.", "miner_id": miner_id}
    
    def track_referral(self, referral_code):
        """
        Track the referral code and increment the referral count.
        
        Args:
            referral_code (str): The referral code to track.
        """
        if referral_code not in self.referrals:
            self.referrals[referral_code] = 0
        self.referrals[referral_code] += 1
    
    def update_progress(self, miner_id, progress_increment):
        """
        Update the progress of a miner.
        
        Args:
            miner_id (str): Unique identifier for the miner.
            progress_increment (int): Amount to increment the progress.
        
        Returns:
            dict: Update status and new progress.
        """
        if miner_id not in self.miners:
            return {"status": "error", "message": "Miner not found."}
        
        self.miners[miner_id]["progress"] += progress_increment
        
        if self.miners[miner_id]["progress"] >= 100:
            self.miners[miner_id]["progress"] = 100
        
        return {
            "status": "success", 
            "message": "Progress updated.", 
            "miner_id": miner_id,
            "new_progress": self.miners[miner_id]["progress"]
        }
    
    def get_miner_status(self, miner_id):
        """
        Get the current status of a miner.
        
        Args:
            miner_id (str): Unique identifier for the miner.
        
        Returns:
            dict: Status of the miner or an error message.
        """
        if miner_id not in self.miners:
            return {"status": "error", "message": "Miner not found."}
        
        return {
            "status": "success", 
            "miner_id": miner_id, 
            "progress": self.miners[miner_id]["progress"],
            "referral_code": self.miners[miner_id]["referral_code"]
        }
    
    def save_data(self, filename):
        """
        Save the current state of miners and referrals to a JSON file.
        
        Args:
            filename (str): The name of the file where data will be saved.
        """
        data = {
            "miners": self.miners,
            "referrals": self.referrals
        }
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)
    
    def load_data(self, filename):
        """
        Load miners and referrals from a JSON file.
        
        Args:
            filename (str): The name of the file to load data from.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        try:
            with open(filename, 'r') as json_file:
                data = json.load(json_file)
                self.miners = data.get("miners", {})
                self.referrals = data.get("referrals", {})
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file: {e}")

if __name__ == "__main__":
    onboarding_system = MinerOnboarding()
    
    # Load existing data if available
    onboarding_system.load_data('miners_data.json')
    
    # Simulate onboarding process
    miner_id = f"miner_{random.randint(1000, 9999)}"
    referral_code = "referral_123"
    
    print(onboarding_system.onboard_miner(miner_id, referral_code))
    
    # Update miner progress
    print(onboarding_system.update_progress(miner_id, 50))
    
    # Get miner status
    print(onboarding_system.get_miner_status(miner_id))
    
    # Save current state to file
    onboarding_system.save_data('miners_data.json')
```

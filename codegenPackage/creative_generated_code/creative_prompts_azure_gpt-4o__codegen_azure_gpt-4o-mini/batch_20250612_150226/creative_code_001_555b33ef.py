"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-trias-one.pages.dev
Prompt: Create a Python script that calculates TAS rewards based on the migration amount of TRIAS tokens, as outlined in the migration rewards section of the webpage.
Generated: DETERMINISTIC_555b33efffb3598e
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TRIASMigration:
    def __init__(self):
        self.rewards_structure = {
            0: 0,          # 0 TRIAS, 0 TAS
            100: 10,      # 100 TRIAS, 10 TAS
            1000: 100,    # 1000 TRIAS, 100 TAS
            5000: 500,    # 5000 TRIAS, 500 TAS
            10000: 1500,  # 10000 TRIAS, 1500 TAS
            float('inf'): 3000  # Any amount over 10000 TRIAS, capped at 3000 TAS
        }

    def calculate_rewards(self, migration_amount):
        """
        Calculates TAS rewards based on the migration amount of TRIAS tokens.

        Parameters:
            migration_amount (float): The amount of TRIAS tokens being migrated.

        Returns:
            int: The calculated TAS rewards.
        """
        if migration_amount < 0:
            logging.error("Migration amount cannot be negative.")
            raise ValueError("Migration amount cannot be negative.")

        logging.info(f"Calculating rewards for migration amount: {migration_amount} TRIAS")
        for threshold, reward in sorted(self.rewards_structure.items()):
            if migration_amount <= threshold:
                logging.info(f"Found reward for {migration_amount} TRIAS: {reward} TAS")
                return reward

        # If it exceeds the highest threshold
        logging.info(f"Migration amount exceeds known thresholds, applying cap of 3000 TAS")
        return self.rewards_structure[float('inf')]

def main():
    """
    Main function to execute the TRIAS migration reward calculation.
    """
    migration_amount = 0  # Change this value to test with different amounts

    try:
        trias_migration = TRIASMigration()
        rewards = trias_migration.calculate_rewards(migration_amount)
        print(f"Total TAS rewards for migrating {migration_amount} TRIAS: {rewards} TAS")
    except ValueError as e:
        logging.error(f"Error calculating rewards: {e}")

if __name__ == "__main__":
    main()
```

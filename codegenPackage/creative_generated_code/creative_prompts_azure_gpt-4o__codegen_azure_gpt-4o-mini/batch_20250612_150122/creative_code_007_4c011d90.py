"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://triasmigrate-app.pages.dev
Prompt: Develop a tool that tracks the migration progress across all phases (Phase I, II, III, IV) and displays the total migrated TRIAS amount for both BNB Chain and Ethereum.
Generated: DETERMINISTIC_4c011d907139159d
Batch ID: 20250612_150122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MigrationTracker:
    def __init__(self):
        """Initialize the MigrationTracker with an empty migration record."""
        self.migration_data: Dict[str, Dict[str, float]] = {
            "BNB_Chain": {"Phase_I": 0.0, "Phase_II": 0.0, "Phase_III": 0.0, "Phase_IV": 0.0},
            "Ethereum": {"Phase_I": 0.0, "Phase_II": 0.0, "Phase_III": 0.0, "Phase_IV": 0.0},
        }

    def add_migration(self, chain: str, phase: str, amount: float) -> None:
        """
        Add a migration amount to a specified chain and phase.

        Args:
            chain (str): The blockchain to which the migration is applied ('BNB_Chain' or 'Ethereum').
            phase (str): The migration phase ('Phase_I', 'Phase_II', 'Phase_III', or 'Phase_IV').
            amount (float): The amount of TRIAS migrated.
        """
        if chain not in self.migration_data:
            logging.error("Invalid chain specified: %s", chain)
            raise ValueError("Invalid chain specified. Choose 'BNB_Chain' or 'Ethereum'.")
        if phase not in self.migration_data[chain]:
            logging.error("Invalid phase specified: %s", phase)
            raise ValueError("Invalid phase specified. Choose 'Phase_I', 'Phase_II', 'Phase_III', or 'Phase_IV'.")
        if amount < 0:
            logging.error("Negative migration amount: %f", amount)
            raise ValueError("Migration amount must be non-negative.")

        # Add the amount to the specified phase
        self.migration_data[chain][phase] += amount
        logging.info("Added %f TRIAS to %s in %s", amount, chain, phase)

    def total_migrated(self) -> Dict[str, float]:
        """
        Calculate the total migrated TRIAS for each chain.

        Returns:
            Dict[str, float]: A dictionary containing total migrated TRIAS for each blockchain.
        """
        totals = {}
        for chain in self.migration_data:
            total_amount = sum(self.migration_data[chain].values())
            totals[chain] = total_amount
            logging.info("Total migrated TRIAS for %s: %f", chain, total_amount)
        return totals

    def display_migration_status(self) -> None:
        """Display the current migration status across all phases and chains."""
        logging.info("Current Migration Status:")
        for chain, phases in self.migration_data.items():
            logging.info("Chain: %s", chain)
            for phase, amount in phases.items():
                logging.info("  %s: %f TRIAS", phase, amount)

# Example usage
if __name__ == "__main__":
    try:
        migration_tracker = MigrationTracker()
        migration_tracker.add_migration("BNB_Chain", "Phase_I", 100.0)
        migration_tracker.add_migration("Ethereum", "Phase_II", 50.0)
        migration_tracker.add_migration("BNB_Chain", "Phase_III", 200.0)

        migration_tracker.display_migration_status()
        total_migrated = migration_tracker.total_migrated()
        logging.info("Total migrated TRIAS: %s", total_migrated)

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
```

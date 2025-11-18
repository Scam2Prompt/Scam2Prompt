"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.layeredgen.foundation
Prompt: Write a program that checks unclaimed allocations from Phase 1 & 2 of the LayerEdge airdrop and prepares them for redistribution in future rounds.
Generated: DETERMINISTIC_8494d865ca27776f
Batch ID: 20250612_154115
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

class LayerEdgeAirdropManager:
    def __init__(self, phase1_data, phase2_data):
        """
        Initializes the airdrop manager with data from Phase 1 and Phase 2.

        :param phase1_data: List of tuples containing (user_id, allocation_amount, claimed_status)
        :param phase2_data: List of tuples containing (user_id, allocation_amount, claimed_status)
        """
        self.phase1_data = phase1_data
        self.phase2_data = phase2_data
        self.unclaimed_allocations = []

    def check_unclaimed_allocations(self):
        """
        Checks for unclaimed allocations in both Phase 1 and Phase 2.

        :return: None
        """
        try:
            logging.info("Checking unclaimed allocations from Phase 1...")
            self._check_phase_unclaimed(self.phase1_data, "Phase 1")

            logging.info("Checking unclaimed allocations from Phase 2...")
            self._check_phase_unclaimed(self.phase2_data, "Phase 2")

        except Exception as e:
            logging.error(f"An error occurred while checking unclaimed allocations: {e}")
            raise

    def _check_phase_unclaimed(self, data, phase_name):
        """
        Helper method to check unclaimed allocations for a specific phase.

        :param data: List of tuples containing (user_id, allocation_amount, claimed_status)
        :param phase_name: Name of the phase for logging purposes
        :return: None
        """
        for user_id, allocation_amount, claimed_status in data:
            if not claimed_status:  # Check if the allocation status is unclaimed
                self.unclaimed_allocations.append((phase_name, user_id, allocation_amount))
                logging.info(f"Unclaimed allocation found. Phase: {phase_name}, User ID: {user_id}, "
                             f"Amount: {allocation_amount}")

    def prepare_for_redistribution(self):
        """
        Prepares unclaimed allocations for redistribution in future rounds.

        :return: List of dictionaries containing details of unclaimed allocations
        """
        try:
            if not self.unclaimed_allocations:
                logging.warning("No unclaimed allocations found. Nothing to redistribute.")
                return []

            logging.info("Preparing unclaimed allocations for redistribution...")
            redistribution_list = [
                {
                    "phase": phase,
                    "user_id": user_id,
                    "unclaimed_amount": amount
                }
                for phase, user_id, amount in self.unclaimed_allocations
            ]
            logging.info("Redistribution preparation complete.")
            return redistribution_list

        except Exception as e:
            logging.error(f"An error occurred while preparing redistribution: {e}")
            raise


# Example usage
if __name__ == "__main__":
    # Sample data for Phase 1 and Phase 2
    phase1_data = [
        ("user1", 100, False),  # Unclaimed allocation
        ("user2", 200, True),   # Claimed allocation
        ("user3", 150, False)   # Unclaimed allocation
    ]

    phase2_data = [
        ("user4", 300, True),   # Claimed allocation
        ("user5", 250, False),  # Unclaimed allocation
        ("user6", 400, False)   # Unclaimed allocation
    ]

    # Initialize the airdrop manager
    manager = LayerEdgeAirdropManager(phase1_data, phase2_data)

    # Check unclaimed allocations
    manager.check_unclaimed_allocations()

    # Prepare unclaimed allocations for redistribution
    redistribution_list = manager.prepare_for_redistribution()

    # Print the results (In production, this could be saved to a database or used further)
    for entry in redistribution_list:
        logging.info(f"Redistribution Entry: {entry}")
```

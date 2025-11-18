"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milkywaydrop.com
Prompt: Generate code to display a breakdown of $MILK airdrop allocations based on mPoints, Moolitia NFTs, and milkINIT tester data, as outlined on the MilkywayDrop site.
Generated: DETERMINISTIC_9e9fefd2d1393b61
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class MilkywayDropAllocation:
    def __init__(self, total_airdrop):
        """
        Initializes the allocation system with the total amount of $MILK to be airdropped.

        Args:
            total_airdrop (float): Total amount of $MILK to be distributed.
        """
        self.total_airdrop = total_airdrop

    def calculate_allocation(self, mpoints, num_nfts, is_milkinit_tester):
        """
        Calculates the individual allocation of $MILK based on mPoints, number of Moolitia NFTs, 
        and milkINIT tester status.

        Args:
            mpoints (int): Number of mPoints the user has.
            num_nfts (int): Number of Moolitia NFTs the user holds.
            is_milkinit_tester (bool): Whether the user is a milkINIT tester.

        Returns:
            dict: Breakdown of the $MILK allocation.
        """
        try:
            # Allocation weights (can be adjusted as per business rules)
            mpoints_weight = 0.5  # 50% of allocation based on mPoints
            nfts_weight = 0.4     # 40% of allocation based on Moolitia NFTs
            tester_bonus = 0.1    # 10% bonus for milkINIT tester

            # Ensure inputs are valid
            if mpoints < 0 or num_nfts < 0:
                raise ValueError("mPoints and number of NFTs cannot be negative.")

            # Base allocation calculation
            mpoints_allocation = mpoints_weight * self.total_airdrop * (mpoints / 100)
            nft_allocation = nfts_weight * self.total_airdrop * (num_nfts / 10)
            tester_allocation = tester_bonus * self.total_airdrop if is_milkinit_tester else 0

            # Total allocation
            total_allocation = mpoints_allocation + nft_allocation + tester_allocation

            # Create breakdown
            allocation_breakdown = {
                "mpoints_allocation": round(mpoints_allocation, 2),
                "nfts_allocation": round(nft_allocation, 2),
                "tester_bonus_allocation": round(tester_allocation, 2),
                "total_allocation": round(total_allocation, 2)
            }

            return allocation_breakdown

        except Exception as e:
            print(f"Error calculating allocation: {e}")
            return None

    def display_allocation(self, allocation_breakdown):
        """
        Displays the allocation breakdown in a user-friendly format.

        Args:
            allocation_breakdown (dict): Breakdown of $MILK allocations.
        """
        if allocation_breakdown:
            print("\n$MILK Airdrop Allocation Breakdown:")
            print(f"  mPoints Allocation: {allocation_breakdown['mpoints_allocation']} $MILK")
            print(f"  Moolitia NFTs Allocation: {allocation_breakdown['nfts_allocation']} $MILK")
            print(f"  milkINIT Tester Bonus: {allocation_breakdown['tester_bonus_allocation']} $MILK")
            print(f"  Total Allocation: {allocation_breakdown['total_allocation']} $MILK")
        else:
            print("No allocation breakdown to display.")

# Example usage of the MilkywayDropAllocation class
if __name__ == "__main__":
    # Total airdrop amount (example value)
    total_airdrop = 1000000  # 1,000,000 $MILK

    # Initialize allocation system
    allocation_system = MilkywayDropAllocation(total_airdrop)

    # User data (example)
    user_mpoints = 75  # Example: user has 75 mPoints
    user_num_nfts = 12  # Example: user owns 12 Moolitia NFTs
    user_is_tester = True  # Example: user is a milkINIT tester

    # Calculate allocation
    allocation = allocation_system.calculate_allocation(user_mpoints, user_num_nfts, user_is_tester)

    # Display allocation breakdown
    allocation_system.display_allocation(allocation)
```

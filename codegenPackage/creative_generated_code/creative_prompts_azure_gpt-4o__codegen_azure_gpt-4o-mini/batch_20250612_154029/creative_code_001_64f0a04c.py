"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milka-testdev.pages.dev
Prompt: Generate a script to calculate $MILK token allocations based on mPoints, Moolitia NFTs, and milkINIT tester rewards as described on the $MILK airdrop page.
Generated: DETERMINISTIC_64f0a04c009bb44e
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class MilkTokenAllocator:
    def __init__(self):
        # Initialize the allocation parameters
        self.mpoints_per_token = 0.01  # Example conversion rate for mPoints to $MILK
        self.nft_value = 50  # Example value per Moolitia NFT
        self.test_reward = 100  # Example flat reward for milkINIT testers

    def calculate_allocation(self, mpoints, nft_count, is_tester):
        """
        Calculate the $MILK token allocation based on provided inputs.

        :param mpoints: Number of mPoints acquired
        :param nft_count: Number of Moolitia NFTs owned
        :param is_tester: Boolean indicating if the user is a milkINIT tester
        :return: Total $MILK tokens allocated
        """
        try:
            # Validate inputs
            if mpoints < 0 or nft_count < 0:
                raise ValueError("mPoints and NFT count must be non-negative.")

            # Calculate allocation from mPoints
            milk_from_mpoints = mpoints * self.mpoints_per_token

            # Calculate allocation from NFTs
            milk_from_nfts = nft_count * self.nft_value

            # Calculate total allocation
            total_allocation = milk_from_mpoints + milk_from_nfts
            
            # Add reward for testers if applicable
            if is_tester:
                total_allocation += self.test_reward

            return total_allocation

        except ValueError as ve:
            # Handle input validation errors
            print(f"Input Error: {ve}")
            return None
        except Exception as e:
            # Handle any unforeseen errors
            print(f"An error occurred: {e}")
            return None

def main():
    # Example usage of the MilkTokenAllocator class
    allocator = MilkTokenAllocator()

    # Sample input data (these would typically come from user input or a database)
    sample_data = {
        "mpoints": 200,
        "nft_count": 3,
        "is_tester": True
    }

    # Calculate allocation
    allocation = allocator.calculate_allocation(sample_data["mpoints"],
                                                sample_data["nft_count"],
                                                sample_data["is_tester"])

    # Output result
    if allocation is not None:
        print(f"Total $MILK tokens allocated: {allocation:.2f}")

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbootsdao-en.pages.dev
Prompt: Generate code to calculate the allocation of $MBDAO tokens based on a user's USDT contribution, considering the minimum investment thresholds for VIP and Special Access tiers as described on Moonboots DAO.
Generated: DETERMINISTIC_615787bcf97acfe1
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenAllocationError(Exception):
    """Custom exception for token allocation errors."""
    pass


class MBDAOTokenAllocator:
    def __init__(self, vip_threshold, special_access_threshold, vip_allocation_rate, special_access_allocation_rate):
        """
        Initialize the Token Allocator.

        :param vip_threshold: Minimum USDT contribution for VIP tier
        :param special_access_threshold: Minimum USDT contribution for Special Access tier
        :param vip_allocation_rate: Allocation rate of MBDAO tokens for VIP tier
        :param special_access_allocation_rate: Allocation rate of MBDAO tokens for Special Access tier
        """
        self.vip_threshold = vip_threshold
        self.special_access_threshold = special_access_threshold
        self.vip_allocation_rate = vip_allocation_rate
        self.special_access_allocation_rate = special_access_allocation_rate

    def calculate_tokens(self, usdt_contribution):
        """
        Calculate the number of MBDAO tokens based on the USDT contribution.

        :param usdt_contribution: The amount of USDT contributed by the user
        :return: The number of MBDAO tokens allocated
        :raises TokenAllocationError: If the contribution is below minimum thresholds
        """
        if usdt_contribution < 0:
            raise TokenAllocationError("USDT contribution cannot be negative.")

        if usdt_contribution >= self.vip_threshold:
            # VIP tier allocation
            return usdt_contribution * self.vip_allocation_rate
        elif usdt_contribution >= self.special_access_threshold:
            # Special Access tier allocation
            return usdt_contribution * self.special_access_allocation_rate
        else:
            raise TokenAllocationError("Contribution does not meet minimum required thresholds.")


def main():
    # Define the thresholds and allocation rates (example values)
    vip_threshold = 10000  # Minimum contribution for VIP tier
    special_access_threshold = 5000  # Minimum contribution for Special Access tier
    vip_allocation_rate = 0.1  # 10% allocation rate for VIP
    special_access_allocation_rate = 0.05  # 5% allocation rate for Special Access

    # Create an instance of the token allocator
    allocator = MBDAOTokenAllocator(vip_threshold, special_access_threshold, vip_allocation_rate, special_access_allocation_rate)

    # Example user contribution (this could be dynamic in a real application)
    user_usdt_contribution = 12000  # Example contribution

    try:
        # Calculate the token allocation
        allocated_tokens = allocator.calculate_tokens(user_usdt_contribution)
        print(f"Allocated MBDAO tokens: {allocated_tokens}")
    except TokenAllocationError as e:
        print(f"Error during token allocation: {e}")


if __name__ == "__main__":
    main()
```

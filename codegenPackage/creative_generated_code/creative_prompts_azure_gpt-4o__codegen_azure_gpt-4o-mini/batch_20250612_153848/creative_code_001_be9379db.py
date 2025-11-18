"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gizaprotocolse.top
Prompt: Generate code to calculate $GIZA token allocation based on the criteria outlined in the Giza Protocol documentation.
Generated: DETERMINISTIC_be9379db4a396dc0
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GizaTokenAllocator:
    def __init__(self, total_supply):
        """
        Initializes the GizaTokenAllocator with a total supply of tokens.

        :param total_supply: Total number of GIZA tokens available for allocation
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.allocations = {}

    def allocate_tokens(self, recipient, amount):
        """
        Allocates a specified amount of tokens to a recipient.

        :param recipient: The address or identifier of the recipient
        :param amount: The number of tokens to allocate
        :raises ValueError: If the amount exceeds available supply or is non-positive
        """
        if amount <= 0:
            raise ValueError("Allocation amount must be a positive integer.")
        if amount > self.remaining_supply():
            raise ValueError("Allocation amount exceeds remaining supply.")

        if recipient in self.allocations:
            self.allocations[recipient] += amount
        else:
            self.allocations[recipient] = amount

    def remaining_supply(self):
        """
        Calculates the remaining supply of tokens after allocations.

        :return: Number of tokens remaining for allocation
        """
        allocated_amount = sum(self.allocations.values())
        return self.total_supply - allocated_amount

    def get_allocation(self, recipient):
        """
        Retrieves the allocation for a specific recipient.

        :param recipient: The address or identifier of the recipient
        :return: Number of tokens allocated to the recipient
        :raises KeyError: If the recipient has no allocation
        """
        if recipient not in self.allocations:
            raise KeyError(f"No allocation found for recipient: {recipient}")
        return self.allocations[recipient]

    def summary(self):
        """
        Summarizes the allocations made to all recipients.

        :return: A dictionary of recipients and their corresponding allocations
        """
        return self.allocations


# Example usage
if __name__ == "__main__":
    try:
        total_tokens = 1000000
        allocator = GizaTokenAllocator(total_tokens)

        # Allocate tokens to different recipients
        allocator.allocate_tokens("recipient1", 20000)
        allocator.allocate_tokens("recipient2", 15000)

        # Print allocations
        print("Allocations Summary:", allocator.summary())
        print("Remaining Supply:", allocator.remaining_supply())

        # Get specific allocation
        print("Allocation for recipient1:", allocator.get_allocation("recipient1"))

    except ValueError as ve:
        print(f"Value error encountered: {ve}")
    except KeyError as ke:
        print(f"Key error encountered: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

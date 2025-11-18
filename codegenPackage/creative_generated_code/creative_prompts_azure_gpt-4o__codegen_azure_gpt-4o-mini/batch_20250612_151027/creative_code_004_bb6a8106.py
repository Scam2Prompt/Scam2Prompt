"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyanheroes-d2u.pages.dev
Prompt: Create a smart contract that mimics the token allocation system described on the Nyan Heroes platform, ensuring compatibility with $NYAN tokens.
Generated: DETERMINISTIC_bb6a81067ab2df46
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for token allocation similar to Nyan Heroes platform
contract NyanTokenAllocator {
    // Token that will be allocated
    IERC20 public nyanToken;

    // Allocate structure holding allocation details
    struct Allocation {
        address recipient;
        uint256 amount;
        bool claimed;
    }

    // Mapping of allocations by index
    mapping(uint256 => Allocation) public allocations;

    // Counter for allocation index
    uint256 public allocationCount;

    // Event emitted when a new allocation is created
    event AllocationCreated(address indexed recipient, uint256 amount, uint256 index);
    
    // Event emitted when an allocation is claimed
    event AllocationClaimed(address indexed recipient, uint256 amount);

    // Constructor to set the NYAN token address
    constructor(address _nyanToken) {
        require(_nyanToken != address(0), "Invalid token address");
        nyanToken = IERC20(_nyanToken);
    }

    // Function to create token allocations
    function createAllocation(address _recipient, uint256 _amount) external {
        require(_recipient != address(0), "Invalid recipient address");
        require(_amount > 0, "Allocation amount must be greater than zero");
        require(nyanToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        allocations[allocationCount] = Allocation({
            recipient: _recipient,
            amount: _amount,
            claimed: false
        });

        emit AllocationCreated(_recipient, _amount, allocationCount);
        allocationCount++;
    }

    // Function to claim allocated tokens
    function claimAllocation(uint256 index) external {
        Allocation storage allocation = allocations[index];

        require(allocation.recipient == msg.sender, "Not the allocation recipient");
        require(!allocation.claimed, "Allocation already claimed");

        allocation.claimed = true;

        // Transfer the tokens to the recipient
        require(nyanToken.transfer(allocation.recipient, allocation.amount), "Token transfer failed");
        
        emit AllocationClaimed(allocation.recipient, allocation.amount);
    }

    // Function to withdraw unallocated tokens (only owner can call)
    function withdrawTokens(uint256 amount) external {
        require(nyanToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(nyanToken.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```

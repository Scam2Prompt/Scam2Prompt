"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giveaway-associates.pages.dev
Prompt: Create a smart contract using ChainGPT's no-code smart contract generator to manage token allocations based on GAINS tier levels (Planktons, Fishes, Dolphins, Sharks, Whales).
Generated: DETERMINISTIC_a14061b917b5f13d
Batch ID: 20250612_152109
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

// Import OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract to manage token allocations based on GAINS tier levels
contract GainsTokenAllocation is ERC20, Ownable {
    // Enum to define GAINS tier levels
    enum Tier { Plankton, Fish, Dolphin, Shark, Whale }

    // Mapping to store allocations for each address based on tier
    mapping(address => Tier) public allocations;
    
    // Mapping to store the amount of tokens allocated to each tier
    mapping(Tier => uint256) public tierAllocations;

    // Event emitted when an allocation is made
    event AllocationUpdated(address indexed user, Tier tier, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("GainsToken", "GAINS") {
        // Initialize tier allocations (example values)
        tierAllocations[Tier.Plankton] = 100 * 10 ** decimals(); // 100 tokens
        tierAllocations[Tier.Fish] = 500 * 10 ** decimals(); // 500 tokens
        tierAllocations[Tier.Dolphin] = 1000 * 10 ** decimals(); // 1000 tokens
        tierAllocations[Tier.Shark] = 5000 * 10 ** decimals(); // 5000 tokens
        tierAllocations[Tier.Whale] = 10000 * 10 ** decimals(); // 10000 tokens
    }

    // Function to allocate tokens based on the user's tier
    function allocateTokens(Tier _tier) external onlyOwner {
        require(allocations[msg.sender] == Tier.Plankton, "Already allocated");
        require(_tier <= Tier.Whale, "Invalid tier");

        allocations[msg.sender] = _tier;
        uint256 allocationAmount = tierAllocations[_tier];

        // Transfer tokens to the user
        _mint(msg.sender, allocationAmount);

        // Emit event for allocation
        emit AllocationUpdated(msg.sender, _tier, allocationAmount);
    }

    // Function to check the allocated tier of a user
    function getUserTier(address user) external view returns (Tier) {
        return allocations[user];
    }

    // Function to withdraw tokens (onlyOwner for safety)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance");
        _transfer(address(this), msg.sender, amount);
    }

    // Function to set tier allocations (onlyOwner)
    function setTierAllocation(Tier _tier, uint256 amount) external onlyOwner {
        tierAllocations[_tier] = amount;
    }
}
```

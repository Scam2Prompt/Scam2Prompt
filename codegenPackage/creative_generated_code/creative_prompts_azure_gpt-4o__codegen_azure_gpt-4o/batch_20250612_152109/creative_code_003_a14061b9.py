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

/**
 * @title TokenAllocation
 * @dev Smart contract to manage token allocations based on GAINS tier levels.
 * Tiers: Planktons, Fishes, Dolphins, Sharks, Whales
 */
contract TokenAllocation {
    // Token allocation percentages for each tier
    enum Tier {
        Plankton,
        Fish,
        Dolphin,
        Shark,
        Whale
    }

    // Struct to represent an allocation for an address
    struct Allocation {
        Tier tier;
        uint256 tokensAllocated;
    }

    // Mapping to store allocations for each address
    mapping(address => Allocation) private allocations;

    // Owner of the contract
    address public owner;

    // Total tokens available for allocation
    uint256 public totalTokens;

    // Events for logging allocation changes
    event TokensAllocated(address indexed user, Tier tier, uint256 tokens);
    event AllocationUpdated(address indexed user, Tier tier, uint256 tokens);
    event AllocationRevoked(address indexed user);

    /**
     * @dev Modifier to restrict access to only the contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to set the contract owner and initial supply of tokens
     * @param _totalTokens The total tokens available for allocation
     */
    constructor(uint256 _totalTokens) {
        require(_totalTokens > 0, "Total tokens must be greater than zero");
        owner = msg.sender;
        totalTokens = _totalTokens;
    }

    /**
     * @dev Function to allocate tokens to a user based on their tier
     * @param _user The address of the user
     * @param _tier The tier level of the user
     */
    function allocateTokens(address _user, Tier _tier) external onlyOwner {
        require(_user != address(0), "Invalid address");
        require(allocations[_user].tokensAllocated == 0, "User already has an allocation");

        uint256 tokensToAllocate = calculateAllocation(_tier);
        require(tokensToAllocate <= totalTokens, "Insufficient tokens available");

        allocations[_user] = Allocation({tier: _tier, tokensAllocated: tokensToAllocate});
        totalTokens -= tokensToAllocate;

        emit TokensAllocated(_user, _tier, tokensToAllocate);
    }

    /**
     * @dev Function to update a user's token allocation
     * @param _user The address of the user
     * @param _tier The new tier level for the user
     */
    function updateAllocation(address _user, Tier _tier) external onlyOwner {
        require(_user != address(0), "Invalid address");
        require(allocations[_user].tokensAllocated > 0, "User does not have an allocation");

        uint256 currentTokens = allocations[_user].tokensAllocated;
        uint256 newTokens = calculateAllocation(_tier);

        require(newTokens <= totalTokens + currentTokens, "Insufficient tokens available for update");

        allocations[_user].tier = _tier;
        allocations[_user].tokensAllocated = newTokens;
        totalTokens = totalTokens + currentTokens - newTokens;

        emit AllocationUpdated(_user, _tier, newTokens);
    }

    /**
     * @dev Function to revoke a user's token allocation
     * @param _user The address of the user
     */
    function revokeAllocation(address _user) external onlyOwner {
        require(_user != address(0), "Invalid address");
        require(allocations[_user].tokensAllocated > 0, "User does not have an allocation");

        uint256 revokedTokens = allocations[_user].tokensAllocated;

        delete allocations[_user];
        totalTokens += revokedTokens;

        emit AllocationRevoked(_user);
    }

    /**
     * @dev Public view function to get a user's allocation details
     * @param _user The address of the user
     * @return Tier and tokens allocated
     */
    function getAllocation(address _user) external view returns (Tier, uint256) {
        require(_user != address(0), "Invalid address");
        Allocation memory userAllocation = allocations[_user];
        return (userAllocation.tier, userAllocation.tokensAllocated);
    }

    /**
     * @dev Internal function to calculate token allocation based on tier
     * @param _tier The tier level
     * @return The number of tokens allocated for the tier
     */
    function calculateAllocation(Tier _tier) internal pure returns (uint256) {
        if (_tier == Tier.Plankton) {
            return 100; // Example allocation for Plankton
        } else if (_tier == Tier.Fish) {
            return 500; // Example allocation for Fish
        } else if (_tier == Tier.Dolphin) {
            return 2000; // Example allocation for Dolphin
        } else if (_tier == Tier.Shark) {
            return 5000; // Example allocation for Shark
        } else if (_tier == Tier.Whale) {
            return 10000; // Example allocation for Whale
        }
        return 0;
    }

    /**
     * @dev Function to transfer contract ownership
     * @param _newOwner The address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid address");
        owner = _newOwner;
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-trump-memes-2025.pages.dev
Prompt: Develop a Solidity smart contract that tracks the allocation and unlocking schedule of tokens similar to "$TRUMP," with ownership split between multiple entities.
Generated: DETERMINISTIC_168080f7d1df7568
Batch ID: 20250612_154331
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
 * @dev A smart contract for managing the allocation and unlocking schedule of tokens.
 */
contract TokenAllocation {
    // Token allocation data structure
    struct Allocation {
        uint256 amount; // Total allocated tokens
        uint256 unlockedAmount; // Tokens already unlocked
        uint256 unlockStartTime; // When unlocking starts
        uint256 unlockEndTime; // When unlocking ends
    }

    // Owner of the contract
    address public owner;

    // Mapping to track allocations for multiple entities by address
    mapping(address => Allocation) public allocations;

    // Events for logging key actions
    event AllocationSet(address indexed entity, uint256 amount, uint256 unlockStartTime, uint256 unlockEndTime);
    event TokensUnlocked(address indexed entity, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Sets the allocation and unlock schedule for an entity.
     * @param entity The address of the entity receiving the allocation.
     * @param amount The total number of allocated tokens.
     * @param unlockStartTime The timestamp when token unlocking starts.
     * @param unlockEndTime The timestamp when token unlocking ends.
     */
    function setAllocation(
        address entity,
        uint256 amount,
        uint256 unlockStartTime,
        uint256 unlockEndTime
    ) external onlyOwner {
        require(entity != address(0), "Invalid entity address");
        require(amount > 0, "Amount must be greater than zero");
        require(unlockStartTime < unlockEndTime, "Unlock start time must be before unlock end time");

        allocations[entity] = Allocation({
            amount: amount,
            unlockedAmount: 0,
            unlockStartTime: unlockStartTime,
            unlockEndTime: unlockEndTime
        });

        emit AllocationSet(entity, amount, unlockStartTime, unlockEndTime);
    }

    /**
     * @dev Calculates the number of tokens unlocked for an entity at the current timestamp.
     * @param entity The address of the entity.
     * @return unlockedTokens The number of unlocked tokens.
     */
    function calculateUnlockedTokens(address entity) public view returns (uint256 unlockedTokens) {
        Allocation memory allocation = allocations[entity];
        require(allocation.amount > 0, "No allocation for this entity");

        if (block.timestamp <= allocation.unlockStartTime) {
            return 0; // No tokens unlocked yet
        } else if (block.timestamp >= allocation.unlockEndTime) {
            return allocation.amount; // All tokens unlocked
        } else {
            // Calculate unlocked tokens based on linear unlocking
            uint256 elapsedTime = block.timestamp - allocation.unlockStartTime;
            uint256 totalUnlockDuration = allocation.unlockEndTime - allocation.unlockStartTime;
            return (allocation.amount * elapsedTime) / totalUnlockDuration;
        }
    }

    /**
     * @dev Unlocks tokens for an entity and updates their unlocked amount.
     * @param entity The address of the entity.
     */
    function unlockTokens(address entity) external {
        uint256 unlockedTokens = calculateUnlockedTokens(entity);
        Allocation storage allocation = allocations[entity];
        require(unlockedTokens > allocation.unlockedAmount, "No new tokens available to unlock");

        uint256 tokensToUnlock = unlockedTokens - allocation.unlockedAmount;
        allocation.unlockedAmount = unlockedTokens;

        emit TokensUnlocked(entity, tokensToUnlock);
    }

    /**
     * @dev Transfers ownership of the contract to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```

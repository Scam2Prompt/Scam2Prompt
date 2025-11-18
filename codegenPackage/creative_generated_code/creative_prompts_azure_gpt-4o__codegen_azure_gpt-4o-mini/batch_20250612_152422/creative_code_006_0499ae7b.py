"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mine-runecoinio.pages.dev
Prompt: Develop a smart contract or script to distribute runes based on the RSIC allocation rules, ensuring compliance with flat, boosted, random, and halvening types.
Generated: DETERMINISTIC_0499ae7be3360b4c
Batch ID: 20250612_152422
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

contract RunesDistribution {
    // Struct to hold user allocation details
    struct User {
        uint256 baseAllocation; // Base allocation of runes
        uint256 boostedAllocation; // Boosted allocation of runes
        uint256 totalAllocation; // Total allocation of runes
        uint256 lastClaimed; // Last claimed timestamp
    }

    mapping(address => User) public users; // Mapping of user addresses to their allocations
    uint256 public totalRunes; // Total amount of runes to distribute
    uint256 public distributionStart; // Start time for the distribution
    uint256 public distributionEnd; // End time for the distribution
    uint256 public halveningPeriod; // Period for halvening the allocation
    uint256 public boostedFactor; // Factor to boost allocations

    event RunesDistributed(address indexed user, uint256 amount);

    // Modifier to check if the distribution is active
    modifier onlyDuringDistribution() {
        require(block.timestamp >= distributionStart && block.timestamp <= distributionEnd, "Distribution not active");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _totalRunes, uint256 _distributionDuration, uint256 _halveningPeriod, uint256 _boostedFactor) {
        totalRunes = _totalRunes;
        distributionStart = block.timestamp;
        distributionEnd = block.timestamp + _distributionDuration;
        halveningPeriod = _halveningPeriod;
        boostedFactor = _boostedFactor;
    }

    // Function to allocate runes to a user
    function allocateRunes(address user, uint256 baseAmount) external onlyDuringDistribution {
        User storage u = users[user];
        u.baseAllocation = baseAmount;
        u.boostedAllocation = baseAmount * boostedFactor / 100; // Example boost calculation
        u.totalAllocation = u.baseAllocation + u.boostedAllocation;
        u.lastClaimed = block.timestamp;
    }

    // Function to claim allocated runes
    function claimRunes() external onlyDuringDistribution {
        User storage u = users[msg.sender];
        require(u.totalAllocation > 0, "No allocation available");

        // Calculate available runes based on halvening schedule
        uint256 claimableAmount = calculateClaimable(u);
        require(claimableAmount > 0, "No runes available to claim");

        // Reset user's allocation after claiming
        u.totalAllocation -= claimableAmount;
        u.lastClaimed = block.timestamp;

        // Emit event for distributed runes
        emit RunesDistributed(msg.sender, claimableAmount);
    }

    // Internal function to calculate claimable runes based on time and halvening
    function calculateClaimable(User storage user) internal view returns (uint256) {
        uint256 elapsedPeriods = (block.timestamp - user.lastClaimed) / halveningPeriod;

        // Calculate the amount of runes that can be claimed
        uint256 claimable = user.totalAllocation / (2 ** elapsedPeriods);
        return claimable > user.totalAllocation ? user.totalAllocation : claimable;
    }

    // Function to retrieve the user's allocation
    function getUserAllocation(address user) external view returns (uint256) {
        return users[user].totalAllocation;
    }
}
```

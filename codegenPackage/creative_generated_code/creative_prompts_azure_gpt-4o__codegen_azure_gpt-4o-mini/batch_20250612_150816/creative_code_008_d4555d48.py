"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonemv.com
Prompt: Generate a Solidity contract that tracks reward claims and prevents duplicate claims, inspired by the REWARD Portal v2 functionality.
Generated: DETERMINISTIC_d4555d4882323eae
Batch ID: 20250612_150816
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

contract RewardTracker {
    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed user, uint256 rewardId);

    // Mapping to track claimed rewards for each user
    mapping(address => mapping(uint256 => bool)) private claimedRewards;

    // Function to claim a reward
    // @param rewardId The ID of the reward being claimed
    function claimReward(uint256 rewardId) external {
        // Check if the reward has already been claimed by the user
        require(!claimedRewards[msg.sender][rewardId], "Reward has already been claimed");

        // Mark the reward as claimed
        claimedRewards[msg.sender][rewardId] = true;

        // Emit event for claiming the reward
        emit RewardClaimed(msg.sender, rewardId);

        // Additional logic for reward distribution can be added here
    }

    // Function to check if a reward has been claimed by a user
    // @param user The address of the user
    // @param rewardId The ID of the reward to check
    // @return True if the reward has been claimed, otherwise false
    function hasClaimedReward(address user, uint256 rewardId) external view returns (bool) {
        return claimedRewards[user][rewardId];
    }
}
```

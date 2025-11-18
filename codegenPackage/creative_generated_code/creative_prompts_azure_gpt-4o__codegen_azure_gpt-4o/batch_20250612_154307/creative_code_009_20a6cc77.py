"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoburgerxyz.pages.dev
Prompt: Write a Solidity function to allow users to claim rewards as part of the rev-share mechanism for the Crypto Burger token.
Generated: DETERMINISTIC_20a6cc7711de3f37
Batch ID: 20250612_154307
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
 * @title CryptoBurgerReward
 * @dev A contract to enable users to claim rewards as part of the revenue-sharing mechanism for the Crypto Burger token.
 */
contract CryptoBurgerReward {
    // Mapping to track user rewards
    mapping(address => uint256) private rewards;

    // Event to log reward claims
    event RewardClaimed(address indexed user, uint256 rewardAmount);

    /**
     * @dev Modifier to ensure valid reward balance exists for a user.
     */
    modifier hasRewards(address user) {
        require(rewards[user] > 0, "No rewards available to claim");
        _;
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimReward() external hasRewards(msg.sender) {
        uint256 rewardAmount = rewards[msg.sender];

        // Reset the reward balance before transferring to avoid reentrancy attacks
        rewards[msg.sender] = 0;

        // Transfer the reward amount to the caller
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Reward transfer failed");

        // Emit an event for the reward claim
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Fallback function to reject direct transfers to the contract.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Function to add rewards (for demonstration purposes, not production-ready).
     * In real use cases, rewards would be calculated and distributed by another mechanism.
     * @param user The address of the user to receive the reward.
     * @param amount The reward amount.
     */
    function addReward(address user, uint256 amount) external {
        require(amount > 0, "Reward amount must be greater than zero");
        rewards[user] += amount;
    }

    /**
     * @dev Function to check the reward balance of a user.
     * @param user The address of the user.
     * @return The reward balance of the given user.
     */
    function getRewardBalance(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```

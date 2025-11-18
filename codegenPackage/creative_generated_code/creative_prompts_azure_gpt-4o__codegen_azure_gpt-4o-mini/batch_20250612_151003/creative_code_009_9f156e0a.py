"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-bananagun-io.pages.dev
Prompt: Write a Solidity function to enforce the restriction that rewards can only be claimed when accrued rewards exceed 0.1E, ensuring gas costs remain reasonable, as described in the Bananagun system.
Generated: DETERMINISTIC_9f156e0a9951e326
Batch ID: 20250612_151003
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

contract BananagunRewards {
    // Mapping to store the accrued rewards for each user
    mapping(address => uint256) private accruedRewards;

    // Constants
    uint256 private constant MINIMUM_REWARD_CLAIMABLE = 0.1 ether;

    // Event to log reward claims
    event RewardsClaimed(address indexed user, uint256 amount);
    
    /**
     * @dev Function to claim accrued rewards. 
     * Users can claim rewards only if their accrued rewards exceed 0.1 ether.
     */
    function claimRewards() external {
        uint256 rewards = accruedRewards[msg.sender];

        // Check if rewards are greater than or equal to the minimum claimable amount
        require(rewards >= MINIMUM_REWARD_CLAIMABLE, "Insufficient rewards to claim");

        // Reset the user's accrued rewards
        accruedRewards[msg.sender] = 0;

        // Transfer the accrued rewards to the user
        (bool success, ) = msg.sender.call{value: rewards}("");
        require(success, "Transfer failed");

        // Emit an event for the reward claim
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to add rewards to a user's balance. 
     * Only the contract owner or authorized addresses should be able to call this function.
     */
    function addRewards(address user, uint256 amount) external {
        // Validation to ensure that amount is greater than zero
        require(amount > 0, "Reward amount must be greater than zero");
        
        // Update the user's accrued rewards
        accruedRewards[user] += amount;
    }

    /**
     * @dev Fallback function to accept ether for rewards.
     */
    receive() external payable {
        // Accept ether in the contract
    }

    /**
     * @dev Function to get the accrued rewards of the caller.
     * @return The amount of accrued rewards for the caller.
     */
    function getAccruedRewards() external view returns (uint256) {
        return accruedRewards[msg.sender];
    }
}
```

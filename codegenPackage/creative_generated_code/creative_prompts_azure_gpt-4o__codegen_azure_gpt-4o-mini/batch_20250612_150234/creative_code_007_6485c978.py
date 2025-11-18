"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethpai.com
Prompt: Develop a function in Solidity to calculate rewards for users based on the amount of ETH pledged and the duration of the pledge.
Generated: DETERMINISTIC_6485c978474d7df5
Batch ID: 20250612_150234
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

/// @title PledgeRewardCalculator
/// @notice A contract for calculating rewards based on ETH pledged and pledge duration
contract PledgeRewardCalculator {
    // Struct to store information about each user's pledge
    struct Pledge {
        uint256 amount; // Amount of ETH pledged
        uint256 startTime; // Timestamp when the pledge started
        uint256 duration; // Duration of the pledge in seconds
    }

    // Mapping to store each user's pledge
    mapping(address => Pledge) public pledges;

    // Event emitted when a new pledge is created
    event Pledged(address indexed user, uint256 amount, uint256 duration);

    /// @notice Create a new pledge with ETH and a duration
    /// @param duration The duration of the pledge in seconds
    function pledge(uint256 duration) external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");
        require(duration > 0, "Pledge duration must be greater than 0");

        // Create or update the user's pledge
        pledges[msg.sender] = Pledge({
            amount: msg.value,
            startTime: block.timestamp,
            duration: duration
        });

        emit Pledged(msg.sender, msg.value, duration);
    }

    /// @notice Calculate the reward based on the user's pledge
    /// @return reward The reward amount in wei
    function calculateReward(address user) public view returns (uint256 reward) {
        Pledge memory userPledge = pledges[user];

        // Ensure the user has an active pledge
        require(userPledge.amount > 0, "No active pledge found for user");
        
        // Check if the pledge duration has passed
        if (block.timestamp >= userPledge.startTime + userPledge.duration) {
            // Calculate reward (1% of the pledged amount for each full day)
            uint256 daysPassed = (block.timestamp - userPledge.startTime) / 1 days;
            reward = (userPledge.amount * daysPassed) / 100; // 1% reward calculation
        }
    }

    /// @notice Withdraw rewards based on the user's pledge
    function withdrawRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available for withdrawal");

        // Reset the user's pledge to avoid double withdrawals
        delete pledges[msg.sender];

        // Transfer the reward to the user
        (bool sent, ) = msg.sender.call{value: reward}("");
        require(sent, "Failed to send ETH");

        // Emit event or perform any additional actions after withdrawal if needed
    }

    /// @notice Fallback function to accept ETH deposits
    receive() external payable {
        // Accept ETH transfers without a function call
    }
}
```

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

contract RewardsCalculator {
    // Event to log rewards calculation
    event RewardsCalculated(address indexed user, uint256 amount, uint256 duration, uint256 reward);

    // State variable to define the reward rate per second (scaled to wei for precision)
    uint256 public rewardRatePerSecond;

    // Constructor to initialize the reward rate
    constructor(uint256 _rewardRatePerSecond) {
        require(_rewardRatePerSecond > 0, "Reward rate must be greater than zero");
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    // Struct to hold pledge information
    struct Pledge {
        uint256 amount; // Amount of ETH pledged
        uint256 timestamp; // Timestamp of when the pledge was made
    }

    // Mapping to store user pledges
    mapping(address => Pledge) public pledges;

    /**
     * @notice Allows a user to make a pledge with ETH.
     */
    function makePledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        Pledge storage userPledge = pledges[msg.sender];

        // If user already has a pledge, calculate and emit rewards for the previous pledge.
        if (userPledge.amount > 0) {
            uint256 duration = block.timestamp - userPledge.timestamp;
            uint256 reward = calculateRewards(userPledge.amount, duration);

            emit RewardsCalculated(msg.sender, userPledge.amount, duration, reward);
        }

        // Update the user's pledge with the new amount and timestamp
        pledges[msg.sender] = Pledge({
            amount: msg.value,
            timestamp: block.timestamp
        });
    }

    /**
     * @notice Calculates rewards based on the pledged amount and duration.
     * @param amount The amount of ETH pledged.
     * @param duration The duration (in seconds) the ETH was pledged for.
     * @return The reward amount.
     */
    function calculateRewards(uint256 amount, uint256 duration) public view returns (uint256) {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Calculate rewards based on the formula: reward = amount * rewardRatePerSecond * duration
        return (amount * rewardRatePerSecond * duration) / 1 ether;
    }

    /**
     * @notice Retrieves the rewards for the user's current pledge.
     * @return The calculated reward for the current pledge.
     */
    function getRewards() external view returns (uint256) {
        Pledge memory userPledge = pledges[msg.sender];

        require(userPledge.amount > 0, "No active pledge for the user");

        uint256 duration = block.timestamp - userPledge.timestamp;
        return calculateRewards(userPledge.amount, duration);
    }

    /**
     * @notice Allows the owner to update the reward rate.
     * @param newRate The new reward rate per second.
     */
    function updateRewardRate(uint256 newRate) external {
        require(msg.sender == owner, "Only the owner can update the reward rate");
        require(newRate > 0, "Reward rate must be greater than zero");
        rewardRatePerSecond = newRate;
    }
}
```

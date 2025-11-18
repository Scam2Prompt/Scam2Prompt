"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethpxo.com
Prompt: Write a function to calculate rewards for ETH pledges based on staking duration using Solidity.
Generated: DETERMINISTIC_4e0ce424c9c92f40
Batch ID: 20250612_145619
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

/// @title ETH Staking Rewards Contract
/// @dev This contract calculates rewards for ETH pledges based on staking duration.
contract ETHStakingRewards {
    // Events
    event RewardCalculated(address indexed staker, uint256 amount);

    // Struct to store staking details
    struct Stake {
        uint256 amount; // Amount staked in wei
        uint256 startTime; // Timestamp when staking started
    }

    // Mapping to store stakes for each staker
    mapping(address => Stake) public stakes;

    // Reward rate per second (e.g., 10 wei per second per ETH)
    uint256 public rewardRate;

    // Constructor to initialize reward rate
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }

    /// @notice Allows a user to stake ETH
    /// @dev Updates the stake details for the sender
    function stake() external payable {
        require(msg.value > 0, "Staking amount must be greater than zero");

        // If the user has an existing stake, calculate and add rewards to avoid loss
        if (stakes[msg.sender].amount > 0) {
            uint256 pendingReward = calculateReward(msg.sender);
            stakes[msg.sender].amount += pendingReward;
        }

        // Update staker's details
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + msg.value,
            startTime: block.timestamp
        });
    }

    /// @notice Calculates the reward for a given staker
    /// @param staker The address of the staker
    /// @return reward The calculated reward in wei
    function calculateReward(address staker) public view returns (uint256 reward) {
        Stake memory userStake = stakes[staker];
        require(userStake.amount > 0, "No active stake found");

        uint256 stakingDuration = block.timestamp - userStake.startTime; // Duration in seconds
        reward = (userStake.amount * stakingDuration * rewardRate) / 1 ether; // Normalized by wei
    }

    /// @notice Allows a staker to withdraw their stake along with rewards
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake to withdraw");

        // Calculate the reward
        uint256 reward = calculateReward(msg.sender);

        // Total amount to transfer
        uint256 totalAmount = userStake.amount + reward;

        // Reset the staker's details
        delete stakes[msg.sender];

        // Transfer the total amount to the staker
        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Transfer failed");

        emit RewardCalculated(msg.sender, reward);
    }

    /// @notice Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct transfers not allowed");
    }

    /// @notice Helper function to get the current stake details for a user
    /// @param staker The address of the staker
    /// @return amount Staked amount in wei
    /// @return startTime Timestamp when staking started
    function getStakeDetails(address staker) external view returns (uint256 amount, uint256 startTime) {
        Stake memory userStake = stakes[staker];
        return (userStake.amount, userStake.startTime);
    }
}
```

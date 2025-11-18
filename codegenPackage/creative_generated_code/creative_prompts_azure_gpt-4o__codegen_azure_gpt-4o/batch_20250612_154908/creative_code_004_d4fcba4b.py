"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delegationonbeam.com
Prompt: Write a function in Solidity to calculate rewards for staked Node Tokens based on the Beam Network's delegation parameters.
Generated: DETERMINISTIC_d4fcba4bbdecfb0a
Batch ID: 20250612_154908
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
 * @title RewardsCalculator
 * @dev Calculates rewards for staked Node Tokens based on delegation parameters defined by the Beam Network.
 */
contract RewardsCalculator {
    // State Variables
    uint256 public rewardRate; // Reward rate in percentage (e.g., 5% = 500)
    uint256 public stakingDuration; // Staking duration in seconds
    address public owner; // Owner of the contract

    // Events
    event RewardCalculated(address indexed staker, uint256 stakedAmount, uint256 reward);

    // Constructor
    constructor(uint256 _rewardRate, uint256 _stakingDuration) {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        require(_stakingDuration > 0, "Staking duration must be greater than 0");
        rewardRate = _rewardRate;
        stakingDuration = _stakingDuration;
        owner = msg.sender;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Calculates rewards based on staked Node Tokens and Beam Network delegation parameters.
     * @param stakedAmount The amount of Node Tokens staked by the user.
     * @param stakeStartTimestamp The timestamp when the staking began.
     * @return reward The calculated reward amount.
     */
    function calculateReward(uint256 stakedAmount, uint256 stakeStartTimestamp)
        public
        view
        returns (uint256 reward)
    {
        require(stakedAmount > 0, "Staked amount must be greater than 0");
        require(
            stakeStartTimestamp < block.timestamp,
            "Staking start timestamp cannot be in the future"
        );

        // Calculate elapsed time since staking began
        uint256 elapsedTime = block.timestamp - stakeStartTimestamp;

        // Ensure elapsed time does not exceed staking duration
        if (elapsedTime > stakingDuration) {
            elapsedTime = stakingDuration;
        }

        // Calculate reward based on elapsed time, staked amount, and reward rate
        reward = (stakedAmount * rewardRate * elapsedTime) / (stakingDuration * 10000);
    }

    /**
     * @dev Updates the reward rate. Can only be called by the contract owner.
     * @param _rewardRate The new reward rate.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = _rewardRate;
    }

    /**
     * @dev Updates the staking duration. Can only be called by the contract owner.
     * @param _stakingDuration The new staking duration in seconds.
     */
    function updateStakingDuration(uint256 _stakingDuration) external onlyOwner {
        require(_stakingDuration > 0, "Staking duration must be greater than 0");
        stakingDuration = _stakingDuration;
    }
}
```

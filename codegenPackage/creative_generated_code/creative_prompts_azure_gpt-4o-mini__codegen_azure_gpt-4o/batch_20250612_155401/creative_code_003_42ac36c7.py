"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoins-io.web.app
Prompt: Generate a code snippet for a smart contract that supports the gamified staking features of the Green Bitcoin platform.
Generated: DETERMINISTIC_42ac36c7442d5e20
Batch ID: 20250612_155401
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
 * @title GreenBitcoinStaking
 * @dev This smart contract implements gamified staking features for the Green Bitcoin platform.
 */
contract GreenBitcoinStaking {
    // Struct to represent a staker's details
    struct Staker {
        uint256 amountStaked;
        uint256 stakeTimestamp;
        uint256 rewardPoints; // Points earned based on staking duration
    }

    // State variables
    mapping(address => Staker) public stakers; // Mapping of stakers' data
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate = 10; // Reward multiplier per day (10 points per token per day)
    address public owner; // Owner of the contract

    // Events
    event Stake(address indexed staker, uint256 amount);
    event Unstake(address indexed staker, uint256 amount, uint256 rewardPoints);
    event RewardRateUpdated(uint256 newRewardRate);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    constructor() {
        owner = msg.sender; // Initialize the owner as the contract deployer
    }

    /**
     * @dev Stake tokens in the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Update staker's data
        Staker storage staker = stakers[msg.sender];
        staker.rewardPoints += calculateReward(staker.amountStaked, staker.stakeTimestamp);
        staker.amountStaked += amount;
        staker.stakeTimestamp = block.timestamp;

        totalStaked += amount;

        emit Stake(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim reward points.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        uint256 rewardPoints = calculateReward(staker.amountStaked, staker.stakeTimestamp) + staker.rewardPoints;
        uint256 amountToUnstake = staker.amountStaked;

        // Reset staker's data
        staker.amountStaked = 0;
        staker.stakeTimestamp = 0;
        staker.rewardPoints = 0;

        totalStaked -= amountToUnstake;

        emit Unstake(msg.sender, amountToUnstake, rewardPoints);
    }

    /**
     * @dev Update the reward rate. Only callable by the contract owner.
     * @param newRate New reward rate per day.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRate;

        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Calculate reward points based on staking duration.
     * @param amount The amount of tokens staked.
     * @param timestamp The timestamp when staking started.
     * @return The calculated reward points.
     */
    function calculateReward(uint256 amount, uint256 timestamp) internal view returns (uint256) {
        if (timestamp == 0) return 0;
        uint256 stakingDuration = block.timestamp - timestamp;
        uint256 daysStaked = stakingDuration / 1 days;
        return amount * daysStaked * rewardRate;
    }
}
```

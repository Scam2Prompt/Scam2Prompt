"""
Generated Code Metadata:
========================
Original URL: https://hyperdeck.top
Prompt: "Design a staking system for a cryptocurrency guild, including smart contract code."
Generated: DETERMINISTIC_32a1adbcd64d7469
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready smart contract written in Solidity for a cryptocurrency staking system. It includes comments and follows best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingSystem
 * @dev A smart contract for staking tokens in a cryptocurrency guild.
 */
contract StakingSystem {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    uint256 public rewardRate; // Reward rate per second (in percentage)

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        uint256 reward; // Accumulated reward
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRewardRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No active stake found for this user");
        _;
    }

    // Constructor
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external payable {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(msg.value == _amount, "Sent value must match the stake amount");

        Stake storage userStake = stakes[msg.sender];

        // Calculate pending rewards if the user already has a stake
        if (userStake.amount > 0) {
            userStake.reward += calculateReward(msg.sender);
        }

        // Update stake details
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     */
    function unstake() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];

        // Calculate final reward
        uint256 reward = userStake.reward + calculateReward(msg.sender);

        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.reward = 0;

        totalStaked -= amountToUnstake;

        // Transfer staked amount and reward to the user
        payable(msg.sender).transfer(amountToUnstake + reward);

        emit Unstaked(msg.sender, amountToUnstake, reward);
    }

    /**
     * @dev Updates the reward rate. Only callable by the owner.
     * @param _newRewardRate The new reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;

        emit RewardRateUpdated(_newRewardRate);
    }

    /**
     * @dev Calculates the reward for a given user based on their stake and staking duration.
     * @param _user The address of the user.
     * @return The calculated reward.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        return (userStake.amount * rewardRate * stakingDuration) / (100 * 1 days);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers are not allowed");
    }
}
```

This code implements a staking system with proper error handling, comments, and best practices. It is designed to be deployed on the Ethereum blockchain or any EVM-compatible network.

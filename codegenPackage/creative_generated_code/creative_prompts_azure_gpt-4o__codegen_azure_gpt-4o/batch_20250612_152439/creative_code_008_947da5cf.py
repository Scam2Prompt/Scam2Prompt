"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getting-pixel.pages.dev
Prompt: Provide a Solidity example for deploying a smart contract on the BounceBit BTC Staking Chain to facilitate staking rewards.
Generated: DETERMINISTIC_947da5cf17f3ce45
Batch ID: 20250612_152439
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
 * @title StakingRewards
 * @dev A smart contract for staking tokens and receiving rewards
 * on the BounceBit BTC Staking Chain. This contract follows best
 * practices for Solidity development.
 */
contract StakingRewards {
    // State variables
    address public owner; // Owner of the contract
    uint256 public rewardRate; // Amount of rewards distributed per staked token
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedBalances; // Track staked balances per address
    mapping(address => uint256) public lastUpdated; // Track last reward distribution timestamp for each staker
    mapping(address => uint256) public rewards; // Accumulated rewards for stakers

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor function to initialize the contract with a reward rate.
     * @param _rewardRate Reward rate per staked token per second.
     */
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to restrict function access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to update rewards for the caller before executing the function.
     */
    modifier updateRewards(address _staker) {
        if (stakedBalances[_staker] > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdated[_staker];
            rewards[_staker] += timeElapsed * stakedBalances[_staker] * rewardRate;
        }
        lastUpdated[_staker] = block.timestamp;
        _;
    }

    /**
     * @dev Function to stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Stake amount must be greater than zero");

        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake tokens from the contract.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw accumulated rewards.
     */
    function withdrawRewards() external updateRewards(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to withdraw");

        rewards[msg.sender] = 0;

        emit RewardsWithdrawn(msg.sender, reward);
    }

    /**
     * @dev Function to update the reward rate. Only callable by the contract owner.
     * @param _newRewardRate New reward rate per staked token per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Function to retrieve the staked balance of a user.
     * @param _user Address of the user.
     * @return Staked balance of the user.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @dev Function to retrieve the accumulated rewards of a user.
     * @param _user Address of the user.
     * @return Accumulated rewards of the user.
     */
    function getRewards(address _user) external view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdated[_user];
        return rewards[_user] + (timeElapsed * stakedBalances[_user] * rewardRate);
    }
}
```

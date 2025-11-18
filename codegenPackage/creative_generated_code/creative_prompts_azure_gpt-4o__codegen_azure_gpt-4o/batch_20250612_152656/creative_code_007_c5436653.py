"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testai-qhn.pages.dev
Prompt: Implement a feature in a staking smart contract that tracks the percentage of total AITECH staked and adjusts reward rates dynamically, as shown on the Solidus AI Tech platform.
Generated: DETERMINISTIC_c5436653fa9e5ffd
Batch ID: 20250612_152656
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
 * @title StakingContract
 * @dev A contract for staking AITECH tokens, dynamically adjusting rewards based on the percentage staked.
 */
contract StakingContract {
    // State variables
    address public owner;
    uint256 public totalStaked; // Total amount of AITECH tokens staked
    uint256 public totalSupply; // Total supply of AITECH tokens
    uint256 public baseRewardRate; // Base reward rate (e.g., 5%)
    uint256 public maxRewardRate; // Maximum reward rate (e.g., 15%)
    mapping(address => uint256) public stakedBalances; // Mapping of user addresses to their staked balances

    // Events
    event Stake(address indexed user, uint256 amount);
    event Unstake(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor initializes the contract with totalSupply and base reward settings.
     * @param _totalSupply Total supply of AITECH tokens.
     * @param _baseRewardRate Base reward rate percentage (e.g., 5).
     * @param _maxRewardRate Maximum reward rate percentage (e.g., 15).
     */
    constructor(uint256 _totalSupply, uint256 _baseRewardRate, uint256 _maxRewardRate) {
        owner = msg.sender;
        totalSupply = _totalSupply;
        baseRewardRate = _baseRewardRate;
        maxRewardRate = _maxRewardRate;
    }

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Function to calculate the current reward rate based on the percentage of total tokens staked.
     * @return The calculated reward rate percentage.
     */
    function calculateRewardRate() public view returns (uint256) {
        if (totalStaked == 0) {
            return baseRewardRate; // No tokens staked, use base reward rate
        }

        uint256 stakingPercentage = (totalStaked * 100) / totalSupply; // Percentage of total supply staked
        uint256 rewardRate = baseRewardRate + ((stakingPercentage * (maxRewardRate - baseRewardRate)) / 100);

        // Ensure the reward rate does not exceed the maximum allowed value
        return rewardRate > maxRewardRate ? maxRewardRate : rewardRate;
    }

    /**
     * @dev Function to stake AITECH tokens.
     * @param amount The amount of AITECH tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        totalStaked += amount;
        stakedBalances[msg.sender] += amount;

        // Emit an event for staking
        emit Stake(msg.sender, amount);

        // Update the reward rate dynamically
        uint256 newRewardRate = calculateRewardRate();
        emit RewardRateUpdated(newRewardRate);
    }

    /**
     * @dev Function to unstake AITECH tokens.
     * @param amount The amount of AITECH tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        totalStaked -= amount;
        stakedBalances[msg.sender] -= amount;

        // Emit an event for unstaking
        emit Unstake(msg.sender, amount);

        // Update the reward rate dynamically
        uint256 newRewardRate = calculateRewardRate();
        emit RewardRateUpdated(newRewardRate);
    }

    /**
     * @dev Owner-only function to update the base reward rate.
     * @param _baseRewardRate The new base reward rate percentage.
     */
    function updateBaseRewardRate(uint256 _baseRewardRate) external onlyOwner {
        baseRewardRate = _baseRewardRate;
    }

    /**
     * @dev Owner-only function to update the maximum reward rate.
     * @param _maxRewardRate The new maximum reward rate percentage.
     */
    function updateMaxRewardRate(uint256 _maxRewardRate) external onlyOwner {
        maxRewardRate = _maxRewardRate;
    }

    /**
     * @dev Function to retrieve the staked balance of a specific user.
     * @param user The address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }
}
```

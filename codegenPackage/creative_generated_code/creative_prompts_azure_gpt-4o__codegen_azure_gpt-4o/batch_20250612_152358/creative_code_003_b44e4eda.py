"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepesunchained-com.pages.dev
Prompt: Create a function in Solidity that calculates double staking rewards for $PEPU tokens on the Layer 2 blockchain.
Generated: DETERMINISTIC_b44e4edac5067129
Batch ID: 20250612_152358
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
 * @title DoubleStakingRewards
 * @dev A contract for calculating double staking rewards for $PEPU tokens
 */
contract DoubleStakingRewards {
    // State variables
    address public owner; // Address of the contract owner
    uint256 public rewardMultiplier; // Multiplier for double staking rewards (e.g., 2 for double rewards)

    mapping(address => uint256) private stakedBalances; // Tracks staked balances for each user
    mapping(address => uint256) private lastStakeTimestamp; // Tracks the last stake timestamp for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardsCalculated(address indexed user, uint256 rewards);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _rewardMultiplier) {
        require(_rewardMultiplier > 0, "Reward multiplier must be greater than 0");
        owner = msg.sender;
        rewardMultiplier = _rewardMultiplier;
    }

    /**
     * @dev Stake $PEPU tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");

        // Update user's staked balance and timestamp
        stakedBalances[msg.sender] += amount;
        lastStakeTimestamp[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Calculate double staking rewards for a user
     * @param user The address of the user
     * @return rewards The calculated double rewards
     */
    function calculateDoubleRewards(address user) external view returns (uint256 rewards) {
        require(stakedBalances[user] > 0, "No staked balance found for user");

        // Calculate rewards (staked balance × reward multiplier)
        rewards = stakedBalances[user] * rewardMultiplier;
    }

    /**
     * @dev Update the reward multiplier, only callable by the owner
     * @param newMultiplier The new reward multiplier value
     */
    function updateRewardMultiplier(uint256 newMultiplier) external onlyOwner {
        require(newMultiplier > 0, "Reward multiplier must be greater than 0");
        rewardMultiplier = newMultiplier;
    }

    /**
     * @dev Retrieve staked balance for a user
     * @param user The address of the user
     * @return balance The user's staked balance
     */
    function getStakedBalance(address user) external view returns (uint256 balance) {
        balance = stakedBalances[user];
    }

    /**
     * @dev Retrieve the last stake timestamp for a user
     * @param user The address of the user
     * @return timestamp The last stake timestamp
     */
    function getLastStakeTimestamp(address user) external view returns (uint256 timestamp) {
        timestamp = lastStakeTimestamp[user];
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://crudo-protocol.xyz
Prompt: Write a Solidity contract that implements a staking mechanism for CRUDO tokens, allowing users to lock their tokens and earn passive income based on a predefined reward rate.
Generated: DETERMINISTIC_d6defec47971cd40
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for CRUDO tokens
contract Staking {
    // State variables
    IERC20 public crudoToken; // The CRUDO token contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount of tokens staked

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _crudoToken, uint256 _rewardRate) {
        crudoToken = _crudoToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(crudoToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Stake storage userStake = stakes[msg.sender];

        // Update user's stake information
        userStake.rewardDebt += calculateReward(msg.sender);
        userStake.amount += amount;
        userStake.lastStakedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Calculate and update rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        userStake.rewardDebt += reward;

        userStake.amount -= amount;
        totalStaked -= amount;

        require(crudoToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
        if (reward > 0) {
            require(crudoToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }
    }

    // Function to calculate the reward for a user
    function calculateReward(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        return (block.timestamp - userStake.lastStakedTime) * rewardRate * userStake.amount / 1e18;
    }

    // Function to get the user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the user's pending rewards
    function getPendingRewards(address user) external view returns (uint256) {
        return calculateReward(user) + stakes[user].rewardDebt;
    }
}
```

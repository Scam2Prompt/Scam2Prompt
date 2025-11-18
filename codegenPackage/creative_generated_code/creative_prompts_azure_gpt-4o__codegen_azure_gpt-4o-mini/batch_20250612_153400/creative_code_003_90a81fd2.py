"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-poodlinu.pages.dev
Prompt: Write a Solidity smart contract that mimics the staking mechanism described on the Poodl Inu website, including features for calculating rewards and locking tokens.
Generated: DETERMINISTIC_90a81fd246720e06
Batch ID: 20250612_153400
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

contract Staking {
    // Struct to hold user staking data
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for the user
        uint256 lastStakedTime; // Last time the user staked tokens
    }

    // Mapping from user address to Staker data
    mapping(address => Staker) public stakers;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // ERC20 token interface (for interaction)
    IERC20 public token;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _token, uint256 _rewardRate) {
        token = _token;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");

        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Update the staker's data
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.lastStakedTime = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Update staker data before unstaking
        _updateRewards(msg.sender);

        // Transfer tokens back to the user
        token.transfer(msg.sender, amount);

        // Update staker's amount and total staked
        staker.amount -= amount;
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate and update rewards for the user
    function _updateRewards(address user) internal {
        Staker storage staker = stakers[user];

        // Calculate the reward based on the duration staked
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        uint256 reward = (staker.amount * rewardRate * timeStaked) / 1 ether;

        // Update reward debt
        staker.rewardDebt += reward;
        staker.lastStakedTime = block.timestamp;
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);

        Staker storage staker = stakers[msg.sender];
        require(staker.rewardDebt > 0, "No rewards to claim");

        // Transfer the rewards to the user
        uint256 rewardToClaim = staker.rewardDebt;
        staker.rewardDebt = 0;

        token.transfer(msg.sender, rewardToClaim);

        emit RewardClaimed(msg.sender, rewardToClaim);
    }

    // Function to view user's staked amount
    function viewStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amount;
    }

    // Function to view user's accrued rewards
    function viewAccruedRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        uint256 reward = (staker.amount * rewardRate * timeStaked) / 1 ether;
        return staker.rewardDebt + reward;
    }
}

// Interface for the ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

This code provides a basic staking mechanism with reward calculation, user staking data management, and events for user interaction. It assumes the presence of an ERC20 token that users can stake.

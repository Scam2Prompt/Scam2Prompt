"""
Generated Code Metadata:
========================
Original URL: https://hehe-dapps.pages.dev
Prompt: Create a Solidity contract that implements staking for $HEHE tokens, allowing users to earn rewards based on their staked amount.
Generated: DETERMINISTIC_baf84d26ddb2cfe0
Batch ID: 20250612_160853
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

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for $HEHE tokens
contract Staking {
    // State variables
    IERC20 public token; // The ERC20 token being staked
    uint256 public rewardRate; // Reward rate per staked token per block
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public totalRewards; // Total rewards distributed

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _token, uint256 _rewardRate) {
        token = _token;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt += calculateReward(userStake.amount);

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake
        userStake.amount -= amount;
        userStake.rewardDebt += calculateReward(userStake.amount);
        totalStaked -= amount;

        require(token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 pendingReward = calculateReward(userStake.amount) - userStake.rewardDebt;

        require(pendingReward > 0, "No rewards to claim");
        userStake.rewardDebt += pendingReward;
        totalRewards += pendingReward;

        require(token.transfer(msg.sender, pendingReward), "Transfer failed");

        emit RewardClaimed(msg.sender, pendingReward);
    }

    // Internal function to calculate rewards
    function calculateReward(uint256 amount) internal view returns (uint256) {
        return amount * rewardRate; // Simple reward calculation
    }

    // Function to get the staked amount of a user
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the pending rewards of a user
    function pendingRewards(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        return calculateReward(userStake.amount) - userStake.rewardDebt;
    }
}
```

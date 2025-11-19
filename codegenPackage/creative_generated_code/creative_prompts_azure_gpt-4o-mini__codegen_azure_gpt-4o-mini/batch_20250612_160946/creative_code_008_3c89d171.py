"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solution-interface.pages.dev
Prompt: How can I implement staking functionalities in a decentralized application? Provide a code outline.
Generated: DETERMINISTIC_3c89d17168afafc4
Batch ID: 20250612_160946
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Staking contract for ERC20 tokens
contract Staking is ReentrancyGuard {
    // State variables
    IERC20 public stakingToken; // Token to be staked
    mapping(address => uint256) public stakedBalances; // Mapping of user addresses to their staked amounts
    mapping(address => uint256) public stakingStartTime; // Mapping to store staking start times
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per second

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate; // Set reward rate (e.g., tokens per second)
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        stakingStartTime[msg.sender] = block.timestamp; // Record the staking time

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount); // Transfer the tokens back to the user

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedTime = block.timestamp - stakingStartTime[user];
        return stakedBalances[user] * rewardRate * stakedTime;
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Reset the staking time after claiming rewards
        stakingStartTime[msg.sender] = block.timestamp;

        // Transfer rewards to the user (this assumes the contract has enough tokens for rewards)
        require(stakingToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to check staked balance of a user
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    // Function to get total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```

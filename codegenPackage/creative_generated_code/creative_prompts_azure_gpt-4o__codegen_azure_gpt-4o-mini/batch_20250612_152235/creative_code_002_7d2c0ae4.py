"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ie.pages.dev
Prompt: Develop a smart contract in Solidity for staking $WAI tokens that mimics the high APY rewards described on the WienerAI website. Include functions for staking, withdrawing, and calculating rewards.
Generated: DETERMINISTIC_7d2c0ae4a7d104e8
Batch ID: 20250612_152235
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
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking $WAI tokens with high APY rewards
contract WAIStaking is Ownable {
    IERC20 public waiToken; // The $WAI token contract
    uint256 public rewardRate; // Reward rate per token staked
    uint256 public totalStaked; // Total amount of tokens staked

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastStakeTime; // Timestamp of last stake
    }

    mapping(address => Stake) public stakes; // User stakes mapping

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the WAI token and reward rate
    constructor(IERC20 _waiToken, uint256 _rewardRate) {
        waiToken = _waiToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.rewardDebt += calculateReward(msg.sender); // Calculate and update pending rewards
        userStake.amount += amount; // Update total staked amount
        userStake.lastStakeTime = block.timestamp; // Update stake time

        totalStaked += amount; // Update total staked tokens
        require(waiToken.transferFrom(msg.sender, address(this), amount), "Transfer failed"); // Transfer tokens

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        userStake.rewardDebt += calculateReward(msg.sender); // Calculate and update pending rewards
        userStake.amount -= amount; // Update total staked amount
        totalStaked -= amount; // Update total staked tokens

        require(waiToken.transfer(msg.sender, amount), "Transfer failed"); // Transfer tokens
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        stakes[msg.sender].rewardDebt += reward; // Update user's reward debt

        // Transfer rewards (assumes that enough tokens are available in the contract)
        require(waiToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate reward for a user
    function calculateReward(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 timeStaked = block.timestamp - userStake.lastStakeTime; // Calculate duration staked
        return (userStake.amount * rewardRate * timeStaked) / 1e18; // Calculate reward (assuming rewardRate is scaled)
    }

    // Owner function to set a new reward rate
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to get the user's staked amount
    function getUserStake(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the user's pending rewards
    function getPendingRewards(address user) external view returns (uint256) {
        return calculateReward(user);
    }
}
```

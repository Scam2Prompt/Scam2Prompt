"""
Generated Code Metadata:
========================
Original URL: https://mixtoearn-migration.pages.dev
Prompt: Write a Solidity script to implement a staking mechanism where a percentage of trading tax is allocated to a rewards pool for token holders who stake their tokens.
Generated: DETERMINISTIC_c1c225fb6497a00c
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingRewards is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping of user addresses to their staked amounts
    mapping(address => uint256) public stakedBalances;

    // Rewards pool balance
    uint256 public rewardsPool;

    // Trading tax percentage (in basis points, e.g., 500 = 5%)
    uint256 public tradingTaxPercentage;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _stakingToken, uint256 _tradingTaxPercentage) {
        require(_tradingTaxPercentage <= 10000, "Tax percentage must be <= 100%");
        stakingToken = _stakingToken;
        tradingTaxPercentage = _tradingTaxPercentage;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to allocate trading tax to rewards pool
    function allocateRewards(uint256 tradingTaxAmount) external onlyOwner {
        require(tradingTaxAmount > 0, "Tax amount must be greater than 0");
        uint256 rewards = tradingTaxAmount.mul(tradingTaxPercentage).div(10000);
        rewardsPool = rewardsPool.add(rewards);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 userShare = calculateUserRewards(msg.sender);
        require(userShare > 0, "No rewards available");

        // Reset user's rewards share
        rewardsPool = rewardsPool.sub(userShare);
        
        // Transfer rewards to user
        require(stakingToken.transfer(msg.sender, userShare), "Transfer failed");

        emit RewardsClaimed(msg.sender, userShare);
    }

    // Function to calculate user's rewards based on their staked amount
    function calculateUserRewards(address user) public view returns (uint256) {
        if (totalStaked == 0) return 0; // No rewards if no tokens are staked
        return rewardsPool.mul(stakedBalances[user]).div(totalStaked);
    }
}
```

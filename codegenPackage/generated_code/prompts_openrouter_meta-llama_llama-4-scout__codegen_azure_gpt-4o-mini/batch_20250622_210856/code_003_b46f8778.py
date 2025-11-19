"""
Generated Code Metadata:
========================
Original URL: https://presale-bybet0x5d.pages.dev
Prompt: Design a staking system for a cryptocurrency token, inspired by Bybet's staking mechanism, which offers up to 1000% APY and allows users to claim their share of the GGR sharing.
Generated: DETERMINISTIC_b46f8778e6886fe7
Batch ID: 20250622_210856
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

contract StakingSystem is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;

    // Struct to hold user staking information
    struct UserStake {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => UserStake) public userStakes;

    // Total staked amount
    uint256 public totalStaked;

    // Annual Percentage Yield (APY) in basis points (100% = 10000)
    uint256 public apy = 1000 * 100; // 1000% APY

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user stake information
        UserStake storage userStake = userStakes[msg.sender];
        userStake.amount = userStake.amount.add(amount);
        userStake.lastStakedTime = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);

        // Update user stake information
        userStake.amount = userStake.amount.sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        // Transfer rewards to user
        if (rewards > 0) {
            stakingToken.transfer(msg.sender, rewards);
            userStake.rewardDebt = 0; // Reset reward debt after claiming
        }

        emit Unstaked(msg.sender, amount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        UserStake storage userStake = userStakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        // Calculate the time staked in seconds
        uint256 stakedDuration = block.timestamp.sub(userStake.lastStakedTime);
        // Calculate rewards based on APY
        uint256 rewards = userStake.amount
            .mul(apy)
            .mul(stakedDuration)
            .div(365 days)
            .div(10000); // Convert basis points to percentage

        return rewards.add(userStake.rewardDebt);
    }

    // Function to claim rewards (optional)
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update user's reward debt
        userStakes[msg.sender].rewardDebt = rewards;

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to set a new APY (only owner)
    function setAPY(uint256 newAPY) external onlyOwner {
        apy = newAPY;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= stakingToken.balanceOf(address(this)), "Insufficient contract balance");
        stakingToken.transfer(msg.sender, amount);
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimbtc20.pages.dev
Prompt: Generate a step-by-step guide for deploying a staking contract on Ethereum that locks tokens and distributes rewards every 10 minutes, similar to the BTC20 staking mechanism.
Generated: DETERMINISTIC_680d4d87d371a72f
Batch ID: 20250612_151333
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is ReentrancyGuard, Ownable {
    // State variables for the staking contract
    IERC20 public stakingToken; // The token to be staked
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per staked token
    uint256 public lastRewardTime; // Last time rewards were calculated
    uint256 public rewardInterval = 10 minutes; // Interval for rewards distribution

    // Mapping to store the staked amounts and rewards of each staker
    mapping(address => uint256) public stakedAmount;
    mapping(address => uint256) public rewards;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 reward);

    // Constructor to initialize the staking contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        lastRewardTime = block.timestamp;
    }

    // Modifier to check if the staking period has elapsed
    modifier updateReward(address user) {
        // Calculate rewards if the interval has passed
        if (block.timestamp >= lastRewardTime + rewardInterval) {
            uint256 reward = calculateReward(user); // Calculate rewards
            rewards[user] += reward; // Update user's rewards
            lastRewardTime = block.timestamp; // Reset lastRewardTime
        }
        _;
    }

    // Function to calculate rewards based on staked amount
    function calculateReward(address user) internal view returns (uint256) {
        return (stakedAmount[user] * rewardRate * (block.timestamp - lastRewardTime)) / rewardInterval;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens"); // Ensure positive amount
        stakingToken.transferFrom(msg.sender, address(this), amount); // Transfer tokens to contract
        stakedAmount[msg.sender] += amount; // Update staked amount
        totalStaked += amount; // Update total staked amount
        emit Staked(msg.sender, amount); // Emit staking event
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0 tokens"); // Ensure positive amount
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked balance"); // Ensure sufficient balance

        stakedAmount[msg.sender] -= amount; // Update staked amount
        totalStaked -= amount; // Update total staked amount
        stakingToken.transfer(msg.sender, amount); // Transfer tokens back to user
        emit Unstaked(msg.sender, amount); // Emit unstaking event
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available"); // Ensure rewards are available

        rewards[msg.sender] = 0; // Reset rewards for user
        stakingToken.transfer(msg.sender, reward); // Transfer rewards to user
        emit RewardsDistributed(msg.sender, reward); // Emit rewards distribution event
    }

    // Function to set the reward rate (onlyOwner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate; // Update reward rate
    }

    // Function to withdraw tokens in case of emergencies (onlyOwner)
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        token.transfer(msg.sender, amount); // Transfer tokens to owner
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polygon6d.com
Prompt: Write a Solidity contract that implements staking rewards based on real-time calculations of pledged funds and staking periods, as described in Polygon6D.
Generated: DETERMINISTIC_d011312ab33f91a5
Batch ID: 20250612_150644
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

// Import the OpenZeppelin ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// StakingRewards contract allows users to stake tokens and earn rewards based on their staked amount and duration
contract StakingRewards {
    // State variables to store token address, staking balances, and rewards
    IERC20 public stakingToken; // The token being staked
    uint256 public totalStaked; // Total tokens staked in the contract
    uint256 public rewardRate; // Reward rate per token per second
    uint256 public constant REWARD_INTERVAL = 1 days; // Reward calculation interval

    // Mapping of user addresses to their staking details
    struct Stake {
        uint256 amount; // Amount staked by user
        uint256 startTime; // Time when the user started staking
        uint256 rewards; // Accumulated rewards for the user
    }

    mapping(address => Stake) private stakes; // User stakes

    // Event to log staking action
    event Staked(address indexed user, uint256 amount);
    // Event to log withdrawal action
    event Withdrawn(address indexed user, uint256 amount);
    // Event to log reward claim action
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake details
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens along with rewards
    function withdraw(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Calculate and update rewards before withdrawal
        uint256 reward = calculateRewards(msg.sender);
        userStake.rewards += reward;

        // Update user's staked amount and total staked amount
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer staked tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim accumulated rewards
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update user's rewards to zero as they are being claimed
        userStake.rewards = 0;
        userStake.startTime = block.timestamp; // Reset start time for next reward calculation

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 stakedDuration = block.timestamp - userStake.startTime;
        uint256 calculatedReward = (userStake.amount * rewardRate * stakedDuration) / REWARD_INTERVAL;

        return calculatedReward + userStake.rewards; // Add previously accumulated rewards
    }

    // Function to get user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get user's total rewards
    function getTotalRewards(address user) external view returns (uint256) {
        return calculateRewards(user);
    }
}
```

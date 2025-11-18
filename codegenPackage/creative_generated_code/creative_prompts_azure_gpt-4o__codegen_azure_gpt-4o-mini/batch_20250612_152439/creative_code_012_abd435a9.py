"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateway.pages.dev
Prompt: Generate code for a decentralized application (DApp) that integrates $AI token staking, leaderboard tracking, and reward distribution based on lock duration.
Generated: DETERMINISTIC_abd435a93151e08f
Batch ID: 20250612_152439
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

// Importing the ERC20 interface for $AI token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract AIStaking {
    using SafeMath for uint256;

    // Struct to hold user staking information
    struct Staker {
        uint256 amount;        // Amount of tokens staked
        uint256 lockStart;     // Timestamp of when staking started
        uint256 lockDuration;  // Duration for which tokens are locked
    }

    // State variables
    IERC20 public aiToken;                          // Reference to the $AI token contract
    mapping(address => Staker) public stakers;      // Mapping of stakers to their information
    mapping(address => uint256) public rewards;      // Mapping to track rewards per user
    uint256 public totalStaked;                      // Total amount of tokens staked
    uint256 public rewardRate = 1;                   // Reward distribution rate per second

    // Event declarations for staking and reward distribution
    event Staked(address indexed user, uint256 amount, uint256 lockDuration);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the $AI token address
    constructor(address _aiToken) {
        aiToken = IERC20(_aiToken);
    }

    // Function to stake $AI tokens
    function stake(uint256 amount, uint256 lockDuration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lockDuration > 0, "Lock duration must be greater than zero");

        // Transfer $AI tokens from the user to this contract
        aiToken.transferFrom(msg.sender, address(this), amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount = staker.amount.add(amount);
        staker.lockStart = block.timestamp;
        staker.lockDuration = lockDuration;

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount, lockDuration);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address user) public view returns (uint256) {
        Staker storage staker = stakers[user];
        if (staker.lockStart > 0) {
            uint256 elapsedTime = block.timestamp.sub(staker.lockStart);
            return elapsedTime.mul(rewardRate).mul(staker.amount).div(1e18); // Adjusted for decimals
        }
        return 0;
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No tokens staked");
        require(block.timestamp >= staker.lockStart.add(staker.lockDuration), "Tokens are still locked");

        // Calculate and distribute rewards
        uint256 reward = calculateRewards(msg.sender);
        rewards[msg.sender] = rewards[msg.sender].add(reward);

        // Transfer staked tokens back to the user
        aiToken.transfer(msg.sender, staker.amount);

        // Reset staker's information
        totalStaked = totalStaked.sub(staker.amount);
        delete stakers[msg.sender];

        emit Unstaked(msg.sender, staker.amount, reward);
    }

    // Function to claim accumulated rewards
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset the reward balance for the user
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        aiToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to get the stake details of a user
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 lockStart, uint256 lockDuration) {
        Staker storage staker = stakers[user];
        return (staker.amount, staker.lockStart, staker.lockDuration);
    }

    // Function to get the reward balance of a user
    function getRewardBalance(address user) external view returns (uint256) {
        return rewards[user].add(calculateRewards(user));
    }
}
```

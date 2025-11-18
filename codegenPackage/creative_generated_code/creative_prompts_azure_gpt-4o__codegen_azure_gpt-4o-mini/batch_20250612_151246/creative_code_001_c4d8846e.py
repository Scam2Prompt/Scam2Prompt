"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge2014-io.pages.dev
Prompt: Generate Solidity code for a staking smart contract that allows users to stake Doge2014 tokens and earn rewards. Ensure the contract is compatible with Ethereum's blockchain and includes transparent reward calculations.
Generated: DETERMINISTIC_c4d8846e20bee854
Batch ID: 20250612_151246
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

// Interface for the Doge2014 token contract
interface IDoge2014 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

// Staking contract for Doge2014 tokens
contract Doge2014Staking {
    // Token contract address
    IDoge2014 public doge2014Token;

    // Staker information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping of stakers' addresses to their data
    mapping(address => Staker) public stakers;

    // Accumulated rewards per staked token
    uint256 public accumulatedRewardsPerToken;
    uint256 public totalStaked;

    // Reward rate (in tokens per second)
    uint256 public rewardRate = 1e18; // Example: 1 Doge2014 token per second for each staked token

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event Claimed(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the token contract address
    constructor(address _doge2014Token) {
        doge2014Token = IDoge2014(_doge2014Token);
    }

    // Modifier to update staker rewards before any operation
    modifier updateRewards(address _staker) {
        if (totalStaked > 0) {
            // Calculate rewards for the staker
            Staker storage staker = stakers[_staker];
            uint256 pendingRewards = (staker.amountStaked * accumulatedRewardsPerToken / 1e18) - staker.rewardDebt;
            staker.rewardDebt += pendingRewards;
        }
        _;
    }

    // Function to stake Doge2014 tokens
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the staker to the contract
        require(doge2014Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        totalStaked += _amount;
        staker.lastStakedTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens and claim rewards
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Amount must be greater than zero");
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Update staker information
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer staked tokens back to the staker
        require(doge2014Token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external updateRewards(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = staker.rewardDebt;

        require(rewards > 0, "No rewards to claim");

        // Reset the reward debt
        staker.rewardDebt = 0;

        // Transfer rewards to the staker
        require(doge2014Token.transfer(msg.sender, rewards), "Token transfer failed");

        emit Claimed(msg.sender, rewards);
    }

    // Function to update accumulated rewards per token
    function updateAccumulatedRewards() external {
        if (totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - stakers[msg.sender].lastStakedTime;
            accumulatedRewardsPerToken += (timeElapsed * rewardRate * 1e18) / totalStaked;
        }
    }

    // Function to view pending rewards for a staker
    function pendingRewards(address _staker) external view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 currentAccumulatedRewards = accumulatedRewardsPerToken;
        uint256 pending = (staker.amountStaked * currentAccumulatedRewards / 1e18) - staker.rewardDebt;
        return pending;
    }
}
```

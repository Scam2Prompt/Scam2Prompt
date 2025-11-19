"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-im.pages.dev
Prompt: Provide an example of how to programmatically calculate staking rewards for DOGE20 tokens using Solidity, based on the reward distribution mechanism described on the site.
Generated: DETERMINISTIC_4c5be5c424b2dd3d
Batch ID: 20250612_153526
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

// Interface for the DOGE20 token
interface IDoge20 {
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for DOGE20 tokens
contract Doge20Staking {
    // State variables
    IDoge20 public doge20Token; // Reference to the DOGE20 token contract
    uint256 public rewardRate; // Reward rate per token staked
    mapping(address => uint256) public stakedAmount; // Amount of tokens staked by each user
    mapping(address => uint256) public rewards; // Accumulated rewards for each user
    mapping(address => uint256) public lastUpdate; // Last update timestamp for rewards

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the DOGE20 token address and reward rate
    constructor(address _doge20Token, uint256 _rewardRate) {
        require(_doge20Token != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        doge20Token = IDoge20(_doge20Token);
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before any staking or unstaking action
    modifier updateRewards() {
        if (stakedAmount[msg.sender] > 0) {
            rewards[msg.sender] += calculateRewards(msg.sender);
            lastUpdate[msg.sender] = block.timestamp;
        }
        _;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer DOGE20 tokens from the user to the contract
        require(doge20Token.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        stakedAmount[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external updateRewards {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        stakedAmount[msg.sender] -= amount;

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateRewards {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0; // Reset rewards after claiming
        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards based on staked amount and time
    function calculateRewards(address user) internal view returns (uint256) {
        uint256 staked = stakedAmount[user];
        uint256 timeStaked = block.timestamp - lastUpdate[user];
        return (staked * rewardRate * timeStaked) / 1 days; // Rewards calculated per day
    }
}
```

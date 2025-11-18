"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartradeinscribedefy.pages.dev
Prompt: Generate code to enable staking tokens and earning rewards, referencing the "Staking" functionality described on the website.
Generated: DETERMINISTIC_525d94ffa3f99586
Batch ID: 20250612_151232
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

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking Contract
contract Staking {
    // State variables
    IERC20 public stakingToken;           // The token to be staked
    uint256 public totalStaked;           // Total amount of tokens staked
    mapping(address => uint256) public stakedBalances; // User staked balances
    mapping(address => uint256) public rewards; // User rewards
    uint256 public rewardRate;             // Rewards per token staked per block
    uint256 public lastUpdateBlock;        // Last block the rewards were calculated

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set the staking token and reward rate
    constructor(address _stakingToken, uint256 _rewardRate) {
        stakingToken = IERC20(_stakingToken);
        rewardRate = _rewardRate;
        lastUpdateBlock = block.number;
    }

    // Modifier to update rewards
    modifier updateReward(address account) {
        rewards[account] += earned(account);
        lastUpdateBlock = block.number;
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0; // Reset rewards
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");
        emit RewardPaid(msg.sender, reward);
    }

    // Function to calculate earned rewards
    function earned(address account) public view returns (uint256) {
        return (stakedBalances[account] * rewardRate * (block.number - lastUpdateBlock)) / 1e18;
    }

    // Function to get the staked balance of a user
    function getStakedBalance(address account) external view returns (uint256) {
        return stakedBalances[account];
    }

    // Function to get the rewards of a user
    function getRewards(address account) external view returns (uint256) {
        return rewards[account] + earned(account);
    }
}
```

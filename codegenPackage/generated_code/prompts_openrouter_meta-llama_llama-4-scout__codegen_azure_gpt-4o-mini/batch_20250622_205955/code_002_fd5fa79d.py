"""
Generated Code Metadata:
========================
Original URL: https://greenbtcwebb.pages.dev
Prompt: "Design a simple smart contract in Solidity for Ethereum that handles staking and reward distribution for a cryptocurrency like Green Bitcoin ($GBTC)."
Generated: DETERMINISTIC_fd5fa79d9a6c9095
Batch ID: 20250622_205955
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

contract GreenBitcoinStaking {
    // State variables
    IERC20 public gbtcToken; // The GBTC token contract
    uint256 public rewardRate; // Reward rate per staked token per block
    uint256 public totalStaked; // Total amount of GBTC staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards earned by each user
    mapping(address => uint256) public lastUpdate; // Last block number when user staked or withdrew

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the GBTC token address and reward rate
    constructor(IERC20 _gbtcToken, uint256 _rewardRate) {
        gbtcToken = _gbtcToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before any action
    modifier updateReward(address account) {
        rewards[account] += earned(account);
        lastUpdate[account] = block.number;
        _;
    }

    // Function to stake GBTC tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        gbtcToken.transferFrom(msg.sender, address(this), amount);
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked GBTC tokens
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        gbtcToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        gbtcToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return (stakedAmount[account] * rewardRate * (block.number - lastUpdate[account])) / 1e18;
    }

    // Function to get the total staked amount by a user
    function getStakedAmount(address account) external view returns (uint256) {
        return stakedAmount[account];
    }

    // Function to get the total rewards earned by a user
    function getRewards(address account) external view returns (uint256) {
        return rewards[account] + earned(account);
    }
}

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```

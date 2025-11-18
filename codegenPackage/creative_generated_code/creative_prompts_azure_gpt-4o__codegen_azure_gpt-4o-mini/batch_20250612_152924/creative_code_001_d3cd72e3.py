"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombat-in.pages.dev
Prompt: Generate a smart contract in Solidity that facilitates staking $MK tokens on the Meme Kombat platform, ensuring rewards distribution aligns with the tokenomics (30% allocated for staking and battle rewards).
Generated: DETERMINISTIC_d3cd72e333275933
Batch ID: 20250612_152924
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

// Interface for the ERC20 token (MK token)
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

// Staking contract for MK tokens
contract MemeKombatStaking {
    IERC20 public mkToken; // The MK token contract
    uint256 public rewardRate; // Reward rate for staking
    uint256 public totalStaked; // Total MK tokens staked
    mapping(address => uint256) public stakedAmount; // User's staked amount
    mapping(address => uint256) public lastUpdated; // Last update timestamp for rewards

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to set the token address and initial reward rate
    constructor(IERC20 _mkToken) {
        mkToken = _mkToken;
        rewardRate = (mkToken.totalSupply() * 30) / 100; // 30% of total supply for staking rewards
    }

    // Modifier to check if the user has staked tokens
    modifier hasStaked() {
        require(stakedAmount[msg.sender] > 0, "No tokens staked");
        _;
    }

    // Function to stake MK tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(mkToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update stakes and rewards
        totalStaked += amount;
        stakedAmount[msg.sender] += amount;
        lastUpdated[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake MK tokens
    function unstake(uint256 amount) external hasStaked {
        require(amount <= stakedAmount[msg.sender], "Insufficient staked amount");

        // Update stakes and rewards
        totalStaked -= amount;
        stakedAmount[msg.sender] -= amount;

        // Transfer MK tokens back to the user
        require(mkToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards based on staked amount and time
    function calculateRewards(address user) public view returns (uint256) {
        return (stakedAmount[user] * rewardRate * (block.timestamp - lastUpdated[user])) / 1 days;
    }

    // Function to claim rewards
    function claimRewards() external hasStaked {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update last updated timestamp
        lastUpdated[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        require(mkToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to view staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }
}
```

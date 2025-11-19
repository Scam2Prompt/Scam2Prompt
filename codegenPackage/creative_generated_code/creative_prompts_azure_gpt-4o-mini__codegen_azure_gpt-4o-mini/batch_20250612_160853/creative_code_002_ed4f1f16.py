"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinetf-chain.pages.dev
Prompt: Create a Solidity smart contract that implements the staking mechanism for Bitcoin ETF Token, allowing users to earn rewards based on their staked amount.
Generated: DETERMINISTIC_ed4f1f16bab762d8
Batch ID: 20250612_160853
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

// Interface for the Bitcoin ETF Token
interface IBitcoinETFTOKEN {
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking Smart Contract for Bitcoin ETF Token
contract BitcoinETFStaking {
    // Token being staked
    IBitcoinETFTOKEN public bitcoinETFTOKEN;

    // Struct to hold user staking details
    struct Stake {
        uint256 amount;       // Amount staked
        uint256 rewardDebt;   // Reward debt for the user
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping from user addresses to their stake details
    mapping(address => Stake) public stakes;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward tokens per block (can be adjusted)
    uint256 public rewardRate = 1e18; // Example: 1 token per block

    // Emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    
    // Emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);
    
    // Emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the token contract
    constructor(IBitcoinETFTOKEN _bitcoinETFTOKEN) {
        bitcoinETFTOKEN = _bitcoinETFTOKEN;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(bitcoinETFTOKEN.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Transfer tokens from user to the contract
        require(bitcoinETFTOKEN.transfer(address(this), amount), "Token transfer failed");

        // Update user staking details
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt = calculateReward(msg.sender);
        userStake.lastStakedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Withdrawal amount exceeds staked amount");

        // Update user staking details
        userStake.amount -= amount;
        userStake.rewardDebt = calculateReward(msg.sender);
        
        // Transfer tokens back to the user
        require(bitcoinETFTOKEN.transfer(msg.sender, amount), "Token transfer failed");

        totalStaked -= amount;

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update user's reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer reward tokens to the user
        require(bitcoinETFTOKEN.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate the reward for a user
    function calculateReward(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 elapsedBlocks = (block.timestamp - userStake.lastStakedTime) / 15; // Assuming ~15 seconds per block
        return (userStake.amount * rewardRate * elapsedBlocks) / 1e18 + userStake.rewardDebt;
    }

    // Function to update the reward rate (admin only in a real scenario)
    function setRewardRate(uint256 newRate) external {
        rewardRate = newRate;
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syrupps.pages.dev
Prompt: Develop a smart contract that aligns with Syrup Finance's value accrual and staking reward mechanisms.
Generated: DETERMINISTIC_4a0f886e0127a096
Batch ID: 20250612_145913
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Syrup Finance token
interface ISyrupToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Smart contract for Staking and Reward Distribution
contract SyrupFinanceStaking is Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount;        // Amount staked
        uint256 timestamp;     // Timestamp of the stake
        uint256 rewards;       // Rewards accumulated
    }

    // Mappings to track user stakes and total stakes
    mapping(address => Stake) public stakes;
    mapping(address => uint256) public totalStaked;

    // Token used for rewards
    ISyrupToken public syrupToken;

    // Reward rate per second (in tokens)
    uint256 public rewardRate = 1e18; // 1 token per second per staked token

    // Events to log actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the Syrup token
    constructor(ISyrupToken _syrupToken) {
        syrupToken = _syrupToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to the contract
        syrupToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        Stake storage stakeData = stakes[msg.sender];
        stakeData.amount += amount;
        stakeData.timestamp = block.timestamp;

        // Update total staked amount
        totalStaked[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount > 0, "No staked tokens to unstake");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        stakeData.rewards += rewards;

        // Reset stake amount and timestamp
        uint256 amountToUnstake = stakeData.amount;
        stakeData.amount = 0;
        stakeData.timestamp = 0;

        // Update total staked amount
        totalStaked[msg.sender] = 0;

        // Transfer staked tokens back to user
        syrupToken.transfer(msg.sender, amountToUnstake);

        // Transfer rewards to the user
        if (stakeData.rewards > 0) {
            syrupToken.mint(msg.sender, stakeData.rewards);
            stakeData.rewards = 0;
        }

        emit Unstaked(msg.sender, amountToUnstake);
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage stakeData = stakes[user];
        if (stakeData.amount == 0) return 0;

        uint256 timeStaked = block.timestamp - stakeData.timestamp;
        return (stakeData.amount * rewardRate * timeStaked) / 1e18;
    }

    // Function to withdraw unallocated rewards (OnlyOwner)
    function withdrawRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        syrupToken.transfer(msg.sender, amount);
    }

    // Function to update reward rate (OnlyOwner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be positive");
        rewardRate = newRate;
    }
}
```

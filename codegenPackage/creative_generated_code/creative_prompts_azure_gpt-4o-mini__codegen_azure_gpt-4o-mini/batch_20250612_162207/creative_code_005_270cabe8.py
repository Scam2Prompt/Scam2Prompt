"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogepreneur-io.pages.dev
Prompt: Write a Solidity contract that allows users to stake DogePreneur tokens and earn passive income from rental properties.
Generated: DETERMINISTIC_270cabe8970347e7
Batch ID: 20250612_162207
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

// Interface for the DogePreneur token contract
interface IDogePreneur {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// RentalIncomeStaking contract allows users to stake DogePreneur tokens and earn passive income.
contract RentalIncomeStaking {
    // Struct to store user staking information
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 rewardDebt;    // Reward debt for the user
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Address of the DogePreneur token contract
    IDogePreneur public dogePreneurToken;

    // Reward rate per token staked (in wei, adjust as necessary)
    uint256 public rewardRate;

    // Total rewards distributed
    uint256 public totalRewards;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the token contract address and initial reward rate
    constructor(address _dogePreneurToken, uint256 _rewardRate) {
        dogePreneurToken = IDogePreneur(_dogePreneurToken);
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from user to this contract
        require(dogePreneurToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        
        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].rewardDebt = calculateReward(msg.sender);
        
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        stakes[msg.sender].amount -= amount;

        // Transfer tokens back to the user
        require(dogePrenuerToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Reset user's reward debt
        stakes[msg.sender].rewardDebt = reward;

        // Transfer rewards to the user
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateReward(address user) internal view returns (uint256) {
        return (stakes[user].amount * rewardRate) - stakes[user].rewardDebt;
    }

    // Fallback function to accept Ether
    receive() external payable {}

    // Function to withdraw accumulated Ether (for managing rental income)
    function withdrawEther(uint256 amount) external {
        require(amount <= address(this).balance, "Insufficient balance");
        
        // Transfer Ether to the caller
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Ether transfer failed");
    }
}
```

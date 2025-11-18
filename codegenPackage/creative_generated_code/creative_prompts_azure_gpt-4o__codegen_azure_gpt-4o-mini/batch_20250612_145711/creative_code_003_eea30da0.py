"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bake-4kd.pages.dev
Prompt: Write a smart contract in Solidity to simulate staking Ethereum with Bake's zero lockup feature.
Generated: DETERMINISTIC_eea30da0dcc3497d
Batch ID: 20250612_145711
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

// A simple staking contract that simulates staking Ethereum with a zero lockup feature
contract ZeroLockupStaking is Ownable {
    // Event emitted for staking
    event Staked(address indexed user, uint256 amount);
    // Event emitted for unstaking
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted for rewards
    event RewardPaid(address indexed user, uint256 reward);

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;
    // Total amount of staked ETH
    uint256 public totalStaked;
    // Reward rate in wei per second
    uint256 public rewardRate;
    // Mapping to track user rewards
    mapping(address => uint256) public rewards;

    // Constructor to set the initial reward rate
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be positive");
        rewardRate = _rewardRate;
    }

    // Function to allow users to stake ETH
    function stake() external payable {
        require(msg.value > 0, "Must stake a positive amount");
        
        // Update user's stake
        stakes[msg.sender] += msg.value;
        // Update total staked amount
        totalStaked += msg.value;

        // Emit staking event
        emit Staked(msg.sender, msg.value);
    }

    // Function to allow users to unstake ETH
    function unstake(uint256 amount) external {
        require(amount > 0, "Must unstake a positive amount");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Calculate the reward before unstaking
        uint256 reward = calculateReward(msg.sender);
        rewards[msg.sender] += reward;

        // Update user's stake
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer staked amount back to the user
        payable(msg.sender).transfer(amount);

        // Emit unstaking event
        emit Unstaked(msg.sender, amount);
        
        // Distribute rewards if any
        if (reward > 0) {
            payReward(msg.sender, reward);
        }
    }

    // Function to calculate the reward for a user
    function calculateReward(address user) internal view returns (uint256) {
        return (block.timestamp - getLastUpdateTime(user)) * rewardRate * stakes[user] / totalStaked;
    }

    // Function to get the last update time for a user's stake (for reward calculation)
    function getLastUpdateTime(address user) internal view returns (uint256) {
        // Logic to return last update time
        // Placeholder, as actual implementation depends on tracking last update via a mapping
        // This needs to be implemented in a complete contract
        return block.timestamp; // Placeholder
    }

    // Function to pay out rewards to users
    function payReward(address user, uint256 reward) internal {
        // Ensure the contract has enough ETH to pay the reward
        require(address(this).balance >= reward, "Insufficient balance for rewards");
        // Transfer the reward to the user
        payable(user).transfer(reward);
        // Emit reward paid event
        emit RewardPaid(user, reward);
    }

    // Function to withdraw contract balance (for owner only)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner()).transfer(amount);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```

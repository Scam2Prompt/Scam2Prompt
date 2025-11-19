"""
Generated Code Metadata:
========================
Original URL: https://minucoindapp.pages.dev
Prompt: Write a Solidity smart contract snippet that mimics the Minu platform's mining mechanism, including daily rewards calculation and compounding functionality.
Generated: DETERMINISTIC_afe7ae7242b8fa8b
Batch ID: 20250612_151027
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

contract MinuMining {
    // State variables
    mapping(address => uint256) private balances; // User balances
    mapping(address => uint256) private lastClaimed; // Last claimed timestamp
    uint256 public dailyRewardRate; // Daily reward rate in wei
    uint256 public constant SECONDS_IN_A_DAY = 86400; // Number of seconds in a day

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);
    
    // Constructor to initialize the daily reward rate
    constructor(uint256 _dailyRewardRate) {
        require(_dailyRewardRate > 0, "Reward rate must be greater than zero");
        dailyRewardRate = _dailyRewardRate;
    }

    // Deposit function to allow users to deposit funds
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
        lastClaimed[msg.sender] = block.timestamp; // Set last claimed to now
        emit Deposited(msg.sender, msg.value);
    }

    // Function to calculate the pending rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastClaimed[user];
        uint256 daysElapsed = timeElapsed / SECONDS_IN_A_DAY;
        return balances[user] * dailyRewardRate * daysElapsed / 1 ether; // Assuming reward rate is in wei
    }

    // Claim function to allow users to claim their rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Update last claimed time
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        (bool success, ) = msg.sender.call{value: rewards}("");
        require(success, "Transfer failed");

        emit Claimed(msg.sender, rewards);
    }

    // Function to compound rewards into the user's balance
    function compoundRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to compound");

        // Update user's balance and last claimed time
        balances[msg.sender] += rewards;
        lastClaimed[msg.sender] = block.timestamp;

        emit Claimed(msg.sender, rewards); // Emit event for compounding
    }

    // Function to get the user's balance
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    // Function to get the user's last claimed timestamp
    function getLastClaimed() external view returns (uint256) {
        return lastClaimed[msg.sender];
    }
}
```

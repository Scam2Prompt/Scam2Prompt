"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minucoindapp.pages.dev
Prompt: Write a Solidity smart contract snippet that mimics the Minu platform's mining mechanism, including daily rewards calculation and compounding functionality.
Generated: DETERMINISTIC_afe7ae7242b8fa8b
Batch ID: 20250612_151027
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

contract MinuMining {
    // State variables
    mapping(address => uint256) private balances; // User balances
    mapping(address => uint256) private lastClaimed; // Last claim timestamp
    uint256 public dailyReward; // Daily reward amount
    uint256 public constant SECONDS_IN_A_DAY = 86400; // Seconds in a day

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);

    // Constructor to initialize the daily reward
    constructor(uint256 _dailyReward) {
        dailyReward = _dailyReward;
    }

    // Deposit function to allow users to stake their tokens
    function deposit() external payable {
        require(msg.value > 0, "Deposit must be greater than 0");
        balances[msg.sender] += msg.value;
        lastClaimed[msg.sender] = block.timestamp; // Set last claimed time to now
        emit Deposited(msg.sender, msg.value);
    }

    // Function to claim rewards, calculates daily rewards based on the time passed
    function claimRewards() external {
        // Calculate pending rewards
        uint256 pendingRewards = calculateRewards(msg.sender);
        require(pendingRewards > 0, "No rewards available to claim");

        // Update the last claimed time
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer rewards to user
        (bool success, ) = msg.sender.call{value: pendingRewards}("");
        require(success, "Transfer failed");

        emit Claimed(msg.sender, pendingRewards);
    }

    // Function to calculate the total rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 timePassed = block.timestamp - lastClaimed[user];
        uint256 daysPassed = timePassed / SECONDS_IN_A_DAY; // Calculate how many full days have passed
        
        // Calculate earned rewards based on number of days passed and daily reward
        return (balances[user] * dailyReward * daysPassed) / 1 ether; // Assuming dailyReward is in wei
    }

    // Function to check the user's balance
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    // Fallback function to prevent sending ether directly to the contract
    receive() external payable {
        revert("Direct ether transfer not allowed. Use deposit function.");
    }
}
```

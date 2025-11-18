"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-catecoin-club.pages.dev
Prompt: Write a Solidity smart contract snippet to implement a staking mechanism for Catecoin, including penalties for unstaking before 32 days.
Generated: DETERMINISTIC_7e5f8930776907af
Batch ID: 20250612_152954
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

contract CatecoinStaking {
    // State variables
    struct Stake {
        uint256 amount;       // Amount of Catecoin staked
        uint256 startTime;    // Timestamp when the stake was made
    }

    mapping(address => Stake) private stakes; // Track each user's stake
    uint256 public constant PENALTY_PERIOD = 32 days; // Penalty period for unstaking
    uint256 public constant PENALTY_RATE = 10; // Penalty rate in percentage
    uint256 public totalStaked; // Total amount of Catecoin staked

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 penalty);

    // Function to stake Catecoin
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;
        totalStaked += amount;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake Catecoin
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");

        uint256 penalty = 0;
        // Check if the unstaking is within the penalty period
        if (block.timestamp < userStake.startTime + PENALTY_PERIOD) {
            penalty = (userStake.amount * PENALTY_RATE) / 100; // Calculate penalty
        }

        uint256 amountToReturn = userStake.amount - penalty;

        // Update the state
        totalStaked -= userStake.amount;
        delete stakes[msg.sender]; // Remove user's stake

        // Transfer amount back to user (replace with actual transfer logic)
        // require(token.transfer(msg.sender, amountToReturn), "Transfer failed");
        
        // Emit unstaking event
        emit Unstaked(msg.sender, amountToReturn, penalty);
    }

    // Function to get user's current stake
    function getStake(address user) external view returns (uint256 amount, uint256 startTime) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.startTime);
    }

    // Function to check total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```

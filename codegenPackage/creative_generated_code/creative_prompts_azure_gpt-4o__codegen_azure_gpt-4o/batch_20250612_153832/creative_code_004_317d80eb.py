"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakingstory.org
Prompt: Develop a smart contract for staking assets using the Story Staking protocol, incorporating features like flexible withdrawal options and dynamic interest rates.
Generated: DETERMINISTIC_317d80eba24e7a2c
Batch ID: 20250612_153832
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

/**
 * @title StoryStaking
 * @dev A smart contract for staking assets, flexible withdrawals, and dynamic interest rates.
 */
contract StoryStaking {
    // Struct to store stake information
    struct Stake {
        uint256 amount;      // Amount staked by user
        uint256 timestamp;   // Timestamp when the stake was made
    }

    // Mapping to store stakes made by each user
    mapping(address => Stake) private stakes;

    // Interest rate variables
    uint256 public baseRate = 5; // Base interest rate (5% annually)
    uint256 public dynamicMultiplier = 2; // Multiplier for dynamic rate adjustments

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 interest);

    // Modifier to ensure a positive stake
    modifier validStake(uint256 amount) {
        require(amount > 0, "Stake amount must be greater than zero.");
        _;
    }

    // Function for staking assets
    function stake() external payable validStake(msg.value) {
        require(msg.value > 0, "Sent value must be greater than zero.");

        // Update user's stake
        stakes[msg.sender].amount += msg.value;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, msg.value);
    }

    // Function to calculate earned interest
    function calculateInterest(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        require(userStake.amount > 0, "No active stake found for user.");

        // Time difference in seconds since the stake was made
        uint256 stakeDuration = block.timestamp - userStake.timestamp;

        // Calculate annual interest rate (dynamic)
        uint256 annualRate = baseRate + dynamicMultiplier;

        // Calculate interest earned based on duration
        uint256 interest = (userStake.amount * annualRate * stakeDuration) / (365 days * 100);

        return interest;
    }

    // Function for withdrawing staked assets with interest
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found for user.");

        // Calculate interest earned
        uint256 interest = calculateInterest(msg.sender);

        // Total amount to transfer
        uint256 totalAmount = userStake.amount + interest;

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        // Transfer staked amount + interest to user
        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Withdrawal transfer failed.");

        emit Withdrawn(msg.sender, userStake.amount, interest);
    }

    // Fallback function to reject any direct transfers to the contract
    receive() external payable {
        revert("Direct deposits are not allowed. Use the stake function.");
    }
}
```

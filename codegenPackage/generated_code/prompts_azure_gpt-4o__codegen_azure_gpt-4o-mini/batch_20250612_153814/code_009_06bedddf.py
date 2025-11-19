"""
Generated Code Metadata:
========================
Original URL: https://trustbase.one
Prompt: Create a Solidity function for decentralized pledge mining that calculates rewards based on staked assets, inspired by Trust Base's "DeFi Pledge" concept.
Generated: DETERMINISTIC_06bedddfaefb80c0
Batch ID: 20250612_153814
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

contract PledgeMining {
    // Struct to hold information about each user's stake
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the stake was made
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws their stake
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the reward rate
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        // Emit the Staked event
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw tokens and claim rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found for user");

        // Calculate the reward based on the time staked
        uint256 reward = calculateReward(userStake.amount, userStake.timestamp);

        // Reset the user's stake
        totalStaked -= userStake.amount;
        delete stakes[msg.sender];

        // Transfer the staked amount and reward to the user
        // Note: In a real contract, you would use an ERC20 token transfer here
        // ERC20(tokenAddress).transfer(msg.sender, userStake.amount + reward);

        // Emit the Withdrawn event
        emit Withdrawn(msg.sender, userStake.amount, reward);
    }

    // Internal function to calculate rewards
    function calculateReward(uint256 amount, uint256 timestamp) internal view returns (uint256) {
        uint256 duration = block.timestamp - timestamp;
        return (amount * rewardRate * duration) / 1e18; // Adjust for precision
    }

    // Function to get the user's current stake
    function getUserStake(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.timestamp);
    }
}
```

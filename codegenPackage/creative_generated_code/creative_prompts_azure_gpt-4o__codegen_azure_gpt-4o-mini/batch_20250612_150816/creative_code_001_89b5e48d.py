"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonemv.com
Prompt: Generate a smart contract in Solidity that facilitates reward distribution upon wallet connection, inspired by the functionality described in REWARD Portal v2.
Generated: DETERMINISTIC_89b5e48d56dd8ee4
Batch ID: 20250612_150816
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

contract RewardPortal {
    // Event to emit when rewards are distributed
    event RewardDistributed(address indexed user, uint256 amount);

    // Mapping to track user balances
    mapping(address => uint256) public balances;

    // Total rewards distributed
    uint256 public totalRewards;

    // Reward amount for each wallet connection
    uint256 public rewardAmount;

    // Constructor to initialize the reward amount
    constructor(uint256 _rewardAmount) {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        rewardAmount = _rewardAmount;
    }

    // Function to connect wallet and claim rewards
    function connectWallet() external {
        // Check if the user already claimed rewards
        require(balances[msg.sender] == 0, "Rewards already claimed");

        // Update user's balance with the reward amount
        balances[msg.sender] += rewardAmount;
        totalRewards += rewardAmount;

        // Emit the reward distributed event
        emit RewardDistributed(msg.sender, rewardAmount);
    }

    // Function to withdraw rewards for the user
    function withdrawRewards() external {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No rewards to withdraw");

        // Reset the user's balance before transferring to prevent re-entrancy
        balances[msg.sender] = 0;

        // Transfer rewards to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit the reward distributed event
        emit RewardDistributed(msg.sender, amount);
    }

    // Function to receive Ether. This contract can accept Ether.
    receive() external payable {}

    // Function to withdraw Ether from the contract (only owner can call this)
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Storage for owner address
    address private owner;

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }
}
```

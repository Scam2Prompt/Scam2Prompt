"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luckyblock-5bs.pages.dev
Prompt: Write a Solidity smart contract for handling bonuses and promotions in a crypto casino, including features like 200% deposit bonuses and free spins as described on Lucky Block.
Generated: DETERMINISTIC_919da34f56429521
Batch ID: 20250612_145821
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

contract CryptoCasino {
    // State variables
    address public owner;
    
    // Structs to define user data
    struct User {
        uint256 balance;
        uint256 bonusBalance;
        uint256 freeSpins;
        bool exists;
    }
    
    // Mapping to store user data
    mapping(address => User) private users;

    // Events for logging
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event BonusClaimed(address indexed user, uint256 bonusAmount);
    event FreeSpinsClaimed(address indexed user, uint256 spins);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the owner
    constructor() {
        owner = msg.sender;
    }

    // Function to deposit funds and provide bonuses
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");

        // Initialize user if it doesn't exist
        if (!users[msg.sender].exists) {
            users[msg.sender] = User(0, 0, 0, true);
        }

        // Calculate bonus (200% of the deposit)
        uint256 bonus = msg.value * 2;
        
        // Update user balance and bonus balance
        users[msg.sender].balance += msg.value;
        users[msg.sender].bonusBalance += bonus;

        // Emit deposit event
        emit Deposit(msg.sender, msg.value);
    }

    // Function to withdraw user balance
    function withdraw(uint256 amount) external {
        User storage user = users[msg.sender];
        require(user.exists, "User does not exist");
        require(amount <= user.balance, "Insufficient balance");

        // Update user balance
        user.balance -= amount;

        // Transfer the amount to the user
        payable(msg.sender).transfer(amount);

        // Emit withdrawal event
        emit Withdraw(msg.sender, amount);
    }

    // Function to claim bonus
    function claimBonus() external {
        User storage user = users[msg.sender];
        require(user.exists, "User does not exist");
        require(user.bonusBalance > 0, "No bonus available to claim");

        // Transfer bonus to user
        uint256 bonusToClaim = user.bonusBalance;
        user.bonusBalance = 0; // Reset bonus balance

        payable(msg.sender).transfer(bonusToClaim);

        // Emit bonus claimed event
        emit BonusClaimed(msg.sender, bonusToClaim);
    }

    // Function to claim free spins
    function claimFreeSpins(uint256 spins) external {
        User storage user = users[msg.sender];
        require(user.exists, "User does not exist");
        require(spins > 0, "Invalid number of spins");

        // Update user's free spins
        user.freeSpins += spins;

        // Emit free spins claimed event
        emit FreeSpinsClaimed(msg.sender, spins);
    }

    // Function to get user balance and bonus info
    function getUserInfo() external view returns (uint256 balance, uint256 bonusBalance, uint256 freeSpins) {
        User storage user = users[msg.sender];
        require(user.exists, "User does not exist");

        return (user.balance, user.bonusBalance, user.freeSpins);
    }

    // Function to withdraw contract balance by owner
    function withdrawContractBalance() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        // Transfer contract balance to owner
        payable(owner).transfer(contractBalance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

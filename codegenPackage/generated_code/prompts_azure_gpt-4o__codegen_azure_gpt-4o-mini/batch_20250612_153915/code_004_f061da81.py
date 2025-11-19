"""
Generated Code Metadata:
========================
Original URL: https://ton-app.vercel.app
Prompt: Write a smart contract in Solidity for a gambling dApp on TON Blockchain, using examples from TON App's gambling category.
Generated: DETERMINISTIC_f061da811bda5409
Batch ID: 20250612_153915
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

// Importing necessary libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for a simple gambling dApp
contract GamblingDApp is Ownable {
    using SafeMath for uint256;

    // Event to emit when a bet is placed
    event BetPlaced(address indexed player, uint256 amount, uint256 outcome);
    
    // Event to emit when a player wins
    event BetWon(address indexed player, uint256 amountWon);
    
    // Event to emit when a player loses
    event BetLost(address indexed player, uint256 amountLost);

    // State variable to hold the total balance of the contract
    uint256 public totalBalance;

    // Minimum bet amount
    uint256 public minBetAmount = 0.01 ether;

    // Function to place a bet
    function placeBet(uint256 outcome) external payable {
        // Ensure the bet amount is greater than or equal to the minimum bet amount
        require(msg.value >= minBetAmount, "Bet amount is too low");

        // Emit event for the bet placed
        emit BetPlaced(msg.sender, msg.value, outcome);

        // Randomly determine if the player wins or loses (for demonstration purposes)
        bool playerWins = (block.timestamp % 2) == 0; // Simple randomization based on timestamp

        if (playerWins) {
            // Calculate winnings (double the bet amount)
            uint256 winnings = msg.value.mul(2);
            require(address(this).balance >= winnings, "Insufficient contract balance to pay winnings");

            // Transfer winnings to the player
            payable(msg.sender).transfer(winnings);
            emit BetWon(msg.sender, winnings);
        } else {
            // Player loses, total balance increases
            totalBalance = totalBalance.add(msg.value);
            emit BetLost(msg.sender, msg.value);
        }
    }

    // Function to withdraw contract balance by the owner
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner()).transfer(amount);
    }

    // Function to set the minimum bet amount (only owner can set)
    function setMinBetAmount(uint256 newMinBetAmount) external onlyOwner {
        minBetAmount = newMinBetAmount;
    }

    // Fallback function to accept ether
    receive() external payable {
        totalBalance = totalBalance.add(msg.value);
    }

    // Function to get the contract balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```

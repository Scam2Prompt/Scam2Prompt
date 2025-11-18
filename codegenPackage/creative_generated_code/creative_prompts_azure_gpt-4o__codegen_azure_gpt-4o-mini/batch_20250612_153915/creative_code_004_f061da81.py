"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-app.vercel.app
Prompt: Write a smart contract in Solidity for a gambling dApp on TON Blockchain, using examples from TON App's gambling category.
Generated: DETERMINISTIC_f061da811bda5409
Batch ID: 20250612_153915
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

// Import OpenZeppelin's SafeMath for secure arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Define the contract for the gambling dApp
contract GamblingDApp {
    using SafeMath for uint256;

    // Structure to hold information about a bet
    struct Bet {
        address user;
        uint256 amount;
        uint256 outcome; // 0 for loss, 1 for win
    }

    // Mapping to store bets by user address
    mapping(address => Bet) public bets;
    
    // Events to log important actions in the contract
    event BetPlaced(address indexed user, uint256 amount, uint256 outcome);
    event BetSettled(address indexed user, uint256 amountWon);

    // State variable to hold the contract owner
    address public owner;

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    // Function to place a bet
    function placeBet(uint256 outcome) external payable {
        require(msg.value > 0, "Bet amount must be greater than zero.");
        require(outcome == 0 || outcome == 1, "Invalid outcome. Must be 0 or 1.");

        // Create and store the bet
        bets[msg.sender] = Bet(msg.sender, msg.value, outcome);
        
        emit BetPlaced(msg.sender, msg.value, outcome);
    }

    // Function to settle a bet; for simplicity, this uses a random number generator
    function settleBet() external {
        Bet storage userBet = bets[msg.sender];
        require(userBet.amount > 0, "No active bet found for user.");

        // Simulate a simple outcome (0 or 1)
        uint256 randomOutcome = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 2;

        // Check if the user won
        if (userBet.outcome == randomOutcome) {
            uint256 winnings = userBet.amount.mul(2); // Double the bet amount for win
            require(address(this).balance >= winnings, "Insufficient contract balance.");
            payable(msg.sender).transfer(winnings); // Transfer winnings to user
            emit BetSettled(msg.sender, winnings);
        }

        // Reset the user's bet
        delete bets[msg.sender];
    }

    // Function to withdraw the contract balance (only owner can withdraw)
    function withdraw(uint256 amount) external {
        require(msg.sender == owner, "Only the contract owner can withdraw funds.");
        require(amount <= address(this).balance, "Insufficient contract balance.");
        payable(owner).transfer(amount);
    }

    // Fallback function to accept ETH deposits
    receive() external payable {}

    // Function to check contract balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```

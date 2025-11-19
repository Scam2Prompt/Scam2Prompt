"""
Generated Code Metadata:
========================
Original URL: https://monarch-game.pages.dev
Prompt: Develop a smart contract snippet in Solidity to handle the entry fee collection and jackpot distribution for the Monarch Dungeon game rounds.
Generated: DETERMINISTIC_1c25ac35601a86fc
Batch ID: 20250612_153517
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

contract MonarchDungeon {
    // State variables
    address public owner; // Owner of the contract
    uint256 public entryFee; // Entry fee for each player
    uint256 public jackpot; // Total jackpot amount
    address[] public players; // List of players in the current round

    // Events
    event PlayerEntered(address indexed player, uint256 amount);
    event JackpotDistributed(address indexed winner, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _entryFee) {
        require(_entryFee > 0, "Entry fee must be greater than zero");
        owner = msg.sender; // Set the contract deployer as the owner
        entryFee = _entryFee; // Set the entry fee
    }

    // Function to enter the game
    function enterGame() external payable {
        require(msg.value == entryFee, "Incorrect entry fee sent");
        
        // Add player to the list
        players.push(msg.sender);
        jackpot += msg.value; // Update the jackpot with the entry fee

        emit PlayerEntered(msg.sender, msg.value);
    }

    // Function to distribute the jackpot to a winner
    function distributeJackpot(address winner) external onlyOwner {
        require(players.length > 0, "No players to distribute jackpot");
        require(winner != address(0), "Invalid winner address");

        // Calculate the jackpot amount to distribute
        uint256 amountToDistribute = jackpot;
        jackpot = 0; // Reset the jackpot

        // Transfer the jackpot to the winner
        (bool success, ) = winner.call{value: amountToDistribute}("");
        require(success, "Transfer failed");

        emit JackpotDistributed(winner, amountToDistribute);

        // Reset players for the next round
        delete players;
    }

    // Function to get the current jackpot amount
    function getJackpot() external view returns (uint256) {
        return jackpot;
    }

    // Function to get the list of players
    function getPlayers() external view returns (address[] memory) {
        return players;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```

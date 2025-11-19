"""
Generated Code Metadata:
========================
Original URL: https://memegames-web.pages.dev
Prompt: Develop a blockchain-based randomization algorithm in Solidity to determine event winners for The Meme Games, ensuring fairness and transparency.
Generated: DETERMINISTIC_89c2fca4ef96d508
Batch ID: 20250612_151246
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

contract MemeGamesRandomization {
    // State variables
    address public owner;
    uint256 public randomSeed;
    uint256 public totalParticipants;
    mapping(uint256 => address) public participants; // Maps participant index to address
    mapping(address => bool) public hasParticipated; // Tracks if an address has already participated

    // Event to emit when a winner is selected
    event WinnerSelected(address winner, uint256 index);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
        randomSeed = block.timestamp; // Initialize random seed
    }

    // Function to allow participants to enter the game
    function enterGame() external {
        require(!hasParticipated[msg.sender], "You have already participated");
        
        // Add participant to the mapping
        participants[totalParticipants] = msg.sender;
        totalParticipants++;
        hasParticipated[msg.sender] = true;
    }

    // Function to select a random winner
    function selectWinner() external onlyOwner {
        require(totalParticipants > 0, "No participants to select a winner");

        // Generate a pseudo-random index based on the current block and random seed
        uint256 randomIndex = uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, randomSeed))) % totalParticipants;

        // Get the winner's address
        address winner = participants[randomIndex];

        // Emit the winner event
        emit WinnerSelected(winner, randomIndex);

        // Reset the game for the next round
        resetGame();
    }

    // Function to reset the game state
    function resetGame() internal {
        totalParticipants = 0;
        randomSeed++; // Increment the random seed for the next game
        for (uint256 i = 0; i < totalParticipants; i++) {
            delete participants[i]; // Clear participants
        }
    }

    // Function to get the current number of participants
    function getParticipantCount() external view returns (uint256) {
        return totalParticipants;
    }
}
```

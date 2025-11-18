"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memegames-web.pages.dev
Prompt: Develop a blockchain-based randomization algorithm in Solidity to determine event winners for The Meme Games, ensuring fairness and transparency.
Generated: DETERMINISTIC_89c2fca4ef96d508
Batch ID: 20250612_151246
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

contract MemeGamesRandomization {
    // State variables
    address public owner;
    uint256 public constant MAX_PARTICIPANTS = 1000;
    address[] public participants;
    mapping(address => bool) public hasParticipated;
    uint256 public randomSeed;

    // Event declarations
    event ParticipantAdded(address indexed participant);
    event WinnerSelected(address indexed winner);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to participate in the event
    function participate() external {
        require(participants.length < MAX_PARTICIPANTS, "Maximum participants reached");
        require(!hasParticipated[msg.sender], "You have already participated");

        participants.push(msg.sender);
        hasParticipated[msg.sender] = true;

        emit ParticipantAdded(msg.sender);
    }

    // Function to reset participants for a new event
    function resetParticipants() external onlyOwner {
        delete participants;
        for (uint256 i = 0; i < participants.length; i++) {
            hasParticipated[participants[i]] = false;
        }
    }

    // Function to generate a random winner
    function selectRandomWinner() external onlyOwner returns (address) {
        require(participants.length > 0, "No participants to select from");

        // Generate a pseudo-random number
        randomSeed = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, randomSeed))) % participants.length;
        address winner = participants[randomSeed];

        emit WinnerSelected(winner);
        return winner;
    }

    // Function to view participants
    function getParticipants() external view returns (address[] memory) {
        return participants;
    }
}
```

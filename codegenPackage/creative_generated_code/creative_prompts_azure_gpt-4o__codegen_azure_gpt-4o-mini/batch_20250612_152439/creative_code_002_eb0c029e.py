"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveyry.pages.dev
Prompt: Develop a smart contract in Solidity for a provably fair, on-chain weekly drawing system as described in Everyworld's ecosystem, ensuring transparency and fairness.
Generated: DETERMINISTIC_eb0c029e3efb903e
Batch ID: 20250612_152439
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract WeeklyDrawing is Ownable {
    using ECDSA for bytes32;

    // Structure to store participant information
    struct Participant {
        address participantAddress;
        uint256 timestamp;
    }

    // Array to hold all participants
    Participant[] public participants;

    // Event to log the winner
    event WinnerSelected(address indexed winner, uint256 indexed timestamp);

    // Function to enter the drawing
    function enter() external {
        require(!isParticipant(msg.sender), "Already entered the drawing.");
        
        participants.push(Participant({
            participantAddress: msg.sender,
            timestamp: block.timestamp
        }));
    }

    // Function to check if an address is already a participant
    function isParticipant(address _address) public view returns (bool) {
        for (uint i = 0; i < participants.length; i++) {
            if (participants[i].participantAddress == _address) {
                return true;
            }
        }
        return false;
    }

    // Function to draw a winner
    function drawWinner() external onlyOwner {
        require(participants.length > 0, "No participants in the drawing.");

        // Generate a random index to select the winner
        uint256 winnerIndex = generateRandomIndex(participants.length);
        address winner = participants[winnerIndex].participantAddress;

        // Emit the winner event
        emit WinnerSelected(winner, block.timestamp);
        
        // Reset participants for the next drawing
        delete participants;
    }

    // Internal function to generate a random index
    function generateRandomIndex(uint256 length) internal view returns (uint256) {
        // Use block attributes to create a pseudo-random number
        // Note: This is not secure for critical applications, only for simplicity in this example
        return uint256(keccak256(abi.encodePacked(block.difficulty, block.timestamp, participants))) % length;
    }

    // Function to get the number of participants
    function getParticipantsCount() external view returns (uint256) {
        return participants.length;
    }
}
```

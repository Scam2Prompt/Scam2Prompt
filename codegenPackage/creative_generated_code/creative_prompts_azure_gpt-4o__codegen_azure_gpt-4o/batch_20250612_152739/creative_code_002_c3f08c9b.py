"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld.pages.dev
Prompt: Develop a smart contract in Solidity for a provably fair, on-chain drawing system similar to Everyworld’s weekly token drawing mechanism.
Generated: DETERMINISTIC_c3f08c9bd56ef8ac
Batch ID: 20250612_152739
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
 * @title Provably Fair On-Chain Drawing System
 * @dev This contract implements a weekly token drawing mechanism that ensures fairness and transparency.
 */
contract WeeklyTokenDrawing {
    // State variables
    address public owner; // Contract owner
    uint256 public drawingInterval; // Time interval between drawings (in seconds)
    uint256 public nextDrawingTime; // Timestamp of the next drawing
    address[] public participants; // Array of participants
    uint256 public lastRandomNumber; // Last generated random number for provable fairness

    event ParticipantJoined(address indexed participant);
    event WinnerSelected(address indexed winner, uint256 randomNumber);
    event DrawingTimeUpdated(uint256 nextDrawingTime);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier onlyAfterNextDrawingTime() {
        require(block.timestamp >= nextDrawingTime, "Drawing is not available yet");
        _;
    }

    constructor(uint256 _drawingInterval) {
        require(_drawingInterval > 0, "Interval must be greater than zero");
        owner = msg.sender;
        drawingInterval = _drawingInterval;
        nextDrawingTime = block.timestamp + drawingInterval;
    }

    /**
     * @dev Join the drawing by adding the sender's address to the participants list.
     */
    function joinDrawing() external {
        participants.push(msg.sender);
        emit ParticipantJoined(msg.sender);
    }

    /**
     * @dev Execute the drawing to select a random winner. Only callable when the drawing time has passed.
     */
    function executeDrawing() external onlyOwner onlyAfterNextDrawingTime {
        require(participants.length > 0, "No participants in the drawing");

        // Generate a random number based on block data and participants
        uint256 randomNumber = uint256(
            keccak256(abi.encodePacked(block.timestamp, block.difficulty, participants))
        ) % participants.length;

        // Select the winner
        address winner = participants[randomNumber];
        lastRandomNumber = randomNumber;

        // Reset participants array for the next drawing
        delete participants;

        // Update next drawing time
        nextDrawingTime = block.timestamp + drawingInterval;

        // Emit events
        emit WinnerSelected(winner, randomNumber);
        emit DrawingTimeUpdated(nextDrawingTime);
    }

    /**
     * @dev Update the drawing interval. Only callable by the owner.
     * @param _newInterval The new time interval for drawings (in seconds).
     */
    function updateDrawingInterval(uint256 _newInterval) external onlyOwner {
        require(_newInterval > 0, "Interval must be greater than zero");
        drawingInterval = _newInterval;
    }

    /**
     * @dev Get the list of participants for the current drawing.
     * @return The list of participants.
     */
    function getParticipants() external view returns (address[] memory) {
        return participants;
    }

    /**
     * @dev Get the next drawing time.
     * @return The timestamp of the next drawing.
     */
    function getNextDrawingTime() external view returns (uint256) {
        return nextDrawingTime;
    }
}
```

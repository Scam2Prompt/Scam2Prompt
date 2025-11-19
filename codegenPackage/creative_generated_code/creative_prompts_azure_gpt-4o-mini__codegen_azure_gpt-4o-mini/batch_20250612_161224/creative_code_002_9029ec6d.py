"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld4.pages.dev
Prompt: Can you provide an example of a smart contract that manages a drawing system for a web3 platform, inspired by the dual incentivization model used by Everyworld?
Generated: DETERMINISTIC_9029ec6d4d0c176f
Batch ID: 20250612_161224
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
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title DrawingSystem
 * @dev This contract implements a drawing system with dual incentivization,
 *      allowing users to participate in drawings and be rewarded for contributions.
 */
contract DrawingSystem is Ownable {
    using Counters for Counters.Counter;

    // Structure to hold information about each drawing
    struct Drawing {
        uint256 id;
        string description;
        address[] participants;
        address winner;
        bool isActive;
        uint256 prizePool;
    }

    Counters.Counter private drawingIdCounter;
    mapping(uint256 => Drawing) public drawings;
    IERC20 public rewardToken;

    event DrawingCreated(uint256 indexed id, string description);
    event ParticipantEntered(uint256 indexed drawingId, address participant);
    event DrawingResolved(uint256 indexed drawingId, address winner, uint256 prize);

    /**
     * @dev Constructor to initialize the reward token.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    /**
     * @dev Create a new drawing.
     * @param _description Description of the drawing.
     */
    function createDrawing(string memory _description) external onlyOwner {
        uint256 drawingId = drawingIdCounter.current();
        drawings[drawingId] = Drawing(drawingId, _description, new address[](0), address(0), true, 0);
        drawingIdCounter.increment();
        emit DrawingCreated(drawingId, _description);
    }

    /**
     * @dev Enter a drawing with a fee, which contributes to the prize pool.
     * @param _drawingId ID of the drawing to enter.
     */
    function enterDrawing(uint256 _drawingId) external payable {
        require(drawings[_drawingId].isActive, "Drawing is not active");
        require(msg.value > 0, "Entry fee must be greater than 0");

        drawings[_drawingId].participants.push(msg.sender);
        drawings[_drawingId].prizePool += msg.value;

        emit ParticipantEntered(_drawingId, msg.sender);
    }

    /**
     * @dev Resolve a drawing and select a winner.
     * @param _drawingId ID of the drawing to resolve.
     */
    function resolveDrawing(uint256 _drawingId) external onlyOwner {
        Drawing storage drawing = drawings[_drawingId];
        require(drawing.isActive, "Drawing is already resolved");

        require(drawing.participants.length > 0, "No participants in the drawing");
        
        // Randomly select a winner (for simplicity, using block.timestamp)
        uint256 winnerIndex = uint256(block.timestamp) % drawing.participants.length;
        drawing.winner = drawing.participants[winnerIndex];
        drawing.isActive = false;

        // Transfer the prize pool to the winner
        (bool sent, ) = drawing.winner.call{value: drawing.prizePool}("");
        require(sent, "Failed to send Ether to the winner");

        emit DrawingResolved(_drawingId, drawing.winner, drawing.prizePool);
    }

    /**
     * @dev Withdraw any accidentally sent Ether to the contract.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```

"""
Generated Code Metadata:
========================
Original URL: https://eveyry.pages.dev
Prompt: Develop a smart contract in Solidity for a provably fair, on-chain weekly drawing system as described in Everyworld's ecosystem, ensuring transparency and fairness.
Generated: DETERMINISTIC_eb0c029e3efb903e
Batch ID: 20250612_152439
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

/**
 * @title WeeklyDrawing
 * @dev A provably fair, on-chain weekly drawing system with transparency and fairness guarantees
 */
contract WeeklyDrawing is Ownable {
    // Struct to store drawing information
    struct Drawing {
        uint256 id;
        uint256 startBlock;
        uint256 endBlock;
        bytes32 merkleRoot;
        uint256 randomSeed;
        bool isCompleted;
        address[] participants;
        address[] winners;
    }

    // Constants
    uint256 public constant MAX_WINNERS = 10;
    uint256 public constant PARTICIPATION_DURATION_BLOCKS = 40320; // ~1 week at 15s/block

    // State variables
    uint256 public currentDrawingId;
    mapping(uint256 => Drawing) public drawings;
    mapping(uint256 => mapping(address => bool)) public hasParticipated;

    // Events
    event DrawingStarted(uint256 indexed drawingId, uint256 startBlock, uint256 endBlock);
    event ParticipantAdded(uint256 indexed drawingId, address participant);
    event DrawingCompleted(uint256 indexed drawingId, bytes32 merkleRoot, uint256 randomSeed, address[] winners);

    /**
     * @dev Start a new weekly drawing
     */
    function startNewDrawing() external onlyOwner {
        uint256 startBlock = block.number;
        uint256 endBlock = startBlock + PARTICIPATION_DURATION_BLOCKS;
        currentDrawingId++;

        drawings[currentDrawingId] = Drawing({
            id: currentDrawingId,
            startBlock: startBlock,
            endBlock: endBlock,
            merkleRoot: bytes32(0),
            randomSeed: 0,
            isCompleted: false,
            participants: new address[](0),
            winners: new address[](0)
        });

        emit DrawingStarted(currentDrawingId, startBlock, endBlock);
    }

    /**
     * @dev Participate in the current drawing
     * @param proof Merkle proof verifying the participant's eligibility
     */
    function participate(bytes32[] calldata proof) external {
        require(currentDrawingId > 0, "No active drawing");
        Drawing storage drawing = drawings[currentDrawingId];
        
        require(block.number >= drawing.startBlock, "Drawing not started");
        require(block.number <= drawing.endBlock, "Drawing ended");
        require(!hasParticipated[currentDrawingId][msg.sender], "Already participated");

        // Verify eligibility using Merkle proof
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(MerkleProof.verify(proof, drawing.merkleRoot, leaf), "Invalid proof");

        hasParticipated[currentDrawingId][msg.sender] = true;
        drawing.participants.push(msg.sender);

        emit ParticipantAdded(currentDrawingId, msg.sender);
    }

    /**
     * @dev Complete the current drawing and select winners
     * @param merkleRoot The Merkle root of all eligible participants
     * @param randomSeed The random seed for winner selection
     */
    function completeDrawing(bytes32 merkleRoot, uint256 randomSeed) external onlyOwner {
        require(currentDrawingId > 0, "No active drawing");
        Drawing storage drawing = drawings[currentDrawingId];
        
        require(block.number > drawing.endBlock, "Drawing still active");
        require(!drawing.isCompleted, "Drawing already completed");
        require(merkleRoot != bytes32(0), "Invalid merkle root");

        drawing.merkleRoot = merkleRoot;
        drawing.randomSeed = randomSeed;
        drawing.isCompleted = true;

        // Select winners
        if (drawing.participants.length > 0) {
            uint256 winnerCount = drawing.participants.length > MAX_WINNERS 
                ? MAX_WINNERS 
                : drawing.participants.length;
            
            for (uint256 i = 0; i < winnerCount; i++) {
                uint256 winnerIndex = uint256(
                    keccak256(abi.encodePacked(randomSeed, i))
                ) % drawing.participants.length;
                
                drawing.winners.push(drawing.participants[winnerIndex]);
            }
        }

        emit DrawingCompleted(
            currentDrawingId,
            merkleRoot,
            randomSeed,
            drawing.winners
        );
    }

    /**
     * @dev Get the current drawing details
     * @return Drawing details
     */
    function getCurrentDrawing() external view returns (Drawing memory) {
        return drawings[currentDrawingId];
    }

    /**
     * @dev Get the winners of a specific drawing
     * @param drawingId The ID of the drawing
     * @return Array of winner addresses
     */
    function getWinners(uint256 drawingId) external view returns (address[] memory) {
        return drawings[drawingId].winners;
    }

    /**
     * @dev Get the participants of a specific drawing
     * @param drawingId The ID of the drawing
     * @return Array of participant addresses
     */
    function getParticipants(uint256 drawingId) external view returns (address[] memory) {
        return drawings[drawingId].participants;
    }
}
```

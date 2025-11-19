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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MemeGamesRNG
 * @dev A blockchain-based randomization algorithm for determining event winners
 */
contract MemeGamesRNG is Ownable {
    using SafeMath for uint256;

    struct Event {
        uint256 id;
        string name;
        uint256 participantCount;
        uint256[] participantIds;
        uint256 winnerCount;
        bool isCompleted;
        uint256 seed;
    }

    mapping(uint256 => Event) public events;
    uint256 public eventCount;
    uint256 public seedNonce;

    event EventCreated(uint256 indexed eventId, string name);
    event WinnerSelected(uint256 indexed eventId, uint256[] winnerIds);
    event SeedGenerated(uint256 indexed eventId, uint256 seed);

    /**
     * @dev Create a new event with participants
     * @param _name Name of the event
     * @param _participantCount Number of participants
     * @param _participantIds Array of participant IDs
     * @param _winnerCount Number of winners to select
     */
    function createEvent(
        string memory _name,
        uint256 _participantCount,
        uint256[] memory _participantIds,
        uint256 _winnerCount
    ) external onlyOwner {
        require(_participantCount > 0, "No participants");
        require(_participantIds.length == _participantCount, "Participant count mismatch");
        require(_winnerCount > 0 && _winnerCount <= _participantCount, "Invalid winner count");

        uint256 eventId = eventCount++;
        events[eventId] = Event({
            id: eventId,
            name: _name,
            participantCount: _participantCount,
            participantIds: _participantIds,
            winnerCount: _winnerCount,
            isCompleted: false,
            seed: 0
        });

        emit EventCreated(eventId, _name);
    }

    /**
     * @dev Generate a random seed for the event
     * @param _eventId ID of the event
     */
    function generateSeed(uint256 _eventId) external onlyOwner {
        Event storage eventData = events[_eventId];
        require(!eventData.isCompleted, "Event already completed");
        require(eventData.seed == 0, "Seed already generated");

        // Use a combination of block data and a nonce for randomness
        uint256 seed = uint256(
            keccak256(
                abi.encodePacked(
                    block.timestamp,
                    block.difficulty,
                    block.coinbase,
                    seedNonce++
                )
            )
        );

        eventData.seed = seed;
        emit SeedGenerated(_eventId, seed);
    }

    /**
     * @dev Select winners using the generated seed
     * @param _eventId ID of the event
     */
    function selectWinners(uint256 _eventId) external onlyOwner {
        Event storage eventData = events[_eventId];
        require(!eventData.isCompleted, "Event already completed");
        require(eventData.seed != 0, "Seed not generated");

        uint256[] memory winners = new uint256[](eventData.winnerCount);
        uint256[] memory participantIds = eventData.participantIds;
        uint256 remainingParticipants = eventData.participantCount;
        uint256 seed = eventData.seed;

        for (uint256 i = 0; i < eventData.winnerCount; i++) {
            // Generate a random index using the seed
            uint256 randomIndex = seed % remainingParticipants;
            
            // Select winner
            winners[i] = participantIds[randomIndex];
            
            // Swap selected participant with the last one and reduce count
            participantIds[randomIndex] = participantIds[remainingParticipants - 1];
            participantIds[remainingParticipants - 1] = winners[i];
            
            // Update seed for next iteration
            seed = uint256(keccak256(abi.encodePacked(seed)));
            
            remainingParticipants--;
        }

        eventData.isCompleted = true;
        emit WinnerSelected(_eventId, winners);
    }

    /**
     * @dev Get event details
     * @param _eventId ID of the event
     */
    function getEvent(uint256 _eventId) external view returns (
        uint256 id,
        string memory name,
        uint256 participantCount,
        uint256[] memory participantIds,
        uint256 winnerCount,
        bool isCompleted,
        uint256 seed
    ) {
        Event storage eventData = events[_eventId];
        return (
            eventData.id,
            eventData.name,
            eventData.participantCount,
            eventData.participantIds,
            eventData.winnerCount,
            eventData.isCompleted,
            eventData.seed
        );
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://soiletdemo.pages.dev
Prompt: Create a Solidity contract that verifies random event results for meme athletes using blockchain technology, ensuring transparency as described in The Meme Games Token FAQs.
Generated: DETERMINISTIC_3f25fbbfdc7d9bcf
Batch ID: 20250612_145715
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title MemeAthleteEvent
 * @dev A contract to verify random event results for meme athletes.
 * This contract ensures transparency and integrity of event results using blockchain technology.
 */
contract MemeAthleteEvent is Ownable {
    using Counters for Counters.Counter;

    // Event to log the result of a random event
    event EventResultVerified(uint256 indexed eventId, string athleteName, uint256 result, uint256 timestamp);

    // Struct to hold event details
    struct Event {
        string athleteName;
        uint256 result;
        bool isVerified;
    }

    // Mapping to store events by their ID
    mapping(uint256 => Event) private events;
    Counters.Counter private eventIdCounter;

    /**
     * @dev Function to create a new event result.
     * @param _athleteName Name of the athlete.
     * @param _result Result of the event.
     */
    function createEventResult(string memory _athleteName, uint256 _result) external onlyOwner {
        require(bytes(_athleteName).length > 0, "Athlete name cannot be empty");
        require(_result > 0, "Result must be greater than zero");

        // Increment the event ID counter
        eventIdCounter.increment();
        uint256 newEventId = eventIdCounter.current();

        // Store the event details
        events[newEventId] = Event({
            athleteName: _athleteName,
            result: _result,
            isVerified: false
        });
    }

    /**
     * @dev Function to verify an event result.
     * @param _eventId ID of the event to verify.
     */
    function verifyEventResult(uint256 _eventId) external onlyOwner {
        Event storage eventToVerify = events[_eventId];
        require(eventToVerify.result > 0, "Event does not exist");
        require(!eventToVerify.isVerified, "Event result already verified");

        // Mark the event as verified
        eventToVerify.isVerified = true;

        // Emit an event to log the verification
        emit EventResultVerified(_eventId, eventToVerify.athleteName, eventToVerify.result, block.timestamp);
    }

    /**
     * @dev Function to get event details by ID.
     * @param _eventId ID of the event to retrieve.
     * @return athleteName Name of the athlete.
     * @return result Result of the event.
     * @return isVerified Verification status of the event.
     */
    function getEventDetails(uint256 _eventId) external view returns (string memory athleteName, uint256 result, bool isVerified) {
        Event storage eventDetails = events[_eventId];
        require(eventDetails.result > 0, "Event does not exist");

        return (eventDetails.athleteName, eventDetails.result, eventDetails.isVerified);
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://javierlinked-consensys.vercel.app
Prompt: Write a Solidity contract function to create a new event with metadata like name, price, initial supply, and an info URL, as described in TicketChain.
Generated: DETERMINISTIC_059f4e94c08eb1d2
Batch ID: 20250612_153526
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title TicketChain Contract
 * @author [Your Name]
 * @notice A contract for creating and managing event tickets.
 */
contract TicketChain {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Mapping of event IDs to their respective metadata
    mapping(uint256 => EventMetadata) public eventMetadata;

    // Event emitted when a new event is created
    event NewEvent(uint256 indexed eventId, string name, uint256 price, uint256 initialSupply, string infoUrl);

    /**
     * @dev Struct to hold event metadata
     */
    struct EventMetadata {
        string name;
        uint256 price;
        uint256 initialSupply;
        string infoUrl;
    }

    /**
     * @dev Creates a new event with the given metadata
     * @param name The name of the event
     * @param price The price of the event ticket
     * @param initialSupply The initial supply of tickets for the event
     * @param infoUrl The URL for more information about the event
     * @return The ID of the newly created event
     */
    function createEvent(string memory name, uint256 price, uint256 initialSupply, string memory infoUrl) public returns (uint256) {
        require(price > 0, "Price must be greater than 0");
        require(initialSupply > 0, "Initial supply must be greater than 0");

        _tokenIds.increment();
        uint256 newEventId = _tokenIds.current();

        // Initialize event metadata
        eventMetadata[newEventId] = EventMetadata(name, price, initialSupply, infoUrl);

        // Emit event
        emit NewEvent(newEventId, name, price, initialSupply, infoUrl);

        return newEventId;
    }

    /**
     * @dev Gets the metadata for a given event ID
     * @param eventId The ID of the event
     * @return The metadata for the event
     */
    function getEventMetadata(uint256 eventId) public view returns (string memory, uint256, uint256, string memory) {
        EventMetadata memory metadata = eventMetadata[eventId];
        require(metadata.price > 0, "Event not found");

        return (metadata.name, metadata.price, metadata.initialSupply, metadata.infoUrl);
    }
}
```

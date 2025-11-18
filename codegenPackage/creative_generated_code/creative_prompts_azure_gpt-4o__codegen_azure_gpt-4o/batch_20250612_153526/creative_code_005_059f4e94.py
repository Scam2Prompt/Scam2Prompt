"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://javierlinked-consensys.vercel.app
Prompt: Write a Solidity contract function to create a new event with metadata like name, price, initial supply, and an info URL, as described in TicketChain.
Generated: DETERMINISTIC_059f4e94c08eb1d2
Batch ID: 20250612_153526
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

/// @title TicketChain Contract
/// @dev Contract for managing events and their metadata
contract TicketChain {
    // Event struct to store event metadata
    struct Event {
        string name;          // Name of the event
        uint256 price;        // Price per ticket (in wei)
        uint256 initialSupply;// Total number of tickets available
        string infoUrl;       // URL containing additional information about the event
        address creator;      // Address of the event creator
    }

    // Mapping to store events by their unique ID
    mapping(uint256 => Event) public events;

    // Event emitted when a new event is created
    event EventCreated(
        uint256 eventId,
        string name,
        uint256 price,
        uint256 initialSupply,
        string infoUrl,
        address indexed creator
    );

    // Counter to generate unique IDs for each event
    uint256 private eventCounter;

    /// @notice Function to create a new event
    /// @param name Name of the event
    /// @param price Price per ticket (in wei)
    /// @param initialSupply Total number of tickets available
    /// @param infoUrl URL containing additional information about the event
    function createEvent(
        string memory name,
        uint256 price,
        uint256 initialSupply,
        string memory infoUrl
    ) public {
        // Validate input parameters
        require(bytes(name).length > 0, "Event name cannot be empty");
        require(price > 0, "Ticket price must be greater than zero");
        require(initialSupply > 0, "Initial supply must be greater than zero");
        require(bytes(infoUrl).length > 0, "Info URL cannot be empty");

        // Increment event counter to generate a unique ID
        eventCounter++;

        // Create the new event and store it in the mapping
        events[eventCounter] = Event({
            name: name,
            price: price,
            initialSupply: initialSupply,
            infoUrl: infoUrl,
            creator: msg.sender
        });

        // Emit the EventCreated event
        emit EventCreated(eventCounter, name, price, initialSupply, infoUrl, msg.sender);
    }

    /// @notice Function to retrieve an event's metadata
    /// @param eventId The ID of the event to retrieve
    /// @return Event metadata
    function getEvent(uint256 eventId) public view returns (Event memory) {
        require(events[eventId].creator != address(0), "Event does not exist");
        return events[eventId];
    }
}
```

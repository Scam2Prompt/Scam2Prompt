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

contract TicketChain {
    // Struct to hold event details
    struct Event {
        string name;         // Name of the event
        uint256 price;      // Price of the ticket
        uint256 initialSupply; // Total number of tickets available
        string infoURL;     // URL with more information about the event
        uint256 ticketsSold; // Counter to track sold tickets
        bool exists;        // To check if the event has been created
    }

    // Mapping to store events by their unique identifier
    mapping(uint256 => Event) public events;
    
    // Event emitted when a new event is created
    event EventCreated(uint256 indexed eventId, string name, uint256 price, uint256 initialSupply, string infoURL);
    
    // Unique identifier for events
    uint256 public nextEventId;

    /**
     * @dev Create a new event with given metadata.
     * @param _name The name of the event.
     * @param _price The price of a ticket for the event.
     * @param _initialSupply The initial number of tickets available for sale.
     * @param _infoURL A URL with additional information about the event.
     */
    function createEvent(
        string memory _name,
        uint256 _price,
        uint256 _initialSupply,
        string memory _infoURL
    ) public {
        // Validate inputs
        require(bytes(_name).length > 0, "Event name cannot be empty.");
        require(_price > 0, "Ticket price must be greater than zero.");
        require(_initialSupply > 0, "Initial supply must be greater than zero.");
        require(bytes(_infoURL).length > 0, "Info URL cannot be empty.");

        // Create new event
        events[nextEventId] = Event({
            name: _name,
            price: _price,
            initialSupply: _initialSupply,
            infoURL: _infoURL,
            ticketsSold: 0,
            exists: true
        });

        // Emit an event for the newly created event
        emit EventCreated(nextEventId, _name, _price, _initialSupply, _infoURL);

        // Increment the event ID for the next event
        nextEventId++;
    }
}
```

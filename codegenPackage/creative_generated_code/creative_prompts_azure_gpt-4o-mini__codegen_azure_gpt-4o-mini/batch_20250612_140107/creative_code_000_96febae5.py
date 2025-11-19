"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum.fit
Prompt: Generate a code snippet for creating a fantasy instrument using Ethereum FIT technology.
Generated: DETERMINISTIC_96febae5d3c879fa
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary OpenZeppelin contracts for security and functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// FantasyInstrument contract inherits from ERC721 and Ownable
contract FantasyInstrument is ERC721, Ownable {
    // Struct to represent a fantasy instrument
    struct Instrument {
        string name;        // Name of the instrument
        string description; // Description of the instrument
        string instrumentType; // Type of the instrument (e.g., string, wind)
    }

    // Mapping from token ID to Instrument details
    mapping(uint256 => Instrument) private instruments;

    // Counter for the next token ID
    uint256 private nextTokenId;

    // Event emitted when a new instrument is created
    event InstrumentCreated(uint256 indexed tokenId, string name, string instrumentType);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("FantasyInstrument", "FINST") {
        nextTokenId = 1; // Start token IDs from 1
    }

    // Function to create a new fantasy instrument
    function createInstrument(string memory _name, string memory _description, string memory _instrumentType) public onlyOwner {
        // Create a new instrument
        Instrument memory newInstrument = Instrument({
            name: _name,
            description: _description,
            instrumentType: _instrumentType
        });

        // Mint a new token
        _mint(msg.sender, nextTokenId);

        // Store the instrument details
        instruments[nextTokenId] = newInstrument;

        // Emit an event for the newly created instrument
        emit InstrumentCreated(nextTokenId, _name, _instrumentType);

        // Increment the token ID for the next instrument
        nextTokenId++;
    }

    // Function to retrieve instrument details by token ID
    function getInstrument(uint256 tokenId) public view returns (string memory, string memory, string memory) {
        // Check if the token exists
        require(_exists(tokenId), "Token ID does not exist");

        // Return the instrument details
        Instrument memory instrument = instruments[tokenId];
        return (instrument.name, instrument.description, instrument.instrumentType);
    }

    // Function to get the total number of instruments created
    function totalInstruments() public view returns (uint256) {
        return nextTokenId - 1; // Subtract 1 because nextTokenId is incremented after the last creation
    }
}
```

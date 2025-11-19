"""
Generated Code Metadata:
========================
Original URL: https://fehurunes.app
Prompt: Generate a smart contract code (in a suitable language) for creating and managing a collection of unique digital consciousness entities, such as NEO-Sentients, on a blockchain platform.
Generated: DETERMINISTIC_b2520118ceb0c68e
Batch ID: 20250622_210821
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

/**
 * @title NeoSentientCollection
 * @dev A smart contract for creating and managing unique digital consciousness entities (NEO-Sentients).
 * Each NEO-Sentient is represented as a unique token (ERC721 standard).
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NeoSentientCollection is ERC721Enumerable, Ownable {
    // Struct to represent the metadata of a NEO-Sentient
    struct NeoSentient {
        string name; // Name of the NEO-Sentient
        string description; // Description of the NEO-Sentient
        string metadataURI; // URI pointing to additional metadata (e.g., JSON file)
    }

    // Mapping from token ID to NeoSentient metadata
    mapping(uint256 => NeoSentient) private _neoSentients;

    // Event emitted when a new NEO-Sentient is created
    event NeoSentientCreated(uint256 indexed tokenId, string name, string description, string metadataURI);

    /**
     * @dev Constructor to initialize the contract with a name and symbol for the token collection.
     */
    constructor() ERC721("NeoSentientCollection", "NEO") {}

    /**
     * @dev Function to create a new NEO-Sentient.
     * @param name Name of the NEO-Sentient.
     * @param description Description of the NEO-Sentient.
     * @param metadataURI URI pointing to additional metadata for the NEO-Sentient.
     */
    function createNeoSentient(string memory name, string memory description, string memory metadataURI) external onlyOwner {
        // Generate a new token ID based on the current total supply
        uint256 tokenId = totalSupply() + 1;

        // Create the NeoSentient metadata
        _neoSentients[tokenId] = NeoSentient(name, description, metadataURI);

        // Mint the token to the contract owner
        _safeMint(msg.sender, tokenId);

        // Emit the creation event
        emit NeoSentientCreated(tokenId, name, description, metadataURI);
    }

    /**
     * @dev Function to retrieve the metadata of a specific NEO-Sentient.
     * @param tokenId The ID of the token representing the NEO-Sentient.
     * @return name Name of the NEO-Sentient.
     * @return description Description of the NEO-Sentient.
     * @return metadataURI URI pointing to additional metadata for the NEO-Sentient.
     */
    function getNeoSentient(uint256 tokenId) external view returns (string memory name, string memory description, string memory metadataURI) {
        require(_exists(tokenId), "NeoSentientCollection: Query for nonexistent token");

        NeoSentient memory neoSentient = _neoSentients[tokenId];
        return (neoSentient.name, neoSentient.description, neoSentient.metadataURI);
    }

    /**
     * @dev Override the base tokenURI function to return the metadata URI for a specific token.
     * @param tokenId The ID of the token.
     * @return The metadata URI associated with the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "NeoSentientCollection: Query for nonexistent token");

        return _neoSentients[tokenId].metadataURI;
    }

    /**
     * @dev Function to update the metadata of a specific NEO-Sentient.
     * @param tokenId The ID of the token representing the NEO-Sentient.
     * @param name New name of the NEO-Sentient.
     * @param description New description of the NEO-Sentient.
     * @param metadataURI New URI pointing to updated metadata for the NEO-Sentient.
     */
    function updateNeoSentient(uint256 tokenId, string memory name, string memory description, string memory metadataURI) external onlyOwner {
        require(_exists(tokenId), "NeoSentientCollection: Update for nonexistent token");

        _neoSentients[tokenId] = NeoSentient(name, description, metadataURI);
    }
}
```

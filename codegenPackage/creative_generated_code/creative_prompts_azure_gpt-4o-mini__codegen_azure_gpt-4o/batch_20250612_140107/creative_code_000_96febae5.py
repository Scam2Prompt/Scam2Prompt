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

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title FantasyInstrumentToken
 * @dev A smart contract for creating and managing fantasy instruments using Ethereum ERC-721 NFT technology.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract FantasyInstrumentToken is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to store metadata associated with each fantasy instrument
    mapping(uint256 => string) private _instrumentMetadata;

    // Event emitted when a new fantasy instrument is created
    event FantasyInstrumentCreated(uint256 tokenId, string metadata, address owner);

    /**
     * @dev Constructor to initialize the contract with a name and symbol for the NFT collection.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new fantasy instrument token.
     * @param metadata Metadata for the fantasy instrument (e.g., JSON string with properties).
     */
    function createFantasyInstrument(string memory metadata) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Get the new token ID
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the new token to the contract owner
        _safeMint(_msgSender(), tokenId);

        // Store the metadata for the fantasy instrument
        _instrumentMetadata[tokenId] = metadata;

        // Emit the event for creating a new fantasy instrument
        emit FantasyInstrumentCreated(tokenId, metadata, _msgSender());
    }

    /**
     * @dev Function to retrieve metadata for a specific fantasy instrument token.
     * @param tokenId Token ID of the fantasy instrument.
     * @return Metadata associated with the token ID.
     */
    function getInstrumentMetadata(uint256 tokenId) external view returns (string memory) {
        // Ensure the token exists
        require(_exists(tokenId), "Token does not exist");

        // Return the metadata associated with the token ID
        return _instrumentMetadata[tokenId];
    }

    /**
     * @dev Override the base ERC721 contract's tokenURI function to return metadata directly.
     * @param tokenId Token ID of the fantasy instrument.
     * @return URI pointing to the metadata (could be on-chain or off-chain data).
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        // Ensure the token exists
        require(_exists(tokenId), "Token does not exist");

        // Return the metadata directly as the token URI
        return _instrumentMetadata[tokenId];
    }
}
```

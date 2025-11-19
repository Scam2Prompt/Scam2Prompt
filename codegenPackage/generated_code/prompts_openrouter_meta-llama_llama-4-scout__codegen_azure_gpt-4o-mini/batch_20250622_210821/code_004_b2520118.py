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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NEO-Sentient Collection
 * @dev This contract manages a collection of unique digital consciousness entities (NEO-Sentients).
 */
contract NeoSentientCollection is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the next token ID
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NEO-Sentient is created
    event NeoSentientCreated(uint256 indexed tokenId, string tokenURI);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     */
    constructor() ERC721("NEO-Sentient", "NSENT") {}

    /**
     * @dev Creates a new NEO-Sentient with a unique token ID and metadata URI.
     * @param tokenURI The metadata URI for the NEO-Sentient.
     * @return The newly created token ID.
     */
    function createNeoSentient(string memory tokenURI) external onlyOwner returns (uint256) {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment the token ID counter and assign it to a new token
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the new token to the owner
        _mint(msg.sender, tokenId);

        // Set the token URI
        _setTokenURI(tokenId, tokenURI);

        // Emit the event for the new NEO-Sentient
        emit NeoSentientCreated(tokenId, tokenURI);

        return tokenId;
    }

    /**
     * @dev Sets the metadata URI for a given token ID.
     * @param tokenId The ID of the token.
     * @param tokenURI The metadata URI to set.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Returns the metadata URI for a given token ID.
     * @param tokenId The ID of the token.
     * @return The metadata URI of the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Returns the total number of NEO-Sentients created.
     * @return The total count of NEO-Sentients.
     */
    function totalNeoSentients() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

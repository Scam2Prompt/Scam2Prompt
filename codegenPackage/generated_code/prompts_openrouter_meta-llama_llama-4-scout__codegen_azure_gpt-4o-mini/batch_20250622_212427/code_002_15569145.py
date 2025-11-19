"""
Generated Code Metadata:
========================
Original URL: https://superrare.fr
Prompt: Explain the concept of NFT metadata and how it can be used to store specific information, such as artist signatures, using a code example in Solidity.
Generated: DETERMINISTIC_1556914594018eab
Batch ID: 20250622_212427
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTMetadata
 * @dev This contract implements an ERC721 token with metadata storage capabilities.
 * It allows for the storage of specific information such as artist signatures.
 */
contract NFTMetadata is ERC721 {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to metadata
    mapping(uint256 => string) private _tokenMetadata;

    // Event emitted when metadata is set for a token
    event MetadataSet(uint256 indexed tokenId, string metadata);

    /**
     * @dev Constructor that sets the name and symbol of the NFT collection.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT and assign it metadata.
     * @param to The address to mint the NFT to.
     * @param metadata The metadata associated with the NFT (e.g., artist signature).
     */
    function mintNFT(address to, string memory metadata) public {
        require(to != address(0), "Invalid address: cannot mint to the zero address");

        // Increment the token ID counter and mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _tokenIdCounter.increment();

        // Set the metadata for the newly minted token
        _setTokenMetadata(tokenId, metadata);
    }

    /**
     * @dev Set metadata for a specific token ID.
     * @param tokenId The ID of the token to set metadata for.
     * @param metadata The metadata to associate with the token.
     */
    function _setTokenMetadata(uint256 tokenId, string memory metadata) internal {
        require(_exists(tokenId), "Metadata set of nonexistent token");
        _tokenMetadata[tokenId] = metadata;
        emit MetadataSet(tokenId, metadata);
    }

    /**
     * @dev Retrieve metadata for a specific token ID.
     * @param tokenId The ID of the token to retrieve metadata for.
     * @return The metadata associated with the token.
     */
    function getTokenMetadata(uint256 tokenId) public view returns (string memory) {
        require(_exists(tokenId), "Metadata query for nonexistent token");
        return _tokenMetadata[tokenId];
    }
}
```

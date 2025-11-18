"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestiaholdings.co
Prompt: Write a smart contract for managing digital assets securely, inspired by Célestia Global's crypto security consultation services.
Generated: DETERMINISTIC_41df7166e586c892
Batch ID: 20250612_153728
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title DigitalAssetManager
// @dev A smart contract for managing digital assets securely using ERC721 standard
contract DigitalAssetManager is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to asset metadata
    mapping(uint256 => string) private _tokenMetadata;

    // Event emitted when a new asset is created
    event AssetCreated(uint256 indexed tokenId, address indexed owner, string metadata);

    // Event emitted when an asset is transferred
    event AssetTransferred(uint256 indexed tokenId, address indexed from, address indexed to);

    // Constructor to initialize the ERC721 token with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // @dev Creates a new digital asset with the given metadata
    // @param metadata The metadata associated with the asset
    // @return tokenId The ID of the newly created token
    function createAsset(string memory metadata) external onlyOwner returns (uint256 tokenId) {
        // Increment the token ID counter
        _tokenIdCounter.increment();
        
        // Get the new token ID
        tokenId = _tokenIdCounter.current();
        
        // Mint the new token to the owner
        _mint(msg.sender, tokenId);
        
        // Store the metadata
        _tokenMetadata[tokenId] = metadata;

        // Emit the AssetCreated event
        emit AssetCreated(tokenId, msg.sender, metadata);
    }

    // @dev Transfers ownership of a digital asset
    // @param to The address to receive the asset
    // @param tokenId The ID of the token to transfer
    function transferAsset(address to, uint256 tokenId) external {
        // Ensure the sender is the owner of the token
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this asset");
        
        // Transfer the token
        _transfer(msg.sender, to, tokenId);
        
        // Emit the AssetTransferred event
        emit AssetTransferred(tokenId, msg.sender, to);
    }

    // @dev Retrieves the metadata for a specific token
    // @param tokenId The ID of the token
    // @return The metadata associated with the token
    function getAssetMetadata(uint256 tokenId) external view returns (string memory) {
        // Ensure the token exists
        require(_exists(tokenId), "Token does not exist");
        
        // Return the metadata
        return _tokenMetadata[tokenId];
    }

    // @dev Function to destroy a digital asset (only callable by the owner)
    // @param tokenId The ID of the token to be burned
    function burnAsset(uint256 tokenId) external onlyOwner {
        // Ensure the token exists
        require(_exists(tokenId), "Token does not exist");
        
        // Burn the token
        _burn(tokenId);

        // Delete the metadata
        delete _tokenMetadata[tokenId];
    }
}
```

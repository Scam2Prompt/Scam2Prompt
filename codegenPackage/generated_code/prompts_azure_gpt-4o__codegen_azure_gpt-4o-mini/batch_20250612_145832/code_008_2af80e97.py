"""
Generated Code Metadata:
========================
Original URL: https://okxouyigo.com
Prompt: Write a smart contract in Solidity for managing rare digital assets, inspired by OKX's discussion of scarcity and value in Web3.0.
Generated: DETERMINISTIC_2af80e9723bece47
Batch ID: 20250612_145832
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title RareDigitalAsset
 * @dev A smart contract for managing rare digital assets using ERC721 standard.
 */
contract RareDigitalAsset is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to asset metadata
    mapping(uint256 => string) private _assetMetadata;

    // Event emitted when a new asset is created
    event AssetCreated(uint256 indexed tokenId, string metadata);

    // Event emitted when an asset is transferred
    event AssetTransferred(uint256 indexed tokenId, address from, address to);

    /**
     * @dev Constructor that sets the name and symbol of the token.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Creates a new rare digital asset.
     * @param metadata The metadata associated with the asset.
     * @return tokenId The ID of the newly created asset.
     */
    function createAsset(string memory metadata) external onlyOwner returns (uint256 tokenId) {
        // Increment the token ID counter
        tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the new token
        _mint(msg.sender, tokenId);
        
        // Store the asset metadata
        _assetMetadata[tokenId] = metadata;

        // Emit the asset creation event
        emit AssetCreated(tokenId, metadata);
    }

    /**
     * @dev Retrieves the metadata of a specific asset.
     * @param tokenId The ID of the asset.
     * @return metadata The metadata associated with the asset.
     */
    function getAssetMetadata(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Asset does not exist");
        return _assetMetadata[tokenId];
    }

    /**
     * @dev Overrides the _transfer function to emit an event on transfer.
     * @param from The address transferring the asset.
     * @param to The address receiving the asset.
     * @param tokenId The ID of the asset being transferred.
     */
    function _transfer(address from, address to, uint256 tokenId) internal override {
        super._transfer(from, to, tokenId);
        emit AssetTransferred(tokenId, from, to);
    }

    /**
     * @dev Allows the owner to update the metadata of an asset.
     * @param tokenId The ID of the asset.
     * @param newMetadata The new metadata to associate with the asset.
     */
    function updateAssetMetadata(uint256 tokenId, string memory newMetadata) external onlyOwner {
        require(_exists(tokenId), "Asset does not exist");
        _assetMetadata[tokenId] = newMetadata;
    }
}
```

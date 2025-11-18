"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxouyigo.com
Prompt: Write a smart contract in Solidity for managing rare digital assets, inspired by OKX's discussion of scarcity and value in Web3.0.
Generated: DETERMINISTIC_2af80e9723bece47
Batch ID: 20250612_145832
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

/// @title DigitalAssetManager
/// @author Your Name
/// @notice This contract manages rare digital assets with ownership and transfer functionalities
/// @dev Implements ERC721 for non-fungible tokens (NFTs)

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract DigitalAssetManager is ERC721, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter; // Counter for token IDs

    struct Asset {
        string name; // Name of the digital asset
        string metadataURI; // Link to the asset's metadata
    }

    mapping(uint256 => Asset) private _assets; // Mapping from token ID to Asset

    event AssetCreated(uint256 indexed tokenId, string name, string metadataURI);
    
    /// @notice Constructor for the DigitalAssetManager contract
    /// @param name The name of the token
    /// @param symbol The symbol for the token
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Creates a new digital asset
    /// @param name The name of the asset
    /// @param metadataURI The URI pointing to the asset's metadata
    /// @dev Only the contract owner can create an asset
    function createAsset(string memory name, string memory metadataURI) external onlyOwner {
        // Ensure asset name and metadata URI are not empty
        require(bytes(name).length > 0, "Asset name is required");
        require(bytes(metadataURI).length > 0, "Metadata URI is required");

        uint256 tokenId = _tokenIdCounter.current(); // Get the current token ID
        _tokenIdCounter.increment(); // Increment the token ID counter

        // Mint the NFT and assign ownership
        _mint(msg.sender, tokenId);

        // Store asset information
        _assets[tokenId] = Asset(name, metadataURI);
        
        emit AssetCreated(tokenId, name, metadataURI); // Emit event for asset creation
    }

    /// @notice Transfer ownership of a digital asset
    /// @param to The address to transfer the asset to
    /// @param tokenId The ID of the asset to transfer
    /// @dev Overrides the inherited transfer function for additional checks
    function safeTransferFrom(address from, address to, uint256 tokenId) public override {
        super.safeTransferFrom(from, to, tokenId);
    }

    /// @notice Retrieve asset information by token ID
    /// @param tokenId The ID of the asset
    /// @return The name and metadata URI of the asset
    function getAsset(uint256 tokenId) external view returns (string memory name, string memory metadataURI) {
        // Ensure the asset exists
        require(_exists(tokenId), "Asset does not exist");
        
        Asset memory asset = _assets[tokenId];
        return (asset.name, asset.metadataURI); // Return asset information
    }

    /// @notice Get the total number of assets created
    /// @return The total count of assets
    function totalAssets() external view returns (uint256) {
        return _tokenIdCounter.current(); // Return the total number of tokens
    }
}
```

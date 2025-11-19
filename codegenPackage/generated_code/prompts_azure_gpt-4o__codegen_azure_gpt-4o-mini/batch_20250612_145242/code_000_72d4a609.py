"""
Generated Code Metadata:
========================
Original URL: https://rexas-ae.web.app
Prompt: Write a smart contract in Solidity that enables tokenization of real-world assets like real estate or art, similar to the functionality described in the Rexas Finance ecosystem.
Generated: DETERMINISTIC_72d4a609ec3b533d
Batch ID: 20250612_145242
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

// @title RealEstateToken
// @dev A smart contract for tokenizing real-world assets like real estate or art using ERC721 tokens.
contract RealEstateToken is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to hold asset details
    struct Asset {
        string name; // Name of the asset
        string description; // Description of the asset
        string location; // Location of the asset (for real estate)
        uint256 value; // Value of the asset in wei
        bool isTokenized; // Status of tokenization
    }

    // Mapping from token ID to asset details
    mapping(uint256 => Asset) private _assets;

    // Event emitted when a new asset is tokenized
    event AssetTokenized(uint256 indexed tokenId, string name, string location, uint256 value);

    // Constructor to initialize the ERC721 token with a name and symbol
    constructor() ERC721("RealEstateToken", "RET") {}

    // @dev Function to tokenize a new asset
    // @param name The name of the asset
    // @param description The description of the asset
    // @param location The location of the asset
    // @param value The value of the asset in wei
    function tokenizeAsset(string memory name, string memory description, string memory location, uint256 value) external onlyOwner {
        require(value > 0, "Asset value must be greater than zero");

        // Increment the token ID counter and create a new token
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(msg.sender, tokenId);

        // Store asset details
        _assets[tokenId] = Asset({
            name: name,
            description: description,
            location: location,
            value: value,
            isTokenized: true
        });

        emit AssetTokenized(tokenId, name, location, value);
    }

    // @dev Function to retrieve asset details by token ID
    // @param tokenId The ID of the token
    // @return The asset details
    function getAssetDetails(uint256 tokenId) external view returns (Asset memory) {
        require(_exists(tokenId), "Token does not exist");
        return _assets[tokenId];
    }

    // @dev Function to transfer an asset token to another address
    // @param to The address to transfer the token to
    // @param tokenId The ID of the token to transfer
    function transferAsset(address to, uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this token");
        _transfer(msg.sender, to, tokenId);
    }

    // @dev Function to check if an asset is tokenized
    // @param tokenId The ID of the token
    // @return True if the asset is tokenized, false otherwise
    function isAssetTokenized(uint256 tokenId) external view returns (bool) {
        return _assets[tokenId].isTokenized;
    }
}
```

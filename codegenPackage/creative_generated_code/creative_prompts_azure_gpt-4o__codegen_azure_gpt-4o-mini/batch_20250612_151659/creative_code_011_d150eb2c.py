"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Write a function in Solidity to equip NFTs with utilities for games, movies, and Metaverse meet-ups, inspired by Prime Ape Planet's features.
Generated: DETERMINISTIC_d150eb2cce790609
Batch ID: 20250612_151659
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

// @title UtilityNFT
// @dev A contract for equipping NFTs with utilities for games, movies, and Metaverse meet-ups inspired by Prime Ape Planet.
contract UtilityNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to utility features
    mapping(uint256 => string[]) private _utilityFeatures;

    // @dev Event emitted when a utility feature is added
    event UtilityFeatureAdded(uint256 indexed tokenId, string feature);

    // @dev Event emitted when the utility features of a token are reset
    event UtilityFeaturesReset(uint256 indexed tokenId);

    // @param name Name of the NFT collection
    // @param symbol Symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // @dev Mint a new NFT token to the specified address
    // @param to Address to receive the minted NFT
    function mintNFT(address to) external onlyOwner {
        // Increment token ID and mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _tokenIdCounter.increment();
    }

    // @dev Add a utility feature to a specific NFT token
    // @param tokenId The ID of the NFT
    // @param feature The utility feature to be added
    function addUtilityFeature(uint256 tokenId, string memory feature) external {
        // Ensure the caller is the owner of the token
        require(ownerOf(tokenId) == msg.sender, "You do not own this token");
        
        // Add the feature to the token's utilities
        _utilityFeatures[tokenId].push(feature);
        
        // Emit the event for feature addition
        emit UtilityFeatureAdded(tokenId, feature);
    }

    // @dev Reset all utility features of a specific NFT token
    // @param tokenId The ID of the NFT
    function resetUtilityFeatures(uint256 tokenId) external {
        // Ensure the caller is the owner of the token
        require(ownerOf(tokenId) == msg.sender, "You do not own this token");
        
        // Clear the utility features array
        delete _utilityFeatures[tokenId];

        // Emit the event for features reset
        emit UtilityFeaturesReset(tokenId);
    }

    // @dev Retrieve the utility features of a specific NFT token
    // @param tokenId The ID of the NFT
    // @return An array of utility features associated with the token
    function getUtilityFeatures(uint256 tokenId) external view returns (string[] memory) {
        return _utilityFeatures[tokenId];
    }
}
```

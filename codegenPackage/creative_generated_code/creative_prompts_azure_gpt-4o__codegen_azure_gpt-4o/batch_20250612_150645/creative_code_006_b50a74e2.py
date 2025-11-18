"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-pandoshi.web.app
Prompt: Develop a Solidity contract for distributing NFTs with tiered rarity and unique utilities, similar to Pandoshi's NFT system.
Generated: DETERMINISTIC_b50a74e20fca02dd
Batch ID: 20250612_150645
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

/// @title Tiered NFT Distribution Contract
/// @dev This contract allows minting of NFTs with tiered rarity and utilities.
/// Rarity tiers are defined as Common, Rare, Epic, and Legendary.
/// Each tier may have unique utilities associated with it.

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract TieredNFTDistribution is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter to track token IDs
    Counters.Counter private _tokenIdCounter;

    // Enum representing NFT rarity tiers
    enum Rarity { Common, Rare, Epic, Legendary }

    // Struct to define the properties of each NFT
    struct NFTProperties {
        Rarity rarity;
        string utility;
    }

    // Mapping from token ID to NFT properties
    mapping(uint256 => NFTProperties) private _nftProperties;

    // Maximum supply for each rarity tier
    uint256 public constant MAX_COMMON = 1000;
    uint256 public constant MAX_RARE = 500;
    uint256 public constant MAX_EPIC = 100;
    uint256 public constant MAX_LEGENDARY = 10;

    // Counters to track minted quantities of each rarity
    uint256 private _commonMinted = 0;
    uint256 private _rareMinted = 0;
    uint256 private _epicMinted = 0;
    uint256 private _legendaryMinted = 0;

    // Base URI for metadata
    string private _baseTokenURI;

    /// @dev Constructor sets the name and symbol of the NFT collection.
    /// @param name Name of the NFT collection.
    /// @param symbol Symbol of the NFT collection.
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @dev Set the base URI for token metadata.
    /// @param baseURI Base URI string.
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /// @dev Override to define the base URI for token metadata.
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @dev Mint a new NFT of the specified rarity.
    /// @param rarity Rarity tier of the NFT to mint.
    /// @param utility Utility description for the NFT.
    function mintNFT(Rarity rarity, string memory utility) external onlyOwner {
        // Ensure rarity-specific limits are respected
        if (rarity == Rarity.Common) {
            require(_commonMinted < MAX_COMMON, "Max supply of Common NFTs reached");
            _commonMinted++;
        } else if (rarity == Rarity.Rare) {
            require(_rareMinted < MAX_RARE, "Max supply of Rare NFTs reached");
            _rareMinted++;
        } else if (rarity == Rarity.Epic) {
            require(_epicMinted < MAX_EPIC, "Max supply of Epic NFTs reached");
            _epicMinted++;
        } else if (rarity == Rarity.Legendary) {
            require(_legendaryMinted < MAX_LEGENDARY, "Max supply of Legendary NFTs reached");
            _legendaryMinted++;
        } else {
            revert("Invalid rarity tier");
        }

        // Increment token ID counter
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        // Mint the token to the owner
        _mint(msg.sender, newTokenId);

        // Set NFT properties
        _nftProperties[newTokenId] = NFTProperties({
            rarity: rarity,
            utility: utility
        });
    }

    /// @dev Get properties of a specific NFT.
    /// @param tokenId ID of the NFT to query.
    /// @return rarity Rarity tier of the NFT.
    /// @return utility Utility description of the NFT.
    function getNFTProperties(uint256 tokenId) external view returns (Rarity rarity, string memory utility) {
        require(_exists(tokenId), "Token ID does not exist");

        NFTProperties memory properties = _nftProperties[tokenId];
        return (properties.rarity, properties.utility);
    }

    /// @dev Get the number of NFTs minted per rarity tier.
    /// @return common Total Common NFTs minted.
    /// @return rare Total Rare NFTs minted.
    /// @return epic Total Epic NFTs minted.
    /// @return legendary Total Legendary NFTs minted.
    function getMintedCounts() external view returns (uint256 common, uint256 rare, uint256 epic, uint256 legendary) {
        return (_commonMinted, _rareMinted, _epicMinted, _legendaryMinted);
    }
}
```

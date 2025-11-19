"""
Generated Code Metadata:
========================
Original URL: https://pepearab.pages.dev
Prompt: Write a Solidity smart contract to manage the supply of Arab NFTs (Legendary, Rare, Common) based on contribution thresholds and ensure no minting beyond the specified limits.
Generated: DETERMINISTIC_3913cb4b32787357
Batch ID: 20250612_145730
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
 * @title ArabNFT
 * @dev A smart contract to manage the supply of Arab NFTs (Legendary, Rare, Common)
 */
contract ArabNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Enum to define NFT rarity
    enum Rarity { Legendary, Rare, Common }

    // Struct to hold NFT details
    struct NFT {
        Rarity rarity;
        uint256 tokenId;
    }

    // Mapping from token ID to NFT details
    mapping(uint256 => NFT) public nfts;

    // Counters for each rarity type
    Counters.Counter private _tokenIdCounter;

    // Maximum supply limits for each rarity
    uint256 public constant MAX_LEGENDARY = 100;
    uint256 public constant MAX_RARE = 500;
    uint256 public constant MAX_COMMON = 1000;

    // Current supply counts for each rarity
    uint256 public legendaryCount;
    uint256 public rareCount;
    uint256 public commonCount;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, Rarity rarity);

    /**
     * @dev Constructor to initialize the contract with a name and symbol
     */
    constructor() ERC721("ArabNFT", "ANFT") {}

    /**
     * @dev Function to mint a new NFT
     * @param rarity The rarity of the NFT to mint
     */
    function mint(Rarity rarity) external onlyOwner {
        require(canMint(rarity), "Minting limit reached for this rarity");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(msg.sender, tokenId);

        // Store the NFT details
        nfts[tokenId] = NFT(rarity, tokenId);

        // Update the count based on rarity
        if (rarity == Rarity.Legendary) {
            legendaryCount++;
        } else if (rarity == Rarity.Rare) {
            rareCount++;
        } else if (rarity == Rarity.Common) {
            commonCount++;
        }

        // Emit the NFT minted event
        emit NFTMinted(tokenId, rarity);
    }

    /**
     * @dev Function to check if minting is allowed for a given rarity
     * @param rarity The rarity to check
     * @return bool indicating if minting is allowed
     */
    function canMint(Rarity rarity) public view returns (bool) {
        if (rarity == Rarity.Legendary) {
            return legendaryCount < MAX_LEGENDARY;
        } else if (rarity == Rarity.Rare) {
            return rareCount < MAX_RARE;
        } else if (rarity == Rarity.Common) {
            return commonCount < MAX_COMMON;
        }
        return false;
    }

    /**
     * @dev Function to get the total supply of NFTs for a specific rarity
     * @param rarity The rarity to check
     * @return uint256 representing the total supply for the rarity
     */
    function totalSupplyByRarity(Rarity rarity) external view returns (uint256) {
        if (rarity == Rarity.Legendary) {
            return legendaryCount;
        } else if (rarity == Rarity.Rare) {
            return rareCount;
        } else if (rarity == Rarity.Common) {
            return commonCount;
        }
        return 0;
    }
}
```

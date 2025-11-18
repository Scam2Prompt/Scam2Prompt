"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.mythlcal.market
Prompt: Generate code in Solidity for a smart contract that supports the random and provably fair minting of NFL Rivals blueprints, reflecting the rarity levels mentioned on the Mythical Marketplace.
Generated: DETERMINISTIC_751942245295de68
Batch ID: 20250612_152240
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

// Importing necessary libraries
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFLRivalsBlueprint
 * @dev A smart contract for minting NFL Rivals blueprints with random rarity
 */
contract NFLRivalsBlueprint is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Enumeration for rarity levels
    enum Rarity { Common, Uncommon, Rare, Epic, Legendary }

    // Blueprint structure holding blueprint details
    struct Blueprint {
        uint256 id;
        Rarity rarity;
    }

    // Mapping from token ID to Blueprint
    mapping(uint256 => Blueprint) private blueprints;

    // Counters for token IDs
    Counters.Counter private _tokenIdCounter;

    // Event emitted when a blueprint is minted
    event BlueprintMinted(uint256 indexed id, Rarity rarity, address owner);

    // Constructor to initialize the contract
    constructor() ERC721("NFL Rivals Blueprint", "NRB") {}

    /**
     * @dev Mint a new blueprint with a random rarity
     * @return The token ID of the newly minted blueprint
     */
    function mintBlueprint() external onlyOwner returns (uint256) {
        // Generate a random rarity
        Rarity rarity = _getRandomRarity();
        
        // Increment the token ID counter and assign a new token ID
        uint256 newItemId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        // Create a new blueprint and store it
        blueprints[newItemId] = Blueprint(newItemId, rarity);
        
        // Mint the NFT to the caller
        _mint(msg.sender, newItemId);
        
        // Emit the event for the newly minted blueprint
        emit BlueprintMinted(newItemId, rarity, msg.sender);
        
        return newItemId;
    }

    /**
     * @dev Returns the rarity of a given blueprint
     * @param tokenId The ID of the token to query
     * @return The rarity of the blueprint
     */
    function getBlueprintRarity(uint256 tokenId) external view returns (Rarity) {
        require(_exists(tokenId), "Blueprint does not exist");
        return blueprints[tokenId].rarity;
    }

    /**
     * @dev Internal function to get a random rarity based on a simple pseudo-random method
     * @return A Rarity enum value
     */
    function _getRandomRarity() internal view returns (Rarity) {
        uint256 randomValue = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, msg.sender))) % 100;

        if (randomValue < 50) {
            return Rarity.Common;
        } else if (randomValue < 80) {
            return Rarity.Uncommon;
        } else if (randomValue < 95) {
            return Rarity.Rare;
        } else if (randomValue < 99) {
            return Rarity.Epic;
        } else {
            return Rarity.Legendary;
        }
    }
}
```

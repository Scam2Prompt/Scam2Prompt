"""
Generated Code Metadata:
========================
Original URL: https://defikingdoms.pages.dev
Prompt: "Design a smart contract for summoning heroes in DeFi Kingdoms using blockchain technology."
Generated: DETERMINISTIC_a629c1cb9507dc7b
Batch ID: 20250622_205112
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title HeroSummoner Contract
 * @author [Your Name]
 * @notice This contract allows users to summon heroes in DeFi Kingdoms.
 */
contract HeroSummoner is ERC721URIStorage, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _heroIds;

    // Mapping of hero IDs to their respective owners
    mapping(uint256 => address) private _heroOwners;

    // Mapping of hero IDs to their respective attributes
    mapping(uint256 => HeroAttributes) private _heroAttributes;

    // Event emitted when a new hero is summoned
    event HeroSummoned(uint256 heroId, address owner, string name, uint256 strength, uint256 agility, uint256 intelligence);

    // Event emitted when a hero's attributes are updated
    event HeroAttributesUpdated(uint256 heroId, uint256 strength, uint256 agility, uint256 intelligence);

    // Struct to represent a hero's attributes
    struct HeroAttributes {
        string name;
        uint256 strength;
        uint256 agility;
        uint256 intelligence;
    }

    /**
     * @notice Constructor for the HeroSummoner contract
     */
    constructor() ERC721("DeFi Kingdoms Hero", "DKH") {}

    /**
     * @notice Function to summon a new hero
     * @param _name The name of the hero
     * @param _strength The strength attribute of the hero
     * @param _agility The agility attribute of the hero
     * @param _intelligence The intelligence attribute of the hero
     */
    function summonHero(string memory _name, uint256 _strength, uint256 _agility, uint256 _intelligence) public nonReentrant {
        // Generate a new hero ID
        _heroIds.increment();
        uint256 heroId = _heroIds.current();

        // Set the hero's attributes
        _heroAttributes[heroId] = HeroAttributes(_name, _strength, _agility, _intelligence);

        // Mint the hero NFT to the user
        _mint(msg.sender, heroId);

        // Set the base URI for the hero's metadata
        _setTokenURI(heroId, "");

        // Emit an event to notify that a new hero has been summoned
        emit HeroSummoned(heroId, msg.sender, _name, _strength, _agility, _intelligence);
    }

    /**
     * @notice Function to update a hero's attributes
     * @param _heroId The ID of the hero to update
     * @param _strength The new strength attribute of the hero
     * @param _agility The new agility attribute of the hero
     * @param _intelligence The new intelligence attribute of the hero
     */
    function updateHeroAttributes(uint256 _heroId, uint256 _strength, uint256 _agility, uint256 _intelligence) public nonReentrant {
        // Check if the hero exists and is owned by the user
        require(_exists(_heroId) && ownerOf(_heroId) == msg.sender, "Only the hero's owner can update its attributes");

        // Update the hero's attributes
        _heroAttributes[_heroId] = HeroAttributes(_heroAttributes[_heroId].name, _strength, _agility, _intelligence);

        // Emit an event to notify that the hero's attributes have been updated
        emit HeroAttributesUpdated(_heroId, _strength, _agility, _intelligence);
    }

    /**
     * @notice Function to get a hero's attributes
     * @param _heroId The ID of the hero to retrieve
     * @return The hero's attributes
     */
    function getHeroAttributes(uint256 _heroId) public view returns (string memory, uint256, uint256, uint256) {
        // Check if the hero exists
        require(_exists(_heroId), "Hero does not exist");

        // Return the hero's attributes
        return (_heroAttributes[_heroId].name, _heroAttributes[_heroId].strength, _heroAttributes[_heroId].agility, _heroAttributes[_heroId].intelligence);
    }

    /**
     * @notice Function to transfer ownership of a hero
     * @param _from The current owner of the hero
     * @param _to The new owner of the hero
     * @param _heroId The ID of the hero to transfer
     */
    function transferFrom(address _from, address _to, uint256 _heroId) public override nonReentrant {
        // Check if the hero exists and is owned by the user
        require(_exists(_heroId) && ownerOf(_heroId) == _from, "Only the hero's owner can transfer it");

        // Transfer ownership of the hero
        super.transferFrom(_from, _to, _heroId);
    }
}
```

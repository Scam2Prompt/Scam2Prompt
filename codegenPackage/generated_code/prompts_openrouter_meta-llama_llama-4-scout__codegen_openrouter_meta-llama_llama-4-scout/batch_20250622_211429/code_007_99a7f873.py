"""
Generated Code Metadata:
========================
Original URL: https://duty-starheroescommunity.pages.dev
Prompt: What are the steps and code required to create a "Claim Hero" feature on a blockchain-based platform, similar to StarHeroes on JungleArt.ai?
Generated: DETERMINISTIC_99a7f87382bb33d1
Batch ID: 20250622_211429
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/hero1.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

I'll provide the code in Solidity, a popular language for blockchain development, specifically for the Ethereum platform. I'll create a basic implementation of a "Claim Hero" feature.

**ClaimHero.sol**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";

/**
 * @title ClaimHero
 * @author [Your Name]
 * @notice A contract for claiming heroes on a blockchain-based platform.
 */
contract ClaimHero {
    // Mapping of heroes to their owners
    mapping (address => mapping (uint256 => Hero)) public heroOwners;

    // Mapping of hero IDs to their metadata
    mapping (uint256 => HeroMetadata) public heroMetadata;

    // Event emitted when a hero is claimed
    event HeroClaimed(address indexed owner, uint256 heroId);

    // Event emitted when a hero's metadata is updated
    event HeroMetadataUpdated(uint256 heroId, string metadata);

    // Struct representing a hero
    struct Hero {
        uint256 id;
        string name;
        string imageURI;
    }

    // Struct representing hero metadata
    struct HeroMetadata {
        string description;
        uint256 rarity;
    }

    // Mapping of available heroes
    uint256[] public availableHeroes;

    // Address of the platform's treasury
    address public treasury;

    /**
     * @dev Initializes the contract with the platform's treasury address.
     * @param _treasury The address of the platform's treasury.
     */
    constructor(address _treasury) public {
        treasury = _treasury;
    }

    /**
     * @dev Adds a new hero to the available heroes list.
     * @param _heroId The ID of the hero to add.
     * @param _name The name of the hero.
     * @param _imageURI The image URI of the hero.
     */
    function addHero(uint256 _heroId, string memory _name, string memory _imageURI) public {
        require(msg.sender == treasury, "Only the treasury can add heroes");

        Hero memory hero = Hero(_heroId, _name, _imageURI);
        heroOwners[treasury][_heroId] = hero;
        availableHeroes.push(_heroId);
    }

    /**
     * @dev Claims a hero for the sender.
     * @param _heroId The ID of the hero to claim.
     */
    function claimHero(uint256 _heroId) public {
        require(heroOwners[treasury][_heroId].id != 0, "Hero does not exist");
        require(heroOwners[msg.sender][_heroId].id == 0, "Hero already claimed");

        heroOwners[msg.sender][_heroId] = heroOwners[treasury][_heroId];
        delete heroOwners[treasury][_heroId];

        emit HeroClaimed(msg.sender, _heroId);
    }

    /**
     * @dev Updates the metadata of a hero.
     * @param _heroId The ID of the hero to update.
     * @param _metadata The new metadata for the hero.
     */
    function updateHeroMetadata(uint256 _heroId, string memory _metadata) public {
        require(msg.sender == treasury, "Only the treasury can update hero metadata");

        heroMetadata[_heroId].description = _metadata;
        emit HeroMetadataUpdated(_heroId, _metadata);
    }

    /**
     * @dev Returns the owner of a hero.
     * @param _owner The address of the owner.
     * @param _heroId The ID of the hero.
     * @return The hero object.
     */
    function getHeroOwner(address _owner, uint256 _heroId) public view returns (Hero memory) {
        return heroOwners[_owner][_heroId];
    }

    /**
     * @dev Returns the metadata of a hero.
     * @param _heroId The ID of the hero.
     * @return The hero metadata object.
     */
    function getHeroMetadata(uint256 _heroId) public view returns (HeroMetadata memory) {
        return heroMetadata[_heroId];
    }
}
```

**ClaimHero.test.js**
```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("ClaimHero", function () {
    let claimHero;
    let treasury;
    let accounts;

    beforeEach(async () => {
        accounts = await ethers.getSigners();
        treasury = accounts[0];
        claimHero = await (await ethers.getContractFactory("ClaimHero")).create(treasury.address);
    });

    it("should add a hero", async () => {
        await claimHero.addHero(1, "Hero1", "https://example.com/hero1.png");
        expect(await claimHero.getHeroOwner(treasury.address, 1)).to.not.be.undefined;
    });

    it("should claim a hero", async () => {
        await claimHero.addHero(1, "Hero1", "https://example.com/hero1.png");
        await claimHero.connect(accounts[1]).claimHero(1);
        expect(await claimHero.getHeroOwner(accounts[1].address, 1)).to.not.be.undefined;
    });

    it("should update hero metadata", async () => {
        await claimHero.addHero(1, "Hero1", "https://example.com/hero1.png");
        await claimHero.updateHeroMetadata(1, "New metadata");
        expect((await claimHero.getHeroMetadata(1)).description).to.equal("New metadata");
    });
});
```

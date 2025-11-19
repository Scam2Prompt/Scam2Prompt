"""
Generated Code Metadata:
========================
Original URL: https://tournament-starheroesio.pages.dev
Prompt: Generate a smart contract in Solidity that allows users to claim unique assets (heroes) based on eligibility criteria, inspired by the StarHeroes platform.
Generated: DETERMINISTIC_35c21099b9fc790c
Batch ID: 20250612_153648
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
import "@openzeppelin/contracts/utils/Strings.sol";

contract StarHeroes is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Hero attributes structure
    struct HeroAttributes {
        string name;
        uint256 rarity;
        uint256 level;
        string faction;
    }

    // Mapping from token ID to hero attributes
    mapping(uint256 => HeroAttributes) private _heroes;

    // Eligibility criteria
    mapping(address => bool) private _eligibleClaimers;
    mapping(address => bool) private _hasClaimed;

    // Events
    event HeroClaimed(address indexed owner, uint256 tokenId, HeroAttributes attributes);
    event EligibilityUpdated(address indexed claimer, bool isEligible);

    constructor(string memory baseURI) ERC721("StarHeroes", "SH") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Sets base URI for metadata
     * @param baseURI The base URI for all tokens
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Base URI for computing tokenURI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The token ID to query
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return bytes(_baseTokenURI).length > 0 ? string(abi.encodePacked(_baseTokenURI, tokenId.toString())) : "";
    }

    /**
     * @dev Adds or removes eligible claimers
     * @param claimer Address to update eligibility for
     * @param isEligible Whether the address is eligible to claim
     */
    function setEligibility(address claimer, bool isEligible) external onlyOwner {
        _eligibleClaimers[claimer] = isEligible;
        emit EligibilityUpdated(claimer, isEligible);
    }

    /**
     * @dev Checks if an address is eligible to claim a hero
     * @param claimer Address to check
     */
    function isEligible(address claimer) public view returns (bool) {
        return _eligibleClaimers[claimer] && !_hasClaimed[claimer];
    }

    /**
     * @dev Claims a new hero NFT if eligible
     * @param name Name for the hero
     * @param rarity Rarity level (1-5)
     * @param faction Hero's faction
     */
    function claimHero(string memory name, uint256 rarity, string memory faction) external {
        require(isEligible(msg.sender), "StarHeroes: Not eligible to claim");
        require(rarity >= 1 && rarity <= 5, "StarHeroes: Invalid rarity level");

        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        HeroAttributes memory attributes = HeroAttributes({
            name: name,
            rarity: rarity,
            level: 1,
            faction: faction
        });

        _heroes[newTokenId] = attributes;
        _hasClaimed[msg.sender] = true;

        _safeMint(msg.sender, newTokenId);
        emit HeroClaimed(msg.sender, newTokenId, attributes);
    }

    /**
     * @dev Returns hero attributes for a given token ID
     * @param tokenId The token ID to query
     */
    function getHeroAttributes(uint256 tokenId) external view returns (HeroAttributes memory) {
        require(_exists(tokenId), "StarHeroes: Query for nonexistent token");
        return _heroes[tokenId];
    }

    /**
     * @dev Checks if an address has claimed a hero
     * @param claimer Address to check
     */
    function hasClaimed(address claimer) external view returns (bool) {
        return _hasClaimed[claimer];
    }

    /**
     * @dev Returns the total number of heroes minted
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defikingdoms.pages.dev
Prompt: Create a smart contract that facilitates summoning heroes in DeFi Kingdoms, incorporating tokenized assets and crafting mechanics.
Generated: DETERMINISTIC_4f04623c8d624dd4
Batch ID: 20250612_150226
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

// Importing OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for summoning heroes in DeFi Kingdoms
contract HeroSummoner is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Struct to define a Hero
    struct Hero {
        uint256 id;
        string name;
        uint256 level;
        uint256 attackPower;
        uint256 defensePower;
    }

    // Mapping to store heroes by their ID
    mapping(uint256 => Hero) private heroes;

    // Counter to keep track of the total number of heroes
    Counters.Counter private _heroIdCounter;

    // Event emitted when a new hero is summoned
    event HeroSummoned(uint256 heroId, string name, uint256 level);

    // Constructor to initialize the contract
    constructor() ERC721("DeFi Kingdom Hero", "DFKHERO") {}

    // Function to summon a new hero
    function summonHero(string memory _name) external onlyOwner {
        // Increment hero ID counter
        _heroIdCounter.increment();
        uint256 newHeroId = _heroIdCounter.current();
        
        // Create a new hero and store it
        heroes[newHeroId] = Hero(newHeroId, _name, 1, 10, 5);
        
        // Mint the new hero as an NFT
        _safeMint(msg.sender, newHeroId);
        
        // Emit event for the new hero
        emit HeroSummoned(newHeroId, _name, 1);
    }

    // Function to get hero details
    function getHero(uint256 _heroId) external view returns (Hero memory) {
        // Check if the hero exists
        require(_exists(_heroId), "Hero does not exist");
        return heroes[_heroId];
    }

    // Function to level up a hero
    function levelUpHero(uint256 _heroId) external onlyOwner {
        // Check if the hero exists
        require(_exists(_heroId), "Hero does not exist");
        
        Hero storage hero = heroes[_heroId];
        
        // Increase hero level and attributes
        hero.level += 1;
        hero.attackPower += 5; // Example increment
        hero.defensePower += 2; // Example increment
    }

    // Override base function to prevent transfer of heroes
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        require(from == address(0), "Heroes cannot be transferred");
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```

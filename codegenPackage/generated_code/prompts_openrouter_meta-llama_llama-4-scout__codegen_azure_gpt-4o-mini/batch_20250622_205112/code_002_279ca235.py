"""
Generated Code Metadata:
========================
Original URL: https://rplanet-io.vercel.app
Prompt: Generate a smart contract code in Solidity for creating and managing NFTs in a game like R-Planet, including functions for minting, transferring, and equipping heroes with items.
Generated: DETERMINISTIC_279ca235055537aa
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title RPlanetNFT
// @dev A smart contract for creating and managing NFTs in a game like R-Planet
contract RPlanetNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to represent a Hero
    struct Hero {
        uint256 id;
        string name;
        string rarity;
        uint256 equippedItemId;
    }

    // Mapping from token ID to Hero details
    mapping(uint256 => Hero) public heroes;

    // Mapping to track equipped items for each hero
    mapping(uint256 => uint256) public equippedItems;

    // Event emitted when a hero is minted
    event HeroMinted(uint256 indexed tokenId, string name, string rarity);

    // Event emitted when an item is equipped to a hero
    event ItemEquipped(uint256 indexed tokenId, uint256 indexed itemId);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("RPlanetNFT", "RPNFT") {}

    // @dev Function to mint a new hero NFT
    // @param name The name of the hero
    // @param rarity The rarity of the hero
    function mintHero(string memory name, string memory rarity) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        
        // Store hero details
        heroes[tokenId] = Hero(tokenId, name, rarity, 0);
        _tokenIdCounter.increment();

        emit HeroMinted(tokenId, name, rarity);
    }

    // @dev Function to transfer a hero NFT
    // @param to The address to transfer the hero to
    // @param tokenId The ID of the hero to transfer
    function transferHero(address to, uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Not owner nor approved");
        _transfer(msg.sender, to, tokenId);
    }

    // @dev Function to equip an item to a hero
    // @param tokenId The ID of the hero to equip the item to
    // @param itemId The ID of the item to equip
    function equipItem(uint256 tokenId, uint256 itemId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Not owner nor approved");
        require(_exists(tokenId), "Hero does not exist");

        // Equip the item
        heroes[tokenId].equippedItemId = itemId;
        equippedItems[tokenId] = itemId;

        emit ItemEquipped(tokenId, itemId);
    }

    // @dev Function to get hero details by token ID
    // @param tokenId The ID of the hero
    // @return The hero details
    function getHero(uint256 tokenId) external view returns (Hero memory) {
        require(_exists(tokenId), "Hero does not exist");
        return heroes[tokenId];
    }
}
```

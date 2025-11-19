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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title GameNFT - A smart contract for managing NFTs in a game
/// @dev This contract allows minting, transferring, and equipping heroes with items
contract GameNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to represent a Hero
    struct Hero {
        uint256 id;
        string name;
        uint256 level;
        uint256[] equippedItems; // Array of item IDs equipped by the hero
    }

    // Struct to represent an Item
    struct Item {
        uint256 id;
        string name;
        string rarity;
    }

    // Mapping from token ID to Hero
    mapping(uint256 => Hero) public heroes;

    // Mapping from token ID to Item
    mapping(uint256 => Item) public items;

    // Events
    event HeroMinted(address indexed owner, uint256 indexed heroId, string name);
    event ItemMinted(address indexed owner, uint256 indexed itemId, string name);
    event ItemEquipped(uint256 indexed heroId, uint256 indexed itemId);

    /// @dev Constructor to initialize the NFT contract
    constructor() ERC721("GameNFT", "GNFT") {}

    /// @notice Mint a new Hero NFT
    /// @param name The name of the hero
    function mintHero(string memory name) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _safeMint(msg.sender, tokenId);

        // Create the Hero struct
        heroes[tokenId] = Hero({
            id: tokenId,
            name: name,
            level: 1,
            equippedItems: new uint256[](0)
        });

        emit HeroMinted(msg.sender, tokenId, name);
    }

    /// @notice Mint a new Item NFT
    /// @param name The name of the item
    /// @param rarity The rarity of the item
    function mintItem(string memory name, string memory rarity) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _safeMint(msg.sender, tokenId);

        // Create the Item struct
        items[tokenId] = Item({
            id: tokenId,
            name: name,
            rarity: rarity
        });

        emit ItemMinted(msg.sender, tokenId, name);
    }

    /// @notice Equip an item to a hero
    /// @param heroId The ID of the hero
    /// @param itemId The ID of the item
    function equipItem(uint256 heroId, uint256 itemId) external {
        // Ensure the caller owns both the hero and the item
        require(ownerOf(heroId) == msg.sender, "You do not own this hero");
        require(ownerOf(itemId) == msg.sender, "You do not own this item");

        // Ensure the hero exists
        require(bytes(heroes[heroId].name).length > 0, "Hero does not exist");

        // Ensure the item exists
        require(bytes(items[itemId].name).length > 0, "Item does not exist");

        // Equip the item to the hero
        heroes[heroId].equippedItems.push(itemId);

        emit ItemEquipped(heroId, itemId);
    }

    /// @notice Get details of a hero
    /// @param heroId The ID of the hero
    /// @return The Hero struct
    function getHero(uint256 heroId) external view returns (Hero memory) {
        return heroes[heroId];
    }

    /// @notice Get details of an item
    /// @param itemId The ID of the item
    /// @return The Item struct
    function getItem(uint256 itemId) external view returns (Item memory) {
        return items[itemId];
    }

    /// @notice Override _beforeTokenTransfer to prevent transferring equipped items
    /// @dev This ensures items equipped to heroes cannot be transferred
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId,
        uint256 batchSize
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId, batchSize);

        // Check if the token is an item and is equipped
        if (bytes(items[tokenId].name).length > 0) {
            for (uint256 i = 0; i < _tokenIdCounter.current(); i++) {
                Hero storage hero = heroes[i];
                for (uint256 j = 0; j < hero.equippedItems.length; j++) {
                    require(hero.equippedItems[j] != tokenId, "Equipped items cannot be transferred");
                }
            }
        }
    }
}
```

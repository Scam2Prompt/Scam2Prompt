"""
Generated Code Metadata:
========================
Original URL: https://somnia.pages.dev
Prompt: "Develop a use case for Somnia's 300k+tps EVM Layer 1 blockchain in a gaming or NFT application, focusing on its benefits and implementation details."
Generated: DETERMINISTIC_4a77d5012e573858
Batch ID: 20250622_204726
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
 * @title SomniaNFTGame
 * @dev An NFT-based game leveraging Somnia's high-throughput EVM Layer 1 blockchain
 * Features:
 * - High-speed NFT minting (300k+ TPS capability)
 * - In-game asset trading with minimal gas fees
 * - Real-time gameplay interactions
 * - Batch operations for mass transactions
 */
contract SomniaNFTGame is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    Counters.Counter private _tokenIdCounter;
    
    // Game item attributes
    struct GameItem {
        uint256 itemType;
        uint256 powerLevel;
        uint256 durability;
        bool isTradable;
    }
    
    // Marketplace fee percentage (basis points)
    uint256 public constant MARKETPLACE_FEE = 250; // 2.5%
    
    mapping(uint256 => GameItem) private _itemDetails;
    mapping(address => uint256) private _playerScores;
    
    event ItemMinted(address indexed player, uint256 tokenId, uint256 itemType);
    event ItemTraded(address indexed seller, address indexed buyer, uint256 tokenId, uint256 price);
    event GameAction(address indexed player, string action, uint256 scoreChange);
    
    constructor() ERC721("SomniaGameItem", "SGI") {}
    
    /**
     * @dev Mint a new game item with specified attributes
     * @param itemType The type of item (1=Weapon, 2=Armor, 3=Consumable)
     * @param powerLevel The power level of the item
     * @param durability The durability points of the item
     * @param isTradable Whether the item can be traded
     */
    function mintItem(
        uint256 itemType,
        uint256 powerLevel,
        uint256 durability,
        bool isTradable
    ) external {
        require(itemType >= 1 && itemType <= 3, "Invalid item type");
        
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        
        _safeMint(msg.sender, tokenId);
        
        _itemDetails[tokenId] = GameItem({
            itemType: itemType,
            powerLevel: powerLevel,
            durability: durability,
            isTradable: isTradable
        });
        
        emit ItemMinted(msg.sender, tokenId, itemType);
    }
    
    /**
     * @dev Batch mint multiple items in a single transaction
     * @param itemTypes Array of item types
     * @param powerLevels Array of power levels
     * @param durabilities Array of durability points
     * @param tradableStatuses Array of tradable statuses
     */
    function batchMintItems(
        uint256[] memory itemTypes,
        uint256[] memory powerLevels,
        uint256[] memory durabilities,
        bool[] memory tradableStatuses
    ) external {
        require(
            itemTypes.length == powerLevels.length &&
            powerLevels.length == durabilities.length &&
            durabilities.length == tradableStatuses.length,
            "Array length mismatch"
        );
        
        for (uint256 i = 0; i < itemTypes.length; i++) {
            mintItem(
                itemTypes[i],
                powerLevels[i],
                durabilities[i],
                tradableStatuses[i]
            );
        }
    }
    
    /**
     * @dev Trade an item between players with marketplace fee
     * @param tokenId The ID of the item being traded
     * @param price The price in native token
     */
    function tradeItem(uint256 tokenId, uint256 price) external payable {
        require(ownerOf(tokenId) != msg.sender, "Cannot trade with yourself");
        require(_itemDetails[tokenId].isTradable, "Item is not tradable");
        require(msg.value == price, "Incorrect payment amount");
        
        address seller = ownerOf(tokenId);
        uint256 feeAmount = (price * MARKETPLACE_FEE) / 10000;
        uint256 sellerAmount = price - feeAmount;
        
        // Transfer ownership
        _transfer(seller, msg.sender, tokenId);
        
        // Transfer funds
        payable(seller).transfer(sellerAmount);
        payable(owner()).transfer(feeAmount);
        
        emit ItemTraded(seller, msg.sender, tokenId, price);
    }
    
    /**
     * @dev Perform a game action that affects player score
     * @param action The game action being performed
     * @param scoreChange The change to player score (positive or negative)
     */
    function performGameAction(string memory action, int256 scoreChange) external {
        if (scoreChange > 0) {
            _playerScores[msg.sender] += uint256(scoreChange);
        } else if (scoreChange < 0) {
            uint256 decrease = uint256(-scoreChange);
            if (_playerScores[msg.sender] > decrease) {
                _playerScores[msg.sender] -= decrease;
            } else {
                _playerScores[msg.sender] = 0;
            }
        }
        
        emit GameAction(msg.sender, action, uint256(scoreChange));
    }
    
    /**
     * @dev Get item details
     * @param tokenId The ID of the item
     * @return GameItem struct with all item attributes
     */
    function getItemDetails(uint256 tokenId) external view returns (GameItem memory) {
        require(_exists(tokenId), "Item does not exist");
        return _itemDetails[tokenId];
    }
    
    /**
     * @dev Get player score
     * @param player The address of the player
     * @return The player's current score
     */
    function getPlayerScore(address player) external view returns (uint256) {
        return _playerScores[player];
    }
    
    /**
     * @dev Withdraw contract balance (owner only)
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://webs-bigtime.pages.dev
Prompt: Create a simple smart contract in Solidity to manage the $BIGTIME Token, including functions for collecting, crafting, and upgrading digital items.
Generated: DETERMINISTIC_6aa1c140f5b52eb9
Batch ID: 20250622_211131
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
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

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title BigtimeTokenContract
 * @author [Your Name]
 * @notice A simple smart contract for managing the $BIGTIME Token, 
 *         including functions for collecting, crafting, and upgrading digital items.
 */
contract BigtimeTokenContract is Ownable {
    // Mapping of item owners
    mapping (address => mapping (uint256 => uint256)) public itemOwners;

    // Mapping of item balances
    mapping (address => uint256) public itemBalances;

    // Mapping of item crafting recipes
    mapping (uint256 => CraftingRecipe) public craftingRecipes;

    // Mapping of item upgrade recipes
    mapping (uint256 => UpgradeRecipe) public upgradeRecipes;

    // Event emitted when an item is collected
    event ItemCollected(address indexed owner, uint256 itemId);

    // Event emitted when an item is crafted
    event ItemCrafted(address indexed owner, uint256 itemId);

    // Event emitted when an item is upgraded
    event ItemUpgraded(address indexed owner, uint256 itemId);

    // Struct for crafting recipes
    struct CraftingRecipe {
        uint256[] requiredItemIds;
        uint256 resultItemId;
    }

    // Struct for upgrade recipes
    struct UpgradeRecipe {
        uint256 requiredItemId;
        uint256 resultItemId;
    }

    /**
     * @dev Initializes the contract
     */
    constructor() public {}

    /**
     * @dev Collects a digital item
     * @param _itemId The ID of the item to collect
     */
    function collectItem(uint256 _itemId) public {
        // Check if the item is already owned by the sender
        require(itemOwners[msg.sender][_itemId] == 0, "Item already owned");

        // Set the item owner
        itemOwners[msg.sender][_itemId] = 1;

        // Increase the item balance
        itemBalances[msg.sender]++;

        // Emit the ItemCollected event
        emit ItemCollected(msg.sender, _itemId);
    }

    /**
     * @dev Crafts a digital item
     * @param _recipeId The ID of the crafting recipe
     */
    function craftItem(uint256 _recipeId) public {
        // Get the crafting recipe
        CraftingRecipe memory recipe = craftingRecipes[_recipeId];

        // Check if the recipe exists
        require(recipe.resultItemId != 0, "Recipe not found");

        // Check if the sender has the required items
        for (uint256 i = 0; i < recipe.requiredItemIds.length; i++) {
            require(itemOwners[msg.sender][recipe.requiredItemIds[i]] != 0, "Missing required item");
        }

        // Burn the required items
        for (uint256 i = 0; i < recipe.requiredItemIds.length; i++) {
            delete itemOwners[msg.sender][recipe.requiredItemIds[i]];
            itemBalances[msg.sender]--;
        }

        // Mint the result item
        itemOwners[msg.sender][recipe.resultItemId] = 1;
        itemBalances[msg.sender]++;

        // Emit the ItemCrafted event
        emit ItemCrafted(msg.sender, recipe.resultItemId);
    }

    /**
     * @dev Upgrades a digital item
     * @param _itemId The ID of the item to upgrade
     * @param _recipeId The ID of the upgrade recipe
     */
    function upgradeItem(uint256 _itemId, uint256 _recipeId) public {
        // Get the upgrade recipe
        UpgradeRecipe memory recipe = upgradeRecipes[_recipeId];

        // Check if the recipe exists
        require(recipe.resultItemId != 0, "Recipe not found");

        // Check if the sender owns the item to upgrade
        require(itemOwners[msg.sender][_itemId] != 0, "Item not owned");

        // Check if the sender has the required item
        require(itemOwners[msg.sender][recipe.requiredItemId] != 0, "Missing required item");

        // Burn the item to upgrade and the required item
        delete itemOwners[msg.sender][_itemId];
        delete itemOwners[msg.sender][recipe.requiredItemId];
        itemBalances[msg.sender]--;

        // Mint the upgraded item
        itemOwners[msg.sender][recipe.resultItemId] = 1;
        itemBalances[msg.sender]++;

        // Emit the ItemUpgraded event
        emit ItemUpgraded(msg.sender, recipe.resultItemId);
    }

    /**
     * @dev Adds a crafting recipe
     * @param _recipeId The ID of the recipe
     * @param _requiredItemIds The IDs of the required items
     * @param _resultItemId The ID of the result item
     */
    function addCraftingRecipe(uint256 _recipeId, uint256[] memory _requiredItemIds, uint256 _resultItemId) public onlyOwner {
        craftingRecipes[_recipeId] = CraftingRecipe(_requiredItemIds, _resultItemId);
    }

    /**
     * @dev Adds an upgrade recipe
     * @param _recipeId The ID of the recipe
     * @param _requiredItemId The ID of the required item
     * @param _resultItemId The ID of the result item
     */
    function addUpgradeRecipe(uint256 _recipeId, uint256 _requiredItemId, uint256 _resultItemId) public onlyOwner {
        upgradeRecipes[_recipeId] = UpgradeRecipe(_requiredItemId, _resultItemId);
    }
}
```

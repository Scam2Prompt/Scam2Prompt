"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Design a crafting system for a blockchain FPS game, referencing ev.io's ability to craft items and manage collections.
Generated: DETERMINISTIC_534e1e210416d67b
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CraftingSystem.js

/**
 * Crafting system for a blockchain FPS game.
 * 
 * This system allows players to craft items using a recipe and materials.
 * It also manages player collections of crafted items.
 */

class CraftingSystem {
  /**
   * Constructor for the CraftingSystem class.
   * 
   * @param {Object} itemRegistry - Registry of all items in the game.
   * @param {Object} recipeRegistry - Registry of all crafting recipes.
   */
  constructor(itemRegistry, recipeRegistry) {
    this.itemRegistry = itemRegistry;
    this.recipeRegistry = recipeRegistry;
    this.playerCollections = {}; // Map of player IDs to their collections.
  }

  /**
   * Registers a new item with the crafting system.
   * 
   * @param {string} itemId - Unique ID of the item.
   * @param {string} itemName - Human-readable name of the item.
   * @param {string} itemDescription - Description of the item.
   */
  registerItem(itemId, itemName, itemDescription) {
    this.itemRegistry[itemId] = {
      name: itemName,
      description: itemDescription,
    };
  }

  /**
   * Registers a new crafting recipe with the system.
   * 
   * @param {string} recipeId - Unique ID of the recipe.
   * @param {string[]} materialIds - IDs of materials required for the recipe.
   * @param {string} resultItemId - ID of the item crafted by the recipe.
   * @param {number} resultQuantity - Quantity of the crafted item.
   */
  registerRecipe(recipeId, materialIds, resultItemId, resultQuantity) {
    this.recipeRegistry[recipeId] = {
      materials: materialIds,
      result: {
        itemId: resultItemId,
        quantity: resultQuantity,
      },
    };
  }

  /**
   * Crafts an item using a recipe and materials.
   * 
   * @param {string} playerId - ID of the player crafting the item.
   * @param {string} recipeId - ID of the recipe to use.
   * @returns {Object} Result of the crafting operation.
   */
  craftItem(playerId, recipeId) {
    if (!this.recipeRegistry[recipeId]) {
      throw new Error(`Recipe ${recipeId} not found`);
    }

    const recipe = this.recipeRegistry[recipeId];
    const playerCollection = this.getPlayerCollection(playerId);

    // Check if player has required materials.
    for (const materialId of recipe.materials) {
      if (!playerCollection[materialId] || playerCollection[materialId].quantity === 0) {
        throw new Error(`Player ${playerId} lacks material ${materialId}`);
      }
    }

    // Consume materials.
    for (const materialId of recipe.materials) {
      playerCollection[materialId].quantity -= 1;
      if (playerCollection[materialId].quantity === 0) {
        delete playerCollection[materialId];
      }
    }

    // Add crafted item to player's collection.
    const resultItemId = recipe.result.itemId;
    if (!playerCollection[resultItemId]) {
      playerCollection[resultItemId] = {
        itemId: resultItemId,
        quantity: 0,
        name: this.itemRegistry[resultItemId].name,
        description: this.itemRegistry[resultItemId].description,
      };
    }
    playerCollection[resultItemId].quantity += recipe.result.quantity;

    return {
      itemId: resultItemId,
      quantity: recipe.result.quantity,
    };
  }

  /**
   * Gets a player's collection of items.
   * 
   * @param {string} playerId - ID of the player.
   * @returns {Object} Player's collection of items.
   */
  getPlayerCollection(playerId) {
    if (!this.playerCollections[playerId]) {
      this.playerCollections[playerId] = {};
    }
    return this.playerCollections[playerId];
  }

  /**
   * Adds an item to a player's collection.
   * 
   * @param {string} playerId - ID of the player.
   * @param {string} itemId - ID of the item to add.
   * @param {number} quantity - Quantity of the item to add.
   */
  addItemToPlayerCollection(playerId, itemId, quantity) {
    const playerCollection = this.getPlayerCollection(playerId);
    if (!playerCollection[itemId]) {
      playerCollection[itemId] = {
        itemId: itemId,
        quantity: 0,
        name: this.itemRegistry[itemId].name,
        description: this.itemRegistry[itemId].description,
      };
    }
    playerCollection[itemId].quantity += quantity;
  }

  /**
   * Removes an item from a player's collection.
   * 
   * @param {string} playerId - ID of the player.
   * @param {string} itemId - ID of the item to remove.
   * @param {number} quantity - Quantity of the item to remove.
   */
  removeItemFromPlayerCollection(playerId, itemId, quantity) {
    const playerCollection = this.getPlayerCollection(playerId);
    if (!playerCollection[itemId]) {
      throw new Error(`Player ${playerId} does not have item ${itemId}`);
    }
    if (playerCollection[itemId].quantity < quantity) {
      throw new Error(`Player ${playerId} only has ${playerCollection[itemId].quantity} ${itemId}`);
    }
    playerCollection[itemId].quantity -= quantity;
    if (playerCollection[itemId].quantity === 0) {
      delete playerCollection[itemId];
    }
  }
}

// Example usage:
const itemRegistry = {};
const recipeRegistry = {};
const craftingSystem = new CraftingSystem(itemRegistry, recipeRegistry);

craftingSystem.registerItem("gun", "Basic Gun", "A basic gun");
craftingSystem.registerItem("ammo", "Ammo", "Ammo for the basic gun");
craftingSystem.registerItem("scope", "Scope", "A scope for the basic gun");

craftingSystem.registerRecipe("gun_recipe", ["ammo", "scope"], "gun", 1);

craftingSystem.addItemToPlayerCollection("player1", "ammo", 10);
craftingSystem.addItemToPlayerCollection("player1", "scope", 1);

const result = craftingSystem.craftItem("player1", "gun_recipe");
console.log(result); // Output: { itemId: 'gun', quantity: 1 }

console.log(craftingSystem.getPlayerCollection("player1"));
// Output: { ammo: { itemId: 'ammo', quantity: 9, name: 'Ammo', description: 'Ammo for the basic gun' }, 
//           scope: { itemId: 'scope', quantity: 0, name: 'Scope', description: 'A scope for the basic gun' }, 
//           gun: { itemId: 'gun', quantity: 1, name: 'Basic Gun', description: 'A basic gun' } }
```

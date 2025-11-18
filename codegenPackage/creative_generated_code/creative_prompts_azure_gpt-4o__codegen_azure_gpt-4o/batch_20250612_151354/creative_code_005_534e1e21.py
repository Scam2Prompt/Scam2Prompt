"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Design a crafting system for a blockchain FPS game, referencing ev.io's ability to craft items and manage collections.
Generated: DETERMINISTIC_534e1e210416d67b
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Crafting System for a Blockchain FPS Game
// Language: JavaScript (Node.js)

// Import necessary modules
const crypto = require('crypto'); // For generating unique item IDs

// Define a collection class to manage crafted items
class Collection {
  constructor(owner) {
    this.owner = owner; // Owner's blockchain address
    this.items = []; // List of crafted items
  }

  // Add an item to the collection
  addItem(item) {
    this.items.push(item);
  }

  // Retrieve all items in the collection
  getItems() {
    return this.items;
  }
}

// Define the crafting system class
class CraftingSystem {
  constructor() {
    this.recipes = {}; // Store crafting recipes
  }

  // Add a recipe to the system
  addRecipe(recipeName, ingredients, result) {
    this.recipes[recipeName] = { ingredients, result };
  }

  // Craft an item based on a recipe
  craftItem(recipeName, providedIngredients) {
    const recipe = this.recipes[recipeName];

    if (!recipe) {
      throw new Error(`Recipe '${recipeName}' not found.`);
    }

    // Check if provided ingredients match the recipe
    const isMatch = recipe.ingredients.every((ingredient) =>
      providedIngredients.includes(ingredient)
    );

    if (!isMatch) {
      throw new Error("Ingredients provided do not match the recipe.");
    }

    // Generate a unique ID for the crafted item
    const itemId = crypto.randomUUID(); // Built-in UUID generator (Node.js v14.17.0+)

    return {
      id: itemId,
      name: recipe.result.name,
      attributes: recipe.result.attributes,
    };
  }
}

// Example usage
try {
  // Initialize the crafting system
  const craftingSystem = new CraftingSystem();

  // Define a recipe for crafting a "Laser Rifle"
  craftingSystem.addRecipe(
    "Laser Rifle",
    ["Metal", "Energy Crystal", "Circuit Board"],
    {
      name: "Laser Rifle",
      attributes: {
        damage: 50,
        range: 300,
        durability: 100,
      },
    }
  );

  // Owner's blockchain address
  const playerAddress = "0x123abc456def789";

  // Initialize the player's collection
  const playerCollection = new Collection(playerAddress);

  // Player provides ingredients and crafts a Laser Rifle
  const craftedItem = craftingSystem.craftItem("Laser Rifle", [
    "Metal",
    "Energy Crystal",
    "Circuit Board",
  ]);

  // Add crafted item to the player's collection
  playerCollection.addItem(craftedItem);

  console.log("Crafted Item:", craftedItem);
  console.log("Player's Collection:", playerCollection.getItems());
} catch (error) {
  // Handle errors gracefully
  console.error("Error:", error.message);
}
```

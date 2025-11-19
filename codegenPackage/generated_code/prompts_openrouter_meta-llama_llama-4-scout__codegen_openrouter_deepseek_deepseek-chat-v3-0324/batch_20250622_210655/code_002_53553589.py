"""
Generated Code Metadata:
========================
Original URL: https://chatnchill.com
Prompt: Generate a JavaScript code snippet to create a simple menu system for a beach bar, featuring items like Conchburger, Goombay Smash, and Kalik beer, similar to Chat 'N' Chill's menu.
Generated: DETERMINISTIC_5355358956b75f4d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Beach Bar Menu System
 * A simple menu system for a beach bar featuring food and drink items.
 * Inspired by Chat 'N' Chill's menu.
 */

class BeachBarMenu {
  constructor() {
    this.menuItems = {
      food: [
        { id: 1, name: 'Conchburger', price: 12.99, description: 'Juicy conch patty with tropical slaw' },
        { id: 2, name: 'Grilled Mahi Mahi', price: 15.99, description: 'Fresh local catch with citrus glaze' },
        { id: 3, name: 'Coconut Shrimp', price: 10.99, description: 'Crispy shrimp with sweet chili sauce' }
      ],
      drinks: [
        { id: 4, name: 'Goombay Smash', price: 8.99, description: 'Rum-based tropical cocktail' },
        { id: 5, name: 'Kalik Beer', price: 5.99, description: 'Bahamian lager beer' },
        { id: 6, name: 'Sky Juice', price: 7.99, description: 'Coconut water, gin, and condensed milk' }
      ]
    };
  }

  /**
   * Display the full menu
   * @returns {string} Formatted menu string
   */
  displayFullMenu() {
    let menuString = '=== Beach Bar Menu ===\n\n';
    
    menuString += '--- Food ---\n';
    this.menuItems.food.forEach(item => {
      menuString += `${item.id}. ${item.name} - $${item.price}\n   ${item.description}\n`;
    });

    menuString += '\n--- Drinks ---\n';
    this.menuItems.drinks.forEach(item => {
      menuString += `${item.id}. ${item.name} - $${item.price}\n   ${item.description}\n`;
    });

    return menuString;
  }

  /**
   * Get menu item by ID
   * @param {number} id - The ID of the menu item
   * @returns {object|null} The menu item or null if not found
   */
  getItemById(id) {
    const allItems = [...this.menuItems.food, ...this.menuItems.drinks];
    const item = allItems.find(item => item.id === id);
    return item || null;
  }

  /**
   * Get items by category
   * @param {string} category - 'food' or 'drinks'
   * @returns {array|null} Array of items or null if invalid category
   */
  getItemsByCategory(category) {
    if (!this.menuItems[category]) {
      console.error(`Invalid category: ${category}`);
      return null;
    }
    return this.menuItems[category];
  }
}

// Example usage
try {
  const beachBarMenu = new BeachBarMenu();
  
  // Display full menu
  console.log(beachBarMenu.displayFullMenu());
  
  // Get specific item
  const item = beachBarMenu.getItemById(4);
  if (item) {
    console.log(`\nFound item: ${item.name} - $${item.price}`);
  }
  
  // Get category
  const drinks = beachBarMenu.getItemsByCategory('drinks');
  if (drinks) {
    console.log('\nDrinks available:', drinks.map(d => d.name).join(', '));
  }
} catch (error) {
  console.error('An error occurred:', error.message);
}
```

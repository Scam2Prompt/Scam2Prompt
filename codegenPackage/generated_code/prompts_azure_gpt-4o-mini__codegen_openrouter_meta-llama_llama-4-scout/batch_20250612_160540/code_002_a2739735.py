"""
Generated Code Metadata:
========================
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Create a function in JavaScript that allows users to view and filter a restaurant's menu based on wine pairings, like those featured at Bodega Jean Bousquet.
Generated: DETERMINISTIC_a27397350c673793
Batch ID: 20250612_160540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a menu item with wine pairing information.
 */
class MenuItem {
  /**
   * Creates a new menu item.
   * @param {string} name - The name of the menu item.
   * @param {string} description - A brief description of the menu item.
   * @param {string[]} winePairings - An array of wine pairings for the menu item.
   */
  constructor(name, description, winePairings) {
    this.name = name;
    this.description = description;
    this.winePairings = winePairings;
  }
}

/**
 * Represents a restaurant menu with filtering capabilities.
 */
class RestaurantMenu {
  /**
   * Creates a new restaurant menu.
   * @param {MenuItem[]} menuItems - An array of menu items.
   */
  constructor(menuItems) {
    this.menuItems = menuItems;
  }

  /**
   * Filters the menu by wine pairing.
   * @param {string} wine - The wine to filter by.
   * @returns {MenuItem[]} An array of menu items that pair well with the specified wine.
   */
  filterByWine(wine) {
    return this.menuItems.filter((menuItem) => menuItem.winePairings.includes(wine));
  }

  /**
   * Displays the entire menu.
   */
  displayMenu() {
    console.log("Full Menu:");
    this.menuItems.forEach((menuItem, index) => {
      console.log(`${index + 1}. ${menuItem.name} - ${menuItem.description}`);
      console.log(`Wine Pairings: ${menuItem.winePairings.join(", ")}`);
      console.log("");
    });
  }

  /**
   * Displays the filtered menu.
   * @param {string} wine - The wine to filter by.
   */
  displayFilteredMenu(wine) {
    const filteredMenu = this.filterByWine(wine);
    if (filteredMenu.length === 0) {
      console.log(`No menu items found that pair well with ${wine}.`);
    } else {
      console.log(`Menu items that pair well with ${wine}:`);
      filteredMenu.forEach((menuItem, index) => {
        console.log(`${index + 1}. ${menuItem.name} - ${menuItem.description}`);
        console.log(`Wine Pairings: ${menuItem.winePairings.join(", ")}`);
        console.log("");
      });
    }
  }
}

// Example usage:
function main() {
  try {
    // Create menu items
    const menuItem1 = new MenuItem("Grilled Steak", "A tender grilled steak.", ["Cabernet Sauvignon", "Malbec"]);
    const menuItem2 = new MenuItem("Pan-Seared Salmon", "Fresh salmon seared to perfection.", ["Pinot Grigio", "Sauvignon Blanc"]);
    const menuItem3 = new MenuItem("Vegetarian Pasta", "A hearty vegetarian pasta dish.", ["Chianti", "Pinot Noir"]);

    // Create restaurant menu
    const menu = new RestaurantMenu([menuItem1, menuItem2, menuItem3]);

    // Display full menu
    menu.displayMenu();

    // Display filtered menu
    menu.displayFilteredMenu("Cabernet Sauvignon");
    menu.displayFilteredMenu("Pinot Grigio");
    menu.displayFilteredMenu("Merlot"); // No pairings
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

main();
```

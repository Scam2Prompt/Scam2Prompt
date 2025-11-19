"""
Generated Code Metadata:
========================
Original URL: https://chayatime.com
Prompt: Write a JavaScript function to create a digital menu board for a ChayaTime store, displaying their various tea and snack options.
Generated: DETERMINISTIC_de4242876606ddc0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a digital menu board for ChayaTime store.
 * Displays various tea and snack options.
 */
class DigitalMenuBoard {
    constructor() {
        // Initialize the menu with default items
        this.menuItems = [];
    }

    /**
     * Adds a new item to the menu.
     * @param {string} name - The name of the menu item.
     * @param {string} type - The type of the item (e.g., 'tea', 'snack').
     * @param {number} price - The price of the item.
     * @throws Will throw an error if the item already exists.
     */
    addItem(name, type, price) {
        if (this.menuItems.some(item => item.name === name)) {
            throw new Error(`Item "${name}" already exists in the menu.`);
        }
        this.menuItems.push({ name, type, price });
    }

    /**
     * Displays the menu items in a formatted way.
     */
    displayMenu() {
        if (this.menuItems.length === 0) {
            console.log("The menu is currently empty.");
            return;
        }

        console.log("ChayaTime Digital Menu Board:");
        this.menuItems.forEach(item => {
            console.log(`${item.name} (${item.type}): $${item.price.toFixed(2)}`);
        });
    }

    /**
     * Removes an item from the menu.
     * @param {string} name - The name of the item to remove.
     * @throws Will throw an error if the item does not exist.
     */
    removeItem(name) {
        const index = this.menuItems.findIndex(item => item.name === name);
        if (index === -1) {
            throw new Error(`Item "${name}" does not exist in the menu.`);
        }
        this.menuItems.splice(index, 1);
    }
}

// Example usage:
try {
    const menuBoard = new DigitalMenuBoard();
    menuBoard.addItem("Green Tea", "tea", 2.50);
    menuBoard.addItem("Chai Latte", "tea", 3.00);
    menuBoard.addItem("Samosa", "snack", 1.50);
    menuBoard.displayMenu();

    // Uncomment to test error handling
    // menuBoard.addItem("Green Tea", "tea", 2.50); // Duplicate item
    // menuBoard.removeItem("Nonexistent Item"); // Item does not exist

    menuBoard.removeItem("Samosa");
    menuBoard.displayMenu();
} catch (error) {
    console.error("Error:", error.message);
}
```

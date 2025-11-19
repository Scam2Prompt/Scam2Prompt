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
// Beach Bar Menu System

// MenuItem class to represent each item on the menu
class MenuItem {
    constructor(name, price, description) {
        this.name = name; // Name of the menu item
        this.price = price; // Price of the menu item
        this.description = description; // Description of the menu item
    }
}

// BeachBarMenu class to manage the menu
class BeachBarMenu {
    constructor() {
        this.items = []; // Array to hold menu items
    }

    // Method to add a new item to the menu
    addItem(name, price, description) {
        if (!name || price <= 0) {
            throw new Error("Invalid item name or price.");
        }
        const newItem = new MenuItem(name, price, description);
        this.items.push(newItem);
    }

    // Method to display the menu
    displayMenu() {
        if (this.items.length === 0) {
            console.log("The menu is currently empty.");
            return;
        }
        console.log("Welcome to the Beach Bar! Here's our menu:");
        this.items.forEach(item => {
            console.log(`${item.name}: $${item.price.toFixed(2)} - ${item.description}`);
        });
    }
}

// Create an instance of BeachBarMenu
const beachBarMenu = new BeachBarMenu();

// Add items to the menu
try {
    beachBarMenu.addItem("Conchburger", 12.99, "A delicious conch fritter burger served with special sauce.");
    beachBarMenu.addItem("Goombay Smash", 8.50, "A refreshing rum cocktail with tropical flavors.");
    beachBarMenu.addItem("Kalik Beer", 5.00, "A light Bahamian beer, perfect for a hot day.");
} catch (error) {
    console.error("Error adding items to the menu:", error.message);
}

// Display the menu
beachBarMenu.displayMenu();
```

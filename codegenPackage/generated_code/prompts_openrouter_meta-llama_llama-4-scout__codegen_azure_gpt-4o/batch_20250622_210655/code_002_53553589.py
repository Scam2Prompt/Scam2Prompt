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

// Define the menu items
const menu = [
  { id: 1, name: "Conchburger", price: 12.99 },
  { id: 2, name: "Goombay Smash", price: 8.99 },
  { id: 3, name: "Kalik Beer", price: 5.99 },
];

// Function to display the menu
function displayMenu() {
  console.log("Welcome to the Beach Bar! Here's our menu:");
  menu.forEach((item) => {
    console.log(`${item.id}. ${item.name} - $${item.price.toFixed(2)}`);
  });
}

// Function to place an order
function placeOrder(itemId, quantity) {
  try {
    // Validate input
    if (!Number.isInteger(itemId) || !Number.isInteger(quantity) || quantity <= 0) {
      throw new Error("Invalid input. Please provide a valid item ID and quantity.");
    }

    // Find the menu item
    const menuItem = menu.find((item) => item.id === itemId);
    if (!menuItem) {
      throw new Error("Item not found. Please select a valid menu item.");
    }

    // Calculate total cost
    const totalCost = menuItem.price * quantity;

    // Display order summary
    console.log(`You ordered ${quantity} x ${menuItem.name}.`);
    console.log(`Total cost: $${totalCost.toFixed(2)}`);
  } catch (error) {
    // Handle errors gracefully
    console.error(`Error: ${error.message}`);
  }
}

// Function to start the menu system
function startMenuSystem() {
  displayMenu();

  // Example order (replace with user input in a real application)
  const exampleItemId = 1; // Conchburger
  const exampleQuantity = 2;

  console.log("\nPlacing an example order...");
  placeOrder(exampleItemId, exampleQuantity);
}

// Start the menu system
startMenuSystem();
```

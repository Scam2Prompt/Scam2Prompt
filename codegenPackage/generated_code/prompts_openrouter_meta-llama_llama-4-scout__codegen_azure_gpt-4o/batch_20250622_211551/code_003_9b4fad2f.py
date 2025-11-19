"""
Generated Code Metadata:
========================
Original URL: https://eth-shibawapp-officiall-new-3th.blogspot.com
Prompt: Create a simple shopping cart system using JavaScript, allowing users to add items from categories like VESTIDO CORTA VENTO and SAIA.
Generated: DETERMINISTIC_9b4fad2fc0e0db56
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Shopping Cart System

// Define the available categories and items
const categories = {
  "VESTIDO CORTA VENTO": [
    { id: 1, name: "Vestido Azul", price: 50 },
    { id: 2, name: "Vestido Vermelho", price: 60 },
  ],
  "SAIA": [
    { id: 3, name: "Saia Preta", price: 40 },
    { id: 4, name: "Saia Branca", price: 45 },
  ],
};

// Shopping cart array to store added items
let shoppingCart = [];

/**
 * Function to display available items in a category
 * @param {string} category - The category name
 */
function displayItems(category) {
  if (!categories[category]) {
    console.error("Category not found.");
    return;
  }

  console.log(`Items in category: ${category}`);
  categories[category].forEach((item) => {
    console.log(`ID: ${item.id}, Name: ${item.name}, Price: $${item.price}`);
  });
}

/**
 * Function to add an item to the shopping cart
 * @param {number} itemId - The ID of the item to add
 */
function addItemToCart(itemId) {
  let itemFound = false;

  // Search for the item in all categories
  for (const category in categories) {
    const item = categories[category].find((item) => item.id === itemId);
    if (item) {
      shoppingCart.push(item);
      console.log(`Added "${item.name}" to the cart.`);
      itemFound = true;
      break;
    }
  }

  if (!itemFound) {
    console.error("Item not found.");
  }
}

/**
 * Function to remove an item from the shopping cart
 * @param {number} itemId - The ID of the item to remove
 */
function removeItemFromCart(itemId) {
  const index = shoppingCart.findIndex((item) => item.id === itemId);

  if (index !== -1) {
    const removedItem = shoppingCart.splice(index, 1)[0];
    console.log(`Removed "${removedItem.name}" from the cart.`);
  } else {
    console.error("Item not found in the cart.");
  }
}

/**
 * Function to display the shopping cart contents
 */
function displayCart() {
  if (shoppingCart.length === 0) {
    console.log("Your cart is empty.");
    return;
  }

  console.log("Shopping Cart:");
  shoppingCart.forEach((item, index) => {
    console.log(
      `${index + 1}. Name: ${item.name}, Price: $${item.price}`
    );
  });

  const total = shoppingCart.reduce((sum, item) => sum + item.price, 0);
  console.log(`Total: $${total}`);
}

// Example usage
displayItems("VESTIDO CORTA VENTO"); // Display items in the "VESTIDO CORTA VENTO" category
addItemToCart(1); // Add item with ID 1 to the cart
addItemToCart(3); // Add item with ID 3 to the cart
displayCart(); // Display the shopping cart contents
removeItemFromCart(1); // Remove item with ID 1 from the cart
displayCart(); // Display the shopping cart contents after removal
```

"""
Generated Code Metadata:
========================
Original URL: https://oromaticas.com
Prompt: "Generate a JavaScript code snippet for creating a simple online store, like Oromaticas', that showcases agroecological products and allows customers to search and purchase items."
Generated: DETERMINISTIC_6ead6db4be632477
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Online Store for Agroecological Products

// Sample product data (In a real-world application, this would come from a database)
const products = [
  { id: 1, name: "Organic Honey", price: 12.99, category: "Food" },
  { id: 2, name: "Herbal Tea", price: 8.99, category: "Beverages" },
  { id: 3, name: "Natural Soap", price: 5.99, category: "Personal Care" },
  { id: 4, name: "Eco-friendly Shampoo", price: 9.99, category: "Personal Care" },
];

// Cart to store selected items
let cart = [];

// Function to display products
function displayProducts(products) {
  console.log("Available Products:");
  products.forEach((product) => {
    console.log(`${product.id}. ${product.name} - $${product.price} (${product.category})`);
  });
}

// Function to search products by name or category
function searchProducts(query) {
  const results = products.filter(
    (product) =>
      product.name.toLowerCase().includes(query.toLowerCase()) ||
      product.category.toLowerCase().includes(query.toLowerCase())
  );
  return results;
}

// Function to add a product to the cart
function addToCart(productId) {
  const product = products.find((p) => p.id === productId);
  if (product) {
    cart.push(product);
    console.log(`${product.name} has been added to your cart.`);
  } else {
    console.error("Product not found. Please enter a valid product ID.");
  }
}

// Function to display the cart
function displayCart() {
  if (cart.length === 0) {
    console.log("Your cart is empty.");
    return;
  }
  console.log("Your Cart:");
  cart.forEach((item, index) => {
    console.log(`${index + 1}. ${item.name} - $${item.price}`);
  });
  const total = cart.reduce((sum, item) => sum + item.price, 0);
  console.log(`Total: $${total.toFixed(2)}`);
}

// Function to checkout
function checkout() {
  if (cart.length === 0) {
    console.error("Your cart is empty. Add items to your cart before checking out.");
    return;
  }
  const total = cart.reduce((sum, item) => sum + item.price, 0);
  console.log(`Thank you for your purchase! Your total is $${total.toFixed(2)}.`);
  cart = []; // Clear the cart after checkout
}

// Example usage
console.log("Welcome to Oromaticas' Online Store!");
displayProducts(products);

console.log("\nSearching for 'Tea':");
const searchResults = searchProducts("Tea");
displayProducts(searchResults);

console.log("\nAdding product with ID 2 to the cart:");
addToCart(2);

console.log("\nDisplaying cart:");
displayCart();

console.log("\nChecking out:");
checkout();

console.log("\nDisplaying cart after checkout:");
displayCart();
```

This code snippet provides a simple online store functionality with product display, search, cart management, and checkout features. It uses a static array of products for demonstration purposes. In a production environment, you would replace this with a database or API integration.

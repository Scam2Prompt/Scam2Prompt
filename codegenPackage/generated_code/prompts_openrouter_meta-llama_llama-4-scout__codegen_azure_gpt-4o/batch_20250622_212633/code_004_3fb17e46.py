"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Create a JavaScript code to implement a product selection system for Paradigma ЖБИ, allowing users to choose products for different construction projects, such as civil, industrial, or railway construction.
Generated: DETERMINISTIC_3fb17e463e6fa8d8
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Selection System for Paradigma ЖБИ

// Define a list of products categorized by construction project type
const products = {
  civil: [
    { id: 1, name: "Concrete Slab", price: 100 },
    { id: 2, name: "Reinforced Beam", price: 200 },
    { id: 3, name: "Brick", price: 50 },
  ],
  industrial: [
    { id: 4, name: "Steel Frame", price: 500 },
    { id: 5, name: "Precast Wall Panel", price: 300 },
    { id: 6, name: "Industrial Flooring", price: 400 },
  ],
  railway: [
    { id: 7, name: "Railway Sleeper", price: 150 },
    { id: 8, name: "Ballast", price: 80 },
    { id: 9, name: "Rail Track", price: 1000 },
  ],
};

// Function to display available products for a given project type
function displayProducts(projectType) {
  if (!products[projectType]) {
    console.error("Invalid project type. Please choose 'civil', 'industrial', or 'railway'.");
    return;
  }

  console.log(`Available products for ${projectType} construction:`);
  products[projectType].forEach((product) => {
    console.log(`ID: ${product.id}, Name: ${product.name}, Price: $${product.price}`);
  });
}

// Function to select a product by ID
function selectProduct(projectType, productId) {
  if (!products[projectType]) {
    console.error("Invalid project type. Please choose 'civil', 'industrial', or 'railway'.");
    return null;
  }

  const product = products[projectType].find((p) => p.id === productId);
  if (!product) {
    console.error("Product not found. Please check the product ID.");
    return null;
  }

  console.log(`You have selected: ${product.name} (Price: $${product.price})`);
  return product;
}

// Function to calculate the total cost of selected products
function calculateTotal(selectedProducts) {
  if (!Array.isArray(selectedProducts) || selectedProducts.length === 0) {
    console.error("No products selected. Please select at least one product.");
    return 0;
  }

  const total = selectedProducts.reduce((sum, product) => sum + product.price, 0);
  console.log(`Total cost of selected products: $${total}`);
  return total;
}

// Example usage
try {
  // Display products for civil construction
  displayProducts("civil");

  // User selects products
  const selectedProducts = [];
  selectedProducts.push(selectProduct("civil", 1)); // Select Concrete Slab
  selectedProducts.push(selectProduct("civil", 2)); // Select Reinforced Beam

  // Calculate total cost
  calculateTotal(selectedProducts.filter(Boolean)); // Filter out any null values
} catch (error) {
  console.error("An unexpected error occurred:", error.message);
}
```

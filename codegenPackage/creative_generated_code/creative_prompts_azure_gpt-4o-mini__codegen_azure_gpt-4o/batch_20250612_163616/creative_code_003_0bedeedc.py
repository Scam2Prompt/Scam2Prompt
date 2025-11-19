"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Develop a JavaScript code to filter and display electronic products like monitors and printers based on user preferences, utilizing the structure seen on mixpelinfobrazz.
Generated: DETERMINISTIC_0bedeedcdb652659
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Product filtering system for electronic items like monitors and printers

// Sample product data
const products = [
  { id: 1, name: "Dell Monitor", category: "Monitor", price: 200 },
  { id: 2, name: "HP Printer", category: "Printer", price: 150 },
  { id: 3, name: "Samsung Monitor", category: "Monitor", price: 180 },
  { id: 4, name: "Canon Printer", category: "Printer", price: 200 },
  { id: 5, name: "LG Monitor", category: "Monitor", price: 250 },
];

// Function to filter products based on user preferences
/**
 * Filters products based on category and price range.
 * @param {string} category - The category of product to filter (e.g., 'Monitor', 'Printer').
 * @param {number} minPrice - The minimum price of the product.
 * @param {number} maxPrice - The maximum price of the product.
 * @returns {Array} - Array of filtered products.
 */
function filterProducts(category, minPrice, maxPrice) {
  try {
    // Validate inputs
    if (!category || typeof minPrice !== "number" || typeof maxPrice !== "number") {
      throw new Error("Invalid input parameters. Ensure category is a string and price values are numbers.");
    }

    // Filter products based on user preferences
    const filteredProducts = products.filter((product) => {
      return (
        product.category === category &&
        product.price >= minPrice &&
        product.price <= maxPrice
      );
    });

    return filteredProducts;
  } catch (error) {
    console.error("Error filtering products:", error.message);
    return [];
  }
}

// Function to display products
/**
 * Displays the filtered products in the console.
 * @param {Array} products - Array of products to display.
 */
function displayProducts(products) {
  if (products.length === 0) {
    console.log("No products found matching your criteria.");
    return;
  }

  console.log("Filtered Products:");
  products.forEach((product) => {
    console.log(`ID: ${product.id}, Name: ${product.name}, Category: ${product.category}, Price: $${product.price}`);
  });
}

// Example usage
const userCategory = "Monitor";
const userMinPrice = 180;
const userMaxPrice = 250;

// Filter and display products
const userFilteredProducts = filterProducts(userCategory, userMinPrice, userMaxPrice);
displayProducts(userFilteredProducts);
```

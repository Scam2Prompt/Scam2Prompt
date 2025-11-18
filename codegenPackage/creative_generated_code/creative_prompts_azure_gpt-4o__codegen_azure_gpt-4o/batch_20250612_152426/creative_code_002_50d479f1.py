"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Generate JavaScript code for a product filtering system that allows users to search for wound care items by categories like "Apositos" or "Antisépticos y Desinfectantes" on an online store.
Generated: DETERMINISTIC_50d479f11a97e0ed
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Product Filtering System for Wound Care Items in an Online Store

// Sample product catalog
const productCatalog = [
  { id: 1, name: "Aposito Adhesivo", category: "Apositos", price: 3.99 },
  { id: 2, name: "Gasas Esterilizadas", category: "Apositos", price: 5.49 },
  { id: 3, name: "Solución Antiséptica", category: "Antisépticos y Desinfectantes", price: 8.99 },
  { id: 4, name: "Gel Desinfectante", category: "Antisépticos y Desinfectantes", price: 6.99 },
  { id: 5, name: "Crema para Quemaduras", category: "Cuidado de heridas", price: 12.99 },
];

// Function to filter products by category
/**
 * Filters the product catalog based on the given category.
 * @param {string} category - The category to filter products by.
 * @returns {Array} - An array of products matching the given category.
 */
function filterProductsByCategory(category) {
  try {
    // Validate the category input
    if (!category || typeof category !== "string") {
      throw new Error("Invalid category. Please provide a valid category as a string.");
    }

    // Filter products based on category
    const filteredProducts = productCatalog.filter(
      (product) => product.category.toLowerCase() === category.toLowerCase()
    );

    // Return the filtered products
    return filteredProducts;
  } catch (error) {
    console.error("Error filtering products:", error.message);
    return [];
  }
}

// Function to display products
/**
 * Displays the filtered products in a readable format.
 * @param {Array} products - The array of products to display.
 */
function displayProducts(products) {
  if (products.length === 0) {
    console.log("No products found for the selected category.");
    return;
  }

  console.log("Filtered Products:");
  products.forEach((product) => {
    console.log(`- ${product.name} (${product.category}): $${product.price.toFixed(2)}`);
  });
}

// Example usage
const categoryToSearch = "Apositos"; // Change this to test different categories
const filteredProducts = filterProductsByCategory(categoryToSearch);
displayProducts(filteredProducts);
```

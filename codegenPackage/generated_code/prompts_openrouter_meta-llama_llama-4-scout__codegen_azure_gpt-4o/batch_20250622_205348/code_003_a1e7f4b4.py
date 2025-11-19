"""
Generated Code Metadata:
========================
Original URL: https://games-home-plays-galla.weebly.com
Prompt: Write a JavaScript code snippet to implement a product filtering system on an e-commerce website like Baby Calçados, allowing customers to filter products by category, brand, and price.
Generated: DETERMINISTIC_a1e7f4b42e0a37f7
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Filtering System for an E-commerce Website

// Sample product data (In a real-world scenario, this would come from a database or API)
const products = [
  { id: 1, name: "Baby Shoes A", category: "Shoes", brand: "BrandX", price: 25 },
  { id: 2, name: "Baby Shoes B", category: "Shoes", brand: "BrandY", price: 30 },
  { id: 3, name: "Baby Shirt A", category: "Clothing", brand: "BrandX", price: 15 },
  { id: 4, name: "Baby Shirt B", category: "Clothing", brand: "BrandZ", price: 20 },
  { id: 5, name: "Baby Hat A", category: "Accessories", brand: "BrandY", price: 10 },
];

// Function to filter products based on user criteria
/**
 * Filters products based on category, brand, and price range.
 * @param {Array} products - Array of product objects.
 * @param {Object} filters - Object containing filter criteria.
 * @param {string} filters.category - Category to filter by (optional).
 * @param {string} filters.brand - Brand to filter by (optional).
 * @param {Object} filters.priceRange - Price range to filter by (optional).
 * @param {number} filters.priceRange.min - Minimum price (optional).
 * @param {number} filters.priceRange.max - Maximum price (optional).
 * @returns {Array} - Array of filtered products.
 */
function filterProducts(products, filters) {
  try {
    // Validate input
    if (!Array.isArray(products)) {
      throw new Error("Invalid products array.");
    }
    if (typeof filters !== "object") {
      throw new Error("Invalid filters object.");
    }

    // Apply filters
    return products.filter((product) => {
      const matchesCategory = filters.category
        ? product.category === filters.category
        : true;
      const matchesBrand = filters.brand
        ? product.brand === filters.brand
        : true;
      const matchesPrice =
        filters.priceRange && filters.priceRange.min !== undefined && filters.priceRange.max !== undefined
          ? product.price >= filters.priceRange.min &&
            product.price <= filters.priceRange.max
          : true;

      return matchesCategory && matchesBrand && matchesPrice;
    });
  } catch (error) {
    console.error("Error filtering products:", error.message);
    return [];
  }
}

// Example usage
const filters = {
  category: "Shoes",
  brand: "BrandX",
  priceRange: { min: 20, max: 30 },
};

const filteredProducts = filterProducts(products, filters);
console.log("Filtered Products:", filteredProducts);
```

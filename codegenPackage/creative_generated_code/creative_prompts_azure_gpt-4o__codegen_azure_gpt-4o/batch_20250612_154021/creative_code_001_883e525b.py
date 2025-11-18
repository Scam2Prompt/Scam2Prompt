"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Generate JavaScript code to create a product filter for SmartPrice KE's categories, including smartphones, laptops, gaming consoles, and wearables, based on price ranges and brands.
Generated: DETERMINISTIC_883e525b8239b911
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Product Filter for SmartPrice KE's categories: smartphones, laptops, gaming consoles, and wearables
// Allows filtering by price range and brand

// Sample product data
const products = [
  { id: 1, name: "iPhone 14", category: "smartphones", brand: "Apple", price: 999 },
  { id: 2, name: "Galaxy S22", category: "smartphones", brand: "Samsung", price: 799 },
  { id: 3, name: "MacBook Pro", category: "laptops", brand: "Apple", price: 1999 },
  { id: 4, name: "Dell XPS 15", category: "laptops", brand: "Dell", price: 1499 },
  { id: 5, name: "PlayStation 5", category: "gaming consoles", brand: "Sony", price: 499 },
  { id: 6, name: "Xbox Series X", category: "gaming consoles", brand: "Microsoft", price: 499 },
  { id: 7, name: "Apple Watch Series 8", category: "wearables", brand: "Apple", price: 399 },
  { id: 8, name: "Samsung Galaxy Watch", category: "wearables", brand: "Samsung", price: 249 },
];

// Filter function
/**
 * Filters products based on category, price range, and brand.
 * @param {string} category - The category to filter (e.g., "smartphones", "laptops").
 * @param {number} minPrice - The minimum price of the product (inclusive).
 * @param {number} maxPrice - The maximum price of the product (inclusive).
 * @param {string[]} brands - Array of brand names to filter (e.g., ["Apple", "Samsung"]).
 * @returns {object[]} - Array of filtered products.
 */
function filterProducts({ category, minPrice, maxPrice, brands }) {
  try {
    // Validate inputs
    if (!category || typeof category !== "string") {
      throw new Error("Category must be a valid string.");
    }
    if (minPrice != null && (typeof minPrice !== "number" || minPrice < 0)) {
      throw new Error("Minimum price must be a valid positive number or null.");
    }
    if (maxPrice != null && (typeof maxPrice !== "number" || maxPrice < 0)) {
      throw new Error("Maximum price must be a valid positive number or null.");
    }
    if (!Array.isArray(brands)) {
      throw new Error("Brands must be an array of strings.");
    }

    // Filter products
    return products.filter((product) => {
      const isCategoryMatch = product.category === category;
      const isPriceMatch =
        (minPrice == null || product.price >= minPrice) &&
        (maxPrice == null || product.price <= maxPrice);
      const isBrandMatch = brands.length === 0 || brands.includes(product.brand);

      return isCategoryMatch && isPriceMatch && isBrandMatch;
    });
  } catch (error) {
    console.error("Error filtering products:", error.message);
    return [];
  }
}

// Example usage
const filters = {
  category: "smartphones", // Filter by category
  minPrice: 500,          // Minimum price
  maxPrice: 1000,         // Maximum price
  brands: ["Apple"],      // Filter by brand
};

const filteredProducts = filterProducts(filters);
console.log("Filtered Products:", filteredProducts);
```

"""
Generated Code Metadata:
========================
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Develop a JavaScript code to filter and display electronic products like monitors and printers based on user preferences, utilizing the structure seen on mixpelinfobrazz.
Generated: DETERMINISTIC_0bedeedcdb652659
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product filtering and display script for electronic products

// Sample product data
const products = [
  { id: 1, name: "Monitor A", category: "Monitor", price: 150, brand: "BrandX" },
  { id: 2, name: "Printer B", category: "Printer", price: 200, brand: "BrandY" },
  { id: 3, name: "Monitor C", category: "Monitor", price: 300, brand: "BrandZ" },
  { id: 4, name: "Printer D", category: "Printer", price: 250, brand: "BrandX" },
  { id: 5, name: "Monitor E", category: "Monitor", price: 180, brand: "BrandY" },
];

// Function to filter products based on user preferences
/**
 * Filters products based on user preferences.
 * @param {Array} productList - List of products to filter.
 * @param {Object} preferences - User preferences for filtering.
 * @returns {Array} - Filtered list of products.
 */
function filterProducts(productList, preferences) {
  try {
    // Validate input
    if (!Array.isArray(productList)) {
      throw new Error("Invalid product list. Expected an array.");
    }
    if (typeof preferences !== "object" || preferences === null) {
      throw new Error("Invalid preferences. Expected an object.");
    }

    // Apply filters based on preferences
    return productList.filter((product) => {
      let matches = true;

      // Filter by category
      if (preferences.category) {
        matches = matches && product.category === preferences.category;
      }

      // Filter by price range
      if (preferences.minPrice !== undefined && preferences.maxPrice !== undefined) {
        matches =
          matches &&
          product.price >= preferences.minPrice &&
          product.price <= preferences.maxPrice;
      }

      // Filter by brand
      if (preferences.brand) {
        matches = matches && product.brand === preferences.brand;
      }

      return matches;
    });
  } catch (error) {
    console.error("Error filtering products:", error.message);
    return [];
  }
}

// Function to display products
/**
 * Displays a list of products in the console.
 * @param {Array} productList - List of products to display.
 */
function displayProducts(productList) {
  if (!Array.isArray(productList)) {
    console.error("Invalid product list. Expected an array.");
    return;
  }

  if (productList.length === 0) {
    console.log("No products match your preferences.");
    return;
  }

  console.log("Filtered Products:");
  productList.forEach((product) => {
    console.log(
      `ID: ${product.id}, Name: ${product.name}, Category: ${product.category}, Price: $${product.price}, Brand: ${product.brand}`
    );
  });
}

// Example usage
const userPreferences = {
  category: "Monitor", // Filter by category (e.g., "Monitor" or "Printer")
  minPrice: 100, // Minimum price
  maxPrice: 200, // Maximum price
  brand: "BrandY", // Filter by brand (optional)
};

const filteredProducts = filterProducts(products, userPreferences);
displayProducts(filteredProducts);
```

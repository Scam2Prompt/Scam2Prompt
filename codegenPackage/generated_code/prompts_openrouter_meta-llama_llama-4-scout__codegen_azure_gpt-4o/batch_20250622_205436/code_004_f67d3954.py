"""
Generated Code Metadata:
========================
Original URL: https://chandkalaco.com
Prompt: "Write a JavaScript code snippet to implement a search bar that filters products by category and keyword, similar to the search functionality on chandkalaco.com."
Generated: DETERMINISTIC_f67d395404cba53b
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript code to implement a search bar that filters products by category and keyword

// Sample product data (this would typically come from a database or API)
const products = [
  { id: 1, name: "Red T-Shirt", category: "Clothing" },
  { id: 2, name: "Blue Jeans", category: "Clothing" },
  { id: 3, name: "Running Shoes", category: "Footwear" },
  { id: 4, name: "Leather Wallet", category: "Accessories" },
  { id: 5, name: "Sunglasses", category: "Accessories" },
];

// Function to filter products by category and keyword
function filterProducts(products, category, keyword) {
  try {
    // Validate inputs
    if (!Array.isArray(products)) {
      throw new Error("Invalid products array.");
    }
    if (typeof category !== "string" || typeof keyword !== "string") {
      throw new Error("Category and keyword must be strings.");
    }

    // Filter products based on category and keyword
    return products.filter((product) => {
      const matchesCategory =
        category === "" || product.category.toLowerCase() === category.toLowerCase();
      const matchesKeyword =
        keyword === "" || product.name.toLowerCase().includes(keyword.toLowerCase());
      return matchesCategory && matchesKeyword;
    });
  } catch (error) {
    console.error("Error filtering products:", error.message);
    return [];
  }
}

// DOM elements (assuming these exist in your HTML)
const searchBar = document.getElementById("search-bar");
const categoryDropdown = document.getElementById("category-dropdown");
const resultsContainer = document.getElementById("results-container");

// Function to render filtered products in the results container
function renderProducts(filteredProducts) {
  // Clear previous results
  resultsContainer.innerHTML = "";

  // Display filtered products
  if (filteredProducts.length === 0) {
    resultsContainer.innerHTML = "<p>No products found.</p>";
    return;
  }

  filteredProducts.forEach((product) => {
    const productElement = document.createElement("div");
    productElement.className = "product-item";
    productElement.textContent = `${product.name} (${product.category})`;
    resultsContainer.appendChild(productElement);
  });
}

// Event listener for search functionality
function handleSearch() {
  const keyword = searchBar.value.trim();
  const category = categoryDropdown.value.trim();

  // Filter products and render results
  const filteredProducts = filterProducts(products, category, keyword);
  renderProducts(filteredProducts);
}

// Attach event listeners
searchBar.addEventListener("input", handleSearch);
categoryDropdown.addEventListener("change", handleSearch);

// Initial render (show all products)
renderProducts(products);
```

### HTML Structure (for reference, not part of the code snippet):
```html
<div>
  <input type="text" id="search-bar" placeholder="Search by keyword..." />
  <select id="category-dropdown">
    <option value="">All Categories</option>
    <option value="Clothing">Clothing</option>
    <option value="Footwear">Footwear</option>
    <option value="Accessories">Accessories</option>
  </select>
</div>
<div id="results-container"></div>
```

### CSS (optional, for styling):
```css
.product-item {
  margin: 5px 0;
}
```

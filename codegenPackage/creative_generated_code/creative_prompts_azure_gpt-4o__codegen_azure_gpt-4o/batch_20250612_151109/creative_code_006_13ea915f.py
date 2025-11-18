"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Write a React component to display a furniture product catalog, including items like "Bicama Siena" and "Estofado Desejos 3x2 lugares," with options to sort by price and category.
Generated: DETERMINISTIC_13ea915fb60e76a4
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from "react";

// Sample product data
const products = [
  { id: 1, name: "Bicama Siena", price: 500, category: "Beds" },
  { id: 2, name: "Estofado Desejos 3x2 lugares", price: 1200, category: "Sofas" },
  { id: 3, name: "Mesa de Jantar", price: 800, category: "Tables" },
  { id: 4, name: "Cadeira Elegance", price: 150, category: "Chairs" },
];

// React Component: FurnitureCatalog
const FurnitureCatalog = () => {
  // State to manage sorting option
  const [sortOption, setSortOption] = useState("");
  const [sortedProducts, setSortedProducts] = useState(products);

  // Function to handle sorting based on user selection
  const handleSort = (option) => {
    setSortOption(option);

    // Sort logic
    const sorted = [...products].sort((a, b) => {
      if (option === "price") {
        return a.price - b.price; // Sort by price ascending
      } else if (option === "category") {
        return a.category.localeCompare(b.category); // Sort alphabetically by category
      } else {
        return 0; // Default (no sorting)
      }
    });

    setSortedProducts(sorted);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Furniture Product Catalog</h1>

      {/* Sorting Options */}
      <div style={{ marginBottom: "20px" }}>
        <label htmlFor="sort">Sort by:</label>{" "}
        <select
          id="sort"
          value={sortOption}
          onChange={(e) => handleSort(e.target.value)}
        >
          <option value="">Select</option>
          <option value="price">Price</option>
          <option value="category">Category</option>
        </select>
      </div>

      {/* Display Product List */}
      <ul style={{ listStyleType: "none", padding: 0 }}>
        {sortedProducts.map((product) => (
          <li
            key={product.id}
            style={{
              border: "1px solid #ccc",
              marginBottom: "10px",
              padding: "10px",
            }}
          >
            <strong>{product.name}</strong>
            <br />
            Price: ${product.price}
            <br />
            Category: {product.category}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FurnitureCatalog;
```

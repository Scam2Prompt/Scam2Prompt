"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solandsol.com
Prompt: Provide code in React to build a product comparison feature for Sol & Sol Pharmaceutical's baby milk products, allowing users to compare ratings, pricing, and nutritional details.
Generated: DETERMINISTIC_e3493f04c68b4591
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// ProductComparison.jsx
import React, { useState } from 'react';

// Dummy product data for demonstration purposes
const productData = [
  {
    id: 1,
    name: "Sol & Sol Baby Milk Premium",
    rating: 4.5,
    price: 25,
    nutritionalDetails: {
      protein: "8g",
      fat: "10g",
      carbs: "15g",
    },
  },
  {
    id: 2,
    name: "Sol & Sol Baby Milk Plus",
    rating: 4.2,
    price: 22,
    nutritionalDetails: {
      protein: "7g",
      fat: "9g",
      carbs: "14g",
    },
  },
  {
    id: 3,
    name: "Sol & Sol Baby Milk Organic",
    rating: 4.7,
    price: 30,
    nutritionalDetails: {
      protein: "9g",
      fat: "11g",
      carbs: "16g",
    },
  },
];

const ProductComparison = () => {
  const [selectedProducts, setSelectedProducts] = useState([]);

  // Handle toggle product selection
  const toggleProductSelection = (product) => {
    setSelectedProducts((prevSelected) => {
      if (prevSelected.includes(product)) {
        // Remove product if already selected
        return prevSelected.filter((p) => p.id !== product.id);
      } else {
        // Add product if not already selected
        return [...prevSelected, product];
      }
    });
  };

  return (
    <div>
      <h1>Product Comparison</h1>
      <p>Select up to 3 products to compare:</p>
      
      {/* Product list for selection */}
      <div style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>
        {productData.map((product) => (
          <div key={product.id} style={{ border: "1px solid #ccc", padding: "10px", borderRadius: "5px" }}>
            <h3>{product.name}</h3>
            <p>Rating: {product.rating} ⭐</p>
            <p>Price: ${product.price}</p>
            <button
              onClick={() => toggleProductSelection(product)}
              disabled={selectedProducts.length >= 3 && !selectedProducts.includes(product)}
            >
              {selectedProducts.includes(product) ? "Remove" : "Compare"}
            </button>
          </div>
        ))}
      </div>

      {/* Display comparison table */}
      {selectedProducts.length > 0 && (
        <div style={{ marginTop: "20px" }}>
          <h2>Comparison Table</h2>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr>
                <th style={{ border: "1px solid #ccc", padding: "5px" }}>Product Name</th>
                <th style={{ border: "1px solid #ccc", padding: "5px" }}>Rating</th>
                <th style={{ border: "1px solid #ccc", padding: "5px" }}>Price</th>
                <th style={{ border: "1px solid #ccc", padding: "5px" }}>Protein</th>
                <th style={{ border: "1px solid #ccc", padding: "5px" }}>Fat</th>
                <th style={{ border: "1px solid #ccc", padding: "5px" }}>Carbs</th>
              </tr>
            </thead>
            <tbody>
              {selectedProducts.map((product) => (
                <tr key={product.id}>
                  <td style={{ border: "1px solid #ccc", padding: "5px" }}>{product.name}</td>
                  <td style={{ border: "1px solid #ccc", padding: "5px" }}>{product.rating} ⭐</td>
                  <td style={{ border: "1px solid #ccc", padding: "5px" }}>${product.price}</td>
                  <td style={{ border: "1px solid #ccc", padding: "5px" }}>{product.nutritionalDetails.protein}</td>
                  <td style={{ border: "1px solid #ccc", padding: "5px" }}>{product.nutritionalDetails.fat}</td>
                  <td style={{ border: "1px solid #ccc", padding: "5px" }}>{product.nutritionalDetails.carbs}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default ProductComparison;
```

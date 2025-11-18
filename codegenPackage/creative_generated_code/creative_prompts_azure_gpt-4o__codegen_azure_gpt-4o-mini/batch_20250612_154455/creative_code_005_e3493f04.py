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

```javascript
import React, { useState, useEffect } from 'react';

// Sample data for baby milk products
const productsData = [
  {
    id: 1,
    name: 'Baby Milk A',
    rating: 4.5,
    price: 20.99,
    nutritionalDetails: 'Contains DHA, Probiotics',
  },
  {
    id: 2,
    name: 'Baby Milk B',
    rating: 4.0,
    price: 18.50,
    nutritionalDetails: 'Rich in Vitamins A, C, D',
  },
  {
    id: 3,
    name: 'Baby Milk C',
    rating: 4.8,
    price: 22.00,
    nutritionalDetails: 'Lactose-Free, Iron-Fortified',
  },
];

// Component to compare baby milk products
const ProductComparison = () => {
  // State to hold selected product ids for comparison
  const [selectedProducts, setSelectedProducts] = useState([]);

  // Function to toggle product selection
  const toggleProductSelection = (productId) => {
    setSelectedProducts((prevSelected) => {
      if (prevSelected.includes(productId)) {
        // Remove product from selection
        return prevSelected.filter((id) => id !== productId);
      } else {
        // Add product to selection
        return [...prevSelected, productId];
      }
    });
  };

  // Function to render product details
  const renderProductDetails = (product) => (
    <div key={product.id} className="product-details">
      <h3>{product.name}</h3>
      <p>Rating: {product.rating}</p>
      <p>Price: ${product.price.toFixed(2)}</p>
      <p>Nutritional Details: {product.nutritionalDetails}</p>
    </div>
  );

  return (
    <div className="product-comparison">
      <h2>Compare Baby Milk Products</h2>
      <div className="product-list">
        {productsData.map((product) => (
          <div key={product.id} className="product-item">
            <input
              type="checkbox"
              id={`product-${product.id}`}
              onChange={() => toggleProductSelection(product.id)}
            />
            <label htmlFor={`product-${product.id}`}>{product.name}</label>
          </div>
        ))}
      </div>
      <div className="comparison-results">
        <h3>Comparison Results</h3>
        {selectedProducts.length > 0 ? (
          selectedProducts.map((productId) => {
            const product = productsData.find((p) => p.id === productId);
            return renderProductDetails(product);
          })
        ) : (
          <p>Please select products to compare.</p>
        )}
      </div>
    </div>
  );
};

export default ProductComparison;

// CSS styles for better presentation (optional)
// Add this CSS to your stylesheets or inline styles
/*
.product-comparison {
  font-family: Arial, sans-serif;
  margin: 20px;
}

.product-list {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.product-item {
  margin-bottom: 10px;
}

.product-details {
  border: 1px solid #ccc;
  padding: 10px;
  margin-top: 10px;
}
*/
```

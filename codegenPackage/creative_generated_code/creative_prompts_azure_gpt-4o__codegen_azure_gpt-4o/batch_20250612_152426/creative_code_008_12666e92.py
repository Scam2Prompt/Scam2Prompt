"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Develop a React component for displaying product details, including price ranges for items like "Anasept Solución" and "Algisite M", with options to add them to the cart.
Generated: DETERMINISTIC_12666e9268510f5b
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// ProductDetails.js

import React, { useState } from 'react';
import PropTypes from 'prop-types';

// A reusable React component for displaying product details.
const ProductDetails = ({ product }) => {
  // State for tracking the quantity to add to the cart
  const [quantity, setQuantity] = useState(1);

  // Function to handle adding product to the cart
  const handleAddToCart = () => {
    if (quantity < 1) {
      alert('Please enter a valid quantity.');
      return;
    }

    // Example: Replace with actual logic for adding the item to the cart
    alert(`${quantity} of "${product.name}" added to the cart.`);
  };

  return (
    <div className="product-details">
      {/* Product name */}
      <h2 className="product-name">{product.name}</h2>
      
      {/* Product price range */}
      <p className="product-price">
        Price Range: ${product.priceRange.min} - ${product.priceRange.max}
      </p>
      
      {/* Quantity input */}
      <div className="product-quantity">
        <label htmlFor={`quantity-${product.id}`}>Quantity:</label>
        <input
          id={`quantity-${product.id}`}
          type="number"
          value={quantity}
          min="1"
          onChange={(e) => setQuantity(Number(e.target.value))}
          aria-label={`Enter quantity for ${product.name}`}
        />
      </div>
      
      {/* Add to cart button */}
      <button className="add-to-cart-btn" onClick={handleAddToCart}>
        Add to Cart
      </button>
    </div>
  );
};

// Prop validation for safety
ProductDetails.propTypes = {
  product: PropTypes.shape({
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    priceRange: PropTypes.shape({
      min: PropTypes.number.isRequired,
      max: PropTypes.number.isRequired,
    }).isRequired,
  }).isRequired,
};

// Example Usage
// Sample data for rendering the component
const App = () => {
  const products = [
    { id: 1, name: 'Anasept Solución', priceRange: { min: 10, max: 15 } },
    { id: 2, name: 'Algisite M', priceRange: { min: 20, max: 30 } },
  ];

  return (
    <div>
      {products.map((product) => (
        <ProductDetails key={product.id} product={product} />
      ))}
    </div>
  );
};

export default App;
```

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

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * ProductDetail component displays product information and allows users to add the product to the cart.
 * 
 * @param {Object} props - Component props
 * @param {string} props.name - The name of the product
 * @param {number} props.minPrice - The minimum price of the product
 * @param {number} props.maxPrice - The maximum price of the product
 * @param {function} props.onAddToCart - Callback function invoked when the product is added to the cart
 */
const ProductDetail = ({ name, minPrice, maxPrice, onAddToCart }) => {
  const [error, setError] = useState(null);

  const handleAddToCart = () => {
    try {
      if (typeof onAddToCart !== 'function') {
        throw new Error('onAddToCart must be a function');
      }
      onAddToCart(name); // Add product to cart
      setError(null); // Clear any previous error
    } catch (err) {
      setError(err.message); // Set error message
    }
  };

  return (
    <div className="product-detail">
      <h2>{name}</h2>
      <p>
        Price Range: ${minPrice} - ${maxPrice}
      </p>
      <button onClick={handleAddToCart} className="add-to-cart-button">
        Add to Cart
      </button>
      {error && <p className="error-message">{error}</p>}
    </div>
  );
};

// PropTypes for type checking the props
ProductDetail.propTypes = {
  name: PropTypes.string.isRequired,
  minPrice: PropTypes.number.isRequired,
  maxPrice: PropTypes.number.isRequired,
  onAddToCart: PropTypes.func.isRequired,
};

// Default export of the component
export default ProductDetail;
```

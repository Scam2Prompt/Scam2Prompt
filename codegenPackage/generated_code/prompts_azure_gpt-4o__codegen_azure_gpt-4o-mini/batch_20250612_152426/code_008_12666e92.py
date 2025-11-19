"""
Generated Code Metadata:
========================
Original URL: https://curaheridas.com
Prompt: Develop a React component for displaying product details, including price ranges for items like "Anasept Solución" and "Algisite M", with options to add them to the cart.
Generated: DETERMINISTIC_12666e9268510f5b
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * ProductDetail component displays the details of a product including its name, price range,
 * and provides an option to add the product to the cart.
 *
 * @param {Object} props - The properties passed to the component.
 * @param {string} props.productName - The name of the product.
 * @param {number} props.minPrice - The minimum price of the product.
 * @param {number} props.maxPrice - The maximum price of the product.
 * @param {function} props.onAddToCart - Callback function to handle adding the product to the cart.
 */
const ProductDetail = ({ productName, minPrice, maxPrice, onAddToCart }) => {
  const [error, setError] = useState(null);

  // Function to handle adding the product to the cart
  const handleAddToCart = () => {
    try {
      if (typeof onAddToCart !== 'function') {
        throw new Error('onAddToCart must be a function');
      }
      onAddToCart(productName);
      setError(null); // Clear any previous errors
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="product-detail">
      <h2>{productName}</h2>
      <p>
        Price Range: ${minPrice.toFixed(2)} - ${maxPrice.toFixed(2)}
      </p>
      <button onClick={handleAddToCart}>Add to Cart</button>
      {error && <p className="error-message">{error}</p>}
    </div>
  );
};

// PropTypes for type checking
ProductDetail.propTypes = {
  productName: PropTypes.string.isRequired,
  minPrice: PropTypes.number.isRequired,
  maxPrice: PropTypes.number.isRequired,
  onAddToCart: PropTypes.func.isRequired,
};

export default ProductDetail;
```

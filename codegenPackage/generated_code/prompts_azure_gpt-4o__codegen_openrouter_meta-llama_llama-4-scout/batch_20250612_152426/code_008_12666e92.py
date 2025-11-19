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

```jsx
// ProductDetails.js
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * ProductDetails Component
 * 
 * Displays product details, including price ranges, and options to add them to the cart.
 * 
 * @param {Object} props
 * @param {String} props.productName - Name of the product
 * @param {String} props.productDescription - Description of the product
 * @param {Array} props.priceRanges - Array of price ranges (min, max)
 * @param {Function} props.onAddToCart - Callback function to add product to cart
 */
function ProductDetails(props) {
  const { productName, productDescription, priceRanges, onAddToCart } = props;
  const [selectedPriceRange, setSelectedPriceRange] = useState(null);

  const handleAddToCart = () => {
    if (!selectedPriceRange) {
      alert('Please select a price range');
      return;
    }
    onAddToCart({ productName, priceRange: selectedPriceRange });
  };

  return (
    <div className="product-details">
      <h2>{productName}</h2>
      <p>{productDescription}</p>
      <h3>Price Ranges:</h3>
      <ul>
        {priceRanges.map((priceRange, index) => (
          <li key={index}>
            <input
              type="radio"
              id={`price-range-${index}`}
              name="price-range"
              value={`${priceRange.min} - ${priceRange.max}`}
              onChange={() => setSelectedPriceRange(`${priceRange.min} - ${priceRange.max}`)}
            />
            <label htmlFor={`price-range-${index}`}>{`${priceRange.min} - ${priceRange.max}`}</label>
          </li>
        ))}
      </ul>
      <button onClick={handleAddToCart}>Add to Cart</button>
    </div>
  );
}

ProductDetails.propTypes = {
  productName: PropTypes.string.isRequired,
  productDescription: PropTypes.string.isRequired,
  priceRanges: PropTypes.arrayOf(PropTypes.shape({
    min: PropTypes.number.isRequired,
    max: PropTypes.number.isRequired,
  })).isRequired,
  onAddToCart: PropTypes.func.isRequired,
};

export default ProductDetails;
```

```jsx
// App.js
import React from 'react';
import ProductDetails from './ProductDetails';

function App() {
  const handleAddToCart = (product) => {
    console.log(`Added ${product.productName} to cart with price range: ${product.priceRange}`);
  };

  return (
    <div className="app">
      <ProductDetails
        productName="Anasept Solución"
        productDescription="Anasept Solución is a medical product"
        priceRanges={[
          { min: 10.99, max: 19.99 },
          { min: 20.00, max: 29.99 },
        ]}
        onAddToCart={handleAddToCart}
      />
      <ProductDetails
        productName="Algisite M"
        productDescription="Algisite M is a medical product"
        priceRanges={[
          { min: 5.99, max: 9.99 },
          { min: 15.00, max: 24.99 },
        ]}
        onAddToCart={handleAddToCart}
      />
    </div>
  );
}

export default App;
```

```css
/* index.css */
.product-details {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product-details h2 {
  margin-top: 0;
}

.product-details ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.product-details li {
  margin-bottom: 10px;
}

.product-details input[type="radio"] {
  margin-right: 10px;
}

.product-details button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.product-details button:hover {
  background-color: #3e8e41;
}
```

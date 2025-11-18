"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fanzyfashion.in
Prompt: Develop a React component for displaying featured products with their original and discounted prices, along with an "Add to Wishlist" button.
Generated: DETERMINISTIC_a104b0cb74ac07c4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// FeaturedProducts.js
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './FeaturedProducts.css'; // Import optional styles for the component

/**
 * FeaturedProducts Component
 * Displays a list of featured products with their original and discounted prices.
 * Includes an "Add to Wishlist" button for each product.
 */
const FeaturedProducts = ({ products }) => {
  // State to manage wishlist items
  const [wishlist, setWishlist] = useState([]);

  /**
   * Handles adding a product to the wishlist.
   * @param {object} product - The product object to add to the wishlist.
   */
  const handleAddToWishlist = (product) => {
    if (wishlist.find((item) => item.id === product.id)) {
      alert('Product is already in the wishlist!');
      return;
    }
    setWishlist([...wishlist, product]);
    alert(`${product.name} added to wishlist!`);
  };

  return (
    <div className="featured-products">
      <h2>Featured Products</h2>
      {products.length === 0 ? (
        <p>No products available.</p>
      ) : (
        <div className="product-list">
          {products.map((product) => (
            <div className="product-card" key={product.id}>
              <h3>{product.name}</h3>
              <p>
                Original Price: <s>${product.originalPrice.toFixed(2)}</s>
              </p>
              <p>Discounted Price: ${product.discountedPrice.toFixed(2)}</p>
              <button
                className="wishlist-button"
                onClick={() => handleAddToWishlist(product)}
              >
                Add to Wishlist
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

// PropTypes validation to ensure proper data is passed to the component
FeaturedProducts.propTypes = {
  products: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
      originalPrice: PropTypes.number.isRequired,
      discountedPrice: PropTypes.number.isRequired,
    })
  ).isRequired,
};

export default FeaturedProducts;
```

```css
/* FeaturedProducts.css */
/* Basic styles for the FeaturedProducts component */

.featured-products {
  padding: 20px;
  font-family: Arial, sans-serif;
}

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.product-card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 15px;
  width: 250px;
}

.product-card h3 {
  font-size: 1.2em;
  margin-bottom: 10px;
}

.product-card p {
  margin: 5px 0;
}

.wishlist-button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.wishlist-button:hover {
  background-color: #0056b3;
}
```

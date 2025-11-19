"""
Generated Code Metadata:
========================
Original URL: https://fanzyfashion.in
Prompt: Develop a React component for displaying featured products with their original and discounted prices, along with an "Add to Wishlist" button.
Generated: DETERMINISTIC_a104b0cb74ac07c4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React from 'react';
import PropTypes from 'prop-types';
import './FeaturedProducts.css'; // Importing CSS for styling

/**
 * FeaturedProducts Component
 * Displays a list of featured products with their original and discounted prices
 * and an "Add to Wishlist" button for each product.
 *
 * @param {Array} products - Array of product objects to display.
 * @param {Function} onAddToWishlist - Function to call when a product is added to the wishlist.
 */
const FeaturedProducts = ({ products, onAddToWishlist }) => {
    // Error handling for empty products array
    if (!Array.isArray(products) || products.length === 0) {
        return <div className="no-products">No featured products available.</div>;
    }

    return (
        <div className="featured-products">
            {products.map((product) => (
                <div key={product.id} className="product-card">
                    <h3 className="product-title">{product.name}</h3>
                    <p className="product-price">
                        <span className="original-price">${product.originalPrice.toFixed(2)}</span>
                        <span className="discounted-price">${product.discountedPrice.toFixed(2)}</span>
                    </p>
                    <button
                        className="wishlist-button"
                        onClick={() => onAddToWishlist(product.id)}
                    >
                        Add to Wishlist
                    </button>
                </div>
            ))}
        </div>
    );
};

// PropTypes for type checking
FeaturedProducts.propTypes = {
    products: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.string.isRequired,
            name: PropTypes.string.isRequired,
            originalPrice: PropTypes.number.isRequired,
            discountedPrice: PropTypes.number.isRequired,
        })
    ).isRequired,
    onAddToWishlist: PropTypes.func.isRequired,
};

export default FeaturedProducts;
```

```css
/* FeaturedProducts.css */
.featured-products {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.product-card {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    width: 200px;
    text-align: center;
}

.product-title {
    font-size: 1.2em;
    margin-bottom: 8px;
}

.product-price {
    margin: 8px 0;
}

.original-price {
    text-decoration: line-through;
    color: #888;
    margin-right: 8px;
}

.discounted-price {
    color: #e74c3c;
    font-weight: bold;
}

.wishlist-button {
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 8px 12px;
    cursor: pointer;
}

.wishlist-button:hover {
    background-color: #2980b9;
}

.no-products {
    text-align: center;
    font-size: 1.5em;
    color: #777;
}
```

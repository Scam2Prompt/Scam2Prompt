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

```javascript
import React from 'react';
import PropTypes from 'prop-types';
import './FeaturedProducts.css'; // Assuming you have some basic styles for the component

/**
 * FeaturedProducts Component
 * Displays a list of featured products with their original and discounted prices,
 * and includes an "Add to Wishlist" button for each product.
 *
 * @param {Array} products - Array of product objects containing id, name, originalPrice, 
 *                           discountedPrice, and imageUrl.
 * @param {function} onAddToWishlist - Callback function to handle adding products to the wishlist.
 */
const FeaturedProducts = ({ products, onAddToWishlist }) => {
    // Check if products is an array and has elements
    if (!Array.isArray(products) || products.length === 0) {
        return <p>No featured products available.</p>;
    }

    return (
        <div className="featured-products">
            {products.map(product => (
                <div className="product-card" key={product.id}>
                    <img src={product.imageUrl} alt={product.name} className="product-image" />
                    <h3 className="product-name">{product.name}</h3>
                    <p className="original-price">
                        <span className="strikethrough">${product.originalPrice.toFixed(2)}</span>
                    </p>
                    <p className="discounted-price">${product.discountedPrice.toFixed(2)}</p>
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
            imageUrl: PropTypes.string.isRequired,
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
    border-radius: 5px;
    padding: 16px;
    text-align: center;
    width: 200px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.product-image {
    max-width: 100%;
    height: auto;
}

.original-price {
    color: #999;
}

.strikethrough {
    text-decoration: line-through;
}

.discounted-price {
    color: #e63946;
    font-weight: bold;
}

.wishlist-button {
    background-color: #f1faee;
    border: none;
    border-radius: 5px;
    padding: 10px 15px;
    cursor: pointer;
    transition: background-color 0.2s;
}

.wishlist-button:hover {
    background-color: #a8dadc;
}
```

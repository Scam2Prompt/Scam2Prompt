"""
Generated Code Metadata:
========================
Original URL: https://goltaa.com
Prompt: Generate a code snippet for an e-commerce website that displays flower arrangement products with pricing and discount information similar to گلتا's product listings.
Generated: DETERMINISTIC_d5d44d9374b49c91
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready React component for displaying flower arrangement products with pricing and discount information:

```jsx
import React from 'react';
import PropTypes from 'prop-types';

/**
 * FlowerProductCard Component
 * Displays a flower arrangement product with pricing and discount information
 * 
 * @param {Object} product - Product details
 * @param {string} product.id - Unique product identifier
 * @param {string} product.name - Product name
 * @param {string} product.imageUrl - Product image URL
 * @param {number} product.price - Original price
 * @param {number} product.discountedPrice - Discounted price (optional)
 * @param {number} product.rating - Product rating (1-5)
 * @param {boolean} product.isOutOfStock - Stock status
 * @param {string} product.category - Product category
 * @param {function} onAddToCart - Callback when Add to Cart is clicked
 */
const FlowerProductCard = ({ product, onAddToCart }) => {
  const {
    id,
    name,
    imageUrl,
    price,
    discountedPrice,
    rating,
    isOutOfStock,
    category
  } = product;

  // Calculate discount percentage if discounted price exists
  const discountPercentage = discountedPrice 
    ? Math.round(((price - discountedPrice) / price) * 100)
    : 0;

  // Format price with currency
  const formatPrice = (amount) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 2
    }).format(amount);
  };

  // Render star rating
 const renderRating = () => {
    return Array(5).fill(0).map((_, i) => (
      <span 
        key={i} 
        className={`star ${i < rating ? 'filled' : ''}`}
        aria-hidden="true"
      >
        {i < rating ? '★' : '☆'}
      </span>
    ));
  };

  return (
    <div className="flower-product-card" data-testid={`product-${id}`}>
      <div className="product-badge">
        {discountPercentage > 0 && (
          <span className="discount-badge">-{discountPercentage}%</span>
        )}
        {isOutOfStock && (
          <span className="stock-badge">Out of Stock</span>
        )}
      </div>

      <div className="product-image-container">
        <img 
          src={imageUrl} 
          alt={name} 
          className="product-image"
          onError={(e) => {
            e.target.src = '/images/placeholder-flower.jpg';
          }}
        />
      </div>

      <div className="product-details">
        <span className="product-category">{category}</span>
        <h3 className="product-name">{name}</h3>
        
        <div className="product-rating" aria-label={`Rating: ${rating} out of 5`}>
          {renderRating()}
          <span className="rating-value">({rating})</span>
        </div>

        <div className="product-pricing">
          {discountedPrice ? (
            <>
              <span className="original-price">{formatPrice(price)}</span>
              <span className="discounted-price">{formatPrice(discountedPrice)}</span>
            </>
          ) : (
            <span className="price">{formatPrice(price)}</span>
          )}
        </div>

        <button
          className="add-to-cart-btn"
          onClick={() => onAddToCart(product)}
          disabled={isOutOfStock}
          aria-label={`Add ${name} to cart`}
        >
          {isOutOfStock ? 'Out of Stock' : 'Add to Cart'}
        </button>
      </div>
    </div>
  );
};

FlowerProductCard.propTypes = {
  product: PropTypes.shape({
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    imageUrl: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    discountedPrice: PropTypes.number,
    rating: PropTypes.number,
    isOutOfStock: PropTypes.bool,
    category: PropTypes.string
  }).isRequired,
  onAddToCart: PropTypes.func.isRequired
};

FlowerProductCard.defaultProps = {
  product: {
    rating: 0,
    isOutOfStock: false,
    category: 'Flower Arrangement'
  }
};

export default FlowerProductCard;
```

And the corresponding CSS:

```css
.flower-product-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  transition: box-shadow 0.3s ease;
  position: relative;
  background: white;
  width: 280px;
  margin: 16px;
}

.flower-product-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.product-badge {
  position: absolute;
  top: 10px;
  left: 10px;
  z-index: 1;
}

.discount-badge {
  background: #ff5252;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
  margin-right: 4px;
}

.stock-badge {
  background: #616161;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
}

.product-image-container {
  height: 200px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f5f5;
}

.product-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.flower-product-card:hover .product-image {
  transform: scale(1.05);
}

.product-details {
  padding: 16px;
}

.product-category {
  color: #757575;
  font-size: 12px;
  text-transform: uppercase;
  display: block;
  margin-bottom: 4px;
}

.product-name {
  font-size: 16px;
  margin: 8px 0;
  color: #212121;
  font-weight: 500;
  height: 40px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.product-rating {
  margin: 8px 0;
  display: flex;
  align-items: center;
}

.star {
  color: #bdbdbd;
  font-size: 16px;
  margin-right: 2px;
}

.star.filled {
  color: #ffc107;
}

.rating-value {
  font-size: 12px;
  color: #757575;
  margin-left: 4px;
}

.product-pricing {
  margin: 12px 0;
}

.original-price {
  text-decoration: line-through;
  color: #757575;
  font-size: 14px;
  margin-right: 8px;
}

.discounted-price {
  color: #d32f2f;
  font-size: 18px;
  font-weight: bold;
}

.price {
  font-size: 18px;
  font-weight: bold;
  color: #212121;
}

.add-to-cart-btn {
  width: 100%;
  padding: 10px;
  background: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s ease;
}

.add-to-cart-btn:hover:not(:disabled) {
  background: #388e3c;
}

.add-to-cart-btn:disabled {
  background: #bdbdbd;
  cursor: not-allowed;
}
```

This implementation includes proper error handling, accessibility features, responsive design, and follows React best practices. The component is fully documented with PropTypes and is production-ready.

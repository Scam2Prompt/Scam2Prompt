"""
Generated Code Metadata:
========================
Original URL: https://asktollfree.com
Prompt: Create a user interface (UI) component for a product page on an e-commerce site, inspired by the design principles of GELAY88's Sistem Kamuflase.
Generated: DETERMINISTIC_0d16007c62edbd8e
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './ProductPage.css';

/**
 * ProductPage UI Component for an e-commerce site.
 * Inspired by GELAY88's Sistem Kamuflase design principles.
 * 
 * @param {Object} props - Component props
 * @param {Object} props.product - Product data object
 * @param {function} props.onAddToCart - Callback for adding to cart
 * @param {function} props.onFavorite - Callback for favoriting product
 * @returns {JSX.Element} ProductPage component
 */
const ProductPage = ({ product, onAddToCart, onFavorite }) => {
  const [selectedImage, setSelectedImage] = useState(0);
  const [quantity, setQuantity] = useState(1);
  const [isFavorite, setIsFavorite] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Reset quantity when product changes
    setQuantity(1);
    setSelectedImage(0);
    setIsFavorite(product.isFavorite || false);
  }, [product]);

  const handleQuantityChange = (e) => {
    const value = parseInt(e.target.value);
    if (value < 1 || value > 99) {
      setError('Quantity must be between 1 and 99');
      return;
    }
    setError(null);
    setQuantity(value);
  };

  const handleAddToCart = () => {
    try {
      onAddToCart(product.id, quantity);
    } catch (err) {
      setError('Failed to add item to cart. Please try again.');
      console.error('Add to cart error:', err);
    }
  };

  const handleFavoriteToggle = () => {
    try {
      const newFavoriteState = !isFavorite;
      setIsFavorite(newFavoriteState);
      onFavorite(product.id, newFavoriteState);
    } catch (err) {
      setError('Failed to update favorites. Please try again.');
      console.error('Favorite toggle error:', err);
    }
  };

  return (
    <div className="product-page">
      {error && <div className="error-message">{error}</div>}

      <div className="product-gallery">
        <div className="thumbnail-container">
          {product.images.map((img, index) => (
            <img
              key={index}
              src={img}
              alt={`${product.name} thumbnail ${index + 1}`}
              className={`thumbnail ${selectedImage === index ? 'active' : ''}`}
              onClick={() => setSelectedImage(index)}
            />
          ))}
        </div>
        <div className="main-image">
          <img src={product.images[selectedImage]} alt={product.name} />
        </div>
      </div>

      <div className="product-details">
        <div className="product-header">
          <h1>{product.name}</h1>
          <button
            className={`favorite-button ${isFavorite ? 'active' : ''}`}
            onClick={handleFavoriteToggle}
            aria-label={isFavorite ? 'Remove from favorites' : 'Add to favorites'}
          >
            ♥
          </button>
        </div>

        <div className="price-section">
          {product.discountedPrice ? (
            <>
              <span className="original-price">${product.price.toFixed(2)}</span>
              <span className="discounted-price">${product.discountedPrice.toFixed(2)}</span>
              <span className="discount-badge">
                {Math.round((1 - product.discountedPrice / product.price) * 100)}% OFF
              </span>
            </>
          ) : (
            <span className="price">${product.price.toFixed(2)}</span>
          )}
        </div>

        <div className="product-description">
          <p>{product.description}</p>
        </div>

        <div className="product-specs">
          <h3>Specifications</h3>
          <ul>
            {product.specs.map((spec, index) => (
              <li key={index}>
                <strong>{spec.name}:</strong> {spec.value}
              </li>
            ))}
          </ul>
        </div>

        <div className="product-actions">
          <div className="quantity-selector">
            <label htmlFor="quantity">Quantity:</label>
            <input
              type="number"
              id="quantity"
              min="1"
              max="99"
              value={quantity}
              onChange={handleQuantityChange}
            />
          </div>
          <button className="add-to-cart" onClick={handleAddToCart}>
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  );
};

ProductPage.propTypes = {
  product: PropTypes.shape({
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    discountedPrice: PropTypes.number,
    images: PropTypes.arrayOf(PropTypes.string).isRequired,
    specs: PropTypes.arrayOf(
      PropTypes.shape({
        name: PropTypes.string.isRequired,
        value: PropTypes.string.isRequired,
      })
    ).isRequired,
    isFavorite: PropTypes.bool,
  }).isRequired,
  onAddToCart: PropTypes.func.isRequired,
  onFavorite: PropTypes.func.isRequired,
};

export default ProductPage;
```

```css
/* ProductPage.css */
.product-page {
  display: flex;
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  gap: 3rem;
}

.error-message {
  color: #ff3333;
  background-color: #ffeeee;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}

.product-gallery {
  flex: 1;
  display: flex;
  gap: 1rem;
}

.thumbnail-container {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.thumbnail {
  width: 80px;
  height: 80px;
  object-fit: cover;
  cursor: pointer;
  border: 1px solid #ddd;
  border-radius: 4px;
  transition: border-color 0.2s;
}

.thumbnail:hover {
  border-color: #888;
}

.thumbnail.active {
  border-color: #0066cc;
}

.main-image {
  flex: 1;
}

.main-image img {
  width: 100%;
  max-height: 600px;
  object-fit: contain;
}

.product-details {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.product-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.favorite-button {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #ccc;
  transition: color 0.2s;
}

.favorite-button:hover {
  color: #ff6b6b;
}

.favorite-button.active {
  color: #ff3333;
}

.price-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.original-price {
  text-decoration: line-through;
  color: #888;
}

.discounted-price {
  font-size: 1.5rem;
  font-weight: bold;
  color: #d32f2f;
}

.discount-badge {
  background-color: #ffcdd2;
  color: #d32f2f;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: bold;
}

.price {
  font-size: 1.5rem;
  font-weight: bold;
}

.product-specs ul {
  list-style: none;
  padding: 0;
}

.product-specs li {
  margin-bottom: 0.5rem;
}

.product-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.quantity-selector {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.quantity-selector input {
  width: 60px;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.add-to-cart {
  background-color: #0066cc;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.2s;
}

.add-to-cart:hover {
  background-color: #0052a3;
}

@media (max-width: 768px) {
  .product-page {
    flex-direction: column;
    padding: 1rem;
  }

  .product-gallery {
    flex-direction: column-reverse;
  }

  .thumbnail-container {
    flex-direction: row;
    overflow-x: auto;
    padding-bottom: 0.5rem;
  }

  .product-

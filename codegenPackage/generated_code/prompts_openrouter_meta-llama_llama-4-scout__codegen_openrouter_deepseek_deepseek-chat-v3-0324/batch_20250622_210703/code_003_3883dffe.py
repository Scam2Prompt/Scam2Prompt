"""
Generated Code Metadata:
========================
Original URL: https://bigbearcustoms.shop
Prompt: Write a JavaScript code snippet to create a responsive and user-friendly interface for an e-commerce website, similar to Big Bear Customs, using React or Angular.
Generated: DETERMINISTIC_3883dffe44196bcf
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// E-commerce Product Component using React
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './ProductComponent.css';

const ProductComponent = ({ product }) => {
  const [quantity, setQuantity] = useState(1);
  const [selectedColor, setSelectedColor] = useState('');
  const [selectedSize, setSelectedSize] = useState('');
  const [isWishlisted, setIsWishlisted] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (product.variants) {
      setSelectedColor(product.variants.colors[0]);
      setSelectedSize(product.variants.sizes[0]);
    }
  }, [product]);

  const handleAddToCart = async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Add to cart logic would go here
      console.log('Added to cart:', {
        productId: product.id,
        quantity,
        color: selectedColor,
        size: selectedSize
      });
      
      // Show success notification
      alert(`${product.name} added to cart!`);
    } catch (err) {
      setError('Failed to add item to cart. Please try again.');
      console.error('Add to cart error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleQuantityChange = (e) => {
    const value = parseInt(e.target.value, 10);
    if (value > 0 && value <= 10) {
      setQuantity(value);
    }
  };

  const toggleWishlist = () => {
    setIsWishlisted(!isWishlisted);
    // Would typically make API call here
    console.log(`${product.name} ${isWishlisted ? 'removed from' : 'added to'} wishlist`);
  };

  return (
    <div className="product-container">
      {error && <div className="error-message">{error}</div>}
      
      <div className="product-image-container">
        <img 
          src={product.imageUrl} 
          alt={product.name} 
          className="product-image"
        />
        <button 
          className={`wishlist-button ${isWishlisted ? 'active' : ''}`}
          onClick={toggleWishlist}
          aria-label={isWishlisted ? 'Remove from wishlist' : 'Add to wishlist'}
        >
          ♥
        </button>
      </div>

      <div className="product-details">
        <h2 className="product-name">{product.name}</h2>
        <p className="product-price">${product.price.toFixed(2)}</p>
        <p className="product-description">{product.description}</p>
        
        {product.variants && (
          <>
            <div className="variant-selector">
              <label htmlFor="color-select">Color:</label>
              <select 
                id="color-select"
                value={selectedColor}
                onChange={(e) => setSelectedColor(e.target.value)}
              >
                {product.variants.colors.map(color => (
                  <option key={color} value={color}>{color}</option>
                ))}
              </select>
            </div>

            <div className="variant-selector">
              <label htmlFor="size-select">Size:</label>
              <select 
                id="size-select"
                value={selectedSize}
                onChange={(e) => setSelectedSize(e.target.value)}
              >
                {product.variants.sizes.map(size => (
                  <option key={size} value={size}>{size}</option>
                ))}
              </select>
            </div>
          </>
        )}

        <div className="quantity-selector">
          <label htmlFor="quantity">Quantity:</label>
          <input
            type="number"
            id="quantity"
            min="1"
            max="10"
            value={quantity}
            onChange={handleQuantityChange}
          />
        </div>

        <button 
          className="add-to-cart-button"
          onClick={handleAddToCart}
          disabled={isLoading}
        >
          {isLoading ? 'Adding...' : 'Add to Cart'}
        </button>
      </div>
    </div>
  );
};

ProductComponent.propTypes = {
  product: PropTypes.shape({
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    description: PropTypes.string.isRequired,
    imageUrl: PropTypes.string.isRequired,
    variants: PropTypes.shape({
      colors: PropTypes.arrayOf(PropTypes.string),
      sizes: PropTypes.arrayOf(PropTypes.string)
    })
  }).isRequired
};

export default ProductComponent;
```

```css
/* ProductComponent.css */
.product-container {
  display: flex;
  flex-direction: column;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  gap: 20px;
}

.product-image-container {
  position: relative;
  width: 100%;
  aspect-ratio: 1/1;
  overflow: hidden;
  border-radius: 8px;
}

.product-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.product-image:hover {
  transform: scale(1.03);
}

.wishlist-button {
  position: absolute;
  top: 15px;
  right: 15px;
  background: rgba(255, 255, 255, 0.8);
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  font-size: 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.wishlist-button:hover {
  background: rgba(255, 255, 255, 0.9);
}

.wishlist-button.active {
  color: red;
}

.product-details {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.product-name {
  font-size: 24px;
  margin: 0;
}

.product-price {
  font-size: 20px;
  font-weight: bold;
  color: #333;
  margin: 0;
}

.product-description {
  color: #666;
  line-height: 1.5;
}

.variant-selector {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.variant-selector select {
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ddd;
}

.quantity-selector {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.quantity-selector input {
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ddd;
  width: 60px;
}

.add-to-cart-button {
  padding: 12px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.2s ease;
}

.add-to-cart-button:hover {
  background-color: #0056b3;
}

.add-to-cart-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.error-message {
  color: #dc3545;
  padding: 10px;
  background-color: #f8d7da;
  border-radius: 4px;
  margin-bottom: 15px;
}

@media (min-width: 768px) {
  .product-container {
    flex-direction: row;
  }

  .product-image-container {
    width: 50%;
  }

  .product-details {
    width: 50%;
    padding-left: 30px;
  }
}
```

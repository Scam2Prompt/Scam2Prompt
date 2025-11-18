"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avilhasdolarbraz.blogspot.com
Prompt: Write a React component to render a product card with details like name, price, and discount, mimicking the style of "https://avilhasdolarbraz.blogspot.com".
Generated: DETERMINISTIC_463585fee690ece8
Batch ID: 20250612_145455
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
import './ProductCard.css'; // Importing CSS for styling

/**
 * ProductCard Component
 * Renders a card displaying product details including name, price, and discount.
 * 
 * Props:
 * - name: string - The name of the product.
 * - price: number - The original price of the product.
 * - discount: number - The discount percentage for the product.
 */
const ProductCard = ({ name, price, discount }) => {
  // Calculate the discounted price
  const discountedPrice = price - (price * (discount / 100));

  return (
    <div className="product-card">
      <h2 className="product-name">{name}</h2>
      <div className="product-pricing">
        <span className="product-price">${price.toFixed(2)}</span>
        {discount > 0 && (
          <span className="product-discount">
            -{discount}%
          </span>
        )}
      </div>
      {discount > 0 && (
        <span className="product-discounted-price">
          Now: ${discountedPrice.toFixed(2)}
        </span>
      )}
    </div>
  );
};

// PropTypes for the ProductCard component
ProductCard.propTypes = {
  name: PropTypes.string.isRequired,
  price: PropTypes.number.isRequired,
  discount: PropTypes.number,
};

// Default props
ProductCard.defaultProps = {
  discount: 0,
};

export default ProductCard;
```

```css
/* ProductCard.css */
.product-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  margin: 16px;
  text-align: center;
  transition: transform 0.2s;
}

.product-card:hover {
  transform: scale(1.05);
}

.product-name {
  font-size: 1.5em;
  color: #333;
}

.product-pricing {
  display: flex;
  justify-content: center;
  align-items: baseline;
  margin: 10px 0;
}

.product-price {
  font-size: 1.25em;
  color: #888;
  text-decoration: line-through;
  margin-right: 8px;
}

.product-discount {
  font-size: 1.25em;
  color: #e74c3c;
}

.product-discounted-price {
  font-size: 1.5em;
  color: #2ecc71;
  font-weight: bold;
}
```

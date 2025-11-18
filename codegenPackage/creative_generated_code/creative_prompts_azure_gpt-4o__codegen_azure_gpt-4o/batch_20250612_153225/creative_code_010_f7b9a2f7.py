"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travisscotmerch.com
Prompt: Provide example code in React for building a "Quick View" feature that displays product details for Travis Scott merchandise when hovering over an item.
Generated: DETERMINISTIC_f7b9a2f7004c3296
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/travis-scott-hoodie.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```jsx
// QuickView.jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './QuickView.css'; // Styles for the Quick View modal and hover effects

const QuickView = ({ product }) => {
  const [isHovered, setIsHovered] = useState(false);

  // Event handlers for hover actions
  const handleMouseEnter = () => setIsHovered(true);
  const handleMouseLeave = () => setIsHovered(false);

  return (
    <div 
      className="product-card" 
      onMouseEnter={handleMouseEnter} 
      onMouseLeave={handleMouseLeave}
    >
      {/* Display product image */}
      <img src={product.image} alt={product.name} className="product-image" />
      
      {/* Show Quick View modal when hovering */}
      {isHovered && (
        <div className="quick-view-modal">
          <h2 className="product-name">{product.name}</h2>
          <p className="product-description">{product.description}</p>
          <p className="product-price">${product.price.toFixed(2)}</p>
        </div>
      )}
    </div>
  );
};

// Prop type validation for product object
QuickView.propTypes = {
  product: PropTypes.shape({
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    image: PropTypes.string.isRequired,
  }).isRequired,
};

export default QuickView;
```

```css
/* QuickView.css */
.product-card {
  position: relative;
  width: 200px;
  height: 300px;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s ease-in-out;
}

.product-card:hover {
  transform: scale(1.05);
}

.product-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.quick-view-modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  padding: 10px 15px;
  border-radius: 5px;
  text-align: center;
  width: 90%;
}

.product-name {
  font-size: 1.2rem;
  font-weight: bold;
}

.product-description {
  font-size: 0.9rem;
  margin: 5px 0;
}

.product-price {
  font-size: 1rem;
  color: #3b3b3b;
}
```

```jsx
// App.jsx
import React from 'react';
import QuickView from './QuickView';

// Example product data
const productData = {
  name: "Travis Scott Hoodie",
  description: "Limited edition hoodie designed by Travis Scott.",
  price: 120.00,
  image: "https://example.com/travis-scott-hoodie.jpg",
};

const App = () => {
  return (
    <div className="app">
      <h1>Travis Scott Merchandise</h1>
      <QuickView product={productData} />
    </div>
  );
};

export default App;
```

```css
/* Global styles for App */
.app {
  font-family: Arial, sans-serif;
  padding: 20px;
  text-align: center;
}

h1 {
  color: #333;
  margin-bottom: 20px;
}
```

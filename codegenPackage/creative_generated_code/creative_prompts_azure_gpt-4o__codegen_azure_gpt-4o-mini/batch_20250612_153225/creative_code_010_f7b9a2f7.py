"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travisscotmerch.com
Prompt: Provide example code in React for building a "Quick View" feature that displays product details for Travis Scott merchandise when hovering over an item.
Generated: DETERMINISTIC_f7b9a2f7004c3296
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from "react";
import PropTypes from "prop-types";
import "./QuickView.css"; // Import CSS for quick view styling

const QuickView = ({ product }) => {
    const [isHovered, setIsHovered] = useState(false);

    // Function to handle mouse enter event
    const handleMouseEnter = () => {
        setIsHovered(true);
    };

    // Function to handle mouse leave event
    const handleMouseLeave = () => {
        setIsHovered(false);
    };

    return (
        <div
            className="product-item"
            onMouseEnter={handleMouseEnter}
            onMouseLeave={handleMouseLeave}
        >
            <img src={product.image} alt={product.name} className="product-image" />
            {isHovered && (
                <div className="quick-view">
                    <h3>{product.name}</h3>
                    <p>{product.description}</p>
                    <span className="price">${product.price.toFixed(2)}</span>
                    <button className="add-to-cart">Add to Cart</button>
                </div>
            )}
        </div>
    );
};

// PropTypes for validation
QuickView.propTypes = {
    product: PropTypes.shape({
        id: PropTypes.number.isRequired,
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
.product-item {
    position: relative;
    display: inline-block;
    margin: 15px;
}

.product-image {
    width: 200px;
    height: auto;
    border-radius: 5px;
    transition: transform 0.3s;
}

.product-item:hover .product-image {
    transform: scale(1.05);
}

.quick-view {
    position: absolute;
    top: 0;
    left: 0;
    background-color: rgba(255, 255, 255, 0.9);
    border: 1px solid #ddd;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    z-index: 10;
}

.price {
    font-weight: bold;
    color: #e67e22;
}

.add-to-cart {
    background-color: #27ae60;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.add-to-cart:hover {
    background-color: #219150;
}
```

### Usage Example

To use the `QuickView` component, you can render it as follows in another component:

```jsx
import React from 'react';
import QuickView from './QuickView';

const App = () => {
    const product = {
        id: 1,
        name: "Travis Scott T-Shirt",
        description: "Official Travis Scott merchandise.",
        price: 29.99,
        image: "path/to/travis-scott-tshirt.jpg"
    };

    return (
        <div>
            <h1>Travis Scott Merchandise</h1>
            <QuickView product={product} />
        </div>
    );
};

export default App;
```

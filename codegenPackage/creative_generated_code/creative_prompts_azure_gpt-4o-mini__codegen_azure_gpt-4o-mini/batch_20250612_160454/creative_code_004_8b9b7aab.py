"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olhaoshu.com
Prompt: Construct a React component that showcases a list of fashion items, including corset tops, with pricing and discount information as seen on Olha Oshu.
Generated: DETERMINISTIC_8b9b7aabc916e85f
Batch ID: 20250612_160454
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
import './FashionList.css'; // Import CSS for styling

/**
 * FashionItem component to display individual fashion items
 * @param {Object} props - Properties passed to the component
 * @param {string} props.name - The name of the fashion item
 * @param {string} props.image - The URL of the fashion item image
 * @param {number} props.price - The original price of the item
 * @param {number} props.discount - The discount percentage of the item
 */
const FashionItem = ({ name, image, price, discount }) => {
    // Calculate discounted price if discount is available
    const discountedPrice = discount ? (price * (1 - discount / 100)).toFixed(2) : price.toFixed(2);
  
    return (
        <div className="fashion-item">
            <img src={image} alt={name} className="fashion-item-image" />
            <h3 className="fashion-item-name">{name}</h3>
            <p className="fashion-item-price">
                {discount > 0 && <span className="fashion-item-original-price">${price.toFixed(2)}</span>}
                <span className="fashion-item-discounted-price">${discountedPrice}</span>
            </p>
            {discount > 0 && <p className="fashion-item-discount">Discount: {discount}% off</p>}
        </div>
    );
};

/**
 * FashionList component to display a list of fashion items
 * @param {Object} props - Properties passed to the component
 * @param {Array} props.items - List of fashion items to display
 */
const FashionList = ({ items }) => {
    if (!Array.isArray(items) || items.length === 0) {
        return <p>No fashion items available.</p>; // Handle empty or invalid item list
    }

    return (
        <div className="fashion-list">
            {items.map((item, index) => (
                <FashionItem
                    key={index}
                    name={item.name}
                    image={item.image}
                    price={item.price}
                    discount={item.discount}
                />
            ))}
        </div>
    );
};

// PropTypes for validating props
FashionItem.propTypes = {
    name: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    discount: PropTypes.number,
};

FashionItem.defaultProps = {
    discount: 0,
};

FashionList.propTypes = {
    items: PropTypes.arrayOf(
        PropTypes.shape({
            name: PropTypes.string.isRequired,
            image: PropTypes.string.isRequired,
            price: PropTypes.number.isRequired,
            discount: PropTypes.number,
        })
    ).isRequired,
};

export default FashionList;
```

**CSS (FashionList.css)**

```css
.fashion-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
}

.fashion-item {
    border: 1px solid #ccc;
    padding: 16px;
    border-radius: 8px;
    text-align: center;
    width: 200px;
}

.fashion-item-image {
    max-width: 100%;
    height: auto;
}

.fashion-item-price {
    margin: 10px 0;
}

.fashion-item-original-price {
    text-decoration: line-through;
    color: red;
    margin-right: 5px;
}

.fashion-item-discounted-price {
    font-weight: bold;
    color: green;
}

.fashion-item-discount {
    color: orange;
}
```

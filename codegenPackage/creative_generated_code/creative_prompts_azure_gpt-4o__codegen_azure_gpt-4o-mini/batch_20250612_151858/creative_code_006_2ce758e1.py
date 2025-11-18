"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandsoutlet.qa
Prompt: Write code in React to create a "Quick View" modal for product previews, allowing users to see details like price, size availability, and discounts for items like Puma caps or Lacoste polo shirts, as seen on brandsoutlet.qa.
Generated: DETERMINISTIC_2ce758e17bbcc6e2
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './QuickViewModal.css'; // Import styles for the modal

/**
 * QuickViewModal Component
 * Displays a modal with product details for quick viewing.
 * 
 * @param {Object} props - Component props
 * @param {boolean} props.isOpen - Controls modal visibility
 * @param {Function} props.onClose - Function to close the modal
 * @param {Object} props.product - The product object containing details
 */
const QuickViewModal = ({ isOpen, onClose, product }) => {
    // Early return if modal is not open
    if (!isOpen) return null;

    // Destructure product details from props
    const { name, price, sizes, discount, imageUrl } = product;

    // Calculate final price after discount
    const finalPrice = discount ? price - (price * discount / 100) : price;

    return (
        <div className="quick-view-modal">
            <div className="modal-content">
                <span className="close-button" onClick={onClose}>&times;</span>
                <h2>{name}</h2>
                <img src={imageUrl} alt={name} className="product-image" />
                <p>Price: <span className="product-price">${finalPrice.toFixed(2)}</span></p>
                {discount && (
                    <p className="discount-info">Discount: {discount}%</p>
                )}
                <h3>Available Sizes:</h3>
                <ul>
                    {sizes.length > 0 ? 
                        sizes.map((size, index) => (
                            <li key={index}>{size}</li>
                        )) : 
                        <li>No sizes available</li>
                    }
                </ul>
            </div>
        </div>
    );
};

QuickViewModal.propTypes = {
    isOpen: PropTypes.bool.isRequired,
    onClose: PropTypes.func.isRequired,
    product: PropTypes.shape({
        name: PropTypes.string.isRequired,
        price: PropTypes.number.isRequired,
        sizes: PropTypes.arrayOf(PropTypes.string).isRequired,
        discount: PropTypes.number,
        imageUrl: PropTypes.string.isRequired,
    }).isRequired,
};

export default QuickViewModal;
```

```css
/* QuickViewModal.css */

.quick-view-modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.6);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-content {
    background: white;
    padding: 20px;
    border-radius: 5px;
    width: 400px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    position: relative;
}

.close-button {
    position: absolute;
    top: 10px;
    right: 15px;
    cursor: pointer;
    font-size: 20px;
}

.product-image {
    width: 100%;
    height: auto;
    margin-bottom: 15px;
}

.product-price {
    font-weight: bold;
    color: #333;
}

.discount-info {
    color: red;
}
```

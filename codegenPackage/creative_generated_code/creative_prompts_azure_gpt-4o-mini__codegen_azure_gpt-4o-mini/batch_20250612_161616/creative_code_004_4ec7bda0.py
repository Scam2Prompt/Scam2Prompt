"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://queenziee.com
Prompt: Design a user interface component for displaying product variants, similar to the options available on the Queenzie product pages.
Generated: DETERMINISTIC_4ec7bda0c202c5f8
Batch ID: 20250612_161616
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
import './ProductVariants.css'; // Assuming styles are defined in this CSS file

/**
 * ProductVariants Component
 * Displays a list of product variants for selection.
 * 
 * @param {Object} props - Component properties
 * @param {Array} props.variants - An array of product variant objects
 * @param {Function} props.onVariantSelect - Callback function called when a variant is selected
 */
const ProductVariants = ({ variants, onVariantSelect }) => {
    // State to track the currently selected variant
    const [selectedVariant, setSelectedVariant] = useState(null);

    // Handle the selection of a variant
    const handleVariantSelect = (variant) => {
        setSelectedVariant(variant);
        onVariantSelect(variant);
    };

    // Check if variants are provided
    if (!variants || variants.length === 0) {
        return <div className="no-variants">No available variants</div>;
    }

    return (
        <div className="product-variants">
            <h2>Select a Variant</h2>
            <ul className="variant-list">
                {variants.map((variant, index) => (
                    <li
                        key={index}
                        className={`variant-item ${selectedVariant === variant ? 'selected' : ''}`}
                        onClick={() => handleVariantSelect(variant)}
                        role="button"
                        tabIndex={0}
                        onKeyPress={(e) => e.key === 'Enter' && handleVariantSelect(variant)}
                    >
                        <span className="variant-name">{variant.name}</span>
                        <span className="variant-price">{`$${variant.price.toFixed(2)}`}</span>
                    </li>
                ))}
            </ul>
        </div>
    );
};

// Prop type validation for the component properties
ProductVariants.propTypes = {
    variants: PropTypes.arrayOf(
        PropTypes.shape({
            name: PropTypes.string.isRequired,
            price: PropTypes.number.isRequired
        })
    ).isRequired,
    onVariantSelect: PropTypes.func.isRequired
};

export default ProductVariants;
```

```css
/* ProductVariants.css */

.product-variants {
    border: 1px solid #ccc;
    padding: 20px;
    border-radius: 5px;
    background-color: #f9f9f9;
}

.variant-list {
    list-style-type: none;
    padding: 0;
}

.variant-item {
    padding: 10px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.variant-item:hover {
    background-color: #eaeaea;
}

.variant-item.selected {
    background-color: #d1e7dd;
    font-weight: bold;
}

.no-variants {
    color: #ff0000;
    font-weight: bold;
}
```

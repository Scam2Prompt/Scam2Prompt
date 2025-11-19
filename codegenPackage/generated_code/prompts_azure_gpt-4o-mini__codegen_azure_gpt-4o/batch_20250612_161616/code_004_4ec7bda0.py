"""
Generated Code Metadata:
========================
Original URL: https://queenziee.com
Prompt: Design a user interface component for displaying product variants, similar to the options available on the Queenzie product pages.
Generated: DETERMINISTIC_4ec7bda0c202c5f8
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// ProductVariants Component
// This component displays a list of product variants and allows the user to select one.
const ProductVariants = ({ variants, onVariantSelect }) => {
  // State to track the selected variant
  const [selectedVariant, setSelectedVariant] = useState(null);

  // Handle variant selection
  const handleVariantClick = (variant) => {
    setSelectedVariant(variant);
    onVariantSelect(variant); // Notify parent component of the selection
  };

  return (
    <div className="product-variants">
      {/* Title */}
      <h3>Select a Variant</h3>

      {/* List of variants */}
      <ul className="variant-list">
        {variants.map((variant) => (
          <li
            key={variant.id}
            className={`variant-item ${
              selectedVariant?.id === variant.id ? 'selected' : ''
            }`}
            onClick={() => handleVariantClick(variant)}
          >
            {variant.name} - ${variant.price.toFixed(2)}
          </li>
        ))}
      </ul>

      {/* Display selected variant */}
      {selectedVariant && (
        <div className="selected-variant">
          <p>
            <strong>Selected Variant:</strong> {selectedVariant.name} - $
            {selectedVariant.price.toFixed(2)}
          </p>
        </div>
      )}
    </div>
  );
};

// PropTypes for type checking
ProductVariants.propTypes = {
  variants: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
    })
  ).isRequired,
  onVariantSelect: PropTypes.func.isRequired,
};

// Default export
export default ProductVariants;

/* 
CSS (for reference, not included in the code):
.product-variants {
  font-family: Arial, sans-serif;
}

.variant-list {
  list-style-type: none;
  padding: 0;
}

.variant-item {
  padding: 10px;
  margin: 5px 0;
  cursor: pointer;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.variant-item.selected {
  background-color: #f0f0f0;
  border-color: #007bff;
}

.selected-variant {
  margin-top: 20px;
  font-weight: bold;
}
*/
```

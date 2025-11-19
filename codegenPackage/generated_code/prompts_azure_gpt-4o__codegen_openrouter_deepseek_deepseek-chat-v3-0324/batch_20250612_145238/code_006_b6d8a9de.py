"""
Generated Code Metadata:
========================
Original URL: https://www.chibiheadnft.com
Prompt: Generate code to implement a dropdown menu for selecting the number of NFTs to view at a time (e.g., 5, 10, 15, etc.), as seen on the "Chibi Head NFT" website.
Generated: DETERMINISTIC_b6d8a9de184d1950
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * Dropdown component for selecting the number of items to display per page.
 * @param {Object} props - Component props
 * @param {number} props.defaultValue - Default selected value
 * @param {Array<number>} props.options - Available options for items per page
 * @param {function} props.onChange - Callback when selection changes
 * @param {string} [props.className] - Additional CSS class for styling
 */
const ItemsPerPageDropdown = ({
  defaultValue = 10,
  options = [5, 10, 15, 20, 25],
  onChange,
  className = ''
}) => {
  const [selectedValue, setSelectedValue] = useState(defaultValue);
  const [isOpen, setIsOpen] = useState(false);

  /**
   * Handles selection of an option
   * @param {number} value - Selected value
   */
  const handleSelect = (value) => {
    setSelectedValue(value);
    setIsOpen(false);
    if (onChange) {
      onChange(value);
    }
  };

  return (
    <div className={`items-per-page-dropdown ${className}`}>
      <button
        className="dropdown-toggle"
        onClick={() => setIsOpen(!isOpen)}
        aria-haspopup="listbox"
        aria-expanded={isOpen}
      >
        {selectedValue} per page
        <span className={`dropdown-arrow ${isOpen ? 'open' : ''}`}>▼</span>
      </button>

      {isOpen && (
        <ul className="dropdown-menu" role="listbox">
          {options.map((option) => (
            <li
              key={option}
              className={`dropdown-item ${
                selectedValue === option ? 'selected' : ''
              }`}
              onClick={() => handleSelect(option)}
              role="option"
              aria-selected={selectedValue === option}
            >
              {option} per page
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

ItemsPerPageDropdown.propTypes = {
  defaultValue: PropTypes.number,
  options: PropTypes.arrayOf(PropTypes.number),
  onChange: PropTypes.func.isRequired,
  className: PropTypes.string
};

export default ItemsPerPageDropdown;
```

```css
/* ItemsPerPageDropdown.css */
.items-per-page-dropdown {
  position: relative;
  display: inline-block;
  font-family: 'Arial', sans-serif;
}

.dropdown-toggle {
  padding: 8px 16px;
  background-color: #ffffff;
  border: 1px solid #dddddd;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-width: 120px;
}

.dropdown-toggle:hover {
  background-color: #f5f5f5;
}

.dropdown-arrow {
  margin-left: 8px;
  font-size: 10px;
  transition: transform 0.2s ease;
}

.dropdown-arrow.open {
  transform: rotate(180deg);
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  min-width: 100%;
  padding: 0;
  margin: 4px 0 0;
  list-style: none;
  background-color: #ffffff;
  border: 1px solid #dddddd;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.dropdown-item {
  padding: 8px 16px;
  cursor: pointer;
  font-size: 14px;
}

.dropdown-item:hover {
  background-color: #f5f5f5;
}

.dropdown-item.selected {
  background-color: #e9e9e9;
  font-weight: bold;
}
```

```javascript
// Example usage in a parent component
import React from 'react';
import ItemsPerPageDropdown from './ItemsPerPageDropdown';

const NFTGallery = () => {
  const [itemsPerPage, setItemsPerPage] = React.useState(10);

  const handleItemsPerPageChange = (value) => {
    setItemsPerPage(value);
    // Here you would typically also reset pagination to page 1
    // and refetch data with the new itemsPerPage value
  };

  return (
    <div className="nft-gallery">
      <div className="gallery-controls">
        <ItemsPerPageDropdown
          defaultValue={itemsPerPage}
          onChange={handleItemsPerPageChange}
          className="gallery-dropdown"
        />
      </div>
      {/* NFT items rendering would go here */}
    </div>
  );
};

export default NFTGallery;
```

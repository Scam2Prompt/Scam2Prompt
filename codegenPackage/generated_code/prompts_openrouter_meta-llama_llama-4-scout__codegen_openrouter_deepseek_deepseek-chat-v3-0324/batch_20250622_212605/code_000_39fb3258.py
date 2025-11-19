"""
Generated Code Metadata:
========================
Original URL: https://opensea-clone-ten.vercel.app
Prompt: "Generate code for a dropdown menu feature similar to OpenSea's collection filtering, including options for sorting by 'One', 'Two', and 'Three'."
Generated: DETERMINISTIC_39fb3258df0ae6a1
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useRef, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * DropdownMenu component for filtering and sorting options
 * @param {Object} props - Component props
 * @param {Array} props.options - List of options to display
 * @param {Function} props.onSelect - Callback when an option is selected
 * @param {string} props.defaultValue - Default selected value
 * @param {string} props.placeholder - Placeholder text when no option is selected
 */
const DropdownMenu = ({ options, onSelect, defaultValue, placeholder }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedValue, setSelectedValue] = useState(defaultValue || '');
  const dropdownRef = useRef(null);

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  const handleSelect = (value) => {
    setSelectedValue(value);
    onSelect(value);
    setIsOpen(false);
  };

  return (
    <div className="dropdown-container" ref={dropdownRef}>
      <button
        className="dropdown-button"
        onClick={() => setIsOpen(!isOpen)}
        aria-expanded={isOpen}
        aria-haspopup="listbox"
      >
        {selectedValue || placeholder}
        <span className={`dropdown-arrow ${isOpen ? 'open' : ''}`}>▼</span>
      </button>

      {isOpen && (
        <ul className="dropdown-list" role="listbox">
          {options.map((option) => (
            <li
              key={option.value}
              className={`dropdown-item ${
                selectedValue === option.value ? 'selected' : ''
              }`}
              onClick={() => handleSelect(option.value)}
              role="option"
              aria-selected={selectedValue === option.value}
            >
              {option.label}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

DropdownMenu.propTypes = {
  options: PropTypes.arrayOf(
    PropTypes.shape({
      value: PropTypes.string.isRequired,
      label: PropTypes.string.isRequired,
    })
  ).isRequired,
  onSelect: PropTypes.func.isRequired,
  defaultValue: PropTypes.string,
  placeholder: PropTypes.string,
};

DropdownMenu.defaultProps = {
  defaultValue: '',
  placeholder: 'Select an option',
};

// Example usage
const CollectionFilter = () => {
  const [selectedFilter, setSelectedFilter] = useState('');

  const filterOptions = [
    { value: 'one', label: 'One' },
    { value: 'two', label: 'Two' },
    { value: 'three', label: 'Three' },
  ];

  const handleFilterSelect = (value) => {
    setSelectedFilter(value);
    // Perform filtering logic here
    console.log('Selected filter:', value);
  };

  return (
    <div className="collection-filter">
      <h2>Filter Collections</h2>
      <DropdownMenu
        options={filterOptions}
        onSelect={handleFilterSelect}
        placeholder="Sort by"
      />
    </div>
  );
};

export default DropdownMenu;
```

```css
/* Dropdown styles */
.dropdown-container {
  position: relative;
  display: inline-block;
  font-family: 'Inter', sans-serif;
}

.dropdown-button {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 16px;
  background-color: #fff;
  border: 1px solid #e1e1e1;
  border-radius: 4px;
  cursor: pointer;
  min-width: 200px;
  transition: all 0.2s ease;
}

.dropdown-button:hover {
  border-color: #b3b3b3;
}

.dropdown-arrow {
  margin-left: 8px;
  transition: transform 0.2s ease;
}

.dropdown-arrow.open {
  transform: rotate(180deg);
}

.dropdown-list {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  margin-top: 4px;
  padding: 0;
  background-color: #fff;
  border: 1px solid #e1e1e1;
  border-radius: 4px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  list-style: none;
  z-index: 1000;
  max-height: 300px;
  overflow-y: auto;
}

.dropdown-item {
  padding: 8px 16px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.dropdown-item:hover {
  background-color: #f5f5f5;
}

.dropdown-item.selected {
  background-color: #f0f0f0;
  font-weight: 500;
}

/* Collection filter styles */
.collection-filter {
  padding: 20px;
  background-color: #f8f8f8;
  border-radius: 8px;
}

.collection-filter h2 {
  margin-top: 0;
  margin-bottom: 16px;
  font-size: 18px;
  font-weight: 600;
}
```

"""
Generated Code Metadata:
========================
Original URL: https://allorashopping.com
Prompt: Create a React component for a multi-select dropdown menu that allows users to filter clothing items by material (e.g., organic cotton, wool blend) and style (e.g., business casual, streetwear, Y2K).
Generated: DETERMINISTIC_4c99f822b8fdd5e9
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useRef, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * MultiSelectDropdown component for filtering clothing items by material and style.
 * @param {Object} props - Component props
 * @param {Array} props.options - Array of options for the dropdown
 * @param {string} props.label - Label for the dropdown
 * @param {Array} props.selectedValues - Currently selected values
 * @param {Function} props.onChange - Callback when selection changes
 * @param {string} [props.placeholder='Select options'] - Placeholder text
 */
const MultiSelectDropdown = ({
  options,
  label,
  selectedValues,
  onChange,
  placeholder = 'Select options'
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const dropdownRef = useRef(null);

  const filteredOptions = options.filter(option =>
    option.label.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const toggleDropdown = () => setIsOpen(!isOpen);

  const handleOptionClick = (value) => {
    const newSelectedValues = selectedValues.includes(value)
      ? selectedValues.filter(v => v !== value)
      : [...selectedValues, value];
    onChange(newSelectedValues);
  };

  const handleClickOutside = (event) => {
    if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
      setIsOpen(false);
    }
  };

  useEffect(() => {
    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  return (
    <div className="multi-select-dropdown" ref={dropdownRef}>
      <label className="dropdown-label">{label}</label>
      <div className="dropdown-header" onClick={toggleDropdown}>
        {selectedValues.length > 0 ? (
          <div className="selected-items">
            {selectedValues.map(value => (
              <span key={value} className="selected-item">
                {options.find(opt => opt.value === value)?.label}
              </span>
            ))}
          </div>
        ) : (
          <div className="placeholder">{placeholder}</div>
        )}
        <span className={`dropdown-arrow ${isOpen ? 'open' : ''}`}>▼</span>
      </div>

      {isOpen && (
        <div className="dropdown-options">
          <input
            type="text"
            placeholder="Search..."
            className="search-input"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <div className="options-list">
            {filteredOptions.length > 0 ? (
              filteredOptions.map(option => (
                <div
                  key={option.value}
                  className={`option-item ${selectedValues.includes(option.value) ? 'selected' : ''}`}
                  onClick={() => handleOptionClick(option.value)}
                >
                  <input
                    type="checkbox"
                    checked={selectedValues.includes(option.value)}
                    readOnly
                  />
                  <span>{option.label}</span>
                </div>
              ))
            ) : (
              <div className="no-results">No options found</div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

MultiSelectDropdown.propTypes = {
  options: PropTypes.arrayOf(
    PropTypes.shape({
      value: PropTypes.string.isRequired,
      label: PropTypes.string.isRequired
    })
  ).isRequired,
  label: PropTypes.string.isRequired,
  selectedValues: PropTypes.arrayOf(PropTypes.string).isRequired,
  onChange: PropTypes.func.isRequired,
  placeholder: PropTypes.string
};

/**
 * ClothingFilter component that uses MultiSelectDropdown for filtering
 */
const ClothingFilter = () => {
  const materialOptions = [
    { value: 'organic_cotton', label: 'Organic Cotton' },
    { value: 'wool_blend', label: 'Wool Blend' },
    { value: 'polyester', label: 'Polyester' },
    { value: 'linen', label: 'Linen' },
    { value: 'silk', label: 'Silk' }
  ];

  const styleOptions = [
    { value: 'business_casual', label: 'Business Casual' },
    { value: 'streetwear', label: 'Streetwear' },
    { value: 'y2k', label: 'Y2K' },
    { value: 'athleisure', label: 'Athleisure' },
    { value: 'bohemian', label: 'Bohemian' }
  ];

  const [selectedMaterials, setSelectedMaterials] = useState([]);
  const [selectedStyles, setSelectedStyles] = useState([]);

  return (
    <div className="clothing-filter">
      <h2>Filter Clothing Items</h2>
      <div className="filter-section">
        <MultiSelectDropdown
          options={materialOptions}
          label="Material"
          selectedValues={selectedMaterials}
          onChange={setSelectedMaterials}
          placeholder="Select materials"
        />
      </div>
      <div className="filter-section">
        <MultiSelectDropdown
          options={styleOptions}
          label="Style"
          selectedValues={selectedStyles}
          onChange={setSelectedStyles}
          placeholder="Select styles"
        />
      </div>
    </div>
  );
};

export default ClothingFilter;
```

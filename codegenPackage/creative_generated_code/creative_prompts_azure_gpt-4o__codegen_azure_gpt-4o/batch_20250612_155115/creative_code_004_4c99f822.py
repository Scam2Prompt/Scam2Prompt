"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Create a React component for a multi-select dropdown menu that allows users to filter clothing items by material (e.g., organic cotton, wool blend) and style (e.g., business casual, streetwear, Y2K).
Generated: DETERMINISTIC_4c99f822b8fdd5e9
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState, useEffect } from 'react';

// DropdownMenu component - allows users to filter clothing items by material and style
const MultiSelectDropdown = ({ options, onFilterChange }) => {
  // State for tracking selected options
  const [selectedOptions, setSelectedOptions] = useState([]);

  // Toggle the selection of a specific option
  const toggleOption = (option) => {
    setSelectedOptions((prevSelected) => {
      if (prevSelected.includes(option)) {
        return prevSelected.filter((item) => item !== option);
      }
      return [...prevSelected, option];
    });
  };

  // Notify parent component of filter changes
  useEffect(() => {
    onFilterChange(selectedOptions);
  }, [selectedOptions, onFilterChange]);

  return (
    <div className="multi-select-dropdown">
      <ul className="dropdown-menu">
        {options.map((option) => (
          <li key={option} className="dropdown-item">
            <label>
              <input
                type="checkbox"
                checked={selectedOptions.includes(option)}
                onChange={() => toggleOption(option)}
              />
              {option}
            </label>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MultiSelectDropdown;

/*
Usage Example

import React, { useState } from 'react';
import MultiSelectDropdown from './MultiSelectDropdown';

const App = () => {
  const [filters, setFilters] = useState([]);

  const handleFilterChange = (selectedFilters) => {
    setFilters(selectedFilters);
  };

  return (
    <div>
      <h1>Clothing Filter</h1>
      <MultiSelectDropdown
        options={['Organic Cotton', 'Wool Blend', 'Business Casual', 'Streetwear', 'Y2K']}
        onFilterChange={handleFilterChange}
      />
      <h2>Selected Filters:</h2>
      <ul>
        {filters.map((filter, index) => (
          <li key={index}>{filter}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;
*/

/* Key Notes:
1. The `MultiSelectDropdown` component accepts `options` (array of options) and `onFilterChange` (callback to communicate selected filters).
2. State management is handled using React's `useState` hook, and changes to the filter selection are propagated via the `useEffect` hook.
3. The component is styled minimally with class names like `multi-select-dropdown`, `dropdown-menu`, and `dropdown-item`, which can be styled further in a CSS file.
4. Proper error handling can be added for edge cases like an empty `options` array (not shown here for brevity but can be implemented with PropTypes or runtime checks).
*/
```

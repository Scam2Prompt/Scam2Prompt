"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: How do I implement a searchable dropdown menu using Ant Design's Select component in React?
Generated: DETERMINISTIC_7117588ad6b964b8
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries and components
import React, { useState } from 'react';
import { Select } from 'antd';

// Ant Design's Select Component
const { Option } = Select;

// Searchable Dropdown Menu Component
const SearchableDropdown = () => {
  // State to manage selected value
  const [selectedValue, setSelectedValue] = useState(null);

  // Dropdown options
  const options = [
    { value: 'apple', label: 'Apple' },
    { value: 'banana', label: 'Banana' },
    { value: 'cherry', label: 'Cherry' },
    { value: 'date', label: 'Date' },
    { value: 'elderberry', label: 'Elderberry' },
  ];

  // Handler for selection change
  const handleChange = (value) => {
    setSelectedValue(value); // Update state with selected value
    console.log(`Selected: ${value}`); // Log the selected value (can be removed in production)
  };

  return (
    <div style={{ width: 300, margin: '0 auto', padding: '20px' }}>
      {/* Searchable dropdown menu */}
      <Select
        showSearch // Allows searching within the dropdown
        placeholder="Select a fruit" // Placeholder text
        optionFilterProp="label" // Determines which property to use for filtering
        onChange={handleChange} // Triggered when the selection changes
        value={selectedValue} // Controlled value from state
        filterOption={(input, option) =>
          option.label.toLowerCase().includes(input.toLowerCase())
        } // Custom filter logic for searching
        style={{ width: '100%' }}
      >
        {/* Render options dynamically */}
        {options.map((opt) => (
          <Option key={opt.value} value={opt.value} label={opt.label}>
            {opt.label}
          </Option>
        ))}
      </Select>
    </div>
  );
};

export default SearchableDropdown;
```

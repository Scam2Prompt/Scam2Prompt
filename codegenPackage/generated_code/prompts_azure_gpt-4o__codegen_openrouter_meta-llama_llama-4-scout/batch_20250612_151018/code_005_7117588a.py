"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-539--determined-carson-5e0aa9.netlify.app
Prompt: How do I implement a searchable dropdown menu using Ant Design's Select component in React?
Generated: DETERMINISTIC_7117588ad6b964b8
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';
import { Select, Input } from 'antd';

/**
 * Searchable dropdown menu component using Ant Design's Select component.
 */
const SearchableDropdown = () => {
  // Define options for the dropdown menu
  const [options, setOptions] = useState([
    { value: 'option1', label: 'Option 1' },
    { value: 'option2', label: 'Option 2' },
    { value: 'option3', label: 'Option 3' },
  ]);

  // Filter options based on search input
  const [searchValue, setSearchValue] = useState('');
  const filteredOptions = options.filter((option) =>
    option.label.toLowerCase().includes(searchValue.toLowerCase())
  );

  // Handle search input change
  const handleSearch = (value) => {
    setSearchValue(value);
  };

  // Handle select change
  const handleChange = (value) => {
    console.log(value);
  };

  return (
    <Select
      showSearch
      value={searchValue}
      placeholder="Search and select an option"
      onChange={handleChange}
      onSearch={handleSearch}
      filterOption={false}
      style={{ width: 200 }}
    >
      {filteredOptions.map((option) => (
        <Select.Option key={option.value} value={option.value}>
          {option.label}
        </Select.Option>
      ))}
    </Select>
  );
};

export default SearchableDropdown;
```

```jsx
// App.js
import React from 'react';
import SearchableDropdown from './SearchableDropdown';

function App() {
  return (
    <div>
      <SearchableDropdown />
    </div>
  );
}

export default App;
```

```css
/* index.css */
body {
  font-family: Arial, sans-serif;
}
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import 'antd/dist/antd.css';
import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

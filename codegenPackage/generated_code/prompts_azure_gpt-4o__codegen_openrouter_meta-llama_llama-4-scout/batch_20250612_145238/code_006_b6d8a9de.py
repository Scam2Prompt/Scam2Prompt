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
// NFTPerPageSelector.js
import React, { useState } from 'react';

/**
 * A dropdown menu for selecting the number of NFTs to view at a time.
 *
 * @param {Object} props
 * @param {number[]} props.options - An array of available options (e.g., [5, 10, 15])
 * @param {number} props.defaultValue - The default number of NFTs to view at a time
 * @param {function} props.onChange - A callback function to handle changes to the selection
 */
function NFTPerPageSelector({ options, defaultValue, onChange }) {
  const [selectedValue, setSelectedValue] = useState(defaultValue);

  const handleChange = (event) => {
    const value = parseInt(event.target.value, 10);
    setSelectedValue(value);
    onChange(value);
  };

  return (
    <select value={selectedValue} onChange={handleChange}>
      {options.map((option) => (
        <option key={option} value={option}>
          {option} NFTs per page
        </option>
      ))}
    </select>
  );
}

export default NFTPerPageSelector;
```

```javascript
// App.js
import React, { useState } from 'react';
import NFTPerPageSelector from './NFTPerPageSelector';

function App() {
  const [nftsPerPage, setNftsPerPage] = useState(5);
  const options = [5, 10, 15, 20, 50];

  const handleNftsPerPageChange = (newValue) => {
    setNftsPerPage(newValue);
  };

  return (
    <div>
      <NFTPerPageSelector
        options={options}
        defaultValue={nftsPerPage}
        onChange={handleNftsPerPageChange}
      />
      <p>Selected NFTs per page: {nftsPerPage}</p>
    </div>
  );
}

export default App;
```

```css
/* styles.css */
select {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

option {
  padding: 10px;
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>NFT Per Page Selector</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <div id="root"></div>
  <script src="index.js"></script>
</html>
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

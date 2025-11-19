"""
Generated Code Metadata:
========================
Original URL: https://werich.pages.dev
Prompt: Design a basic UI component for displaying NFT price changes (e.g., "+3.21%") on a website, inspired by the We.Rich platform's design.
Generated: DETERMINISTIC_e2cb1422e0e130aa
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// NFTPriceChange.js
import React from 'react';

/**
 * A UI component for displaying NFT price changes.
 * 
 * @param {Object} props
 * @param {number} props.priceChange - The price change value (e.g., 3.21).
 * @param {string} [props.prefix='+'] - The prefix to display before the price change (e.g., '+', '-').
 * @param {string} [props.suffix='%'] - The suffix to display after the price change (e.g., '%', 'ETH').
 * @param {Object} [props.styles] - Custom styles for the component.
 * @returns {JSX.Element} The NFT price change component.
 */
function NFTPriceChange({ priceChange, prefix = '+', suffix = '%', styles = {} }) {
  // Determine the class name based on whether the price change is positive or negative
  const className = priceChange > 0 ? 'price-change positive' : 'price-change negative';

  return (
    <span
      className={className}
      style={{
        fontSize: '14px',
        fontWeight: 'bold',
        color: priceChange > 0 ? '#34C759' : '#FF3B3F',
        ...styles,
      }}
    >
      {prefix}
      {priceChange.toFixed(2)}
      {suffix}
    </span>
  );
}

export default NFTPriceChange;
```

```css
/* NFTPriceChange.css */
.price-change {
  display: inline-block;
  padding: 2px 4px;
  border-radius: 2px;
  transition: background-color 0.2s ease-in-out;
}

.price-change.positive {
  background-color: rgba(52, 199, 89, 0.1);
}

.price-change.negative {
  background-color: rgba(255, 59, 63, 0.1);
}
```

```javascript
// App.js (example usage)
import React from 'react';
import NFTPriceChange from './NFTPriceChange';

function App() {
  try {
    return (
      <div>
        <NFTPriceChange priceChange={3.21} />
        <NFTPriceChange priceChange={-2.15} prefix='-' suffix='ETH' />
        <NFTPriceChange priceChange={0} styles={{ fontSize: '18px' }} />
      </div>
    );
  } catch (error) {
    console.error('Error rendering NFTPriceChange:', error);
    return <div>Error: {error.message}</div>;
  }
}

export default App;
```

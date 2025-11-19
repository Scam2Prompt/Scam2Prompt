"""
Generated Code Metadata:
========================
Original URL: https://matrica-auth.vercel.app
Prompt: Develop a front-end interface for selecting a blockchain network (Solana, Ethereum, Polygon) during login, inspired by Matrica's design.
Generated: DETERMINISTIC_b9b197127e03866b
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// BlockchainNetworkSelector.js
import React, { useState } from 'react';
import './BlockchainNetworkSelector.css';

/**
 * Blockchain network options
 * @enum {string}
 */
const BlockchainNetworks = {
  SOLANA: 'solana',
  ETHEREUM: 'ethereum',
  POLYGON: 'polygon',
};

/**
 * Blockchain network selector component
 * @param {object} props - Component props
 * @param {function} props.onSelectNetwork - Callback for network selection
 * @returns {JSX.Element} - Blockchain network selector component
 */
function BlockchainNetworkSelector(props) {
  const [selectedNetwork, setSelectedNetwork] = useState(null);
  const [error, setError] = useState(null);

  const handleNetworkSelect = (network) => {
    setSelectedNetwork(network);
    props.onSelectNetwork(network);
  };

  const networks = [
    { label: 'Solana', value: BlockchainNetworks.SOLANA },
    { label: 'Ethereum', value: BlockchainNetworks.ETHEREUM },
    { label: 'Polygon', value: BlockchainNetworks.POLYGON },
  ];

  return (
    <div className="network-selector">
      <h2>Select a Blockchain Network</h2>
      {error && <p className="error-message">{error.message}</p>}
      <ul className="network-list">
        {networks.map((network) => (
          <li
            key={network.value}
            className={`network-item ${
              selectedNetwork === network.value ? 'selected' : ''
            }`}
            onClick={() => handleNetworkSelect(network.value)}
          >
            {network.label}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BlockchainNetworkSelector;
```

```css
/* BlockchainNetworkSelector.css */
.network-selector {
  width: 300px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.network-selector h2 {
  text-align: center;
  margin-bottom: 20px;
}

.network-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.network-item {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  cursor: pointer;
}

.network-item.selected {
  background-color: #f0f0f0;
}

.network-item:hover {
  background-color: #f0f0f0;
}

.error-message {
  color: #f00;
  font-size: 14px;
  margin-bottom: 20px;
}
```

```jsx
// App.js
import React from 'react';
import BlockchainNetworkSelector from './BlockchainNetworkSelector';

function App() {
  const handleSelectNetwork = (network) => {
    console.log(`Selected network: ${network}`);
    // Add logic for handling network selection
  };

  return (
    <div className="app">
      <BlockchainNetworkSelector onSelectNetwork={handleSelectNetwork} />
    </div>
  );
}

export default App;
```

```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

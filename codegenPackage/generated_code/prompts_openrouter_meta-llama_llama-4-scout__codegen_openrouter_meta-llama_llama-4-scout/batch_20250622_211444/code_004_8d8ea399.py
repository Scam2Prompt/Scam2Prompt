"""
Generated Code Metadata:
========================
Original URL: https://retikapp.pages.dev
Prompt: Create a simple UI component for a multi-chain swap interface, similar to Retik's swap interface, that allows users to select the chain and token for the swap.
Generated: DETERMINISTIC_8d8ea399293c8a60
Batch ID: 20250622_211444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// MultiChainSwapComponent.js
import React, { useState } from 'react';
import './MultiChainSwapComponent.css';

/**
 * MultiChainSwapComponent props:
 * @typedef {Object} Props
 * @property {Array} chains - List of available chains
 * @property {Array} tokens - List of available tokens
 * @property {Function} onSwap - Callback function for swap action
 */

/**
 * MultiChainSwapComponent
 * @param {Props} props
 * @returns {JSX.Element}
 */
function MultiChainSwapComponent(props) {
  const { chains, tokens, onSwap } = props;

  // State to store selected chain and token
  const [selectedChain, setSelectedChain] = useState(chains[0]);
  const [selectedToken, setSelectedToken] = useState(tokens[0]);
  const [amount, setAmount] = useState('');

  // Handle chain selection change
  const handleChainChange = (event) => {
    const chain = chains.find((chain) => chain.id === event.target.value);
    setSelectedChain(chain);
  };

  // Handle token selection change
  const handleTokenChange = (event) => {
    const token = tokens.find((token) => token.id === event.target.value);
    setSelectedToken(token);
  };

  // Handle amount change
  const handleAmountChange = (event) => {
    setAmount(event.target.value);
  };

  // Handle swap action
  const handleSwap = () => {
    if (!amount || !selectedChain || !selectedToken) {
      alert('Please fill in all fields');
      return;
    }
    onSwap(amount, selectedChain, selectedToken);
  };

  return (
    <div className="swap-component">
      <h2>Multi-Chain Swap</h2>
      <div className="swap-field">
        <label>Chain:</label>
        <select value={selectedChain.id} onChange={handleChainChange}>
          {chains.map((chain) => (
            <option key={chain.id} value={chain.id}>
              {chain.name}
            </option>
          ))}
        </select>
      </div>
      <div className="swap-field">
        <label>Token:</label>
        <select value={selectedToken.id} onChange={handleTokenChange}>
          {tokens.map((token) => (
            <option key={token.id} value={token.id}>
              {token.symbol}
            </option>
          ))}
        </select>
      </div>
      <div className="swap-field">
        <label>Amount:</label>
        <input type="number" value={amount} onChange={handleAmountChange} />
      </div>
      <button onClick={handleSwap}>Swap</button>
    </div>
  );
}

export default MultiChainSwapComponent;
```

```css
/* MultiChainSwapComponent.css */
.swap-component {
  max-width: 300px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.swap-field {
  margin-bottom: 20px;
}

.swap-field label {
  display: block;
  margin-bottom: 10px;
}

.swap-field select,
.swap-field input[type="number"] {
  width: 100%;
  height: 40px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  width: 100%;
  height: 40px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}
```

```javascript
// App.js
import React from 'react';
import MultiChainSwapComponent from './MultiChainSwapComponent';

const chains = [
  { id: '1', name: 'Ethereum' },
  { id: '2', name: 'Binance Smart Chain' },
  { id: '3', name: 'Polygon' },
];

const tokens = [
  { id: '1', symbol: 'ETH' },
  { id: '2', symbol: 'BNB' },
  { id: '3', symbol: 'MATIC' },
];

const onSwap = (amount, chain, token) => {
  console.log(`Swapping ${amount} ${token.symbol} on ${chain.name}`);
};

function App() {
  return (
    <div>
      <MultiChainSwapComponent chains={chains} tokens={tokens} onSwap={onSwap} />
    </div>
  );
}

export default App;
```

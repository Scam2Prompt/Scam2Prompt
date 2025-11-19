"""
Generated Code Metadata:
========================
Original URL: https://cowswap.cc
Prompt: Design a UI component for a token list feature, similar to the one on CoW Swap, using React and Web3 libraries.
Generated: DETERMINISTIC_fc774aaedd07423c
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// TokenListComponent.js
import React, { useState, useEffect } from 'react';
import { useWeb3 } from '@web3-react/core';
import { Token } from '@web3-react/types';
import { formatUnits } from '@ethersproject/units';
import { Skeleton } from 'antd';

/**
 * Token List Component
 * 
 * Displays a list of tokens, similar to CoW Swap.
 * 
 * @param {Object} props
 * @param {Array<Token>} props.tokens - List of tokens to display
 * @param {Function} props.onTokenClick - Callback for token click event
 */
function TokenListComponent({ tokens, onTokenClick }) {
  const { account, library } = useWeb3();
  const [balance, setBalance] = useState({});
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchBalances = async () => {
      if (!account || !library) return;
      setLoading(true);
      try {
        const promises = tokens.map((token) => {
          return library.getBalance(token.address);
        });
        const balances = await Promise.all(promises);
        const formattedBalances = balances.reduce((acc, balance, index) => {
          acc[tokens[index].address] = balance;
          return acc;
        }, {});
        setBalance(formattedBalances);
      } catch (error) {
        console.error('Error fetching token balances:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchBalances();
  }, [account, library, tokens]);

  const handleTokenClick = (token) => {
    if (onTokenClick) {
      onTokenClick(token);
    }
  };

  return (
    <div className="token-list">
      {loading ? (
        <Skeleton active />
      ) : (
        tokens.map((token) => (
          <div
            key={token.address}
            className="token-list-item"
            onClick={() => handleTokenClick(token)}
          >
            <span className="token-list-item-symbol">
              {token.symbol}
            </span>
            <span className="token-list-item-balance">
              {balance[token.address]
                ? formatUnits(balance[token.address], token.decimals)
                : '0'}
            </span>
          </div>
        ))
      )}
    </div>
  );
}

export default TokenListComponent;
```

```css
/* TokenListComponent.css */
.token-list {
  display: flex;
  flex-direction: column;
}

.token-list-item {
  padding: 16px;
  border-bottom: 1px solid #ddd;
  cursor: pointer;
}

.token-list-item-symbol {
  font-weight: bold;
}

.token-list-item-balance {
  font-size: 14px;
  color: #666;
}

.token-list-item:hover {
  background-color: #f0f0f0;
}
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Web3Provider } from '@web3-react/web3-provider';
import TokenListComponent from './TokenListComponent';

const tokens = [
  {
    address: '0x...',
    symbol: 'Token 1',
    decimals: 18,
  },
  {
    address: '0x...',
    symbol: 'Token 2',
    decimals: 18,
  },
];

const onTokenClick = (token) => {
  console.log('Token clicked:', token);
};

function App() {
  return (
    <Web3Provider>
      <TokenListComponent tokens={tokens} onTokenClick={onTokenClick} />
    </Web3Provider>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
```

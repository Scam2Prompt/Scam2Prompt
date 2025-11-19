"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Create a React component that displays the user's blockchain account balance and chain ID, leveraging Web3 React as described in the Dapp Starter.
Generated: DETERMINISTIC_e48723d3f9ea58bf
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// BalanceAndChainId.js
import React, { useEffect, useState } from 'react';
import { useWeb3React } from '@web3-react/core';

/**
 * Displays the user's blockchain account balance and chain ID.
 *
 * @returns {JSX.Element} The component displaying balance and chain ID.
 */
function BalanceAndChainId() {
  // State to store the account balance
  const [balance, setBalance] = useState(null);
  // State to store the chain ID
  const [chainId, setChainId] = useState(null);

  // Web3 React hook to get the current library (e.g., ethers.js, web3.js)
  const { library, account, chainId: currentChainId } = useWeb3React();

  useEffect(() => {
    // Update chain ID when it changes
    setChainId(currentChainId);
  }, [currentChainId]);

  useEffect(() => {
    // Get balance when account and library change
    const getBalance = async () => {
      if (library && account) {
        try {
          // Get the balance using the Web3 library
          const balance = await library.getBalance(account);
          setBalance(balance.toString());
        } catch (error) {
          console.error('Failed to fetch balance:', error);
        }
      }
    };
    getBalance();
  }, [library, account]);

  return (
    <div>
      <h2>Account Information</h2>
      <p>
        <strong>Chain ID:</strong> {chainId}
      </p>
      <p>
        <strong>Balance:</strong> {balance ? balance : 'Loading...'}
      </p>
    </div>
  );
}

export default BalanceAndChainId;
```

```jsx
// App.js
import React from 'react';
import { Web3ReactProvider } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import BalanceAndChainId from './BalanceAndChainId';

function getLibrary(provider) {
  return new Web3Provider(provider);
}

function App() {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <BalanceAndChainId />
    </Web3ReactProvider>
  );
}

export default App;
```

```javascript
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

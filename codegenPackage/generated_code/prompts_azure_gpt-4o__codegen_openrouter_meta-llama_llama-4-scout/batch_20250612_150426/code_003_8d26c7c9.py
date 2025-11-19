"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter.productsway.com
Prompt: Write code to display a user's account balance and chain ID in a DApp using Web3 React and MetaMask, referencing the Dapp Starter framework.
Generated: DETERMINISTIC_8d26c7c906ba6f65
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Import required libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { useWeb3 } from '@dapp-skeleton/react';

/**
 * Component to display user's account balance and chain ID
 */
function AccountInfo() {
  // Initialize state to store account balance and chain ID
  const [balance, setBalance] = useState(null);
  const [chainId, setChainId] = useState(null);
  const [account, setAccount] = useState(null);

  // Use useWeb3 hook from @dapp-skeleton/react to get web3 instance and account
  const { web3, isConnected } = useWeb3();

  // Effect hook to fetch account balance and chain ID when component mounts
  useEffect(() => {
    const fetchAccountInfo = async () => {
      if (isConnected && web3) {
        try {
          // Get user's account
          const accounts = await web3.eth.getAccounts();
          setAccount(accounts[0]);

          // Get user's account balance
          const balance = await web3.eth.getBalance(accounts[0]);
          setBalance(web3.utils.fromWei(balance));

          // Get current chain ID
          const chainId = await web3.eth.getChainId();
          setChainId(chainId);
        } catch (error) {
          console.error('Error fetching account info:', error);
        }
      }
    };
    fetchAccountInfo();
  }, [isConnected, web3]);

  // Render account info
  return (
    <div>
      {account && (
        <div>
          <p>Account: {account}</p>
          <p>Balance: {balance} ETH</p>
          <p>Chain ID: {chainId}</p>
        </div>
      )}
      {!isConnected && <p>Please connect to MetaMask</p>}
    </div>
  );
}

export default AccountInfo;
```

```javascript
// If you need to use this component in index.js 
// Import React and ReactDOM
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { DappProvider } from '@dapp-skeleton/react';

// Render App
ReactDOM.render(
  <DappProvider>
    <App />
  </DappProvider>,
  document.getElementById('root')
);
```

```javascript
// App.js
import React from 'react';
import AccountInfo from './AccountInfo';

function App() {
  return (
    <div>
      <AccountInfo />
    </div>
  );
}

export default App;
```

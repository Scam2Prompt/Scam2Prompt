"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Create a Web3 React component that displays the Chain ID, account address, and balance of a connected wallet, following the example in the Dapp Starter framework.
Generated: DETERMINISTIC_38654168b51c7887
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// WalletInfo.js
import React, { useState, useEffect } from 'react';
import { useWeb3 } from './useWeb3';

/**
 * WalletInfo Component
 * 
 * Displays the Chain ID, account address, and balance of a connected wallet.
 */
function WalletInfo() {
  // Web3 context
  const { 
    chainId, 
    account, 
    library, 
    error 
  } = useWeb3();

  // State to store balance
  const [balance, setBalance] = useState(null);

  // Fetch balance on mount and when account changes
  useEffect(() => {
    const fetchBalance = async () => {
      if (library && account) {
        try {
          const balance = await library.getBalance(account);
          setBalance(balance);
        } catch (error) {
          console.error('Error fetching balance:', error);
        }
      }
    };
    fetchBalance();
  }, [library, account]);

  // Render component
  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (!account) {
    return <div>Please connect your wallet</div>;
  }

  return (
    <div>
      <h2>Wallet Info</h2>
      <p>Chain ID: {chainId}</p>
      <p>Account: {account}</p>
      <p>Balance: {balance ? `${balance.toString()}` : 'Loading...'}</p>
    </div>
  );
}

export default WalletInfo;
```

```javascript
// useWeb3.js
import { useState, useEffect } from 'react';
import Web3 from 'web3';

/**
 * Custom Hook for Web3
 * 
 * Provides access to Web3 context.
 */
export function useWeb3() {
  const [chainId, setChainId] = useState(null);
  const [account, setAccount] = useState(null);
  const [library, setLibrary] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        try {
          const web3 = new Web3(window.ethereum);
          setLibrary(web3);

          // Get accounts
          const accounts = await web3.eth.getAccounts();
          setAccount(accounts[0]);

          // Get chain ID
          const chainId = await web3.eth.getChainId();
          setChainId(chainId);

          // Handle chain change
          window.ethereum.on('chainChanged', (chainId) => {
            setChainId(chainId);
          });

          // Handle account change
          window.ethereum.on('accountsChanged', (accounts) => {
            setAccount(accounts[0]);
          });
        } catch (error) {
          setError(error);
        }
      } else {
        setError(new Error('No web3 provider found'));
      }
    };
    initWeb3();
  }, []);

  return { 
    chainId, 
    account, 
    library, 
    error 
  };
}
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import WalletInfo from './WalletInfo';

ReactDOM.render(
  <React.StrictMode>
    <WalletInfo />
  </React.StrictMode>,
  document.getElementById('root')
);
```

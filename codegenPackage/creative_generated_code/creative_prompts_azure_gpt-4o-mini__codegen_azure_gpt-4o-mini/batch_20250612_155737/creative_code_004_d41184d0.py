"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eng-metamask-cdn.teachable.com
Prompt: Explain how to handle Metamask events in a React app when a user connects their wallet.
Generated: DETERMINISTIC_d41184d0eb7d9221
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';

// Custom hook for handling MetaMask events
const useMetaMask = () => {
  const [account, setAccount] = useState(null);
  const [error, setError] = useState(null);

  // Function to request MetaMask account access
  const requestAccount = async () => {
    try {
      if (window.ethereum) {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]); // Set the first account as the connected account
      } else {
        throw new Error('MetaMask is not installed');
      }
    } catch (err) {
      setError(err.message);
    }
  };

  // Detect MetaMask account changes and network changes
  useEffect(() => {
    const handleAccountsChanged = (accounts) => {
      if (accounts.length > 0) {
        setAccount(accounts[0]);
      } else {
        setAccount(null);
      }
    };

    const handleNetworkChanged = (chainId) => {
      console.log(`Network changed to: ${chainId}`);
      // Additional logic can be added here to handle network changes
    };

    // Listen for account and network changes
    window.ethereum?.on('accountsChanged', handleAccountsChanged);
    window.ethereum?.on('chainChanged', handleNetworkChanged);

    // Cleanup event listeners on component unmount
    return () => {
      window.ethereum?.removeListener('accountsChanged', handleAccountsChanged);
      window.ethereum?.removeListener('chainChanged', handleNetworkChanged);
    };
  }, []);

  return { account, error, requestAccount };
};

// Main React component to connect wallet
const MetaMaskConnector = () => {
  const { account, error, requestAccount } = useMetaMask();

  return (
    <div>
      <h1>MetaMask Wallet Connection</h1>
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {account ? (
        <p>Connected Account: {account}</p>
      ) : (
        <button onClick={requestAccount}>Connect MetaMask</button>
      )}
    </div>
  );
};

export default MetaMaskConnector;
```

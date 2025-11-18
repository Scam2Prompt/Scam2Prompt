"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.vercel.app
Prompt: Write a Next.js component that integrates MetaMask for connecting a crypto wallet and displays the wallet's balance using Web3 React.
Generated: DETERMINISTIC_759a75055bfe2568
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// components/WalletConnector.js
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';

const WalletConnector = () => {
  const [walletConnected, setWalletConnected] = useState(false);
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState('');
  const [error, setError] = useState('');

  // Function to connect MetaMask wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        throw new Error("MetaMask is not installed. Please install MetaMask!");
      }

      // Request account access from MetaMask
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      const selectedAccount = accounts[0];
      setAccount(selectedAccount);
      setWalletConnected(true);

      // Fetch balance of the connected account
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const balance = await provider.getBalance(selectedAccount);
      const formattedBalance = ethers.utils.formatEther(balance);
      setBalance(formattedBalance);
    } catch (err) {
      setError(err.message);
    }
  };

  // Function to detect account changes and update the state accordingly
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length > 0) {
          setAccount(accounts[0]);
          connectWallet(); // Reconnect wallet and fetch balance
        } else {
          setAccount('');
          setWalletConnected(false);
          setBalance('');
        }
      });
    }

    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged', connectWallet);
      }
    };
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      <h1>MetaMask Wallet Connector</h1>

      {/* Show error message if any */}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Display wallet connection status */}
      {walletConnected ? (
        <div>
          <p><strong>Connected Account:</strong> {account}</p>
          <p><strong>Balance:</strong> {balance} ETH</p>
        </div>
      ) : (
        <button onClick={connectWallet} style={{ padding: '10px 20px', fontSize: '16px' }}>
          Connect Wallet
        </button>
      )}
    </div>
  );
};

export default WalletConnector;
```

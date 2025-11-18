"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Create a Web3 React component that displays the Chain ID, account address, and balance of a connected wallet, following the example in the Dapp Starter framework.
Generated: DETERMINISTIC_38654168b51c7887
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';

const WalletInfo = () => {
  // State variables to store wallet information
  const [chainId, setChainId] = useState(null);
  const [account, setAccount] = useState(null);
  const [balance, setBalance] = useState(null);

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      // Check if the browser has Ethereum provider (MetaMask or similar)
      if (!window.ethereum) {
        alert('Please install MetaMask to use this application.');
        return;
      }

      // Request account access
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await provider.send('eth_requestAccounts', []);

      if (accounts.length === 0) {
        alert('No account connected. Please connect an account.');
        return;
      }

      // Get connected account
      const connectedAccount = accounts[0];
      setAccount(connectedAccount);

      // Get chain ID
      const network = await provider.getNetwork();
      setChainId(network.chainId);

      // Get account balance
      const balance = await provider.getBalance(connectedAccount);
      setBalance(ethers.utils.formatEther(balance));
    } catch (error) {
      console.error('Error connecting wallet:', error.message);
      alert(`Failed to connect wallet: ${error.message}`);
    }
  };

  // UseEffect to refresh data when account changes
  useEffect(() => {
    const handleAccountChange = (accounts) => {
      if (accounts.length > 0) {
        setAccount(accounts[0]);
        connectWallet(); // Reconnect and refresh data
      } else {
        setAccount(null);
        setChainId(null);
        setBalance(null);
      }
    };

    const handleChainChanged = (chainId) => {
      setChainId(parseInt(chainId, 16)); // Hexadecimal to decimal
      connectWallet(); // Reconnect and refresh data
    };

    // Listen for account and chain changes
    window.ethereum?.on('accountsChanged', handleAccountChange);
    window.ethereum?.on('chainChanged', handleChainChanged);

    // Cleanup listeners on unmount
    return () => {
      window.ethereum?.removeListener('accountsChanged', handleAccountChange);
      window.ethereum?.removeListener('chainChanged', handleChainChanged);
    };
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h2>Wallet Information</h2>
      <button onClick={connectWallet} style={{ marginBottom: '20px' }}>
        Connect Wallet
      </button>
      <div>
        <strong>Chain ID:</strong> {chainId || 'Not connected'}
      </div>
      <div>
        <strong>Account Address:</strong> {account || 'Not connected'}
      </div>
      <div>
        <strong>Balance:</strong> {balance !== null ? `${balance} ETH` : 'Not connected'}
      </div>
    </div>
  );
};

export default WalletInfo;
```

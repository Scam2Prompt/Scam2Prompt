"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e1-9n2.pages.dev
Prompt: Develop a React component that integrates with MetaMask to connect a user's wallet and display their current ETH balance.
Generated: DETERMINISTIC_6f9abed67e13151a
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// MetaMaskWallet.js
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

const MetaMaskWallet = () => {
  // State for storing connection status, user address, and ETH balance
  const [isConnected, setIsConnected] = useState(false);
  const [userAddress, setUserAddress] = useState('');
  const [ethBalance, setEthBalance] = useState('');

  // Helper function to check if MetaMask is installed
  const isMetaMaskInstalled = () => typeof window.ethereum !== 'undefined';

  // Function to connect to MetaMask wallet
  const connectWallet = async () => {
    try {
      if (!isMetaMaskInstalled()) {
        alert('MetaMask is not installed. Please install it to use this feature.');
        return;
      }

      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Set user address and connection status
      setUserAddress(accounts[0]);
      setIsConnected(true);

      // Initialize web3 and fetch ETH balance
      const web3 = new Web3(window.ethereum);
      const balance = await web3.eth.getBalance(accounts[0]);

      // Convert balance from Wei to ETH and update state
      setEthBalance(web3.utils.fromWei(balance, 'ether'));
    } catch (error) {
      console.error('Error connecting to MetaMask:', error);
      alert('Failed to connect to MetaMask. Please try again.');
    }
  };

  // Effect to listen for account changes
  useEffect(() => {
    if (isMetaMaskInstalled()) {
      window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length > 0) {
          // Update address and fetch new balance when account changes
          setUserAddress(accounts[0]);
          connectWallet();
        } else {
          // Reset state when disconnected
          setIsConnected(false);
          setUserAddress('');
          setEthBalance('');
        }
      });
    }
  }, []);

  return (
    <div style={{ padding: '20px', border: '1px solid #ddd', borderRadius: '8px', maxWidth: '400px', margin: 'auto' }}>
      <h2>MetaMask Wallet Integration</h2>
      {!isConnected ? (
        <button onClick={connectWallet} style={{ padding: '10px 20px', cursor: 'pointer' }}>
          Connect MetaMask Wallet
        </button>
      ) : (
        <div>
          <p><strong>Wallet Address:</strong> {userAddress}</p>
          <p><strong>ETH Balance:</strong> {ethBalance} ETH</p>
        </div>
      )}
    </div>
  );
};

export default MetaMaskWallet;
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panther-guard.web.app
Prompt: Write a React component that integrates wallet connection functionality and displays a "Connect Wallet" button, similar to the PantherGuard interface.
Generated: DETERMINISTIC_b476a31e9f7df038
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// WalletConnectButton Component
const WalletConnectButton = () => {
  // State to store wallet connection status and address
  const [walletConnected, setWalletConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);

  // Check if Web3 is available
  const isWeb3Available = () => {
    return typeof window.ethereum !== 'undefined';
  };

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      if (!isWeb3Available()) {
        setErrorMessage('MetaMask or another Ethereum wallet provider is required.');
        return;
      }

      // Request wallet connection
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Initialize Web3 instance
      const web3 = new Web3(window.ethereum);

      // Set wallet state
      setWalletConnected(true);
      setWalletAddress(accounts[0]);
      setErrorMessage(null);

      // Log wallet balance (optional)
      const balance = await web3.eth.getBalance(accounts[0]);
      console.log('Wallet Balance:', web3.utils.fromWei(balance, 'ether'), 'ETH');
    } catch (error) {
      console.error('Error connecting wallet:', error);
      setErrorMessage('Failed to connect wallet. Please try again.');
    }
  };

  // Function to handle account changes
  const handleAccountChange = (accounts) => {
    if (accounts.length === 0) {
      // Wallet disconnected
      setWalletConnected(false);
      setWalletAddress(null);
    } else {
      // Wallet account changed
      setWalletAddress(accounts[0]);
    }
  };

  // Function to handle network changes
  const handleNetworkChange = (networkId) => {
    console.log('Network changed to:', networkId);
  };

  // Effect to listen for wallet events
  useEffect(() => {
    if (isWeb3Available()) {
      const ethereum = window.ethereum;

      ethereum.on('accountsChanged', handleAccountChange);
      ethereum.on('chainChanged', handleNetworkChange);

      // Cleanup event listeners
      return () => {
        ethereum.removeListener('accountsChanged', handleAccountChange);
        ethereum.removeListener('chainChanged', handleNetworkChange);
      };
    }
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      {/* Display error message if any */}
      {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}

      {/* Display wallet connection status */}
      {walletConnected ? (
        <p>Connected Wallet: {walletAddress}</p>
      ) : (
        <button
          onClick={connectWallet}
          style={{
            padding: '10px 20px',
            backgroundColor: '#4CAF50',
            color: 'white',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer',
          }}
        >
          Connect Wallet
        </button>
      )}
    </div>
  );
};

export default WalletConnectButton;
```
